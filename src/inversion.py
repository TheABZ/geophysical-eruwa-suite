import numpy as np
from scipy.optimize import least_squares
from src.forward_model import Resistivity1DForward


class Resistivity1DInversion:
    """Inversion engine for 1D Schlumberger resistivity data

    using Levenberg-Marquardt least-squares optimization.
    """

    def __init__(
        self, ab_half: np.ndarray, observed_rho_a: np.ndarray, n_layers: int
    ):
        self.ab_half = ab_half
        self.d_obs = observed_rho_a
        self.n_layers = n_layers

    def _residuals(self, log_params: np.ndarray) -> np.ndarray:
        params = np.exp(log_params)
        rhos = params[: self.n_layers]
        thicknesses = params[self.n_layers :]

        fwd = Resistivity1DForward(rhos, thicknesses)
        d_pred = fwd.forward(self.ab_half)

        return np.log(d_pred) - np.log(self.d_obs)

    def invert(self, initial_rhos: list[float], initial_thicknesses: list[float]):
        init_params = np.array(
            initial_rhos + initial_thicknesses, dtype=np.float64
        )
        log_init = np.log(init_params)

        result = least_squares(self._residuals, log_init, method="lm")

        inv_params = np.exp(result.x)
        inv_rhos = inv_params[: self.n_layers].tolist()
        inv_thicknesses = inv_params[self.n_layers :].tolist()

        fwd_final = Resistivity1DForward(
            inv_rhos, inv_thicknesses
        ).forward(self.ab_half)
        rms_error = (
            np.sqrt(np.mean(((self.d_obs - fwd_final) / self.d_obs) ** 2)) * 100
        )

        return inv_rhos, inv_thicknesses, rms_error