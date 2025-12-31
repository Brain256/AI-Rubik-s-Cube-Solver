# Build and Setup Guide

## Prerequisites

- Python 3.13+
- pip

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Brain256/AI-Rubik-s-Cube-Solver.git
   cd AI-Rubiks-Cube-Solver
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   ```

3. **Activate virtual environment**
   
   macOS/Linux:
   ```bash
   source venv/bin/activate
   ```
   
   Windows:
   ```cmd
   venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the visualizer**
   ```bash
   python simulation/cube_visualizer.py
   ```

## GPU Support (Optional)

For PyTorch with CUDA:
```bash
pip uninstall torch torchvision
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

See [PyTorch website](https://pytorch.org/get-started/locally/) for other CUDA versions.
