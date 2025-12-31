# AI Rubik's Cube Solver

## Project Overview

This project implements an AI agent that learns to solve a 2x2 Rubik's Cube from scratch using reinforcement learning. The goal is to train an intelligent system that discovers solving strategies without any prior knowledge of Rubik's Cube algorithms or solution methods.

## Project Purpose

The primary objective is to explore how reinforcement learning agents can learn complex spatial reasoning and planning tasks in a constrained environment. The 2x2 Rubik's Cube provides an ideal testing ground with:

- **8 corner pieces** with 3.6 million possible configurations
- **Deterministic state transitions** - each move produces a predictable result
- **Clear goal state** - solved configuration is well-defined
- **Rich problem space** - requires multi-step planning and strategy

## Reinforcement Learning Approach

### Problem Formulation

The Rubik's Cube solving problem is formulated as a Markov Decision Process (MDP):

- **State Space**: Current configuration of the cube (all sticker positions)
- **Action Space**: 18 possible moves (6 faces × 3 rotations: clockwise, counterclockwise, 180°)
- **Reward Function**: Designed to incentivize progress toward the solved state
- **Goal**: Learn a policy π(s) that maps states to actions that minimize steps to solution

### Training Methods

To be completed

- Balance exploration vs exploitation

## Moves Notation

Standard Rubik's Cube notation:
- **U**: Up (top face clockwise)
- **D**: Down (bottom face clockwise)
- **F**: Front face clockwise
- **B**: Back face clockwise
- **R**: Right face clockwise
- **L**: Left face clockwise
- **'** (prime): Counterclockwise rotation (e.g., U')
- **2**: 180° rotation (e.g., U2)

## Dependencies

- **NumPy**: State representation and array operations
- **VPython**: 3D visualization
- **PyTorch**: (Coming soon) Neural network training
- **Gymnasium**: (Coming soon) RL environment interface

See [BUILD.md](BUILD.md) for detailed setup instructions.

## Future Directions

- Extend to 3x3 Rubik's Cube
- Transfer learning from 2x2 to larger cubes
- Multi-task learning across different scramble depths
- Competitive benchmarking against human solvers and traditional algorithms

---

*Last Updated: December 2025*
