import numpy as np


class Resistivity1DForward:
    """1D Forward Numerical Modeling for Schlumberger Electrical Resistivity Sounding

    Uses digital linear filtering (Guptasarma 10-point filter) to solve the
    Hankel transform integral for multi-layer Earth resistivity.
    """

    # Guptasarma (1979) 10-point linear filter coefficients for Schlumberger array
    FILTER_WEIGHTS = np.array(
        [
            0.00049,
            -0.00319,
            0.01358,
            -0.03823,
            0.08781,
            -0.18341,
            0.34965,
            0.60533,
            0.18029,
            -0.01232,
        ]
    )

    # Shift values for filter sampling distances
    FILTER_SHIFTS = np.array(
        [
            -2.830,
            -2.330,
            -1.830,
            -1.330,
            -0.830,
            -0.330,
            0.170,
            0.670,
            1.170,
            1.670,
        ]
    )

    def __init__(self, resistivities: list[float], thicknesses: list[float]):
        """Parameters:

        -----------
        resistivities : list of float
            Resistivity values (Ohm-m) for each layer [rho_1, rho_2, ...,
            rho_n].
        thicknesses : list of float
            Layer thicknesses (m) for [h_1, h_2, ..., h_(n-1)]. (Bottom layer
            is infinite).
        """
        if len(resistivities) != len(thicknesses) + 1:
            raise ValueError(
                "Number of resistivities must be exactly 1 more than number of thicknesses."
            )

        self.rho = np.array(resistivities, dtype=np.float64)
        self.h = np.array(thicknesses, dtype=np.float64)
        self.n_layers = len(self.rho)

    def _compute_transform(self, lam: float) -> float:
        """Computes the kernel resistivity transform T(lambda) recursively from

        the bottom layer (n) to the surface layer (1).
        """
        # Base condition: T_n = rho_n for the infinite half-space basement
        T = self.rho[-1]

        # Recursive step from layer n-1 up to layer 1
        for i in range(self.n_layers - 2, -1, -1):
            tan_h = np.tanh(lam * self.h[i])
            T = (T + self.rho[i] * tan_h) / (1.0 + (T / self.rho[i]) * tan_h)

        return T

    def forward(self, ab_half_spacings: np.ndarray) -> np.ndarray:
        """Calculates synthetic apparent resistivity for a vector of AB/2

        spacings.
        """
        app_resistivity = []

        for s in ab_half_spacings:
            # Calculate sampling points lambda_k = 10^(shift) / s
            lambdas = (10 ** self.FILTER_SHIFTS) / s

            # Evaluate Kernel T(lambda) at each sampling point
            T_values = np.array([self._compute_transform(lam) for lam in lambdas])

            # Apply digital filter dot product
            rho_a = np.sum(T_values * self.FILTER_WEIGHTS)
            app_resistivity.append(rho_a)

        return np.array(app_resistivity)