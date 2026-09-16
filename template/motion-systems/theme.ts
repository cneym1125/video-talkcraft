export const C = {
  bg: '#071426',
  bgPanel: 'rgba(18, 35, 59, 0.90)',
  accent: '#FF5A52',
  // Compatibility aliases share one accent by default. Pick a different single
  // accent for the whole production instead of enabling all three colors.
  cyan: '#FF5A52',
  gold: '#FF5A52',
  red: '#FF5A52',
  green: '#63E6A4',
  text: '#FFFFFF',
  dim: '#CFD8E6',
  line: 'rgba(255, 90, 82, 0.24)',
  gridLine: 'rgba(255, 255, 255, 0.08)',
};

export const FONT = {
  cn: '"PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif',
  mono: 'Menlo, "SF Mono", "Cascadia Code", monospace',
};

// 2026-09-02 user baseline: one-time 1.5x upgrade from the legacy type scale.
// These are hard production floors, not demo recommendations. If content does
// not fit, shorten/split the copy instead of shrinking or visually scaling it.
export const TYPE_SCALE = 1.5;
export const T = {
  hero: 192,
  display: 132,
  headline: 96,
  tagline: 72,
  body: 66,
  subtitle: 66,
  subtitleLong: 57,
  subtitleVertical: 72,
  subtitleVerticalLong: 69,
  caption: 48,
  micro: 36,
} as const;

export const gridBg: React.CSSProperties = {
  backgroundColor: C.bg,
  backgroundImage:
    `linear-gradient(${C.gridLine} 2px, transparent 2px),` +
    `linear-gradient(90deg, ${C.gridLine} 2px, transparent 2px)`,
  backgroundSize: '108px 108px',
};
