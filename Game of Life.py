import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = 100
ON = 255
OFF = 0
vals = [ON, OFF]

grid = np.random.choice(vals, N * N, p=[0.2, 0.8]).reshape(N, N)

pause = [False]

def update(frameNum, img, grid, N, pause):
    if pause[0]:
        return img,
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]) / 255)
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

def toggle_pause(event):
    if event.key == ' ':
        pause[0] = not pause[0]

fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest')
fig.canvas.mpl_connect('key_press_event', toggle_pause)

ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, pause), frames=10, interval=50, save_count=50)
plt.show()
