import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from scipy.interpolate import griddata


def plot_2d_cst_pseudosection(csv_path, output_dir="outputs"):
    df = pd.read_csv(csv_path)

    spacings = np.array([5, 10, 15, 20, 25, 30])
    pseudo_depths = spacings * 0.5

    X_list, Z_list, Rho_list = [], [], []
    for idx, row in df.iterrows():
        st = row["Station"]
        for a_val, z in zip(spacings, pseudo_depths):
            col_name = f"a_{a_val}"
            if col_name in row and not np.isnan(row[col_name]):
                X_list.append(st)
                Z_list.append(z)
                Rho_list.append(row[col_name])

    X, Z, Rho = np.array(X_list), np.array(Z_list), np.array(Rho_list)

    # 2D Grid Interpolation
    grid_x, grid_z = np.mgrid[min(X):max(X):200j, min(Z):max(Z):100j]
    grid_rho = griddata((X, Z), Rho, (grid_x, grid_z), method='cubic')

    # Filter grid to positive values to avoid log scale warnings
    grid_rho_clean = np.where(grid_rho > 0, grid_rho, np.nan)

    valid_rho = Rho[Rho > 0]
    vmin = np.nanmin(valid_rho) if len(valid_rho) > 0 else 10.0
    vmax = np.nanmax(valid_rho) if len(valid_rho) > 0 else 1000.0

    plt.figure(figsize=(10, 4.5))
    contour = plt.contourf(
        grid_x, grid_z, grid_rho_clean,
        levels=50,
        cmap='turbo',
        norm=LogNorm(vmin=vmin, vmax=vmax)
    )
    cbar = plt.colorbar(contour)
    cbar.set_label('Apparent Resistivity (Ω·m)', rotation=270, labelpad=15)

    plt.gca().invert_yaxis()
    plt.title('2D Resistivity Pseudosection (CST Profile)', fontweight='bold')
    plt.xlabel('Traverse Position (m)')
    plt.ylabel('Pseudodepth (m)')
    plt.tight_layout()

    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, "cst_2d_pseudosection.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[✓] Generated 2D CST Pseudosection: {out_path}")