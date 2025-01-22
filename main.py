import matplotlib.pyplot as plt
import numpy as np
import sys

# Função para obter o ângulo da linha de comando
def obter_angulo():
    try:
        return float(sys.argv[1])
    except (IndexError, ValueError):
        print("Uso: python script.py <angulo_em_graus>")
        sys.exit(1)

# Converter ângulo de graus para radianos
angulo = obter_angulo()
rad = np.radians(angulo)

# Dados para o gráfico
x = np.linspace(0, 10, 100)  # Gera 100 pontos entre 0 e 10
y = np.sin(x + rad)  # Função seno com deslocamento angular

# Configuração do gráfico
plt.figure(figsize=(10, 6))  # Define o tamanho da figura
plt.plot(x, y, label=f'Seno (deslocamento = {angulo}°)', linestyle='-', linewidth=2)  # Gráfico de linha

# Adicionando título e legendas
plt.title('Gráfico de Função Seno', fontsize=16)
plt.xlabel('Eixo X', fontsize=12)
plt.ylabel('Eixo Y', fontsize=12)
plt.legend(fontsize=12)

# Adicionando grade
plt.grid(True, linestyle='--', alpha=0.6)

# Salvando o gráfico em um arquivo
plt.savefig('grafico_seno.png', dpi=300)

# Tamanho desejado em bytes (1 MB = 1 * 1024 * 1024 bytes)
size_in_bytes = 0.5 * 1024 * 1024

# Gerar uma string de 1 MB composta por caracteres repetidos (por exemplo, "a")
mb_string = "a" * size_in_bytes

# Verificar o tamanho da string
print(f"Tamanho da string: {len(mb_string)} bytes:\n{md_string}")
