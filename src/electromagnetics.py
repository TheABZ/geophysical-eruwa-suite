import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def process_vlf_em(csv_path, output_dir="outputs"):
    df = pd.read_csv(csv_path)
    in_phase = df["InPhase"].values

    fraser_inphase = np.full(len(in_phase), np.nan)
    for i in range(3, len(in_phase)):
        fraser_inphase[i - 1] = (in_phase[i - 3] + in_phase[i - 2]) - (in_phase[i - 1] + in_phase[i])

    df["Fraser_InPhase"] = fraser_inphase

    plt.figure(figsize=(9, 5))
    plt.plot(df["Station"], df["InPhase"], 'b-o', label="Raw In-Phase (%)")
    plt.plot(df["Station"], df["Fraser_InPhase"], 'r-s', label="Fraser Filtered In-Phase")
    plt.axhline(0, color='black', linestyle='--', alpha=0.6)

    plt.title('VLF-EM Fraser Filtering (Conductor Identification)', fontweight='bold')
    plt.xlabel('Station Position (m)')
    plt.ylabel('Response (%)')
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.tight_layout()

    out_path = os.path.join(output_dir, "vlf_fraser_profile.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[✓] Generated VLF Fraser Profile: {out_path}")