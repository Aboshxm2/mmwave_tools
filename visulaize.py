import sys
import pandas as pd
import matplotlib.pyplot as plt

if (len(sys.argv) > 1):
    CSV_FILE=sys.argv[1]
else:
    print ("Error: you must provide a csv file")
    exit()

FRAME_INTERVAL_MS = 55

df = pd.read_csv(CSV_FILE)
df = df.sort_values(by='frame')
df['time'] = df['frame'] * FRAME_INTERVAL_MS

fig, ax = plt.subplots(3, 1, sharex=True)
ax[0].plot(df['time'], df['x'], marker='o', linestyle='None', color='red', label='Horizontal')
ax[0].set_ylabel('Horizontal (m)')
ax[1].plot(df['time'], df['z'], marker='o', linestyle='None', color='blue', label='Vertical')
ax[1].set_ylabel('Vertical (m)')
ax[2].plot(df['time'], df['y'], marker='o', linestyle='None', label='Depth')
ax[2].set_ylabel('Depth (m)')
ax[2].set_xlabel('Time (ms)')
ax[0].grid(True)
ax[1].grid(True)
ax[2].grid(True)
fig.suptitle('70 Centimeters - 5 Seconds')
plt.show()
