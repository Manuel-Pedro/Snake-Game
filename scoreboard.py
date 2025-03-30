from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


class Scoreboard(Turtle):

    """
        Classe responsável por exibir e atualizar a pontuação do jogador na tela.

        Herda da classe Turtle da biblioteca turtle e cria uma interface simples
        para mostrar a pontuação do jogador durante o jogo, bem como exibir a
        mensagem de "GAME OVER" ao final do jogo.

        Atributos:
            score (int): Armazena a pontuação atual do jogador.

        Métodos:
            __init__(): Inicializa o placar com pontuação zero e exibe na parte
                        superior da tela.
            update_scoreboard(): Atualiza o texto do placar com a pontuação atual,
                                 se for igual a zero (chamado no início).
            game_over(): Exibe a mensagem "GAME OVER" no centro da tela.
            increase_score(): Incrementa a pontuação em 1, limpa o texto anterior
                              e exibe a nova pontuação.
        """
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        if self.score == 0:
            self.clear()
            self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()


    #def game_over(self):
    #    self.color("red")
    #    self.goto(0, 0)
    #    self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

