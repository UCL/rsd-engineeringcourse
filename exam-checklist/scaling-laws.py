"""
This script generates the annotated benchmarking plot that appears in the exam knowledge checklist.

It will overwrite whatever is inside ./images/power-law-scaling.svg after executing.
"""

import numpy as np
import matplotlib.pyplot as plt

N = np.logspace(0.0, 10.0, num=1000, base=10.0, dtype=float)


def arrow_style(color: str = "black"):
    return {
        "arrowstyle": "->",
        "fill": False,
        "linestyle": "--",
        "color": color,
    }


def pl(x):
    return 3.0 * x**1.5


data_pl = pl(N)

f_pl, ax_pl = plt.subplots(1, 2)
ax_pl: tuple[plt.Axes]

# Power-law, log-log axes

ax_pl[0].loglog(N, data_pl, color="black")
ax_pl[0].set_xlabel(r"$N$")
ax_pl[0].set_ylabel(r"$t$")
ax_pl[0].set_aspect("equal")
ax_pl[0].set_xticks(10.0 ** np.arange(0.0, 11.0, 2.0))
ax_pl[0].set_yticks(10.0 ** np.arange(0.0, 17.0, 1.0))
ax_pl[0].grid(visible=True, which="major")

ax_pl[0].annotate(
    r"At $N=10^0$," "\n" r"$t \approx 10^{0.5} \approx 3$",
    xy=(1.0, 3.0),
    xytext=(10**4, 10**1),
    color="blue",
    arrowprops=arrow_style("blue"),
    va="bottom",
    ha="center",
)
ax_pl[0].annotate(
    r"$\Delta t = $" "\n" r"$10^{15.5} - 10^2$",
    xy=(10**1, 3 * 10**15),
    xytext=(10**1, 10**9),
    color="red",
    ha="center",
    arrowprops=arrow_style("red"),
)
ax_pl[0].annotate(
    "",
    xy=(10**1, 10**2),
    xytext=(10**1, 10**9),
    color="red",
    ha="center",
    arrowprops=arrow_style("red"),
)
ax_pl[0].annotate(
    r"$\Delta N = 10^{10} - 10^1$",
    xy=(10**10, 3 * 10**15),
    xytext=(10**8, 3 * 10**15),
    color="red",
    va="center",
    ha="right",
    arrowprops=arrow_style("red"),
)
ax_pl[0].annotate(
    "",
    xy=(10**1, 3 * 10**15),
    xytext=(10**2.75, 3 * 10**15),
    va="center",
    ha="left",
    arrowprops=arrow_style("red"),
)
ax_pl[0].annotate(
    r"$\frac{15.5 - 2}{10 - 1} = \frac{13.5}{9} = 1.5$",
    xy=(10**4, 10**12),
    color="red",
    va="center",
    ha="center",
)

# Power law, log'd quantities

ax_pl[1].plot(np.log(N), np.log(data_pl), color="black")
ax_pl[1].set_xlabel(r"$\log N$")
ax_pl[1].set_ylabel(r"$\log t$")
ax_pl[1].set_aspect("equal")
ax_pl[1].set_xticks(np.arange(0.0, 25.0, 2.0))
ax_pl[1].set_yticks(np.arange(0.0, 37.0, 2.0))
ax_pl[1].grid(visible=True, which="major")

ax_pl[1].annotate(
    r"$\Delta y = 30$",
    xy=(2, 4),
    xytext=(2, 20),
    color="red",
    ha="center",
    va="top",
    arrowprops=arrow_style("red"),
)
ax_pl[1].annotate(
    "",
    xy=(2, 34),
    xytext=(2, 20),
    ha="center",
    va="bottom",
    arrowprops=arrow_style("red"),
)
ax_pl[1].annotate(
    "",
    xy=(2, 34),
    xytext=(6, 34),
    va="center",
    ha="left",
    arrowprops=arrow_style("red"),
)
ax_pl[1].annotate(
    r"$\Delta x = 20$",
    xy=(22, 34),
    xytext=(12, 34),
    color="red",
    va="center",
    ha="right",
    arrowprops=arrow_style("red"),
)
ax_pl[1].annotate(
    r"$\frac{\Delta y}{\Delta x} = 1.5$",
    xy=(4, 29),
    color="red",
    va="center",
    ha="left",
)
ax_pl[1].annotate(
    "y-intercept at \n" r"$1.1 \approx \log 3$",
    xy=(0, np.log(3.0)),
    xytext=(10.25, 7),
    arrowprops=arrow_style("blue"),
    ha="left",
    va="center",
    color="blue",
)

f_pl.suptitle(r"Power law scaling, $t = 3N^{1.5}$")
f_pl.tight_layout()
f_pl.savefig("images/power-law-scaling.svg")
