import os
import matplotlib.pyplot as plt
import numpy as np
from src.forward_model import calculate_apparent_resistivity


def plot_ves_curve(ab2_field, rho_field, rho_model, h_model, station_name, output_dir="outputs"):
    """
    Plots raw field data against WinResist model response.
    """
    # Generate smooth AB/2 curve for forward model line
    ab2_smooth = np.logspace(np.log10(min(ab2_field)), np.log10(max(ab2_field)), 100)
    rho_model_curve = calculate_apparent_resistivity(ab2_smooth, rho_model, h_model)

    plt.figure(figsize=(7, 6))

    # Field points
    plt.loglog(ab2_field, rho_field, 'ro', label='Observed Field Data (PASI 16GL-N)')

    # WinResist model curve
    plt.loglog(ab2_smooth, rho_model_curve, 'b-', linewidth=2, label='Model Response (WinResist)')

    plt.title(f'1D Sounding Curve & Inversion Fit ({station_name})', fontweight='bold')
    plt.xlabel('AB/2 Spacing (m)')
    plt.ylabel('Apparent Resistivity (Ω·m)')
    plt.grid(True, which="both", ls="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()

    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, f"{station_name.lower().replace(' ', '_')}_fit.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[✓] Generated VES Fit Plot: {out_path}")