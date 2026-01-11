import pygame
import numpy as np
from random import randint


window_height = 500
window_width = 500
border_x = 30
border_y = 30

class Window:
    def __init__(self):
        self.page = 0
        pygame.init()

        self.window = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("2D/3D Maze")

        self.direction = 0
        self.maze_init()
        self.radius = min(self.maze_x/self.matrix_x, self.maze_y/self.matrix_y) *0.25

        rand_y = 5
        rand_x = 5
        while self.maze_matrix[rand_y][rand_x]:
            rand_x, rand_y = self.random_coordinates()
        
        self.x = (rand_x+0.5) * (self.maze_x / self.matrix_x) + border_x
        self.y = (rand_y+0.5) * (self.maze_y / self.matrix_y) + border_y


    def maze_init(self):
        self.matrix_x = 20
        self.matrix_y = 20
        self.maze_matrix = np.zeros((self.matrix_y, self.matrix_x))

        self.maze_x = (window_width - 2*border_x)
        self.maze_y = (window_height - 2*border_y)

        percent_walls = 30
        no_walls = int( self.matrix_x*self.matrix_y * (percent_walls/100) )
    
        cells = [(x, y) for y in range(self.matrix_y) for x in range(self.matrix_x)]
        np.random.shuffle(cells)
        for x, y in cells[:no_walls]:
            self.maze_matrix[y][x] = 1



    def random_coordinates(self):
        rand_x = randint(0, len(self.maze_matrix[0])-1)
        rand_y = randint(0, len(self.maze_matrix)-1)
        return rand_x, rand_y


    def maze_structure(self):
        square_x = self.maze_x / self.matrix_x
        square_y = self.maze_y / self.matrix_y

        position_y = 0 + border_y
        for i in self.maze_matrix:
            position_x = 0 + border_x
            for j in i:
                if j == 0:
                    pygame.draw.rect(self.window, (100, 100, 100), (position_x, position_y, square_x, square_y)) 
                else:
                    pygame.draw.rect(self.window, (50, 50, 50), (position_x, position_y, square_x, square_y)) 
                position_x += square_x
            position_y += square_y
     

    def find_cell(self, x, y):
        grid_x = self.maze_x / self.matrix_x         
        cell_x = int(np.floor( (x-border_x) / grid_x ))
        grid_y = self.maze_y / self.matrix_y         
        cell_y = int(np.floor( (y-border_y) / grid_y ))
        return cell_x, cell_y
    

    def find_next_coord(self, x, y, angle, length):
        x2 = x + np.cos(angle) * length
        y2 = y + np.sin(angle) * length
        return x2, y2
    
    #first raycasting function
    # marching step algorithm
    def raycasting(self, angle):
        self.max_length = max(self.maze_x/self.matrix_x, self.maze_y/self.matrix_y) * 7.5

        line_length = 0
        increment = 1
        x2, y2 = self.x, self.y
        while line_length < self.max_length:
            line_length += increment
            x2, y2 = self.find_next_coord(self.x, self.y, angle, line_length)
            x_square, y_square = self.find_cell(x2, y2)
        
            if (
                x_square < 0 or
                y_square < 0 or
                x_square >= self.matrix_x or
                y_square >= self.matrix_y or
                self.maze_matrix[y_square][x_square] == 1
            ):
                break
        if self.page==0:
            pygame.draw.line(self.window, (255,255,255), (x2, y2), (self.x, self.y))

        return line_length
    


    #DDA (Digital Differential Analyzer)
    def raycasting_DDA(self, angle):
        self.max_length = max(self.maze_x/self.matrix_x, self.maze_y/self.matrix_y) * 7.5

        # Change to cell coordinate system
        cell_width = self.maze_x / self.matrix_x
        cell_height = self.maze_y / self.matrix_y
        map_x = int((self.x-border_x) / cell_width)
        map_y = int((self.y-border_y) / cell_height)

        #ray direction as a unit vector
        ray_dx = np.cos(angle)
        ray_dy = np.sin(angle)

        #Scaling Vector
        scale_x = float('inf') if ray_dx == 0 else abs(1 / ray_dx)
        scale_y = float('inf') if ray_dy == 0 else abs(1 / ray_dy)

        sign_x = int( np.sign(ray_dx) )
        sign_y = int( np.sign(ray_dy) )

        ray_start_x = (self.x - border_x) / (cell_width)
        ray_start_y = (self.y - border_y) / (cell_height)

        if sign_x != 0:
            ray_length_x = (
                ((map_x + 1) - ray_start_x) if sign_x == 1 else (ray_start_x - map_x)
            ) * cell_width * scale_x
        else:
            ray_length_x = float('inf')

        if sign_y != 0:
            ray_length_y = (
                ((map_y + 1) - ray_start_y) if sign_y == 1 else (ray_start_y - map_y)
            ) * cell_height * scale_y
        else:
            ray_length_y = float('inf')
 

        hit = False
        side = None
        while not hit:
            if abs(ray_length_x) <= abs(ray_length_y):
                map_x += 1*sign_x
                ray_length_x += scale_x * cell_width
                side = 0
            else:
                map_y += 1*sign_y 
                ray_length_y += scale_y * cell_height
                side = 1
            
            if (
                map_x < 0 or
                map_y < 0 or
                map_x >= self.matrix_x or
                map_y >= self.matrix_y or
                self.maze_matrix[map_y][map_x] == 1
            ):
                hit = True
            elif min(ray_length_x, ray_length_y) >= self.max_length:
                side = 2
                break

        if side == 0:
            line_length = ray_length_x - (scale_x * cell_width)
        elif side == 1:
            line_length = ray_length_y - (scale_y * cell_height)
        else:
            line_length = self.max_length
       
        #draw ray paths
        if self.page==0:
            x2 = self.x + (sign_x * line_length * 1/scale_x)
            y2 = self.y + (sign_y * line_length * 1/scale_y)
            pygame.draw.line(self.window, (255,255,255), (x2, y2), (self.x, self.y))


        return line_length

 

    def calculate_distant_to_wall(self):
        self.field_view_angle = 80
        angle = self.direction - self.field_view_angle/2 
        angle = np.deg2rad(angle)

        self.number_of_rays = 80
        step = int(self.field_view_angle/self.number_of_rays)
        self.length_list = []
        for theta in range( int(-self.field_view_angle/2), int(self.field_view_angle/2), step):
            angle = np.deg2rad(self.direction + theta)
            line_length = self.raycasting_DDA(angle)
            self.length_list.append((line_length, angle))


    def button(self, button_pressed):
        position_x = 5
        position_y = 5
        height = 20
        width = 50
        smallfont = pygame.font.SysFont('Corbel',20)
        text = smallfont.render('View' , True , (25,25,25))

        mouse = pygame.mouse.get_pos()
        if position_x <= mouse[0] <= position_x+width and position_y <= mouse[1] <= position_y + height:
            if button_pressed:
                if self.page == 1:
                    self.page = 0
                else:
                    self.page = 1            
            pygame.draw.rect(self.window, (100,100,100), (position_x, position_y, width, height)) 
        else:   
            pygame.draw.rect(self.window, (170,170,170), (position_x, position_y, width, height)) 
        self.window.blit(text , (width/2 -15,height/2-4))


    def can_move(self, x, y):
        offsets = [
            ( self.radius,  0),
            (-self.radius,  0),
            ( 0,  self.radius),
            ( 0, -self.radius),
        ]

        for ox, oy in offsets:
            x_sq, y_sq = self.find_cell(x + ox, y + oy)

            if (
                x_sq < 0 or
                y_sq < 0 or
                x_sq >= self.matrix_x or
                y_sq >= self.matrix_y or
                self.maze_matrix[y_sq][x_sq] == 1
            ):
                return False
        return True    
 
    
    def two_d_view(self):        
        self.maze_structure()
        pygame.draw.circle(self.window, (255, 0, 0), (self.x, self.y), self.radius) 

  
    def three_d_view(self):
        pygame.draw.rect(self.window, (50,50,50), (border_x, window_height/2, self.maze_x, self.maze_y/2)) 

        width = self.maze_x / len(self.length_list)
        position_x = border_x

        proj_plane_dist = (self.maze_x / 2) / np.tan(np.deg2rad(self.field_view_angle / 2))
        wall_height = 20

        for length, angle in self.length_list:
            if length < self.max_length:
                
                # new corrected method
                corrected_length = length * np.cos(angle - np.deg2rad(self.direction))
                corrected_length = max(corrected_length, 0.0001)
                height = (wall_height / corrected_length) * proj_plane_dist
                height = min(height, self.maze_y)
                colour = 255 / (1 + corrected_length * 0.01)
                colour = max(40, min(200, int(colour)))

                position_y = border_y + self.maze_y/2 - height/2


                pygame.draw.rect(self.window, (colour,colour,colour), (position_x+0.25, position_y, width-0.5, height)) 
            position_x += width
        


    def main_loop(self, vel):
        run = True
        while run:
            pygame.time.delay(2) # Time Delay
             
            button_pressed = False
            # Key Press 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    button_pressed = True             

            keys = pygame.key.get_pressed() 
            rad = np.deg2rad(self.direction)

            dx = np.cos(rad) * vel
            dy = np.sin(rad) * vel

            if keys[pygame.K_w]:
                if self.can_move(self.x + dx, self.y + dy):
                    self.x += dx
                    self.y += dy

            if keys[pygame.K_s]:
                if self.can_move(self.x - dx, self.y - dy):
                    self.x -= dx
                    self.y -= dy

            if keys[pygame.K_a]:
                # strafe left (perpendicular)
                left_rad = rad - np.pi / 2
                lx = np.cos(left_rad) * vel
                ly = np.sin(left_rad) * vel
                if self.can_move(self.x + lx, self.y + ly):
                    self.x += lx
                    self.y += ly

            if keys[pygame.K_d]:
                # strafe right (perpendicular)
                right_rad = rad + np.pi / 2
                rx = np.cos(right_rad) * vel
                ry = np.sin(right_rad) * vel
                if self.can_move(self.x + rx, self.y + ry):
                    self.x += rx
                    self.y += ry

            if keys[pygame.K_LEFT]:
                self.direction -= rot_vel
                if self.direction < 0:
                    self.direction +=360
            if keys[pygame.K_RIGHT]:
                self.direction += rot_vel
                if self.direction > 360:
                    self.direction -=360
            
            self.window.fill((0, 0, 0))
            self.button(button_pressed)
            #print(self.page)
            if self.page == 0:
                self.two_d_view()
            else:
                self.three_d_view()
              
            self.calculate_distant_to_wall()
            pygame.display.update() 

        pygame.quit()


maze = Window()
vel = 0.25
rot_vel = 1
maze.main_loop(vel)
