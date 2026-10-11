import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


def plot_sounding_results(
    ab_half: np.ndarray,
    apparent_resistivity: np.ndarray,
    resistivities: list[float],
    thicknesses: list[float],
):
    """Generates a publication-grade 2-panel figure comparing the 1D Earth model

    profile against the Schlumberger sounding curve.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))

    # --- Panel 1: Layered Earth Profile ---
    cum_depths = np.cumsum(thicknesses)
    max_depth = cum_depths[-1] * 1.5

    depth_steps = [0]
    rho_steps = [resistivities[0]]

    for i in range(len(thicknesses)):
        depth_steps.extend([cum_depths[i], cum_depths[i]])
        rho_steps.extend([resistivities[i], resistivities[i + 1]])

    depth_steps.append(max_depth)
    rho_steps.append(resistivities[-1])

    ax1.plot(
        rho_steps,
        depth_steps,
        color="crimson",
        linewidth=2.5,
        label="Subsurface Model",
    )
    ax1.set_xscale("log")
    ax1.invert_yaxis()
    ax1.set_xlabel(r"True Resistivity $\rho$ ($\Omega\cdot\mathrm{m}$)")
    ax1.set_ylabel("Depth $z$ (m)")
    ax1.set_title("Target 1D Subsurface Model Profile")
    ax1.grid(True, which="both", ls="--", alpha=0.5)

    # Format logarithmic ticks to prevent minor-label clutter
    ax1.xaxis.set_major_formatter(ticker.FormatStrFormatter("%g"))
    ax1.xaxis.set_minor_formatter(ticker.NullFormatter())

    # --- Panel 2: Schlumberger Sounding Curve ---
    ax2.loglog(
        ab_half,
        apparent_resistivity,
        "o-",
        color="navy",
        linewidth=2,
        markersize=5,
        label="Synthetic Apparent Resistivity",
    )
    ax2.set_xlabel(r"Electrode Spacing $AB/2$ (m)")
    ax2.set_ylabel(r"Apparent Resistivity $\rho_a$ ($\Omega\cdot\mathrm{m}$)")
    ax2.set_title("Forward Schlumberger Sounding Curve")
    ax2.grid(True, which="both", ls="--", alpha=0.5)
    ax2.legend()
    plt.tight_layout()
    plt.savefig("data/sounding_plot.png", dpi=300, bbox_inches="tight")
    plt.show()