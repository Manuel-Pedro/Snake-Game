from snake import Snake


UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Control:

    """
        Classe responsável por controlar a direção da cobra no jogo.

        Essa classe atua como um controlador de movimentos da instância da classe
        Snake, modificando a direção da cabeça da cobra conforme comandos (geralmente
        ligados a teclas do teclado).

        Atributos:
            move_snake (Snake): Instância da cobra que será controlada.

        Métodos:
            up(): Altera a direção da cobra para cima, se não estiver indo para baixo.
            down(): Altera a direção da cobra para baixo, se não estiver indo para cima.
            left(): Altera a direção da cobra para a esquerda, se não estiver indo para a direita.
            right(): Altera a direção da cobra para a direita, se não estiver indo para a esquerda.
        """

    def __init__(self, move_snake: Snake):
        self.move_snake = move_snake

    def up(self):
        if self.move_snake.head.heading() != DOWN:
            self.move_snake.head.setheading(UP)

    def down(self):
        if self.move_snake.head.heading() != UP:
            self.move_snake.head.setheading(DOWN)

    def left(self):
        if self.move_snake.head.heading() != RIGHT:
            self.move_snake.head.setheading(LEFT)

    def right(self):
        if self.move_snake.head.heading() != LEFT:
            self.move_snake.head.setheading(RIGHT)

