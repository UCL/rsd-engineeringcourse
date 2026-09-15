from typing import Callable

import numpy as np


def linear_weighting(x_min, x_max) -> Callable[[np.ndarray], np.ndarray]:
    """
    Return the function

    f(x) =
        0                               if x <= x_min
        1                               if x >= x_max
        (x - x_min) / (x_max - x_min)   if x_min < x < x_max
    """

    def f(x: np.ndarray) -> np.ndarray:
        """ """
        if not isinstance(x, np.ndarray):
            x = np.asarray([x], dtype=float)

        x_lt_min = x <= x_min
        x_gt_max = x >= x_max
        other_x = (x_min < x) & (x < x_max)

        eval = np.zeros_like(x)
        eval[x_lt_min] = 0.0
        eval[x_gt_max] = 1.0
        eval[other_x] = (x[other_x] - x_min) / (x_max - x_min)
        return eval

    return f
