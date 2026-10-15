# Machine Learning 101

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-2.x-013243?logo=numpy&logoColor=white)

Core machine learning algorithms built from scratch in Python. The goal is to understand what happens under the hood before reaching for a library, so each algorithm is implemented with plain NumPy and explained step by step.

## Contents

- Gradient descent: [grad.py](https://github.com/namitha9eshan/machine_learning_101/blob/main/grad.py)

More algorithms will be added as the repo grows.

## What is covered

### Gradient Descent
An iterative optimization algorithm that minimizes a cost function by repeatedly moving the parameters in the direction of the steepest decrease. The implementation covers:

- Defining a cost function and its gradient
- Updating parameters with a configurable learning rate
- Running for a set number of iterations and tracking the cost
- Plotting convergence with Matplotlib

## Tech Stack

- Python 3.12
- NumPy for numerical computation
- Matplotlib for visualization
- [uv](https://docs.astral.sh/uv/) for dependency and environment management

## Getting Started

### Prerequisites

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and [Git](https://git-scm.com/).

### Installation

```bash
git clone https://github.com/namitha9eshan/machine_learning_101.git
cd machine_learning_101
uv sync
```

`uv sync` creates a `.venv` folder and installs the exact package versions recorded in `uv.lock`.

### Run an example

```bash
uv run gradient_descent.py
```

### Using pip instead

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS / Linux
pip install -r requirements.txt
python gradient_descent.py
```

## Project Structure

```
machine_learning_101/
├── gradient_descent.py   # Gradient descent from scratch
├── src/                  # Package source
├── pyproject.toml        # Project metadata and dependencies
├── uv.lock               # Locked dependency versions
├── requirements.txt      # pip-compatible dependency list
├── .python-version       # Python version used by uv
└── README.md
```

## Roadmap

- [x] Gradient descent
- [ ] Linear regression
- [ ] Logistic regression
- [ ] k-Nearest Neighbors
- [ ] Decision trees

## Author

**namitha9eshan** - [GitHub](https://github.com/namitha9eshan)

Feedback and suggestions are welcome. Feel free to open an issue.