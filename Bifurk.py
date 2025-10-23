import numpy as np
import matplotlib.pyplot as plt

# Настройки для LaTeX
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 12


def f(u, r):
    return r * u ** 2 * np.exp(-u)


# Параметры
r_min, r_max = 0, 20
num_r = 5000
num_skip = 200
num_draw = 100

r_values = np.linspace(r_min, r_max, num_r)

plt.figure(figsize=(14, 8))

for r in r_values:
    u = 0.5
    for _ in range(num_skip):
        u = f(u, r)

    points_to_draw = []
    for _ in range(num_draw):
        u = f(u, r)
        points_to_draw.append(u)

    plt.plot([r] * len(points_to_draw), points_to_draw, ',k', alpha=0.2, markersize=0.5)

plt.xlabel(r'Параметр $r$')
plt.ylabel(r'$u_t$')
plt.title(r'Бифуркационная диаграмма: $u_{t+1} = r \cdot u_t^2 \cdot e^{-u_t}$')
plt.grid(True, alpha=0.2)
plt.tight_layout()
plt.show()