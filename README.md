
```markdown
# Game of Life

The Game of Life is a cellular automaton devised by mathematician John Horton Conway. It is a zero-player game, meaning its evolution is determined by its initial state, with no further input required.

## Getting Started

These instructions will help you get the Game of Life up and running on your local machine for development, testing, and exploration.

---

### Prerequisites

Ensure you have Python installed with its corresponding libraries (numpy and matplotlib):

### Installing

Follow these steps to run the Game of Life:

1. Clone or download the repository:

```cmd
git clone https://github.com/ryanjabbour/Game_of_Life-Ryan_Jabbour-CDOF2.git
cd Game_of_Life-Ryan_Jabbour-CDOF2
```

2. Run the Python script:

```cmd
python game_of_life.py
```

You should see an animated simulation of Conway's Game of Life in a 2D grid, with enhanced features like color-coding and the ability to pause and resume the simulation using the spacebar.

---

## Features

- **Color-Coding for Cell States**: Cells are now visually differentiated based on their state:
  - Newly born cells are colored distinctively.
  - Surviving cells are displayed in a different color.
  - Dying cells are also highlighted for clear identification.

- **Pause and Resume**: The simulation can be paused and resumed by pressing the spacebar during the animation. A "Paused" label will appear when the game is paused.

- **Optimized Neighbor Counting**: The neighbor counting process has been optimized using NumPy operations to improve performance, especially on larger grids. This reduces the computational cost by vectorizing the neighbor calculation.

---

## Running the Tests

You can test modifications and logic by running the script with different parameters or adding assertions in the code.

### Example Test (End-to-End)

Modify the `N` parameter to change the grid size or adjust the probabilities in the random initialization:

```python
N = 50  # Change grid size
grid = np.random.choice([ON, OFF], N*N, p=[0.3, 0.7]).reshape(N, N)
```

### Code Style Tests

Ensure the script adheres to PEP 8 standards. Use tools like `flake8` for automated checks:

```cmd
pip install flake8
flake8 game_of_life.py
```

---

## Deployment

You can deploy this project as a standalone Python script. It can also be extended for web-based visualization using frameworks like Flask or Django.

---

## Built With

- **Python** - Core programming language
- **Numpy** - Used for efficient array operations
- **Matplotlib** - Used for plotting and animation

---

## Authors

- **Ryan Jabbour** - *Initial work* - [YourGitHubProfile](https://github.com/ryanjabbour)

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.

---

## Acknowledgments

- Inspired by John Horton Conway's original work.
- Thanks to the open-source community for libraries and resources.
```

This is the complete README file, now including the details for the new features like color-coding, pause/resume functionality, and optimized neighbor counting.
