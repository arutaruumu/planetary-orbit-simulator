# Planetary Orbit Simulator

### A Numerical Simulation of the Sun–Earth–Moon System Using Newtonian Gravity

**Author:** Nada Satya Maharani  
**Year:** 2026

A computational physics project that simulates a simplified **three-body gravitational system** consisting of the Sun, Earth, and Moon.

The project combines classical mechanics, differential equations, numerical integration, and scientific visualization using Python.

---

## Overview

The simulation models the mutual gravitational interaction between:

- **Sun**
- **Earth**
- **Moon**

Unlike a simple two-body model, all three bodies are treated as massive particles and interact gravitationally with one another.

The computational workflow is:

**Physical Parameters → Initial Conditions → Gravity → Equations of Motion → Numerical Integration → Analysis → Visualization**

---

## Physics Covered

This project explores:

- Newton's law of universal gravitation
- Newton's second law of motion
- N-body gravitational dynamics
- Coupled differential equations
- Numerical integration
- Orbital trajectories
- Velocity and acceleration
- Kinetic and gravitational potential energy
- Angular momentum
- Conservation of energy
- Conservation of angular momentum
- Numerical error analysis
- Scientific visualization and animation

---

## Mathematical Model

For body `i`, the gravitational acceleration is calculated as

$$
\vec a_i =
G\sum_{j\ne i}
m_j
\frac{\vec r_j-\vec r_i}
{|\vec r_j-\vec r_i|^3}.
$$

The equations of motion are

$$
\frac{d\vec r}{dt}=\vec v,
\qquad
\frac{d\vec v}{dt}=\vec a.
$$

The system is integrated numerically using SciPy's `solve_ivp()` with the **DOP853** method.

---

## Analysis

The notebook analyzes:

### Orbital Motion
- Sun–Earth orbital trajectory
- Earth–Moon relative trajectory

### Kinematics
- Velocity magnitude
- Acceleration magnitude
- Velocity and acceleration vectors

### Conservation Laws
- Kinetic energy
- Potential energy
- Total mechanical energy
- Total angular momentum
- Relative conservation errors

### Visualization
- Static orbital plots
- Earth–Moon local-scale plot
- Vector field-style orbital visualization
- Animated Sun–Earth–Moon system

---

## Project Structure

```text
planetary-orbit-simulator/
│
├── README.md
├── planetary_orbit_simulator.ipynb
├── requirements.txt
├── .gitignore
├── LICENSE
│
└── results/
    └── .gitkeep
```

The **Jupyter Notebook contains the complete step-by-step scientific explanation and experiment workflow**, while the `src/` directory contains the reusable implementation modules.

---

## Technologies

- **Python**
- **NumPy** — numerical arrays and vector calculations
- **SciPy** — numerical integration with `solve_ivp`
- **Matplotlib** — scientific visualization and animation
- **Google Colab / Jupyter Notebook**

---

## Running the Project

### Google Colab

Upload `planetary_orbit_simulator.ipynb` to Google Colab and run the cells from top to bottom.

### Local Jupyter

Install the dependencies:

```bash
pip install -r requirements.txt
```

Then open:

```text
planetary_orbit_simulator.ipynb
```

---

## Model Assumptions & Limitations

This is a **simplified educational computational model**, not a precision astronomical simulator.

The current model:

- uses simplified initial conditions;
- is restricted to two-dimensional motion;
- treats celestial bodies as point masses;
- uses Newtonian gravity;
- ignores relativistic effects;
- does not use high-precision astronomical ephemeris data.

These assumptions keep the model understandable while still demonstrating the main computational ideas behind gravitational N-body simulations.

---

## Possible Future Extensions

Possible improvements include:

- 3D orbital dynamics
- More celestial bodies
- Precision astronomical initial conditions
- Adaptive accuracy studies
- Comparison of numerical integration methods
- Center-of-mass analysis
- Orbital eccentricity calculation
- Momentum conservation analysis
- Restricted three-body problem
- Lagrange point investigation
- Comparison with real astronomical data

---

## Learning Outcome

This project connects **computer science** with **classical and computational physics**:

```text
Python
   ↓
Numerical Computation
   ↓
Differential Equations
   ↓
N-Body Simulation
   ↓
Classical Mechanics
   ↓
Scientific Analysis
   ↓
Visualization
```

The project is intended as a portfolio piece demonstrating the use of programming and numerical methods to investigate a physical system.

---

## Author

**Nada Satya Maharani**

This project was developed as an independent computational physics project, combining programming, numerical methods, and classical mechanics.

---

## License

This project is released under the MIT License.
