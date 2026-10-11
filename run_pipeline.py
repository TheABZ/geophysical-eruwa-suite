import os
from src.electrical import plot_2d_cst_pseudosection
from src.electromagnetics import process_vlf_em


def main():
    print("==========================================================")
    print("   RUNNING GEOPHYSICAL ANALYSIS PIPELINE (ERUWA SITE)     ")
    print("==========================================================\n")

    # Create output directory for generated plots
    os.makedirs("outputs", exist_ok=True)

    # 1. Process 2D CST Resistivity Pseudosection
    if os.path.exists("data/cst_data.csv"):
        plot_2d_cst_pseudosection("data/cst_data.csv")
    else:
        print("[!] Warning: data/cst_data.csv not found.")

    # 2. Process VLF-EM Fraser Filter Profile
    if os.path.exists("data/vlf_data.csv"):
        process_vlf_em("data/vlf_data.csv")
    else:
        print("[!] Warning: data/vlf_data.csv not found.")

    print("\n[✓] All figures generated and saved inside 'outputs/' folder!")


if __name__ == "__main__":
    main()