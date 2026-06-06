import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ── Parameters ─────────────────────────────────────────────
m    = 1200
Cd   = 0.30
A    = 2.2
rho  = 1.225
F_engine = 4000
dt   = 0.01
t    = np.arange(0, 30, dt)

# ── Simulation ─────────────────────────────────────────────
v_log, drag_log, acc_log = [], [], []
v = 0

for i in range(len(t)):
    F_drag = 0.5 * rho * Cd * A * v**2
    F_net  = F_engine - F_drag
    a      = F_net / m
    v     += a * dt

    v_log.append(v)
    drag_log.append(F_drag)
    acc_log.append(a)

# ── Animation ──────────────────────────────────────────────
fig, axes = plt.subplots(3, 1, figsize=(10, 8), facecolor='#0a0a0a')
fig.suptitle('AERODYNAMIC DRAG SIMULATOR', color='white', fontsize=14, fontweight='bold')

titles  = ['VEHICLE SPEED (m/s)', 'DRAG FORCE (N)', 'ACCELERATION (m/s2)']
colors  = ['#4fc3f7', '#ef5350', '#66bb6a']
ylimits = [(0, max(v_log)*1.2), (0, max(drag_log)*1.2), (0, max(acc_log)*1.2)]

lines = []
for ax, title, color, ylim in zip(axes, titles, colors, ylimits):
    ax.set_facecolor('#111111')
    ax.set_title(title, color=color, fontsize=9, fontweight='bold')
    ax.set_xlim(0, t[-1])
    ax.set_ylim(*ylim)
    ax.grid(True, alpha=0.2, color='#333333')
    ax.tick_params(colors='white', labelsize=7)
    for spine in ax.spines.values():
        spine.set_edgecolor('#333333')
    line, = ax.plot([], [], color=color, lw=2)
    lines.append(line)

time_text = axes[0].text(0.02, 0.85, '', transform=axes[0].transAxes,
                          color='white', fontsize=9)
info_text = axes[0].text(0.70, 0.85, '', transform=axes[0].transAxes,
                          color='yellow', fontsize=9, fontweight='bold')

plt.tight_layout()

STEP = 10

def update(frame):
    i = min(frame * STEP, len(t) - 1)
    x = t[:i]

    lines[0].set_data(x, v_log[:i])
    lines[1].set_data(x, drag_log[:i])
    lines[2].set_data(x, acc_log[:i])

    time_text.set_text(f't = {t[i]:.1f}s')
    info_text.set_text(
        f'Speed: {v_log[i]:.1f} m/s ({v_log[i]*3.6:.0f} km/h)  '
        f'Drag: {drag_log[i]:.0f} N'
    )
    return lines + [time_text, info_text]

frames = len(t) // STEP
ani = animation.FuncAnimation(fig, update, frames=frames, interval=30, blit=True)

print("Saving GIF...")
ani.save('drag_animation.gif', writer='pillow', fps=20)
print("Done! drag_animation.gif saved!")

plt.show()