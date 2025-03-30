import random
from turtle import Turtle



class Food(Turtle):

    """
    Classe que representa o alimento no jogo da cobrinha.

    Esta classe herda da classe Turtle da biblioteca turtle e configura um objeto
    com aparência de um pequeno círculo azul que aparece em posições aleatórias
    na tela. A função principal da classe é gerar novos alimentos após serem
    coletados pela cobra.

    Métodos:
        __init__(): Inicializa o objeto Food com as características visuais e
                    posiciona-o em um local aleatório.
        refresh(): Atualiza a posição do alimento para um novo local aleatório
                   dentro da área visível da tela.
    """

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

