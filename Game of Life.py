import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = 100
ON = 255
OFF = 0
NEW = 128
vals = [ON, OFF]

grid = np.random.choice(vals, N * N, p=[0.2, 0.8]).reshape(N, N)

pause = [False]

def count_neighbors(grid, N):
    neighbors = (
        np.roll(grid, 1, axis=0) + np.roll(grid, -1, axis=0) +
        np.roll(grid, 1, axis=1) + np.roll(grid, -1, axis=1) +
        np.roll(np.roll(grid, 1, axis=0), 1, axis=1) +
        np.roll(np.roll(grid, 1, axis=0), -1, axis=1) +
        np.roll(np.roll(grid, -1, axis=0), 1, axis=1) +
        np.roll(np.roll(grid, -1, axis=0), -1, axis=1)
    ) // 255
    return neighbors

def update(frameNum, img, grid, N, pause):
    if pause[0]:
        return img,
    neighbors = count_neighbors(grid, N)
    newGrid = np.where((grid == ON) & ((neighbors < 2) | (neighbors > 3)), OFF, grid)
    newGrid = np.where((grid == OFF) & (neighbors == 3), NEW, newGrid)
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

def toggle_pause(event):
    if event.key == ' ':
        pause[0] = not pause[0]

fig, ax = plt.subplots()
img = ax.imshow(grid, cmap='viridis', interpolation='nearest')
fig.canvas.mpl_connect('key_press_event', toggle_pause)

ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, pause), frames=10, interval=50, save_count=50)
plt.show()
