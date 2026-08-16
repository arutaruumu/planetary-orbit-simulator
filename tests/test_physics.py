import numpy as np

from src.gravity import compute_accelerations
from src.analysis import (
    compute_energy,
    compute_angular_momentum,
)


def test_gravity_direction():

    G = 1.0

    masses = np.array([
        1.0,
        1.0
    ])

    positions = np.array([
        [0.0, 0.0],
        [1.0, 0.0]
    ])

    accelerations = compute_accelerations(
        positions,
        masses,
        G
    )

    assert accelerations[0, 0] > 0
    assert accelerations[1, 0] < 0


def test_gravity_magnitude():

    G = 1.0

    masses = np.array([
        1.0,
        1.0
    ])

    positions = np.array([
        [0.0, 0.0],
        [1.0, 0.0]
    ])

    accelerations = compute_accelerations(
        positions,
        masses,
        G
    )

    assert np.isclose(
        np.linalg.norm(accelerations[0]),
        1.0
    )

    assert np.isclose(
        np.linalg.norm(accelerations[1]),
        1.0
    )


def test_angular_momentum():

    masses = np.array([1.0])

    positions = np.array([
        [1.0, 0.0]
    ])

    velocities = np.array([
        [0.0, 1.0]
    ])

    angular_momentum = compute_angular_momentum(
        positions,
        velocities,
        masses
    )

    assert np.isclose(
        angular_momentum,
        1.0
    )