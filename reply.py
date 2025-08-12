import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button
import sys

if (len(sys.argv) > 1):
    CSV_FILE=sys.argv[1]
else:
    print ("Error: you must provide a csv file")
    exit()

FRAME_INTERVAL_MS = 55

df = pd.read_csv(CSV_FILE)
df = df.sort_values(by='frame')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter([], [], [])
ax.set_xlim(df['x'].min() - 1, df['x'].max() + 1)
ax.set_ylim(df['y'].min() - 1, df['y'].max() + 1)
ax.set_zlim(df['z'].min() - 1, df['z'].max() + 1)

ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.set_zlabel('z (m)')

current_frame_idx = 0

def update(frame_idx):
    global current_frame_idx
    current_frame_idx = frame_idx
    frame_data = df[df['frame'] == frame_idx]
    if frame_data.empty:
        sc._offsets3d = ([],
                         [],
                         [])
    else:
        sc._offsets3d = (frame_data['x'].values,
                        frame_data['y'].values,
                        frame_data['z'].values)
    ax.set_title(f'Frame: {frame_idx} | Time: {frame_idx * FRAME_INTERVAL_MS} ms')
    return sc,

def next_frame(e):
    ani.event_source.stop()
    global current_frame_idx
    if current_frame_idx+1 > df['frame'].max():
        update(0)
    else:
        update(current_frame_idx+1)
    plt.draw()

def prev_frame(e):
    ani.event_source.stop()
    global current_frame_idx
    if current_frame_idx-1 < 0:
        update(df['frame'].max())
    else:
        update(current_frame_idx-1)
    plt.draw()

def toggle_animation(e):
    if ani.event_source.running:
        ani.event_source.stop()
    else:
        ani.event_source.start()

axprev = plt.axes([0.3, 0.05, 0.1, 0.075])
axnext = plt.axes([0.6, 0.05, 0.1, 0.075])
# axplay = plt.axes([0.425, 0.05, 0.15, 0.075])
bnext = Button(axnext, 'Next')
bprev = Button(axprev, 'Previous')
# bplay = Button(axplay, 'Pause/Continue')
bnext.on_clicked(next_frame)
bprev.on_clicked(prev_frame)
# bplay.on_clicked(toggle_animation)

ani = animation.FuncAnimation(
    fig, update, frames=df['frame'].max(), interval=FRAME_INTERVAL_MS
)

plt.show()
