
import matplotlib.pyplot as plt

plt.ion()

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class arvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        self.raiz = self._inserir(self.raiz, valor)

    def _inserir(self, no, valor):
        if no is None:
            return No(valor)

        # Maiores a direita, menores a esquerda
        if valor < no.valor:
            no.esquerda = self._inserir(no.esquerda, valor)
        else:
            no.direita = self._inserir(no.direita, valor)

        return no  # Corrigido: fora do if/else para garantir o retorno correto

def desenhar_no(ax, no, x, y, distancia):
    if no is not None:
        ax.text(
            x,
            y,
            str(no.valor),
            fontsize=14,
            ha="center",
            va="center",
            bbox=dict(
                boxstyle="circle",
                facecolor="lightblue",
            )
        )

        if no.esquerda:
            ax.plot([x, x - distancia], [y - 0.1, y - 1], color="black")
            desenhar_no(ax, no.esquerda, x - distancia, y - 1, distancia / 2)

        if no.direita:  # Corrigido: agora é um if independente do esquerdo
            ax.plot([x, x + distancia], [y - 0.1, y - 1], color="black")
            desenhar_no(ax, no.direita, x + distancia, y - 1, distancia / 2)

def desenhar_arvore(raiz, valor_atual=None):
    plt.clf()
    fig = plt.gcf()
    fig.set_size_inches(10, 6)
    ax = plt.gca()
    ax.axis("off")

    if valor_atual is not None:
        ax.set_title(f"Valor atual: {valor_atual}", fontsize=16)

    desenhar_no(ax, raiz, 0, 0, 4)
    plt.draw()
    plt.pause(0.5)

# Bloco principal de execução (fora das funções)
if __name__ == "__main__":
    arvore = arvoreBinaria()

    print("ÁRVORE BINÁRIA DE BUSCA (BST)")
    print("Digite valores inteiros (-1 para sair)")

    while True:
        try:
            entrada = int(input("Digite um valor: "))

            if entrada == -1:
                break

            arvore.inserir(entrada)
            desenhar_arvore(arvore.raiz, entrada)
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

    plt.ioff()
    plt.show()