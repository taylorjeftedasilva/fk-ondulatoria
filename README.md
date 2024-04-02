# README

Este é um repositório contendo um código Python para gerar um gráfico com base em dados específicos. Siga as instruções abaixo para instalar as dependências e executar o código.

## Instalação de Dependências

Para instalar as dependências necessárias, execute o seguinte comando:

```bash
pip install -r requirements.txt
```

Certifique-se de que o Python e o pip estejam devidamente instalados em seu ambiente.

## Executando o Código

Com as dependências instaladas, você pode executar o código diretamente a partir do terminal. Após abrir o terminal, execute o seguinte comando:

```python
from gerar_grafico import *
```

Isso resultará na execução de todo o código contido no arquivo `gerar_grafico.py`, gerando um gráfico dos dados.

Os dados usados para gerar o gráfico são os seguintes:

- Tempo (`t`): Intervalo de tempo desejado.
- Deslocamento (`s`): Representa o deslocamento ao longo do tempo.
- Velocidade (`v`): Representa a velocidade ao longo do tempo.
- Aceleração (`a`): Representa a aceleração ao longo do tempo.
- Energia (`E`): Representa a energia ao longo do tempo.

Você pode ajustar o intervalo de tempo (`t`) conforme desejado, modificando os parâmetros no código.

## Exemplo de Uso

```python
t = np.linspace(0, 10, 1000)  # Intervalo de tempo de 0 a 10 segundos
s = 3.7 * np.sin(15.4 * t + np.pi/2)
v = 3.7 * 15.4 * np.cos(15.4 * t + np.pi/2)
a = -3.7 * (15.4)**2 * np.sin(15.4 * t + np.pi/2)
E = 0.25 * v**2
```

Este exemplo define um intervalo de tempo de 0 a 10 segundos e gera os dados de deslocamento (`s`), velocidade (`v`), aceleração (`a`) e energia (`E`) correspondentes.

Sinta-se à vontade para modificar e adaptar o código conforme necessário para atender às suas necessidades. Se tiver alguma dúvida ou problema, não hesite em entrar em contato.

**Aproveite!** 🚀
