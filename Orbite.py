import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'serif'

def f(u, r):
    return r * u**2 * np.exp(-u)

# Parameters
r = 6
u0 = 0.3
num_iterations = 20

# Generate orbit
orbit = [u0]
for _ in range(num_iterations - 1):
    u_next = f(orbit[-1], r)
    orbit.append(u_next)

# Find fixed points
from scipy.optimize import fsolve
def fixed_point_equation(u, r):
    return 1 - r * u * np.exp(-u)

fixed_points = [0]  # u=0 is always a fixed point
for guess in [0.5, 1.0, 2.0]:
    try:
        fp = fsolve(fixed_point_equation, guess, args=(r,))[0]
        if fp > 0 and abs(fixed_point_equation(fp, r)) < 0.001:
            # Check if unique
            is_unique = True
            for existing in fixed_points:
                if abs(fp - existing) < 0.01:
                    is_unique = False
                    break
            if is_unique:
                fixed_points.append(fp)
    except:
        pass

# Plotting
plt.figure(figsize=(10, 6))
for fp in fixed_points:
    if fp > 0:
        plt.axhline(y=fp, linestyle='--', color='black', alpha=0.7,
                   label=rf'Неподвижная точка: ${fp:.3f}$')

plt.plot(orbit, marker='o', linestyle='-', color='blue', label='Орбита')
plt.xlabel(r'Итерация $t$')
plt.ylabel(r'$u_t$')
plt.title(r'Орбита системы: $u_{t+1} = r \cdot u_t^2 \cdot e^{-u_t}$')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

print(f"Начальное значение: $u_0 = {u0}$")
print(f"Конечное значение: $u_{{{num_iterations}}} = {orbit[-1]:.6f}$")
print(f"Неподвижные точки при $r={r}$: {[f'${fp:.4f}$' for fp in fixed_points]}")