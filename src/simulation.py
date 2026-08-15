"""
Numerical simulation of the Sun-Earth-Moon system.
"""

import numpy as np
from scipy.integrate import solve_ivp

from .gravity import compute_accelerations


def derivatives(
    time: float,
    state: np.ndarray,
    masses: np.ndarray,
    gravitational_constant: float
) -> np.ndarray:
    """
    Compute the derivatives of the N-body state vector.

    The state vector contains all positions followed by
    all velocities.

    Parameters
    ----------
    time : float
        Current simulation time.
    state : np.ndarray
        Flattened position and velocity state vector.
    masses : np.ndarray
        Masses of the bodies.
    gravitational_constant : float
        Newtonian gravitational constant G.

    Returns
    -------
    np.ndarray
        Time derivative of the state vector.
    """

    number_of_bodies = len(masses)

    positions = state[:number_of_bodies * 2].reshape(
        number_of_bodies,
        2
    )

    velocities = state[number_of_bodies * 2:].reshape(
        number_of_bodies,
        2
    )

    accelerations = compute_accelerations(
        positions,
        masses,
        gravitational_constant
    )

    return np.concatenate([
        velocities.flatten(),
        accelerations.flatten()
    ])


def create_initial_state(
    positions: np.ndarray,
    velocities: np.ndarray
) -> np.ndarray:
    """
    Convert position and velocity arrays into a single
    flattened state vector.
    """

    return np.concatenate([
        positions.flatten(),
        velocities.flatten()
    ])


def simulate(
    initial_state: np.ndarray,
    masses: np.ndarray,
    gravitational_constant: float,
    simulation_time: float,
    number_of_points: int = 6000,
    relative_tolerance: float = 1e-9,
    absolute_tolerance: float = 1e-9,
    method: str = "DOP853"
):
    """
    Integrate the N-body equations of motion.

    Returns
    -------
    scipy.integrate.OdeResult
        Numerical solution returned by solve_ivp.
    """

    time = np.linspace(
        0,
        simulation_time,
        number_of_points
    )

    solution = solve_ivp(
        derivatives,
        (0, simulation_time),
        initial_state,
        args=(masses, gravitational_constant),
        t_eval=time,
        rtol=relative_tolerance,
        atol=absolute_tolerance,
        method=method
    )

    if not solution.success:
        raise RuntimeError(
            f"Simulation failed: {solution.message}"
        )

    return solution