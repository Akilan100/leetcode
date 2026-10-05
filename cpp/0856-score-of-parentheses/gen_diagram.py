#!/usr/bin/env python3
"""
Generate algorithm visualization diagram for LeetCode 856 - Score of Parentheses
Dark-mode, neon accent colors, matches existing repo aesthetic.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch

# --- Palette ---
BG          = '#0d1117'
PANEL_BG    = '#161b22'
PANEL_BORD  = '#30363d'
CYAN        = '#00d4ff'
GREEN       = '#39ff14'
AMBER       = '#ffb700'
CORAL       = '#ff4d6d'
PURPLE      = '#bd93f9'
WHITE       = '#e6edf3'
MUTED       = '#8b949e'

# --- Figure setup ---
DPI = 100
W_PX, H_PX = 2863, 1470
fig = plt.figure(figsize=(W_PX / DPI, H_PX / DPI), dpi=DPI, facecolor=BG)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_facecolor(BG)
ax.set_xlim(0, W_PX)
ax.set_ylim(0, H_PX)
ax.axis('off')

# --- Helper: rounded rectangle ---
def rounded_rect(ax, x, y, w, h, color, alpha=1.0, radius=18, edge=None, lw=2):
    edge = edge or color
    box = FancyBboxPatch((x, y), w, h,
                          boxstyle=f"round,pad=0,rounding_size={radius}",
                          linewidth=lw, edgecolor=edge,
                          facecolor=color, alpha=alpha,
                          zorder=2)
    ax.add_patch(box)
    return box

# --- Outer border glow ---
for lw, alpha in [(8, 0.12), (4, 0.22), (2, 0.5)]:
    rounded_rect(ax, 20, 20, W_PX - 40, H_PX - 40, 'none', radius=30,
                 edge=CYAN, lw=lw, alpha=alpha)
rounded_rect(ax, 20, 20, W_PX - 40, H_PX - 40, PANEL_BG, radius=30,
             edge=CYAN, lw=1.5, alpha=1.0)

# ===========================================================================
# HEADER
# ===========================================================================
HEADER_Y = H_PX - 120

# Difficulty badge (left)
rounded_rect(ax, 60, HEADER_Y - 28, 180, 56, '#2d1b00', radius=28,
             edge=AMBER, lw=2)
ax.text(150, HEADER_Y, 'Medium', ha='center', va='center',
        fontsize=26, color=AMBER, fontweight='bold', zorder=5)

# Title (center)
ax.text(W_PX / 2, HEADER_Y + 10, '856. Score of Parentheses',
        ha='center', va='center', fontsize=42, color=WHITE,
        fontweight='bold', zorder=5)
ax.text(W_PX / 2, HEADER_Y - 32, 'Algorithm Trace  ·  Bit-Shift Approach (O(1) Space)',
        ha='center', va='center', fontsize=24, color=MUTED, zorder=5)

# Complexity badge (right)
rounded_rect(ax, W_PX - 460, HEADER_Y - 32, 400, 64, '#001a2e', radius=32,
             edge=CYAN, lw=2)
ax.text(W_PX - 260, HEADER_Y, 'Time: O(N)  |  Space: O(1)',
        ha='center', va='center', fontsize=24, color=CYAN,
        fontweight='bold', zorder=5)

# --- Separator line ---
SEP_Y = HEADER_Y - 75
ax.plot([60, W_PX - 60], [SEP_Y, SEP_Y], color=PANEL_BORD, lw=2, zorder=3)

# ===========================================================================
# SECTION TITLES
# ===========================================================================
LEFT_CX   = W_PX * 0.27
RIGHT_CX  = W_PX * 0.74
BODY_TOP  = SEP_Y - 45

ax.text(LEFT_CX, BODY_TOP, '⚡ Step-by-Step Execution Trace',
        ha='center', va='top', fontsize=28, color=WHITE, fontweight='bold', zorder=5)
ax.text(RIGHT_CX, BODY_TOP, '◆ Depth & Score Accumulation Flow',
        ha='center', va='top', fontsize=28, color=WHITE, fontweight='bold', zorder=5)

# vertical divider
DIV_X = W_PX * 0.50
ax.plot([DIV_X, DIV_X], [130, BODY_TOP - 10],
        color=PANEL_BORD, lw=2, linestyle='--', zorder=3)

# ===========================================================================
# LEFT PANEL: algorithm key + step table
# ===========================================================================
s       = '(()(()))'
depths  = []
scores  = []
events  = []
depth   = 0
score   = 0

for i, c in enumerate(s):
    if c == '(':
        depth += 1
        added = 0
        evt   = ''
    else:
        depth -= 1
        if i > 0 and s[i - 1] == '(':
            added = 1 << depth
            score += added
            evt   = f'score += 1 << {depth} = {added}'
        else:
            added = 0
            evt   = '—'
    depths.append(depth)
    scores.append(score)
    events.append(evt)

# --- Key insight box ---
KEY_TOP  = BODY_TOP - 60
KEY_W    = int(W_PX * 0.44)
KEY_H    = 150
KEY_X    = 60
rounded_rect(ax, KEY_X, KEY_TOP - KEY_H, KEY_W, KEY_H, '#0d1a0d', radius=18,
             edge=GREEN, lw=2)
ax.text(KEY_X + 30, KEY_TOP - 22, '⚙  Core Bit-Shift Invariant', fontsize=22, color=GREEN,
        fontweight='bold', va='top', zorder=5)
ax.text(KEY_X + 30, KEY_TOP - 60,
        "When s[i] == '('  →  depth++\n"
        "When s[i] == ')'  →  depth--\n"
        "  If s[i-1] == '(' → score += (1 << depth)   // Innermost () adds 2^depth",
        fontsize=19, color=WHITE, va='top', zorder=5,
        fontfamily='monospace', linespacing=1.5)

# --- Step table ---
TABLE_TOP = KEY_TOP - KEY_H - 30
ROW_H     = 68
COL_W     = [60, 90, 130, 90, 100, 390]   # i, char, op, depth, score, event
COL_X     = [KEY_X + 15]
for w in COL_W[:-1]:
    COL_X.append(COL_X[-1] + w)

HEADERS = ['i', 'char', 'operation', 'depth', 'score', 'event & explanation']

# header row bg
rounded_rect(ax, KEY_X, TABLE_TOP - ROW_H + 5, KEY_W, ROW_H,
             '#1c2128', radius=10, edge=PANEL_BORD, lw=1.5)
for j, (h, hx) in enumerate(zip(HEADERS, COL_X)):
    ax.text(hx + COL_W[j] / 2, TABLE_TOP - ROW_H/2 + 5,
            h, ha='center', va='center', fontsize=20, color=CYAN,
            fontweight='bold', zorder=5)

ops = ['depth++', 'depth++', 'depth-- (check)', 'depth++', 'depth++',
       'depth-- (check)', 'depth-- (check)', 'depth-- (check)']

for row_i, (char, op, d, sc, ev) in enumerate(zip(s, ops, depths, scores, events)):
    ry = TABLE_TOP - (row_i + 2) * ROW_H + 5
    is_score_row = ev and ev != '—'
    row_bg   = '#14261a' if is_score_row else '#12161f'
    row_edge = GREEN     if is_score_row else PANEL_BORD
    rounded_rect(ax, KEY_X, ry, KEY_W, ROW_H - 6,
                 row_bg, radius=8, edge=row_edge, lw=1.5)

    # i
    ax.text(COL_X[0] + COL_W[0]/2, ry + ROW_H/2 - 3,
            str(row_i), ha='center', va='center',
            fontsize=20, color=MUTED, zorder=5)
    # char
    c_color = AMBER if char == '(' else CORAL
    ax.text(COL_X[1] + COL_W[1]/2, ry + ROW_H/2 - 3,
            char, ha='center', va='center',
            fontsize=26, color=c_color, fontweight='bold', fontfamily='monospace', zorder=5)
    # op
    op_color = CYAN if '++' in op else PURPLE
    ax.text(COL_X[2] + COL_W[2]/2, ry + ROW_H/2 - 3,
            op, ha='center', va='center',
            fontsize=17, color=op_color, fontweight='bold', zorder=5)
    # depth
    ax.text(COL_X[3] + COL_W[3]/2, ry + ROW_H/2 - 3,
            str(d), ha='center', va='center',
            fontsize=22, color=CYAN, fontweight='bold', zorder=5)
    # score
    ax.text(COL_X[4] + COL_W[4]/2, ry + ROW_H/2 - 3,
            str(sc), ha='center', va='center',
            fontsize=22, color=GREEN, fontweight='bold', zorder=5)
    # event
    ev_color = GREEN if is_score_row else MUTED
    ax.text(COL_X[5] + COL_W[5]/2, ry + ROW_H/2 - 3,
            ev if ev else '', ha='center', va='center',
            fontsize=18, color=ev_color, fontfamily='monospace', zorder=5)

# ===========================================================================
# RIGHT PANEL: Visual representation of depth & score
# ===========================================================================
CHART_L   = int(DIV_X + 50)
CHART_R   = W_PX - 60
CHART_W   = CHART_R - CHART_L
CHART_TOP = BODY_TOP - 60
CHART_BOT = 200

GRAPH_TOP = CHART_TOP - 40
GRAPH_BOT = CHART_BOT + 180

GRAPH_H   = GRAPH_TOP - GRAPH_BOT
GRAPH_W   = CHART_W - 60

n_steps = len(s)
bar_w   = GRAPH_W / n_steps * 0.52
step_x  = [CHART_L + 50 + GRAPH_W * (i + 0.5) / n_steps for i in range(n_steps)]

# --- Depth chart container ---
rounded_rect(ax, CHART_L, GRAPH_BOT - 100, CHART_W, GRAPH_H + 170, '#11151c', radius=18,
             edge=PANEL_BORD, lw=1.5)

# Grid lines
max_depth = 3
BAR_UNIT  = (GRAPH_H - 80) / (max_depth + 1)

for gd in range(0, max_depth + 2):
    gy = GRAPH_BOT + gd * BAR_UNIT
    ax.plot([CHART_L + 50, CHART_L + 50 + GRAPH_W], [gy, gy],
            color=PANEL_BORD, lw=1, linestyle=':', alpha=0.6, zorder=3)
    ax.text(CHART_L + 30, gy, str(gd), ha='right', va='center',
            fontsize=18, color=MUTED, zorder=5)

ax.text(CHART_L + 15, GRAPH_BOT + GRAPH_H / 2 - 20, 'depth level',
        ha='center', va='center', fontsize=18, color=MUTED,
        rotation=90, zorder=5)

for i, (d, sc) in enumerate(zip(depths, scores)):
    bx   = step_x[i]
    char = s[i]
    bar_h = d * BAR_UNIT
    is_score = events[i] and events[i] != '—'

    bar_color = CYAN if char == '(' else PURPLE
    if is_score:
        bar_color = GREEN
    rect = mpatches.Rectangle(
        (bx - bar_w/2, GRAPH_BOT), bar_w, bar_h,
        linewidth=1.5, edgecolor=bar_color,
        facecolor=bar_color, alpha=0.5, zorder=4)
    ax.add_patch(rect)
    ax.plot([bx - bar_w/2, bx + bar_w/2],
            [GRAPH_BOT + bar_h, GRAPH_BOT + bar_h],
            color=bar_color, lw=3, alpha=0.9, zorder=5)

    # depth label
    ax.text(bx, GRAPH_BOT + bar_h + 12, f"d={d}",
            ha='center', va='bottom', fontsize=17,
            color=bar_color, fontweight='bold', zorder=6)

    # score bubble when score added
    if is_score:
        added = 1 << d
        bubble_y = GRAPH_BOT + bar_h + 55
        rounded_rect(ax, bx - 60, bubble_y, 120, 44, '#14261a',
                     radius=22, edge=GREEN, lw=2)
        ax.text(bx, bubble_y + 22, f'+{added} pts', ha='center', va='center',
                fontsize=18, color=GREEN, fontweight='bold', zorder=7)
        ax.plot([bx, bx], [GRAPH_BOT + bar_h + 3, bubble_y - 2],
                color=GREEN, lw=1.5, linestyle=':', zorder=5)

# --- Character timeline row ---
TL_Y = GRAPH_BOT - 50
for i, char in enumerate(s):
    bx     = step_x[i]
    c_col  = AMBER if char == '(' else CORAL
    is_sc  = events[i] and events[i] != '—'
    bg     = '#14261a' if is_sc else '#1c2128'
    ec     = GREEN    if is_sc else c_col
    rounded_rect(ax, bx - 30, TL_Y - 30, 60, 60, bg,
                 radius=10, edge=ec, lw=2)
    ax.text(bx, TL_Y, char, ha='center', va='center',
            fontsize=28, color=c_col, fontweight='bold',
            fontfamily='monospace', zorder=6)
    ax.text(bx, TL_Y - 42, f"i={i}", ha='center', va='center',
            fontsize=15, color=MUTED, zorder=6)

# Legend
legend_y = GRAPH_TOP + 35
ax.text(CHART_L + 60, legend_y, '■', fontsize=20, color=CYAN, va='center')
ax.text(CHART_L + 80, legend_y, "Open '(' -> depth++", fontsize=17, color=MUTED, va='center')
ax.text(CHART_L + 340, legend_y, '■', fontsize=20, color=PURPLE, va='center')
ax.text(CHART_L + 360, legend_y, "Close ')' (no add)", fontsize=17, color=MUTED, va='center')
ax.text(CHART_L + 620, legend_y, '■', fontsize=20, color=GREEN, va='center')
ax.text(CHART_L + 640, legend_y, "Innermost '()' -> score += 1<<depth", fontsize=17, color=MUTED, va='center')

# ===========================================================================
# BOTTOM: complexity + input banner
# ===========================================================================
BOT_Y  = 75
BOT_H  = 80

# Input panel
rounded_rect(ax, 60, BOT_Y - BOT_H/2, 650, BOT_H, '#0d1a2e', radius=20,
             edge=CYAN, lw=2)
ax.text(60 + 325, BOT_Y, "Input: \"(()(()))\"   ➜   Final Score = 6",
        ha='center', va='center', fontsize=22, color=WHITE,
        fontweight='bold', fontfamily='monospace', zorder=5)

# Center: verified banner
MID_X = W_PX / 2 + 100
rounded_rect(ax, 740, BOT_Y - BOT_H/2, 1100, BOT_H, '#14261a', radius=20,
             edge=GREEN, lw=2)
ax.text(740 + 550, BOT_Y, '✔  O(N) Single-Pass  ·  O(1) Auxiliary Space  ·  Bit-Shift Equivalent to 2^depth',
        ha='center', va='center', fontsize=20, color=GREEN,
        fontweight='bold', zorder=5)

# Complexity panel (right)
CMP_X = W_PX - 850
rounded_rect(ax, 1870, BOT_Y - BOT_H/2, W_PX - 1930, BOT_H, '#001a2e', radius=20,
             edge=CYAN, lw=2)
ax.text(1870 + (W_PX - 1930)/2, BOT_Y, 'Time: O(N)   |   Space: O(1)',
        ha='center', va='center', fontsize=22, color=CYAN,
        fontweight='bold', zorder=5)

# --- Save ---
OUT = '/home/kali/leetcode-solutions/cpp/0856-score-of-parentheses/diagram.png'
plt.savefig(OUT, dpi=DPI, facecolor=BG)
print(f'Successfully generated: {OUT}')
