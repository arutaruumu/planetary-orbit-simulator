"""
Physical analysis functions for the planetary orbit simulator.
"""

import numpy as np

from .gravity import compute_accelerations


def extract_solution(
    solution,
    number_of_bodies: int
):
    """
    Extract position and velocity histories from a solve_ivp solution.
    """

    data = solution.y.T

    position_size = number_of_bodies * 2

    positions = data[:, :position_size].reshape(
        -1,
        number_of_bodies,
        2
    )

    velocities = data[:, position_size:].reshape(
        -1,
        number_of_bodies,
        2
    )

    return positions, velocities


def calculate_acceleration_history(
    positions_history: np.ndarray,
    masses: np.ndarray,
    gravitational_constant: float
) -> np.ndarray:
    """
    Calculate acceleration for every timestep.
    """

    return np.array([
        compute_accelerations(
            positions,
            masses,
            gravitational_constant
        )
        for positions in positions_history
    ])


def calculate_velocity_magnitudes(
    velocities_history: np.ndarray
) -> np.ndarray:
    """
    Calculate velocity magnitude for every body at every timestep.
    """

    return np.linalg.norm(
        velocities_history,
        axis=2
    )


def calculate_acceleration_magnitudes(
    accelerations_history: np.ndarray
) -> np.ndarray:
    """
    Calculate acceleration magnitude for every body.
    """

    return np.linalg.norm(
        accelerations_history,
        axis=2
    )


def compute_energy(
    positions: np.ndarray,
    velocities: np.ndarray,
    masses: np.ndarray,
    gravitational_constant: float
):
    """
    Calculate kinetic, potential, and total mechanical energy.
    """

    kinetic_energy = 0.0

    for i in range(len(masses)):

        velocity_squared = np.dot(
            velocities[i],
            velocities[i]
        )

        kinetic_energy += (
            0.5
            * masses[i]
            * velocity_squared
        )

    potential_energy = 0.0

    for i in range(len(masses)):

        for j in range(i + 1, len(masses)):

            distance = np.linalg.norm(
                positions[j] - positions[i]
            )

            potential_energy -= (
                gravitational_constant
                * masses[i]
                * masses[j]
                / distance
            )

    total_energy = (
        kinetic_energy
        + potential_energy
    )

    return (
        kinetic_energy,
        potential_energy,
        total_energy
    )


def calculate_energy_history(
    positions_history: np.ndarray,
    velocities_history: np.ndarray,
    masses: np.ndarray,
    gravitational_constant: float
) -> np.ndarray:
    """
    Calculate energy components for every timestep.
    """

    return np.array([
        compute_energy(
            positions,
            velocities,
            masses,
            gravitational_constant
        )
        for positions, velocities
        in zip(
            positions_history,
            velocities_history
        )
    ])


def compute_angular_momentum(
    positions: np.ndarray,
    velocities: np.ndarray,
    masses: np.ndarray
) -> float:
    """
    Calculate total z-component of angular momentum
    for a two-dimensional system.
    """

    total_angular_momentum = 0.0

    for i in range(len(masses)):

        x, y = positions[i]
        vx, vy = velocities[i]

        total_angular_momentum += (
            masses[i]
            * (x * vy - y * vx)
        )

    return total_angular_momentum


def calculate_angular_momentum_history(
    positions_history: np.ndarray,
    velocities_history: np.ndarray,
    masses: np.ndarray
) -> np.ndarray:
    """
    Calculate total angular momentum for every timestep.
    """

    return np.array([
        compute_angular_momentum(
            positions,
            velocities,
            masses
        )
        for positions, velocities
        in zip(
            positions_history,
            velocities_history
        )
    ])


def relative_conservation_error(
    values: np.ndarray
) -> np.ndarray:
    """
    Calculate relative conservation error with respect
    to the initial value.
    """

    initial_value = values[0]

    return (
        (values - initial_value)
        / abs(initial_value)
    )