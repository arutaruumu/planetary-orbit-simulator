"""
Gravitational calculations for the planetary orbit simulator.
"""

import numpy as np


def compute_accelerations(
    positions: np.ndarray,
    masses: np.ndarray,
    gravitational_constant: float
) -> np.ndarray:
    """
    Calculate the gravitational acceleration acting on each body.

    Parameters
    ----------
    positions : np.ndarray
        Array with shape (N, 2), containing the x and y positions
        of N bodies.
    masses : np.ndarray
        Array with shape (N,), containing the masses of the bodies.
    gravitational_constant : float
        Newtonian gravitational constant G.

    Returns
    -------
    np.ndarray
        Array with shape (N, 2) containing the acceleration
        of each body.
    """

    number_of_bodies = len(positions)

    accelerations = np.zeros_like(positions, dtype=float)

    for i in range(number_of_bodies):

        for j in range(number_of_bodies):

            if i == j:
                continue

            displacement = positions[j] - positions[i]

            distance = np.linalg.norm(displacement)

            if distance == 0:
                raise ValueError(
                    "Two bodies cannot occupy the same position."
                )

            accelerations[i] += (
                gravitational_constant
                * masses[j]
                * displacement
                / distance**3
            )

    return accelerations