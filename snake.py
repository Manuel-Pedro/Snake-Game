from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class  Snake:

    """
        Classe que representa a cobra no jogo da cobrinha (Snake Game).

        A cobra é formada por uma lista de segmentos (objetos Turtle) que se movem
        em conjunto. A classe é responsável por criar a cobra inicial, movimentá-la
        pela tela, e estendê-la ao consumir alimentos.

        Atributos:
            segments (list): Lista de segmentos (Turtle) que formam o corpo da cobra.
            head (Turtle): Referência para o primeiro segmento da cobra (a cabeça).

        Métodos:
            __init__(): Inicializa a cobra com segmentos nas posições definidas
                        em STARTING_POSITIONS e define o primeiro segmento como a cabeça.
            create_snake(): Cria a cobra inicial com base nas posições iniciais.
            add_segment(position): Adiciona um novo segmento na posição especificada.
            extend(): Adiciona um novo segmento na cauda da cobra, estendendo o corpo.
            move(): Move a cobra para frente, fazendo os segmentos seguirem o da frente.
        """

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("White")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)



