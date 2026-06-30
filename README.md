LaunchLab

A Python-based projectile motion simulator that models and visualises the flight of a projectile under different physical conditions using numerical methods.

The project demonstrates scientific computing concepts including numerical integration, object-oriented design, and data visualisation with NumPy and Matplotlib.

Features
Simulates 2D projectile motion using time-step numerical integration
Supports variable gravity, wind, and air resistance
Calculates key outputs:
flight time
maximum height
range
impact velocity
Plots full trajectory using Matplotlib
Compares multiple launch conditions on the same graph
Modular design with separate physics, simulation, and plotting components
Optional CLI interface for running simulations
Physics Model

The simulation is based on Newtonian mechanics:

Gravity acts downward with constant acceleration
Velocity is updated each timestep
Position is updated using velocity
Optional drag model:
linear: F
d
	​

=−cv
quadratic: F
d
	​

=−cv
2

Numerical integration is performed using a fixed time-step method.

Project Structure
trajectory_sim/
│
├── main.py              # Entry point (CLI / experiment runner)
├── simulation.py       # Core simulation loop
├── projectile.py       # Projectile object (state)
├── environment.py      # Gravity, wind, air properties
├── physics.py          # Force and motion calculations
├── plotting.py         # Matplotlib visualization
├── config.py           # Default parameters
│
└── tests/
    ├── test_physics.py
    └── test_simulation.py
Requirements
Python 3.10+
NumPy
Matplotlib

Install dependencies:

pip install numpy matplotlib
Usage
Run basic simulation
python main.py
Optional CLI mode
python main.py --speed 50 --angle 45 --wind 2
Example Output

The simulator generates:

trajectory plots (x vs y)
comparison graphs for different angles or conditions
numerical results in the terminal
Example Results

Typical outputs include:

Maximum height (m)
Total range (m)
Flight duration (s)

These depend on input conditions such as launch angle, speed, and environmental factors.

Testing

Run tests with:

pytest

Tests include:

conservation checks (no air resistance case)
sanity checks on trajectory shape
boundary conditions (ground impact detection)
Learning Outcomes Covered

This project is designed to align with introductory scientific computing outcomes:

Python control flow, functions, and data structures
Program design and problem decomposition
Code modularisation and complexity reduction
Numerical computation using NumPy
Data visualisation with Matplotlib
Basic object-oriented programming
Future Improvements
Animated trajectory simulation
3D projectile extension
Terrain collision detection
Parameter optimisation (best launch angle search)
Monte Carlo simulation for uncertainty modelling
GUI interface using Tkinter or PyQt
License

This project is intended for educational use.
