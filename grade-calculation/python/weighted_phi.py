from typing import Callable, Optional

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import newton


class WeightedPhi:
    """
    Class object that represents a weighting function.

    Instances can be evaluated using function syntax, and store their parameters internally.
    Weighting functions are some variation on the mapping:

    phi(x) =
        min_value                                                               if x <= 0
        max_value                                                               if x >= 1
        min_value + (max_value - min_value) * exp((x-1)**2 / (1 - (x-1)**2))    if 0 < x < 1

    If the inner attribute is set, this defines a function which the above mapping is composed
    with. IE an instance with self.inner(x) = f(x) will perform the mapping phi(f(x)).
    The inner function is intended to be a non-decreasing, continuous mapping of [0,1] to [0,1].
    Note that this function does not have to be differentiable (though smoothness is lost if it
    is not, of course).
    """

    _w_max: float
    _w_min: float

    inner: Callable[[np.ndarray], np.ndarray]

    @staticmethod
    def phi(x: np.ndarray) -> np.ndarray:
        """
        Return an evaluation of the function

        phi(x) =
            0                               if x <= 0,
            1                               if x >= 1,
            exp(-(x-1)**2 / (1 - (x-1)**2)) if 0 < x < 1.
        """
        evaluation = np.zeros_like(x)

        x_lt_0 = x <= 0.0
        x_gt_1 = x >= 1.0
        other_x = (0.0 < x) & (x < 1.0)

        evaluation[x_lt_0] = 0.0
        evaluation[x_gt_1] = 1.0
        evaluation[other_x] = np.exp(
            -((x[other_x] - 1.0) ** 2) / (1.0 - (x[other_x] - 1.0) ** 2)
        )
        return evaluation

    @property
    def gamma(self) -> float:
        """
        Factor which determines whether self^{-1}(1) exists.

        If this factor is equal to 1, the function cannot attain the value 1.
        """
        return np.log((1.0 - self.w_min) / (self.w_max - self.w_min))

    @property
    def invert_unity(self) -> float:
        """
        The value y for which

        self(inner^{-1}(y)) = 1.

        It can be computed analytically as

        1 +/- sqrt(self.gamma / (self.gamma - 1))

        though since the inner function is assumed to map into [0,1], only the
        -ve root is going to be attained.
        """
        return 1 - np.sqrt(self.gamma / (self.gamma - 1))

    @property
    def w_max(self) -> float:
        return self._w_max

    @w_max.setter
    def w_max(self, new_value: float) -> None:
        assert (
            new_value > self.w_min
        ), f"New value for max ({new_value}) is less than current min value ({self.w_min})"
        self._w_max = new_value

    @property
    def w_min(self) -> float:
        return self._w_min

    @w_min.setter
    def w_min(self, new_value: float) -> None:
        assert (
            new_value < self.w_max
        ), f"New value for min ({new_value}) is greater than current max value ({self.w_min})"
        self._w_min = new_value

    def __call__(self, x: np.ndarray) -> np.ndarray:
        """
        Evaluate this weighted function, returning the corresponding values.
        """
        return self.w_min + (self.w_max - self.w_min) * self.phi(self.inner(x))

    def __init__(
        self,
        min_value: float = 0.4,
        max_value: float = 1.0,
        inner: Optional[Callable[[np.ndarray], np.ndarray]] = None,
    ) -> None:
        """ """
        # Ensure that values can be assigned on instantiation.
        self._w_min = 0.0
        self._w_max = 1.0

        self.w_min = min_value
        self.w_max = max_value

        # Assign the inner function if given, otherwise ensure that its the identity.
        if inner is not None:
            self.inner = inner
        else:
            self.inner = lambda x: x

    def _check_attains_unity(self) -> bool:
        """
        Assert that the weighted function attains the value 1 within the interval for which
        it is a non-constant function.

        The function can only attain unity in this interval if self.gamma is sufficiently
        different from 1.
        """
        return not np.any(np.isclose(self.gamma, 1.0))

    def attains_unity_at(self, x0: float = 0.5, **newton_args) -> float:
        """
        Return the value of x for which self(x) = 1.

        Root is computed approximately using Newton-Raphson.
        The value 1 is attained when

        self.inner(x)   = 1 - sqrt(self.gamma / (self.gamma - 1))
                        = self.invert_unity(),

        and can only be attained if gamma =/= 1.

        newton_args (and the value x0 if supplied) are passed to scipy.optimize.newton.
        x0 can also be supplied as a key in the newton_args, and will be used. Otherwise,
        the method will be given 0.5 as a starting guess.
        """
        assert self._check_attains_unity(), (
            f"{self.gamma} is too close to 1, "
            "this function does not attain the value 1."
        )

        # Now solve self.inner(x) = self.invert_unity(),
        # Use a supplied x0 in the optional arguments if it is provided.
        if "x0" not in newton_args:
            newton_args["x0"] = x0

        # Need to solve when the inner function equals the inversion value,
        # so translate into lambda function before passing to Newton.
        def newton_func(x):
            return self.inner(x) - self.invert_unity

        answer = newton(func=newton_func, **newton_args)
        if isinstance(answer, np.ndarray) and answer.size == 1:
            answer = answer[0]
        return answer

    def plot(self, n_eval_pts: int = 1000) -> None:
        """
        Create a plot over the interval [0,1] of the weighting function,
        highlighting key features.

        Features highlighted on the plot will be:
        - The value self.w_min (y-axis)
        - The value self.w_max (y-axis)
        - The value 1 (y-axis)
        """
        fig, ax = plt.subplots()
        y_min = self.w_min * 0.9
        y_max = self.w_max * 1.1
        x_unity = self.attains_unity_at()

        ax.set_title(f"Weighting function (unity at {np.round(x_unity, decimals=3)})")
        ax.set_xlabel("x")
        ax.set_ylabel("G(x)")
        ax.set_xlim(0.0, 1.0)
        ax.set_ylim(y_min, y_max)

        # Plot weighting function
        x = np.linspace(0.0, 1.0, num=n_eval_pts)
        ax.plot(x, self(x))

        # Plot value at which unity is attained
        ax.vlines(x_unity, y_min, 1.0, color="black", linestyles="dashed")
        ax.hlines(1.0, 0.0, x_unity, color="black", linestyles="dashed")

        fig.savefig("plot.png")
        fig.show()
        return
