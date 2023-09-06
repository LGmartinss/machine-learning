import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Crie uma grade 3D de valores x, y e z
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# Calcule uma função fictícia dependente de x e y (exemplo de kernel)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Crie uma figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plote a superfície 3D da função (kernel)
surf = ax.plot_surface(X, Y, Z, cmap='viridis')

# Adicione uma barra de cores
fig.colorbar(surf)

# Rotule os eixos
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Valor')

# Adicione um título ao gráfico
plt.title('Superfície de um Kernel')

# Mostre o gráfico
plt.show()
