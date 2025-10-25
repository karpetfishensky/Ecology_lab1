import numpy as np
import matplotlib.pyplot as plt

# Настройки для красивого отображения формул
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 12

# Параметры
r_values = np.linspace(2, 15, 500)
num_iterations = 1000
transient = 100


# Функция системы
def f(x, r):
    return r * x ** 2 * np.exp(-x)


# Производная функции
def f_derivative(x, r):
    return r * x * np.exp(-x) * (2 - x)


# Функция для вычисления экспоненты Ляпунова
def lyapunov_exponent(r, x0=1.0):
    x = x0
    lyap_sum = 0
    valid_iterations = 0

    for i in range(num_iterations):
        x = f(x, r)
        if i >= transient:
            deriv = abs(f_derivative(x, r))
            if deriv > 1e-15:
                lyap_sum += np.log(deriv)
                valid_iterations += 1

    return lyap_sum / valid_iterations if valid_iterations > 0 else 0


# Расчет показателя Ляпунова
lyapunov = []
for r in r_values:
    lyap_vals = [lyapunov_exponent(r, x0) for x0 in [0.5, 1.0, 1.5, 2.0]]
    lyapunov.append(np.mean(lyap_vals))

# Построение графика с LaTeX формулами
plt.figure(figsize=(12, 8))
plt.plot(r_values, lyapunov, color='blue', linewidth=1)
plt.axhline(0, color='red', linestyle='--', linewidth=1)

# Использование LaTeX для подписей
plt.xlabel(r'Параметр $r$', fontsize=14)
plt.ylabel(r'Показатель Ляпунова $\lambda$', fontsize=14)
plt.title(r'График показателя Ляпунова для системы $u_{t+1} = r \cdot u_t^2 \cdot e^{-u_t}$',
          fontsize=16, pad=20)

plt.grid(True, alpha=0.3)
plt.ylim(-7, 1)

# Добавляем пояснения с использованием LaTeX
plt.text(0.02, 0.98, r'$\lambda > 0$: хаотическое поведение',
         transform=plt.gca().transAxes, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
plt.text(0.02, 0.88, r'$\lambda < 0$: регулярное поведение',
         transform=plt.gca().transAxes, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.show()