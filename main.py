import numpy as np
from src.exporter import export_sounding_to_csv
from src.forward_model import Resistivity1DForward
from src.inversion import Resistivity1DInversion
from src.visualize import plot_sounding_results
if __name__ == "__main__":
    print("==================================================")
    print(" 1D ELECTRICAL RESISTIVITY FORWARD & INVERSION ")
    print("==================================================\n")

    # True Synthetic Model (H-type aquifer)
    true_rhos = [120.0, 25.0, 800.0]
    true_thicknesses = [2.5, 15.0]
    ab_half = np.logspace(np.log10(1.5), np.log10(250), 35)

    # Forward Modeling
    fwd_engine = Resistivity1DForward(true_rhos, true_thicknesses)
    clean_rho_a = fwd_engine.forward(ab_half)

    # Gaussian Noise Injection (Simulating field errors)
    np.random.seed(42)
    noisy_rho_a = clean_rho_a + np.random.normal(
        0, 0.05 * clean_rho_a, size=clean_rho_a.shape
    )

    # Export dataset to CSV
    export_sounding_to_csv(ab_half, clean_rho_a, noisy_rho_a)

    # Perform Inversion from an initial guess
    print("\n--- Running Levenberg-Marquardt Inversion ---")
    initial_guess_rhos = [80.0, 50.0, 400.0]
    initial_guess_thick = [5.0, 10.0]

    inversion_engine = Resistivity1DInversion(ab_half, noisy_rho_a, n_layers=3)
    inv_rhos, inv_thick, rms_err = inversion_engine.invert(
        initial_guess_rhos, initial_guess_thick
    )

    print(f"Inversion Finished with RMS Error: {rms_err:.2f}%\n")
    print("Target True Resistivities :", true_rhos)
    print("Inverted Resistivities    :", [round(r, 2) for r in inv_rhos])
    print("\nTarget True Thicknesses   :", true_thicknesses)
    print("Inverted Thicknesses      :", [round(t, 2) for t in inv_thick])

    # Plot final model output
    plot_sounding_results(ab_half, noisy_rho_a, inv_rhos, inv_thick)