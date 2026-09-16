"""关卡 1.75：卡片保真 lint——动效实现必须复制自 template/cards/<slug>.tsx。

用法：
  python3 scripts/card_lint.py <工程src目录> [slug,slug,...]
  slug 列表给出时逐一要求存在（从 SHOTBOOK 用到的卡列出）；省略时只查
  <工程src>/cards/ 里已有的文件（此时"漏复制整张卡"查不出来，尽量传全量清单）。

判定：
  1) <工程src>/cards/<slug>.tsx 必须存在——SKILL.md ④ 的实现方式就是
     "复制 tsx 进工程改 CONFIG"，工程里没有这份文件 = 凭卡名手写了简化版
     （回弹/拍击/密度全丢、取景框括号方向画反，2026-08-30 翻车实录）→ FAIL（P1 级）。
  2) 与 skill 的 template/cards/<slug>.tsx 归一化文本相似度 ≥ 0.55
     （difflib；改 CONFIG/theme/文案在容忍内，从零重写过不了）。
  3) 只要生产副本含可编辑文字样式，文件顶部必须显式声明
     `// production-type-mapped: ...`（已按 theme T 字阶映射），或
     `// production-type-exception: product-ui ...`（真产品皮/证据原生小字，父镜头已加大字 callout）。
     无声明 = 直接复制了 960×540 旧 demo 字号 → FAIL（P1）。

template 目录按脚本自身位置解析（scripts/ 的上一级 / template/cards）。
"""
import difflib
import re
import sys
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parent.parent / "template" / "cards"
THRESHOLD = 0.55
TYPE_MARKER = re.compile(r"production-type-(?:mapped|exception)\s*:", re.I)
TEXT_STYLE = re.compile(r"font-size\s*:|fontSize\s*:|<text\b", re.I)


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def main() -> int:
    src = Path(sys.argv[1])
    cards_dir = src / "cards"
    if len(sys.argv) > 2:
        slugs = [s.strip() for s in sys.argv[2].split(",") if s.strip()]
    else:
        slugs = sorted(p.stem for p in cards_dir.glob("*.tsx")) if cards_dir.is_dir() else []
        print(f"（未传 slug 清单，只校验 {cards_dir} 里已有的 {len(slugs)} 份——漏复制的卡查不出来）")
    if not slugs:
        print("FAIL: 工程里没有 src/cards/*.tsx——所有动效都不是从卡片源码复制的")
        return 1

    bad = 0
    for slug in slugs:
        tpl = TEMPLATE / f"{slug}.tsx"
        got = cards_dir / f"{slug}.tsx"
        if not tpl.exists():
            print(f"SKIP {slug}: template 里没有这张卡（slug 拼错？）")
            bad += 1
            continue
        if not got.exists():
            print(f"MISS {slug}: 工程缺 src/cards/{slug}.tsx（没有复制卡源码 = 手写简化版）")
            bad += 1
            continue
        tpl_text = tpl.read_text()
        got_text = got.read_text()
        ratio = difflib.SequenceMatcher(None, norm(tpl_text), norm(got_text)).ratio()
        similarity_ok = ratio >= THRESHOLD
        type_required = bool(TEXT_STYLE.search(got_text))
        type_ok = not type_required or bool(TYPE_MARKER.search(got_text))
        ok = similarity_ok and type_ok
        bad += 0 if ok else 1
        detail = f"相似度 {ratio:.2f}"
        if not similarity_ok:
            detail += f" < {THRESHOLD}（改动大到不像同一张卡）"
        if not type_ok:
            detail += "；缺 production-type-mapped/exception 声明（旧 demo 字号未完成生产迁移）"
        print(f"{'OK  ' if ok else 'FAIL'} {slug}: {detail}")
    print(f"\n{'PASS' if bad == 0 else 'FAIL'}: {len(slugs) - bad}/{len(slugs)} 张卡保真")
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
