import numpy as np
import matplotlib.pyplot as plt

# Definição das funções
t = np.linspace(0, 2, 1000)  # Intervalo de tempo de 0 a 2 segundos
s = 3.7 * np.sin(15.4 * t + np.pi/2)
v = 3.7 * 15.4 * np.cos(15.4 * t + np.pi/2)
a = -3.7 * (15.4)**2 * np.sin(15.4 * t + np.pi/2)
E = 0.25 * v**2

# Plotagem dos gráficos
plt.figure(figsize=(12, 8))

# Gráfico da posição
plt.subplot(4, 1, 1)
plt.plot(t, s, label='Posição (s)')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (cm)')
plt.title('Gráfico da Posição ao Longo do Tempo')
plt.grid(True)
plt.legend()

# Gráfico da velocidade
plt.subplot(4, 1, 2)
plt.plot(t, v, label='Velocidade (v)')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (cm/s)')
plt.title('Gráfico da Velocidade ao Longo do Tempo')
plt.grid(True)
plt.legend()

# Gráfico da aceleração
plt.subplot(4, 1, 3)
plt.plot(t, a, label='Aceleração (a)')
plt.xlabel('Tempo (s)')
plt.ylabel('Aceleração (cm/s²)')
plt.title('Gráfico da Aceleração ao Longo do Tempo')
plt.grid(True)
plt.legend()
plt.tight_layout()


# Plotagem do gráfico energia total.
plt.subplot(4, 1, 4)
plt.plot(v, E, label='Energia Total')
plt.xlabel('Velocidade do Líquido (m/s)')
plt.ylabel('Energia Total (Joules)')
plt.title('Gráfico da Energia Total Transmitida pela Bomba para o Líquido')
plt.grid(True)
plt.legend()
plt.show()