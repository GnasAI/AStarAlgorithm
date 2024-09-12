from settings import *
clicked =  False
found = None
class Button():
        
    #colours for button and text
    button_clr = RED
    hover_clr = (75, 225, 255)
    click_clr = (50, 150, 255)
    text_clr = BLACK
    width = 130
    height = 70

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self,win):

        global clicked
        action = False

        
        pos = pygame.mouse.get_pos()

        
        button_rect = Rect(self.x, self.y, self.width, self.height)
        
        
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(win, self.click_clr, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(win, self.hover_clr, button_rect)
        else:
            pygame.draw.rect(win, self.button_clr, button_rect)
        
        
        pygame.draw.line(win, 'white', (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(win, 'white', (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(win, 'black', (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(win, 'black', (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

        
        text_img = font.render(self.text, True, self.text_clr)
        text_len = text_img.get_width()
        win.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        return action
          
class Node:
    def __init__(self, row, col, width, total_rows):
        self.row =row
        self.col =col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row,self.col
    
    def is_closed(self):
        return self.color== RED
    
    def is_open(self):
        return self.color == YELLOW
    
    def is_barrier(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == PINK
    
    def is_end(self):
        return self.color == TURQUOISE
    
    def reset(self):
        self.color = WHITE
    
    def make_start(self):
        self.color = PINK

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = YELLOW
    
    def make_barrier(self):
        self.color = BLACK
    
    def make_end(self):
        self.color = TURQUOISE
    
    def make_path(self):
        self.color = SILVER

    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.width))
    
    def update_neighbors(self,grid):
        self.neighbors = []
        len = self.total_rows-1
        if self.row < len and not grid[self.row + 1][self.col].is_barrier(): # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
            self.neighbors.append(grid[self.row - 1][self.col])
        if self.col < len and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

        if self.col < len and self.row <len and not grid[self.row+1][self.col+1].is_barrier():#DOWN RIGHT
            self.neighbors.append(grid[self.row+1][self.col+1])
        if self.col > 0 and self.row <len and not grid[self.row+1][self.col-1].is_barrier(): #DOWN LEFT
             self.neighbors.append(grid[self.row+1][self.col-1])
        if self.col < len and self.row > 0 and not grid[self.row-1][self.col+1].is_barrier(): #UP RIGHT
             self.neighbors.append(grid[self.row-1][self.col+1])
        if self.col > 0 and self.row > 0 and not grid[self.row-1][self.col-1].is_barrier(): #UP LEFT
             self.neighbors.append(grid[self.row-1][self.col-1])

    def __lt__(self,other):
        return False
    

def h(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    return abs(x1-x2) +abs(y1-y2)

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()

def algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            start.make_start()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1
            try:
                if temp_g_score < g_score[neighbor]:    
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                    if neighbor not in open_set_hash:
                        count += 1
                        open_set.put((f_score[neighbor], count, neighbor))
                        open_set_hash.add(neighbor)
                        neighbor.make_open()
            except:
                pass
        draw()
        WIN.blit(nhom5,(650,50))
        WIN.blit(a,(680,150))
        WIN.blit(star,(665,250))
        WIN.blit(algo,(630,350))
        WIN.blit(finding,(640,500))
            

        
        
        pygame.display.update()
        if current != start:
            current.make_closed()

    return False

def make_grid(rows,width):
    grid = []
    gap = width //rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Node(i,j,gap,rows)
            grid[i].append(spot)
    return grid

def draw_grid(win,rows,width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win,GREY,(0, i * gap), (width, i * gap))
        for j in range(rows+1):
            pygame.draw.line(win,GREY,(j*gap,0),(j*gap,width))
def draw(win,grid,rows,width):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)

    
    
    draw_grid(win,rows,width)    
def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


