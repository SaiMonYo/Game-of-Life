import pygame

WHITE = (255, 255, 255)
BLACK = ( 0 ,  0 ,  0 )

class Square:
    def __init__(self):
        self.state = False


class Grid:
    def __init__(self, win, grid_width, grid_height):
        self.win = win
        self.screen_width, self.screen_height = self.win.get_size()

        self.grid_width = grid_width
        self.grid_height = grid_height

        self.gap = self.screen_width // self.grid_width
        self.grid = [[Square() for i in range(self.grid_width)] for j in range(self.grid_height)]

    def get_neighbours(self, pos):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        n_count = 0
        for d in directions:
            x = pos[0] + d[0]
            y = pos[1] + d[1]
            if 0 <= x < len(self.grid[0]):
                if 0 <= y < len(self.grid[1]):
                    if self.grid[y][x].state:
                        n_count += 1
        return n_count

    def rules(self, n, state):
        if state:
            if n < 2:
                return False
            elif n == 2 or n == 3:
                return True
            else:
                return False
        if n == 3:
            return True

    def on_click(self, gridX, gridY, state):
        self.grid[gridY][gridX].state = state
    
    def loop(self):
        tmp = [[[] for x in range(self.grid_width)] for y in range(self.grid_height)]
        for j, row in enumerate(self.grid):
            for i, sq in enumerate(row):
                n = self.get_neighbours((i, j))
                tmp[j][i] = self.rules(n, sq.state)

        for rowT, rowS in zip(tmp, self.grid):
            for st, sq in zip(rowT, rowS):
                sq.state = st

    def draw_lines(self):
        for y in range(self.grid_height + 1):
            pygame.draw.line(self.win, BLACK, (0, self.gap * y), (self.screen_width, self.gap * y))
        for x in range(self.grid_width + 1):
            pygame.draw.line(self.win, BLACK, (self.gap * x, 0), (self.gap * x, self.screen_height))

    def draw_grid(self):
        for y, row in enumerate(self.grid):
            for x, sq in enumerate(row):
                if sq.state:
                    pygame.draw.rect(self.win, BLACK, (x * self.gap, y * self.gap, self.gap, self.gap))
                
