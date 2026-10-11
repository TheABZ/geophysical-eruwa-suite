import numpy as np


def schlumberger_kernel(rho, h, lam):
    """
    Computes the resistivity transform T(lambda) for a 3-layer earth model.
    rho: list/array of 3 layer resistivities [rho1, rho2, rho3]
    h: list/array of 2 layer thicknesses [h1, h2]
    """
    rho1, rho2, rho3 = rho
    h1, h2 = h

    # Kernel calculation from bottom layer up
    u3 = rho3
    u2 = rho2 * (u3 + rho2 * np.tanh(lam * h2)) / (rho2 + u3 * np.tanh(lam * h2))
    u1 = rho1 * (u2 + rho1 * np.tanh(lam * h1)) / (rho1 + u2 * np.tanh(lam * h1))

    return u1


def calculate_apparent_resistivity(ab2_spacings, rho, h):
    """
    Computes theoretical apparent resistivity for given AB/2 spacings
    using a 3-layer forward model.
    """
    rho_app = []
    for s in ab2_spacings:
        # Evaluate filter integral approximation
        lam = 1.0 / s
        r_val = schlumberger_kernel(rho, h, lam)
        rho_app.append(r_val)

    return np.array(rho_app)