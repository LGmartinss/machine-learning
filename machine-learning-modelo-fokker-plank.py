import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parâmetros do sistema
D = 0.1  # Coeficiente de difusão
x_min, x_max = -5, 5  # Limites do espaço
t_min, t_max = 0, 1  # Limites do tempo

# Crie uma grade tridimensional de valores x, t e p (densidade de probabilidade)
x = np.linspace(x_min, x_max, 100)
t = np.linspace(t_min, t_max, 100)
X, T = np.meshgrid(x, t)

# Calcule a densidade de probabilidade fictícia (uma gaussiana)
mu = 0  # Média
sigma = 1  # Desvio padrão
P = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((X - mu)**2) / (2 * sigma**2))

# Crie uma figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plote a superfície 3D da densidade de probabilidade
surf = ax.plot_surface(X, T, P, cmap='viridis')

# Adicione uma barra de cores
fig.colorbar(surf)

# Rotule os eixos
ax.set_xlabel('Espaço (x)')
ax.set_ylabel('Tempo (t)')
ax.set_zlabel('Densidade de Probabilidade (P)')

# Adicione um título ao gráfico
plt.title('Distribuição de Probabilidade em um Sistema Unidimensional')

# Mostre o gráfico
plt.show()
