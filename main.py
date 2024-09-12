from AStar import *

def main(win,width):
    global found
    
    grid = make_grid(ROWS,width)

    start =None
    end =None

    run =  True
    while run:
        draw(win,grid,ROWS,width)
        run_btn = Button(630,30,"RUN")
        if run_btn.draw_button(win):
            if  start and  end:
                for row in grid:
                    for spot in row:
                        spot.update_neighbors(grid)

                found =algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
        if not found:
            result = font.render("No Solution",True,"red")
            win.blit(result,(630,500))
        else:
            result = font.render("Found!!!",True,"red")
            win.blit(result,(650,500))
            
    
        clear_btn = Button(630,170,"CLEAR")
        if clear_btn.draw_button(win):
            start = None
            end = None
            found = False
            grid = make_grid(ROWS, width)
        ran_btn = Button(630,310,"RANDOM")
        if ran_btn.draw_button(win):        
            grid = make_grid(ROWS, width)
            start = None
            end = None
            for row in grid:
                 for spot in row:
                      ran = random.randint(1,RANDOM_RATE)
                      if ran==1:
                           spot.make_barrier()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =False
            if pygame.mouse.get_pressed()[0]: # LEFT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                if 0<= row <=ROWS-1 and 0<=col<=ROWS-1:
                    spot = grid[row][col]
                    if not start and spot != end:
                        start = spot
                        start.make_start()
                    elif not end and spot != start:
                        end = spot
                        end.make_end()

                    elif spot != end and spot != start:
                        spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]: # RIGHT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                if 0<= row <=ROWS-1 and 0<=col<=ROWS-1:
                    spot = grid[row][col]
                    spot.reset()
                    if spot == start:
                        start = None
                    elif spot == end:
                        end = None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)

                    found =algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
                    
                if event.key == pygame.K_r:
                    start = None
                    end = None
                    found =False
                    grid = make_grid(ROWS, width)
                    grid = make_grid(ROWS, width)
                    for row in grid:
                     for spot in row:
                        ran = random.randint(1,RANDOM_RATE)
                        if ran==1:
                           spot.make_barrier()

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    found =False
                    
                    
    pygame.quit()

main(WIN,WIDTH)