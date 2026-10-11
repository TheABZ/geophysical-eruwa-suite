import csv
import os
import numpy as np


def export_sounding_to_csv(
    ab_half: np.ndarray,
    rho_clean: np.ndarray,
    rho_noisy: np.ndarray,
    filepath: str = "data/sounding_data.csv",
):
    """Exports AB/2 spacing, clean apparent resistivity, and noisy apparent

    resistivity values to CSV.
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            ["AB_2_m", "Apparent_Resistivity_Clean", "Apparent_Resistivity_Noisy"]
        )
        for s, rc, rn in zip(ab_half, rho_clean, rho_noisy):
            writer.writerow([f"{s:.4f}", f"{rc:.4f}", f"{rn:.4f}"])

    print(f"Data exported successfully to '{filepath}'.")