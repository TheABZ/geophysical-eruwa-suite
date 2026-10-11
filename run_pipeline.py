import os
from src.electrical import plot_2d_cst_pseudosection
from src.electromagnetics import process_vlf_em
from src.visualize import plot_ves_curve


def main():
    print("==========================================================")
    print("   RUNNING GEOPHYSICAL ANALYSIS PIPELINE (ERUWA SITE)     ")
    print("==========================================================\n")

    os.makedirs("outputs", exist_ok=True)

    # 1. 2D CST Profile
    if os.path.exists("data/cst_data.csv"):
        plot_2d_cst_pseudosection("data/cst_data.csv")

    # 2. VLF Profile
    if os.path.exists("data/vlf_data.csv"):
        process_vlf_em("data/vlf_data.csv")

    # 3. VES 2 (Station 126m) WinResist Fit Comparison
    # Raw field points from project report
    ab2_ves2 = [1, 2, 3, 4, 6, 9, 12, 15, 20, 25, 32, 40, 50, 65, 80]
    rho_ves2 = [1287.55, 987.12, 572.83, 360.50, 126.44, 81.18, 112.90, 105.55, 137.88, 186.23, 273.14, 301.40, 333.74,
                503.63, 642.76]

    # WinResist Inverted Model Parameters (Station 126m):
    # rho1 = 2033.3, rho2 = 76.5, rho3 = 2914.0
    # h1 = 1.2, h2 = 8.8
    rho_winresist = [2033.3, 76.5, 2914.0]
    h_winresist = [1.2, 8.8]

    plot_ves_curve(ab2_ves2, rho_ves2, rho_winresist, h_winresist, "VES 2 Station 126m")

    print("\n[✓] All figures generated and saved inside 'outputs/' folder!")


if __name__ == "__main__":
    main()