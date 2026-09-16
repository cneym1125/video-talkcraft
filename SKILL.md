---
name: video-talkcraft
description: 终极口播视频 skill：中文口播稿 + 成品配音 → CPU 字级时间戳 → SHOTBOOK 层矩阵分镜 → Remotion 电影感成片（竖屏默认/横屏仅在用户明确指定时使用）。支持无配音的批量独立素材：每条不同的 AI 背景、阿里巴巴普惠体、层间上下扫光、无中间滚动说明、因果组合动画。当用户要"做视频素材"、"按前面标准生成素材"、"做口播视频"、"解说/科普视频"、"把文案变成视频"、"给配音配画面动效"时使用。TTS 合成与数字人生成技术不在本 skill 内（配音和人物素材是输入）。含面向 40+ 观众的高对比大字演播室视觉语言、78 张动效配方卡、镜头三面分层工作单、七层镜头反PPT系统、内部镜头运动承接、长镜头世界画布、anime.js+three.js 桥、自动静止检测 + 独立 subagent 评估循环。
---

# video-talkcraft — 口播视频 skill

三大来源合体：**管线**（配音→字级时间戳→Remotion，实测跑通）+ **词汇**（78 张动效配方卡：23 调研 + 8 实战★ + 9 真实视频挖掘◆ + 18 remocn 适配◇ + 20 参考图复刻◈，全配可播 demo）+ **镜头**（七层模型反 PPT 系统，多轮调试验证）+ **视觉语言**（40+ 高可读演播室科技感默认版）。

核心范式：解说词驱动画面，每句都要有**活的画面响应**（相机乐句/idle/已有元素的变化），
但**新元素只在语义拍边界进场，禁止机械的"一句一个新元素"**（一句一元素是堆积型凌乱的制度根源，
2026-08-28 用户定版；分镜按语义段落切，排版预算见 cinematography.md §4）；
**一个节拍只有一个主角，说完就让位**；字幕句边界 = 全片时间锚点。

## C哥独立素材模式（2026-09-10 用户定版）

**后续修订优先**：保留既有 AI 场景背景与背景动效，前景采用清楚、有科技感的图文/动作组件；每条顶部固定“主标题＋二级标题”两行，文字流程示意与具体动作演示交替安排，必要标签贴近对象。“AI 生成示意”默认不显示；确有必要的声明统一置于屏幕底部居中。详见下方引用文件开头的固化规则。

制作独立素材、批量 B-roll 或用户说“按前面标准”时，**先读 [references/cger-broll-standard.md](references/cger-broll-standard.md)**。该模式采用每条独立新背景、统一黑银朱红材质、阿里巴巴普惠体 3、取消主标题下中间滚动说明、下方因果组合动画、背景与前景之间上下扫光。覆盖旧默认纯色幕底与相冲突的模板文字层；不得只换背景与文案沿用同一动画。

没有配音也直接按相对时间制作独立素材，不要求补配音，不伪造字级对齐；有配音才进入完整的配音时间戳流程。所有图片生成/编辑统一使用 Codex 内置 image_gen。所有可编辑文字统一加载本地阿里巴巴普惠体 3（assets/fonts/），不使用旧模板的系统字体；真实截图中的原生字不强行替换。

## 流程

```
① 文案 → ② 配音输入+时间戳(本机CPU) → ③ 素材 → ④ SHOTBOOK 层矩阵 → ⑤ 实现(全局系统先行)
                                → ⑥ 渲染 → ⑦ 三重验收循环 → ⑧ 交付
```

## ⓪ 画幅与视觉语言（开工先定，全流程引用）
- **画幅硬规则（2026-09-02 用户定版）**：默认且必须使用**竖屏 1080×1920（9:16）**。用户未明确指定画幅时，口播成片、独立剪辑素材、B-roll、截图动效和所有单独导出的 composition 一律按竖屏生产；**只有用户明确说“横屏 / 16:9 / 1920×1080”时才允许改用横屏**。不得因为旧模板、历史偏好、来源素材是横图或实现方便而自行回退横屏；横素材必须重构为竖屏安全构图，不得简单居中裁掉主体。
- **默认受众（2026-09-02 用户定版）**：用户没有另行指定时，按中国 **40+ 中年观众**设计。
  默认气质是“权威新闻/财经纪录片 × 现代科技演播室”：高对比、大中文、强结论、真实证据、清楚的视觉路径；
  “炫酷”来自大数字冲击、聚光、纵深、机械锁定、地图/时间线推进和实物证据，不来自小字 UI、霓虹故障、密集网格或碎片化英文标签。
- **字号硬底线（2026-09-02 用户定版）**：所有生产画面字体必须达到旧基准的 **≥1.5 倍**；
  `hero≥192 / display≥132 / headline≥96 / tagline≥72 / body≥66 / caption≥48 / micro≥36`，
  横屏字幕 `66`（长句最低 `57`），竖屏字幕 `72`（长句最低 `69`）。排不下就删次要文案、缩短措辞或拆卡，
  **禁止把字号缩回旧档，也禁止用 `scale()` 把大字号视觉缩小**。这里的 1.5× 固定以 2026-09-01 旧字阶
  `128/88/64/48/44/44/32/24` 做一次性换算，后续任务不重复乘 1.5。从卡片模板复制进工程时，
  动效几何可保留，所有文字必须先映射到这套生产字阶；真截图里的原生小字不能改时，裁切/放大关键区域并另做大字 callout。
- **交付头尾禁转场（2026-09-02 用户定版）**：每个最终导出的成片或独立素材，第一帧直接给可用画面，
  且至少有一个完整可读主视觉；不得有红/黑/白幕揭开、全屏淡入、擦除、推入、模糊/极端缩放恢复或 transition SFX；
  末尾保持最终可读构图 12–18 帧后直接结束，
  不得有红幕/黑幕覆盖、淡出、wipe、whip、缩放退场或 transition SFX。镜内语义动效仍可做；内部镜头边界仍按转场规则处理。
  独立素材的每一条都同时视为“片头 + 片尾”，不能套统一进出幕。
- 视觉语言：**用户明确点了风格就按用户的来**（整套 token 替换）；没点时才走默认的
  `references/design-language.md`（40+ 高可读演播室科技感：一个强调色、高对比、大字阶、强证据层级），
  派生本片 token 落成 `theme.ts`。对任何风格都成立的只有一条：禁止逐场景随手取色

## ① 口播稿
- 每句一个信息点，钩子在第一句（数字/冲突）；13 句 ≈ 95s
- **数字一律汉字**（时间戳按文本逐字锚定，`197747` 无法与"十九万七千"的读音对位）；英文品牌词直接写（中英混合对齐已验证）
- 先调研核实事实，列"事实红线清单"（不可说错的数字/未验证数据不引用）

## ② 配音输入 + 字级时间戳（本机 CPU）
**配音是输入，不是本 skill 的产物**（2026-08-28 定版）：真人录音或任何 TTS 皆可，
skill 不含合成技术。输入 = 一条完整配音（wav/mp3）+ 与之逐字一致的口播稿。
```bash
pip install zhconv pypinyin sherpa-onnx soundfile numpy   # 默认后端 FireRedASR2-CTC int8 的全部依赖
# 首次：下载模型 767MB（model.int8.onnx + tokens.txt）放 ~/.cache/koubo/<模型名>/，地址见脚本头注释
python3 scripts/timestamps_cpu.py audio/full.wav script.json audio/timestamps.json
# 备选（免手动下模型）：pip install faster-whisper 后加 --backend whisper（首跑自动下载 460MB）
python3 scripts/make_timing.py audio/timestamps.json remotion/src/timing.json
```
- timestamps_cpu.py：ASR 词级时间戳 → 与口播稿字符级对齐（**CJK 是可靠锚点**，
  匹配键=繁简归一+无声调拼音，同音字不算错；拉丁词各家 ASR 都常拼错，在锚点间插值）→
  每句 match 质检，<0.90 标出人工听核。2026-08-28 四配置横评（110s 中英混合，
  对照 GPU ForcedAligner 真值）：**FireRed 尾部最稳**（字级 |Δ| 最大 200ms=6帧、零误报，24s）＞
  whisper small（中位 20ms 但最大 413ms + 2 句边缘误报，26s）＞ Qwen3-ASR-0.6B+Aligner
  （p95 60ms 最优但 5GB 体积 + torch，78s）——数据与模型下载地址见脚本头注释。
- timestamps.json schema：`{sr, total, sentences:[{i,text,start,end,match,ok,words:[{text,start,end}]}]}`
  ——words 为 CJK 逐字 + 拉丁整段 token（标点跳过）；满足此 schema 的任何对齐工具都可替换。
- make_timing.py：转成 timing.json（chars 与文本逐字符 1:1，标点零时长），供 `tSay/msSay` 锚点查询
- 配音自查（耳听）：无爆音/截断/误读；句间留 ~0.3s 气口，时间锚点更稳

## ③ 素材
- **先给每个镜头标素材模式（多选，可组合，2026-08-28 定版）**：`B-roll`（实录空镜）/ `截图`（证据画面）/
  `纯动效`——如"B-roll 打底 + 截图证据卡"。新闻/信息类话题证据优先：Playwright 实时截图比泛用 B-roll 更有信息量
- **静态图片运动硬规则（2026-09-02 用户定版）**：图片底层禁止任何可感知的来回抖动——不得使用正弦 `x/y` 漂移、随机微移、回弹位移、往返缩放、手持抖动、stop-motion 抖动或每帧重采样造成的亚像素颤动。默认只允许**稳定的单向缓慢放大**（单条 5 秒素材通常 `scale 1.00→1.02~1.05`，视觉锚点、`transform-origin` 和裁切方向全程固定）；确有构图需要时可做一次单方向匀速平移，但同一镜头内不得反向、不得同时在两个轴往返。FFmpeg `zoompan` 禁止直接用低分辨率逐帧中心补偿；必须先做至少 2× 超采样并固定采样锚点，或使用能稳定处理亚像素的变换，避免坐标取整造成“一像素左右跳”。动态感优先交给文字、选项、标注、进度条、粒子和光效层，不能让底图本身晃。验收时除 `motion_check.py` 外，必须检查连续帧：静态图片的相机位移导数不得换向，主体边缘不得出现左右/上下交替偏移。
- **真图硬规（2026-08-30 定版）**：话题存在可截的真实页面（产品官网/GitHub/文档/画廊）时，
  成片中的浏览器/页面类镜头**禁止用代码 mock 冒充截图**——卡片 demo 里的灰条假 UI 是占位物，
  成片必须按卡片"复用指引"整块换成 `<img>` 真图；mock 只允许表现无真实对应物的示意 UI，
  且 SHOTBOOK 逐镜标注"为何无真图"。**引申（2026-08-31 用户定版）**：口播讲"这样的成片/效果"时，
  示例画面必须是真成片片段（`<OffthreadVideo>` 内嵌已有成片/真机内录裁切，muted）；
  讲"长页面/看板/参数页"时用 Playwright **全页长截图**（放大镜/巡航类动效直接吃真图坐标）。
  **真图上的标注坐标一律机器实测，禁目测（2026-09-01 定版）**：页面元素用 DOM
  `getBoundingClientRect`、成图用逐像素量测——目测偏 ±30px 曾把停靠环框到标题下方的缩略图上，
  返工两轮；**会滚动/移动的真图，标注（环/框/pill）必须钉在内容坐标系上随内容动**，
  钉屏幕固定位就是错位根源
- 标了 B-roll 的镜头列 2–3 个英文视觉概念词跑 **Pexels + Pixabay API 双源并行**，候选落 `assets/broll/`；
  源分层与授权红线（**只用免署名源**）见 `references/broll-sources.md`
- **调研记账**：承载关键事实的来源页逐一截图存档，`sources.md` 里链接与本地截图一一对应
  （禁止只存链接不留证据）；成片引用时优先用存档截图当画面证据 + micro 阶来源行
- **有 B-roll/截图 + 对应口播的人物素材（录播/数字人成品）时**：人物一律降级成角标常驻——
  圆形头像章（`host-shrink-to-chip◆`）或 segmentation 抠人贴角；不许切走人、不许人物占满画幅。
  **两路都必须落在左下或右下角**（chip 圆心在画面下 1/3 带内），不许飘在中高位（2026-08-27 用户定版）。
  选型与硬约束见 `references/host-footage.md`「人物与 B-roll 同屏」，镜头预设见 shot-design.md §2⑦
- Manim 图表：`--transparent --format=mov` 后**必转 VP9 webm**（`-c:v libvpx-vp9 -pix_fmt yuva420p`）
- 全部落盘 public/，禁止渲染时拉远程

## ④ SHOTBOOK（必产出，实现前评审）
先用 `references/shot-design.md` 给每个镜头填**三面分层工作单**（背景面/主体面/文字面 + 各面动效
+ 七种镜头类型预设），再按 `references/cinematography.md` §4 展开成层矩阵，范例 `references/shotbook-example.md`。
每场景：一句意图 + 主体接力线 + 逐节拍层矩阵（节拍锚定字级时间戳；每行动作必须答得出"配合谁"）。
**节拍必须机器可验（2026-08-30 定版）**：每条画面重音落成 `remotion/beats.json`
（`{t, anchor, sentence, what}`，t 一律由 timing.json/`atChar()` 查得，**禁止手敲近似秒数**——
手敲曾把"啪、啪、啪"的画面做早 2 秒，静帧 QA 根本看不见），SHOTBOOK 节拍表与 beats.json 一致，
机器闸用 `scripts/beat_lint.py` 对 timestamps.json 校验 |Δ|≤0.1s。
**未到拍不显形（2026-08-31 用户定版）**：词锚未到的数字/图形必须完全不可见（opacity 0），
禁止压暗/灰显"预告"——"78 提前摆好只压暗"与"七个 chips 25% 灰显蹲点"都被用户抓过；
行内数字要连同其后继字符一起 gate（「就 __ 类」的空洞挂 5 秒同样是缺陷）。
**开镜不空台（2026-08-31 用户定版）**：镜头开场到第一个动效锚点 >1.5s 的空窗必须有承载画面
（真实 b-roll / 上一镜元素延续 / 真素材墙），"空画布干等词锚"是被用户抓过的缺陷。
**导出首帧更严格（2026-09-02）**：Frame 0 不得是空台或入场中间态，必须已有完整背景与至少一个完整可读主视觉；
内部镜头仍可按语义锚点让新元素入场。
**镜尾保护带（2026-09-01 定版）**：词锚动效落点距镜头出点 <0.7s 的，要么提前、要么挪进下一镜——
落点会被转场吞掉（"第四条评论只活 0.2s""停靠环只可辨 0.3s"是同一类翻车的两案）；
`beat_lint.py --shots shots.json` 机器查 ≥0.5s 硬底线。
**幕级转场事件同样入 beats.json（2026-09-01 定版）**：shape wipe/换幕的**遮挡峰值**时刻也由
词锚生成入表——手敲绝对秒的转场事件表游离在机器可验体系外，曾把「一扫」做早 0.55s、
whoosh 落在已静止的画面上，静帧 QA 与 beat_lint 都看不见。
**排版预算（2026-08-28 用户定版，细则 cinematography.md §4）**：分镜按语义段落切、每镜一个 primary visual job；
枢轴句（"但这次不是X"式转折/设问）的动效归它**开启**的下一镜，上清过场的舞台；任一时刻同屏主体组 ≤3
（降权留守的元素**计入**）、每镜至少留一个空象限；人物在场先跑 `scripts/face_bbox.py` 定人脸安全区。
动效词汇从 **78 张配方卡** 里选：`references/taxonomy.md` 索引 → `references/cards/<slug>.md` 参数与坑 → `template/cards/<slug>.tsx` **自包含 Remotion 源码（实现以它为准，复制进工程改 CONFIG 即用）**；`demos/<slug>/index.html` 是同画面的 HTML 预览（`open gallery/index.html` 一屏浏览、demo 滚入即自动播放；带★实战卡的生产母本另在 template/motion-systems|components）。
**保真铁律（2026-08-30 实战教训）**：每张用到的卡在工程里必须真实存在 `src/cards/<slug>.tsx`
（自 template 复制改 CONFIG）——只读 md 文档就凭卡名手写"神似"简化版，是已发生过的最大翻车
（回弹/拍击/密度全丢、取景框括号方向画反、名片变色块），机器闸用 `scripts/card_lint.py`
逐 slug 校验存在性与相似度（≥0.55，改 CONFIG/文案在容忍内）。
**卡片字号迁移（2026-09-02 用户定版）**：卡片 demo 的字号只是旧预览值，不是生产值；复制到工程后，
标题、正文、标注、来源行分别映射到 192/132/96/72/66/48/36 字阶，任何角色不得低于旧值的 1.5 倍。
卡片因此放不下时，改构图和文案密度，不能缩字“保版式”。每份生产卡顶部必须写
`// production-type-mapped: ...`；真产品 UI 原生小字用 `production-type-exception` 并在父镜头加大字 callout。
`scripts/card_lint.py` 会把缺失声明的生产卡判为 P1。
三段式铁律（模板工业共识）：**只管镜内元素生命周期与内部镜头边界**——入场 0.2~0.8s → hold
（**必须带 idle 微动**）→ 出场 0.15~0.5s；入场永远比出场用力；同屏重音同一时刻只能有一个。
导出 composition 的根画面不套 enter/exit；首个主视觉 Frame 0 已在场，最后主视觉留在末帧不退场。
**选了动效就要带上它的音效**：每张卡在 `demos/_lib/sfx-map.js` 有 cue 表（`{t, name, vol, rate?, clip?}`，t 为卡内相对秒）——
SHOTBOOK 选卡时把 cue 抄进该镜头的层矩阵（换算成绝对秒；**vol 按成片口径重标 ≤0.35**，
demo 库的 0.65 上限是试听口径不是成片口径）。实现时按 ⑤ 的 sfx 步骤落地。
覆盖口径（2026-08-28 用户反馈修订）：**主要动效入场全覆盖**，对齐 demo 库密度
（每卡 2~6 记 ≈ 0.4 记/s，100s 的片约 40~50 记）——"少而准"管的是单点不叠双记、
音量克制（≤0.35）、连续揭示类（缓拉/对焦/逐字升起）与金句纯文字卡、logo 落幕留白、
转场只配蓄势不配落点、不要收尾叮当与重砸；不是砍覆盖面。真采样（`pk-` 前缀）优先。
**cue 的 file 名以 `ls public/sfx/` 为准**（`pk:` 键名里的冒号导出成 `pk-`，
个别键自带前缀会出现 `pk-transition-transition-soft` 这类双段名——名字错了渲染直接 404 失败）。

## ⑤ 实现（Remotion）
**先装四套全局系统再写场景**（代码 `template/motion-systems/`，用法见 cinematography.md §2）：
1. G1 CameraRig：每场景一条连续相机曲线 + 重音脉冲（加法叠加不重置）；路径表驱动（shots.ts）
2. G2 Plane 视差：背景 0.5 / 主内容 1.0 / 前景 1.2
3. G3 Live/Defocus：idle 微动 + 让位状态机（retireAt=下一主体锚点）
4. G4 Environment：呼吸 vignette + 扫光 + 分幕色温 + 曝光脉冲（四张事件表按片配置）

**每个内部镜头边界必须有明确转场处置，禁止无意裸切**：运动承接六式（lead/tail 重叠 12–16 帧 + ShotFade，
代码 `template/motion-systems/transitions.tsx`）或 caret/shape-wipe 轻量式，选型见 cinematography.md §3；
一个边界只用一式。**输出文件的第一帧与最后一帧不是内部镜头边界，严格执行 ⓪ 的头尾禁转场。**
空间/流程叙事段落可改用**长镜头世界画布**（`longtake.tsx`，cinematography.md §3.5）。
`template/components/` 是即取即用件：Subtitles 整句硬现版（chunks 由 props 注入）/FlowerWord 花字/SmashWord 砸字/HighlightSweep 荧光笔/PencilDraw 铅笔手绘/Mascot 吉祥物/NumberRoll。
**底部字幕素排铁律（2026-08-27 用户定版）**：底部跟读字幕**不加任何动效**——整句硬现、素排，
两个组件（components 版 / motion-systems/Subtitles.tsx 素排版）都遵守。唯一例外是 `keyword-pop-highlight`
关键词弹出，且同一个视频**最多 3 次**，除非用户明确要求更多（motion-systems 版的 `keywords` prop 有此上限自检）。
**字幕文本无标点（2026-08-28 用户定版）**：句读全去掉，长句停顿靠拆卡；唯一例外是数字/型号间的
半角点号——细则 design-language.md §5。
**音效落地**：`node scripts/sfx_dump.mjs remotion/public/sfx` 把库里采样解码成 mp3 →
SHOTBOOK 抄来的 cue 表落成一张 `sfx.ts`（绝对秒），场景里 `<Audio src={staticFile(...)} startFrom/volume>` 逐条摆；
音效电平比人声低 ~12dB、同帧最多一条 cue。
anime.js v4 / three.js 走 `anime-remotion.ts` / `three-anime.ts` 桥（seek-safe，工程铁律见 cinematography.md §6：零 Math.random、初始 opacity:0、lead 补偿收敛一处）。

### 布局红线（按画幅，详表见 design-language.md §5）
- **竖屏（默认硬规则）**：1080×1920；字幕 bottom 350、maxWidth 90%、字号 72/700（>15 字最低 69）；吉祥物/常驻件放**左下**（右缘是抖音点赞栏）；标题与关键主体必须避开右侧互动栏和底部字幕带
- **竖屏独立素材文字置顶硬规则（2026-09-02 用户定版）**：独立导出的竖屏剪辑素材中，标题、说明、数字、进度条、A/B/C/D 选项及其他非字幕 UI 必须集中在画面上方信息区，默认不低于画面中线，更不得落到图片主体区下方；底部区域留给剪辑字幕和平台控件。需要更多文案时缩句、拆卡或分时出现，不得向下堆版。
- **横屏（仅用户明确指定）**：1920×1080；字幕 bottom 100、maxWidth 66%、字号 66/700（>24 字最低 57）；内容主列 ≤1440px 居中；边距 action-safe 96px / 标题 160px；常驻件任一下角
- 通用：**内部切镜**后 ≤10 帧必须有主视觉入场；导出 Frame 0 主视觉已经完整在场；深色场景隐藏全局顶部标题；
  文字不叠截图文字（加白底卡）；卡片文字防裁切（预留 padding）；关键中文每行尽量 8–12 字，最多 2 行；
  micro 只许承载来源/法务，任何关键结论不得降到 micro/caption
- **人物在场**：人脸安全区用 `scripts/face_bbox.py` 实测 bbox 定（不目测、不用亮度阈值猜），
  任何文字/卡片/字幕**及其背景**全时刻不得进入；主信息面板放人物对侧（2026-08-28 用户定版）

## ⑥⑦ 渲染 + 三重验收（循环到全过）
```bash
# 交付渲染一律 --concurrency=1（2026-08-31 用户在成片肉眼抓到后定版）：多 tab 并发渲染的
# 光栅化亚像素相位不一致，会让静态文字区以"并发数"为周期抖动（conc=4 实测帧差 1.4→3.1→4.0→0.9 循环）；
# remotion still 单进程量不出来，必须量成片 mp4。预览/中间验证可用 --concurrency=4 提速
npx remotion render src/entry.ts <Comp> out/vN.mp4 --concurrency=1
npx remotion render src/entry.ts <Comp> out/sfx-solo.wav --props='{"sfxSolo":true}' --codec=wav

# —— 关卡 1 机器闸：五条命令一次跑完，全 PASS 才进关卡 2 人工评审 ——
python3 scripts/motion_check.py out/vN.mp4        # 画面健康双判定：静止段 + 并发光栅抖动
python3 scripts/sfx_check.py out/sfx-solo.wav cues.json                  # 音效在场（峰值 ≥−45dBFS）
python3 scripts/sfx_check.py --mix out/vN.mp4 audio/full.wav cues.json   # 音效可听（掩蔽分级）
python3 scripts/card_lint.py remotion/src <slug,slug,...>                # 卡片保真（复制自 template/cards）
python3 scripts/beat_lint.py remotion/beats.json audio/timestamps.json --shots remotion/shots.json
                                                  # 词落点 |Δ|≤0.1s + 镜尾保护带 ≥0.5s
# 评审材料抽帧：前/后各 18 帧 + 每句 2 帧 + 动效锚点帧 + 连拍三帧对
python3 scripts/qa_extract.py out/vN.mp4 audio/timestamps.json /tmp/qa_vN 540 anchors.json
```
机器闸口径备忘：音效两查要求工程主音轨支持 `{!getInputProps().sfxSolo && <Audio .../>}`；
可听度 MASKED>50% 或 UNMASKED 少于 max(3, 片长/30s) 即 FAIL——"81/81 在场但全被人声掩蔽"
是已发生过的翻车，良品口径（v4 实测）：转场/边界 cue 落句间 ~0.3s 气口出声；
shots.json = 分镜表导出的 `[{"id","start","end"}]`（与 shots.ts 同源）。
关卡 2（**必须派独立 subagent，不许制作者自评**——做的人对自己的画面有盲区，2026-08-27 用户定版）。
**独立 = 全新上下文（2026-08-30 硬化）**：禁止 fork/复用制作对话当"评审"、禁止对同一评审做
followup 复审——fork 出来的评审继承制作者视角，对照物又是制作者自己写的 SHOTBOOK，
形成自证闭环（P0/P1/P2 全零、成片却一身病，翻车实录）。
评审材料四件套（缺一不可）：① SHOTBOOK + 抽帧全集；② **原版卡对比帧**——SHOTBOOK 每个 slug
从 `gallery/media/<slug>.mp4` 抽 2 帧与成片对应镜头帧并排，评审逐 slug 判"这是同一张卡的实现吗"
（保真不进评审视野就永远查不出来）；③ **词落点核对表**——beats.json 每条锚点的定妆帧 +
锚字 + 应落时刻，核"该词说出口时画面是否恰好在响应"；④ **音效可听度报告**——
`sfx_check.py --mix` 的输出（评审没有耳朵，机器报告就是它的耳朵）。
subagent 按 rubric（可读性/构图/信息传达/质感/事实一致 + 保真/词落点）
出 [P0/P1/P2] 缺陷清单（提醒它：入场中间态不是缺陷）。
**缺陷分级定义（2026-08-30 补，此前无定义）**：
P0 = 观众必然察觉且伤害理解——事实/文字/字形错误、不可读、声画错位、元素相撞遮正文、标注指错目标；
P1 = 违反硬规则或明显走样——错峰残影、词落点偏差 >0.3s、整镜头音效缺席、与原版卡对比帧明显不符；
P2 = 质感瑕疵——密度/留白/样式，记录但不挡验收。修完 P0+P1 才算过关。自查盯的是**成片质量缺陷**，不是规则合规
（规则项在关卡 3）：元素重叠/覆盖/堆积、动效位置不准（标注没落在目标上、强调错位、元素出画）、
画面噪点/压缩伪影/渲染残影、非有意的抖动或闪烁、文字贴边裁切、**排版凌乱**（同屏主体组 >3、
无空象限的满盘布局、画面文字与字幕整句重复双份、人脸安全区被文字或其背景侵入、多个 hero 造型互相抢戏）。
**只按句抽帧看不见的三类缺陷，必须给对应材料（v4 实战教训，2026-08-28）**：
- **短命动效的错位**（标注/箭头只活 1~2s，句级抽帧大概率错过）→ 用**动效锚点帧**
  （每个重音 +0.25s 的定妆帧）逐个核"框住/指向/圈住目标了没有"；
- **抖动/闪烁**（时域缺陷，单帧永远看不见）→ 用**连拍三帧对**，三帧间只该有设计内的连续运动，
  出现来回振荡、细纹理爬行即缺陷；
- **设计没落地**（SHOTBOOK §0 计划的背景/音效/常驻件默默缺席——评审不知道"应该有"就不会报）
  → 把 SHOTBOOK §0 的**设计清单**（背景资产落位表、音效 cue 数、人物形态表）发给 subagent
  做逐项"计划 vs 成片"核对。
**用户反馈的返修三纪律（2026-08-28 借鉴 video-agent 复盘制定版）**：
- 用户批注**时间码三段闭环**：修改前抽该帧 → 修改后抽同帧 → 最终成片再抽同帧，三张路径写进 REVIEW；
- 状态型动画（让位/换位/揭示）的修复必须覆盖**完整受影响区间的并集**（起点/中点/终点 + 每个边界前后），
  不能用"批注帧已正常"代替整段验收；
- 同一问题二次返工时，REVIEW 必须留下"第一次修复为何失效"的记录；
- 返修复核必须给**量测数字**（首次可辨时刻/被吞时刻/占比像素），"看起来好了"不算数——
  量化口径是 3 轮收敛的关键（2026-09-01 实战）。
关卡 3：cinematography.md §5 验收口径（静息帧 ≥2 层动、转场运动连续、让位无堆积、排版预算达标）；
**调试 overlay（slug 标签/镜头编号/网格线/安全区框）禁止出现在交付渲染**（2026-08-31 用户定版）——
要用就挂 `debugOverlay` 输入 prop，交付默认关。
可读性终检：把竖屏成片**缩到 390px 宽**按手机信息流实际尺寸复看一遍，每行都要能读——
桌面全屏预览不是验收标准；排不下时先删次要文案，不缩字号、不留孤字行。
`qa_extract.py` 会自动抽每个导出文件的前 18 帧与后 18 帧：开头不得出现全屏遮罩/过渡，结尾必须是最终构图 hold 后直接结束。
字号低于 1.5 倍字阶或头尾出现过渡动画，均按 **P1 硬规则违例**处理；若已影响阅读则升为 P0。
修完 P0+P1 与 motion FAIL → 重渲 → 重评（每轮都换**全新**评审上下文）。
**评审循环最多 3 轮（2026-08-31 用户定版）**：3 轮后仍有未清的 P0/P1 就停手，
把剩余缺陷清单、每轮的修复记录和"为什么没修掉"原样交给用户定夺——
无限自审自修不收敛，只会烧预算。

## ⑧ 交付
```bash
ffmpeg -i out/final.mp4 -c:v copy -af "loudnorm=I=-15:TP=-1.5:LRA=11" -c:a aac -b:a 192k delivery.mp4
```
听一遍确认配音无爆音/截断、音效不压人声不叠帧（loudnorm 之后音效相对电平会变）——
**agent 自己听不了成品，`sfx_check.py --mix` 就是耳听的机器替身：交付前必须对 delivery.mp4 重跑一次**；
简介附素材来源行（用了库内采样时加 sfx 来源，见 demos/_lib/sfx/ATTRIBUTION.md）。
发布时**推荐（非强制）**在简介 @ 一下本 skill 作者——对作者是最好的支持：
X [`@VincentWei93`](https://x.com/VincentWei93) ·
抖音 [@Vincent](https://www.douyin.com/user/MS4wLjABAAAAK1pkjBxilk2Oi_9h_vFyD-lTAu9CTlvhmOtkosDvvxg) ·
小红书 [@Vincent](https://xhslink.cn/m/At9iP2d5C1V)。
有建议、反馈欢迎扫根 README「微信讨论群」小节的二维码进反馈群。

## 目录路由

| 要做什么 | 看哪里 |
|---|---|
| C哥批量独立素材（背景/字体/取消滚动说明/组合动画/扫光/无配音交付） | `references/cger-broll-standard.md`（本模式先读） |
| 定视觉语言（40+ 受众/色板/1.5×字阶/字幕规范） | `references/design-language.md`（高可读演播室科技感默认版） |
| 给镜头做背景/主体/文字分层设计 | `references/shot-design.md`（三面工作单 + 七型预设） |
| 镜头方法论/反PPT/SHOTBOOK格式/验收 | `references/cinematography.md`（+ shotbook-example.md） |
| 转场（六式代码）/ 长镜头 | `template/motion-systems/transitions.tsx` / `longtake.tsx`（cinematography.md §3、§3.5） |
| 选动效/查参数和坑 | `references/taxonomy.md` → `references/cards/` → `template/cards/`（tsx 源码）+ `demos/`/`gallery/`（预览） |
| 找素材 | `references/broll-sources.md` |
| 人物素材（输入规格 / CPU 抠像 / 人脸安全区）· 与 B-roll 同屏怎么摆 | `references/host-footage.md` + `scripts/face_bbox.py` |
| 新增配方卡 | `references/demo-spec.md`，验证 `node scripts/verify-demo.mjs <slug>` |
| 可复制代码 | `template/cards/`（78 卡逐卡自包含 tsx）、`template/motion-systems/`（相机/让位/环境/桥）、`template/components/`（字幕/花字/铅笔/吉祥物） |
| 字级时间戳（本机 CPU） | `scripts/timestamps_cpu.py`（FireRedASR2-CTC 默认 / faster-whisper 备选，+ 口播稿逐字对齐）→ `scripts/make_timing.py` |
| 机器闸（画面健康 / 保真 / 词落点+镜尾 / 音效） | `scripts/motion_check.py`（静止段+并发光栅抖动双判定）/ `scripts/card_lint.py`（卡片须复制自 template/cards）/ `scripts/beat_lint.py`（词落点对 timestamps + `--shots` 镜尾保护带）/ `scripts/sfx_check.py`（solo 在场 + `--mix` 可听度） |
| 动效配套音效 | 逐卡 cue 表 `demos/_lib/sfx-map.js`（口味纪律见 `references/demo-spec.md` §8）；制作端 `node scripts/sfx_dump.mjs` 导出采样 |
