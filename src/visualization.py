"""
Visualization utilities for the planetary orbit simulator.
"""

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation


def plot_orbits(
    positions_history: np.ndarray,
    astronomical_unit: float
):
    """
    Plot the Sun-Earth-Moon orbital trajectories.
    """

    figure, axis = plt.subplots(
        figsize=(10, 10)
    )

    axis.scatter(
        positions_history[:, 0, 0] / astronomical_unit,
        positions_history[:, 0, 1] / astronomical_unit,
        s=100,
        label="Sun"
    )

    axis.plot(
        positions_history[:, 1, 0] / astronomical_unit,
        positions_history[:, 1, 1] / astronomical_unit,
        label="Earth orbit"
    )

    axis.plot(
        positions_history[:, 2, 0] / astronomical_unit,
        positions_history[:, 2, 1] / astronomical_unit,
        label="Moon trajectory"
    )

    axis.scatter(
        positions_history[-1, 1, 0] / astronomical_unit,
        positions_history[-1, 1, 1] / astronomical_unit,
        s=40
    )

    axis.scatter(
        positions_history[-1, 2, 0] / astronomical_unit,
        positions_history[-1, 2, 1] / astronomical_unit,
        s=20
    )

    axis.set_xlabel("x [AU]")
    axis.set_ylabel("y [AU]")
    axis.set_title(
        "Sun-Earth-Moon Orbital System"
    )

    axis.set_aspect("equal")
    axis.legend()

    return figure, axis


def plot_earth_moon_orbit(
    positions_history: np.ndarray
):
    """
    Plot the Moon trajectory relative to Earth.
    """

    earth_positions = positions_history[:, 1]
    moon_positions = positions_history[:, 2]

    relative_positions = (
        moon_positions
        - earth_positions
    )

    figure, axis = plt.subplots(
        figsize=(8, 8)
    )

    axis.plot(
        relative_positions[:, 0] / 1e6,
        relative_positions[:, 1] / 1e6
    )

    axis.scatter(
        0,
        0,
        s=100,
        label="Earth"
    )

    axis.set_xlabel(
        "x relative to Earth [million km]"
    )

    axis.set_ylabel(
        "y relative to Earth [million km]"
    )

    axis.set_title(
        "Moon Orbit Around Earth"
    )

    axis.set_aspect("equal")
    axis.legend()

    return figure, axis


def plot_time_series(
    time_days,
    values,
    labels,
    ylabel,
    title,
    scale=1.0
):
    """
    Plot multiple physical quantities against time.
    """

    figure, axis = plt.subplots(
        figsize=(12, 6)
    )

    for index, label in enumerate(labels):

        axis.plot(
            time_days,
            values[:, index] / scale,
            label=label
        )

    axis.set_xlabel("Time [days]")
    axis.set_ylabel(ylabel)
    axis.set_title(title)
    axis.legend()

    return figure, axis


def plot_conservation_error(
    time_days,
    error,
    ylabel,
    title
):
    """
    Plot relative conservation error.
    """

    figure, axis = plt.subplots(
        figsize=(12, 5)
    )

    axis.plot(
        time_days,
        error
    )

    axis.set_xlabel("Time [days]")
    axis.set_ylabel(ylabel)
    axis.set_title(title)

    return figure, axis


def create_orbit_animation(
    positions_history,
    astronomical_unit,
    frame_step=30
):
    """
    Create an animated visualization of the
    Sun-Earth-Moon system.
    """

    figure, axis = plt.subplots(
        figsize=(10, 10)
    )

    axis.set_xlim(-1.2, 1.2)
    axis.set_ylim(-1.2, 1.2)

    axis.set_xlabel("x [AU]")
    axis.set_ylabel("y [AU]")

    axis.set_title(
        "Sun-Earth-Moon Newtonian Gravity Simulation"
    )

    axis.set_aspect("equal")

    axis.plot(
        positions_history[:, 1, 0] / astronomical_unit,
        positions_history[:, 1, 1] / astronomical_unit,
        alpha=0.3,
        label="Earth trajectory"
    )

    sun_dot, = axis.plot(
        [],
        [],
        "o",
        markersize=12,
        label="Sun"
    )

    earth_dot, = axis.plot(
        [],
        [],
        "o",
        markersize=6,
        label="Earth"
    )

    moon_dot, = axis.plot(
        [],
        [],
        "o",
        markersize=3,
        label="Moon"
    )

    earth_trail, = axis.plot(
        [],
        [],
        linewidth=1
    )

    moon_trail, = axis.plot(
        [],
        [],
        linewidth=1
    )

    axis.legend()

    def initialize():

        sun_dot.set_data([], [])
        earth_dot.set_data([], [])
        moon_dot.set_data([], [])

        earth_trail.set_data([], [])
        moon_trail.set_data([], [])

        return (
            sun_dot,
            earth_dot,
            moon_dot,
            earth_trail,
            moon_trail
        )

    def update(frame):

        sun = (
            positions_history[frame, 0]
            / astronomical_unit
        )

        earth = (
            positions_history[frame, 1]
            / astronomical_unit
        )

        moon = (
            positions_history[frame, 2]
            / astronomical_unit
        )

        sun_dot.set_data(
            [sun[0]],
            [sun[1]]
        )

        earth_dot.set_data(
            [earth[0]],
            [earth[1]]
        )

        moon_dot.set_data(
            [moon[0]],
            [moon[1]]
        )

        earth_trail.set_data(
            positions_history[
                :frame + 1,
                1,
                0
            ] / astronomical_unit,

            positions_history[
                :frame + 1,
                1,
                1
            ] / astronomical_unit
        )

        moon_trail.set_data(
            positions_history[
                :frame + 1,
                2,
                0
            ] / astronomical_unit,

            positions_history[
                :frame + 1,
                2,
                1
            ] / astronomical_unit
        )

        return (
            sun_dot,
            earth_dot,
            moon_dot,
            earth_trail,
            moon_trail
        )

    animation = FuncAnimation(
        figure,
        update,
        frames=range(
            0,
            len(positions_history),
            frame_step
        ),
        init_func=initialize,
        interval=20,
        blit=True
    )

    return figure, animation