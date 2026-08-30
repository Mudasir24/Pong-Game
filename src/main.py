import pygame
import random
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

file_path = os.path.join(BASE_DIR, "leaderboard.json")

def save_dict_to_file(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file)
        print(f"Data successfully saved to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def load_dict_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from file '{file_path}': {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Load the dictionary from the file
loaded_data = load_dict_from_file(file_path)


pygame.init()
screen = pygame.display.set_mode((900,600))
screen = pygame.display.get_surface()
pygame.display.set_caption("Pong Game")

# load images
play_img = pygame.image.load(os.path.join(ASSETS_DIR, "pl1.png")).convert_alpha()
play2_img = pygame.image.load(os.path.join(ASSETS_DIR, "pl2.png")).convert_alpha()
options_img = pygame.image.load(os.path.join(ASSETS_DIR, "op1.png")).convert_alpha()
options2_img = pygame.image.load(os.path.join(ASSETS_DIR, "op2.png")).convert_alpha()
exit_img = pygame.image.load(os.path.join(ASSETS_DIR, "ex1.png")).convert_alpha()
exit2_img = pygame.image.load(os.path.join(ASSETS_DIR, "ex2.png")).convert_alpha()
classic1_img = pygame.image.load(os.path.join(ASSETS_DIR, "cl1.png")).convert_alpha()
classic2_img = pygame.image.load(os.path.join(ASSETS_DIR, "cl2.png")).convert_alpha()
timer1_img = pygame.image.load(os.path.join(ASSETS_DIR, "tr1.png")).convert_alpha()
timer2_img = pygame.image.load(os.path.join(ASSETS_DIR, "tr2.png")).convert_alpha()
survival1_img = pygame.image.load(os.path.join(ASSETS_DIR, "sr1.png")).convert_alpha()
survival2_img = pygame.image.load(os.path.join(ASSETS_DIR, "sr2.png")).convert_alpha()
return1_img = pygame.image.load(os.path.join(ASSETS_DIR, "mm1.png")).convert_alpha()
return2_img = pygame.image.load(os.path.join(ASSETS_DIR, "mm2.png")).convert_alpha()
single1_img = pygame.image.load(os.path.join(ASSETS_DIR, "sp1.png")).convert_alpha()
single2_img = pygame.image.load(os.path.join(ASSETS_DIR, "sp2.png")).convert_alpha()
multi1_img = pygame.image.load(os.path.join(ASSETS_DIR, "mp1.png")).convert_alpha()
multi2_img = pygame.image.load(os.path.join(ASSETS_DIR, "mp2.png")).convert_alpha()
heart1_img = pygame.image.load(os.path.join(ASSETS_DIR, "heart_red.png")).convert_alpha()
heading_img = pygame.image.load(os.path.join(ASSETS_DIR, "heading.png")).convert_alpha()
red1_img = pygame.image.load(os.path.join(ASSETS_DIR, "red1.png")).convert_alpha()
red2_img = pygame.image.load(os.path.join(ASSETS_DIR, "red2.png")).convert_alpha()
green1_img = pygame.image.load(os.path.join(ASSETS_DIR, "green1.png")).convert_alpha()
green2_img = pygame.image.load(os.path.join(ASSETS_DIR, "green2.png")).convert_alpha()
blue1_img = pygame.image.load(os.path.join(ASSETS_DIR, "blue1.png")).convert_alpha()
blue2_img = pygame.image.load(os.path.join(ASSETS_DIR, "blue2.png")).convert_alpha()
white1_img = pygame.image.load(os.path.join(ASSETS_DIR, "white1.png")).convert_alpha()
white2_img = pygame.image.load(os.path.join(ASSETS_DIR, "white2.png")).convert_alpha()
five1_img = pygame.image.load(os.path.join(ASSETS_DIR, "5_1.png")).convert_alpha()
five2_img = pygame.image.load(os.path.join(ASSETS_DIR, "5_2.png")).convert_alpha()
ten1_img = pygame.image.load(os.path.join(ASSETS_DIR, "10_1.png")).convert_alpha()
ten2_img = pygame.image.load(os.path.join(ASSETS_DIR, "10_2.png")).convert_alpha()
fifteen1_img = pygame.image.load(os.path.join(ASSETS_DIR, "15_1.png")).convert_alpha()
fifteen2_img = pygame.image.load(os.path.join(ASSETS_DIR, "15_2.png")).convert_alpha()
back1_img = pygame.image.load(os.path.join(ASSETS_DIR, "back1.png")).convert_alpha()
back2_img = pygame.image.load(os.path.join(ASSETS_DIR, "back2.png")).convert_alpha()
setscore_img = pygame.image.load(os.path.join(ASSETS_DIR, "setscore.png")).convert_alpha()
paddlecolor_img = pygame.image.load(os.path.join(ASSETS_DIR, "pddcolor.png")).convert_alpha()
surc1_img = pygame.image.load(os.path.join(ASSETS_DIR, "surc1.png")).convert_alpha()
surc2_img = pygame.image.load(os.path.join(ASSETS_DIR, "surc2.png")).convert_alpha()
leaderboard_img = pygame.image.load(os.path.join(ASSETS_DIR, "lead1.png")).convert_alpha()
leaderboard2_img = pygame.image.load(os.path.join(ASSETS_DIR, "lead2.png")).convert_alpha()
eyn_img = pygame.image.load(os.path.join(ASSETS_DIR, "eyn.png")).convert_alpha()
ldrh_img = pygame.image.load(os.path.join(ASSETS_DIR, "ldrh.png")).convert_alpha()

ball_sound = pygame.mixer.Sound(os.path.join(ASSETS_DIR, "pong.ogg"))
click_sound = pygame.mixer.Sound(os.path.join(ASSETS_DIR, "click.mp3"))
score_sound = pygame.mixer.Sound(os.path.join(ASSETS_DIR, "score.mp3"))
background_sound = pygame.mixer.Sound(os.path.join(ASSETS_DIR, "background.mp3"))
gameover_sound = pygame.mixer.Sound(os.path.join(ASSETS_DIR, "gameover.wav"))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#paddle
class paddle:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.w = 15
        self.h = 100
        self.color = WHITE
        self.screen = screen
        self.speed = 15

    def change_color(self, color):
        self.color = color

    def draw(self):
        pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.w, self.h])

    def move(self, direction):
        if direction == "up":
            self.y -= self.speed
        elif direction == "down":
            self.y += self.speed

    def check_collision(self):
        if self.y < 0:
            self.y = 0
        elif self.y > 500:
            self.y = 500

    def change_color(self, color):
        self.color = color

    def update(self):
        self.check_collision()
        self.draw()

#ball
class ball:
    def __init__(self, x, y, color, screen,speed, reset_speed = 5,max_speed = 15):
        self.x = x
        self.y = y
        self.color = color
        self.screen = screen
        self.speed = speed
        self.max_speed = max_speed
        self.reset_speed = reset_speed
        self.xdirection = random.choice([1, -1])
        self.ydirection = random.choice([1, -1])

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), 10)

    def move(self):
        self.x += self.speed * self.xdirection   
        self.y += self.speed * self.ydirection


    def check_collision(self):  
        if self.y < 10:
            self.y = 10
            self.ydirection *= -1
            ball_sound.play()
        elif self.y > 590:
            self.y = 590
            self.ydirection *= -1
            ball_sound.play()

        if self.x < 10:
            score2.increase_score()
            heart1.decrease_hearts()
            self.reset()

        elif self.x > 890:
            score1.increase_score()
            heart2.decrease_hearts()
            self.reset()

    def ball_paddle_collision(self):
        if self.x <= 35 and self.y >= paddle1.y and self.y <= paddle1.y + 100:
            self.x = 35
            self.xdirection *= -1
            ball_sound.play()
            if self.speed < self.max_speed:
                self.increase_speed()

        elif self.x >= 865 and self.y >= paddle2.y and self.y <= paddle2.y + 100:
            self.x = 865
            self.xdirection *= -1
            ball_sound.play()
            if self.speed < self.max_speed:
                self.increase_speed()


    def reset(self):
        self.x = 450
        self.y = 300
        self.speed = self.reset_speed
        self.xdirection = random.choice([1, -1])
        self.ydirection = random.choice([1, -1])

    def update(self):
        self.move()
        self.check_collision()
        self.ball_paddle_collision()
        self.draw()


    def increase_speed(self):
        self.speed += 0.75

#score
class score:
    def __init__(self, x, y, screen, max_score = 5):
        self.x = x
        self.y = y
        self.score = 0
        self.screen = screen
        self.max_score = max_score

    def draw(self):
        font = pygame.font.Font(None, 52)
        text = font.render(str(self.score), 1, (255, 255, 255))
        self.screen.blit(text, (self.x, self.y))

    def increase_score(self):
        self.score += 1
        score_sound.play()

    def reset_score(self): 
        self.score = 0

    def change_max_score(self, max_score):
        self.max_score = max_score


    def update(self):
        self.draw()

#timer
class timer:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.i = 1860
        self.j = 0

    def draw(self):
        font = pygame.font.Font(None, 52)
        text = font.render(str(self.j), 1, WHITE)
        self.screen.blit(text, (self.x, self.y))

    def reset(self):
        self.x = 430
        self.i = 1860
        self.j = 0

    def update(self):
        self.i -= 1
        self.j = self.i // 60
        if self.j <= 9:
            self.x = 440
        self.draw()

class timerup:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.i = 0
        self.j = 0
        

    def draw(self):
        font = pygame.font.Font(None, 52)
        text = font.render(str(self.j), 1, WHITE)
        self.screen.blit(text, (self.x, self.y))

    def reset(self):
        self.x = 440
        self.i = 0
        self.j = 0
    
    def update(self):
        self.i += 1
        self.j = self.i // 60
        if self.j >= 10:
            self.x = 430
        self.draw()
    
#heart
class heart:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.hearts = 3
        width = heart1_img.get_width()
        height = heart1_img.get_height()
        self.heart1_img = pygame.transform.scale(heart1_img, (int(width * 0.5), int(height * 0.5)))
        self.screen = screen

    def draw_hearts(self):
        for i in range(self.hearts):
            self.screen.blit(self.heart1_img, (self.x + 70 * i, self.y))

    def decrease_hearts(self):
        self.hearts -= 1

    def reset_hearts(self):
        self.hearts = 3
    
    def update(self):
        self.draw_hearts()
    
#button
class button():
    def __init__(self ,x ,y ,img ,scale):
        width = img.get_width()
        height = img.get_height()
        self.img = pygame.transform.scale(img, (int(width * scale), int(height * scale)))
        self.rect = self.img.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        click = False
        #mouse position
        pos = pygame.mouse.get_pos()

        #check if clicked
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                click = True
                click_sound.play()

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #drawing buttons
        surface.blit(self.img, (self.rect.x, self.rect.y))

        return click
    
    def hover(self, surface):
        #mouse position
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            return True
        
        return False

#text
class text:
    def __init__(self, x, y, text, color, size):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.size = size

    def draw(self):
        font = pygame.font.Font("freesansbold.ttf", self.size)
        text = font.render(self.text, 1, self.color)
        screen.blit(text, (self.x, self.y))

    def draw_play_again(self):
        font = pygame.font.Font("freesansbold.ttf", self.size)
        pygame.font.Font.set_italic(font, True)
        text = font.render(self.text, 1, self.color)
        screen.blit(text, (self.x, self.y))

    def change_text(self, text):
        self.text = text

    def update(self):
        self.draw()

#main menu
class main_menu(): 
    def __init__(self):
        self.heading = button(175, 70, heading_img, 1.1)

        self.play_button = button(280, 200, play_img, 0.95)
        self.play_button2 = button(280, 200, play2_img, 0.95)

        self.play2_button = button(295, 200, play_img, 0.85)
        self.play2_button2 = button(295, 200, play2_img, 0.85)

        self.options_button = button(336, 340, options_img, 0.65)
        self.options2_button = button(336, 340, options2_img, 0.65) 
              
        self.exit_button = button(336, 420, exit_img, 0.65)
        self.exit2_button = button(336, 420, exit2_img, 0.65)

        self.classic1_button = button(300, 80, classic1_img, 0.85)
        self.classic2_button = button(300, 80, classic2_img, 0.85)

        self.timer_button = button(300, 180, timer1_img, 0.85)
        self.timer2_button = button(300, 180, timer2_img, 0.85)

        self.surv_button = button(300, 288, survival1_img, 0.85)
        self.surv2_button = button(300, 288, survival2_img, 0.85)

        self.surc1_button = button(265, 388, surc1_img, 0.85)
        self.surc2_button = button(265, 388, surc2_img, 0.85)

        self.leaderboard_button = button(290, 320, leaderboard_img, 0.85)
        self.leaderboard2_button = button(290, 320, leaderboard2_img, 0.85)

        self.mm1_button = button(365, 500, return1_img, 0.45)
        self.mm2_button = button(365, 500, return2_img, 0.45)

        self.single1_button = button(315, 220, single1_img, 0.67)
        self.single2_button = button(315, 220, single2_img, 0.67)

        self.multi1_button = button(315, 320, multi1_img, 0.67)
        self.multi2_button = button(315, 320, multi2_img, 0.67)

        self.eyn_button = button(270, 200, eyn_img, 0.85)

        self.ldrh_button = button(260, 25, ldrh_img, 0.9)

        self.five1_button = button(270, 180, five1_img, 0.6)
        self.five2_button = button(270, 180, five2_img, 0.6)

        self.ten1_button = button(425, 180, ten1_img, 0.6)
        self.ten2_button = button(425, 180, ten2_img, 0.6)

        self.fifteen1_button = button(580, 180, fifteen1_img, 0.6)
        self.fifteen2_button = button(580, 180, fifteen2_img, 0.6)

        self.back1_button = button(385, 470, back1_img, 0.45)
        self.back2_button = button(385, 470, back2_img, 0.45)

        self.red1_button = button(380, 380, red1_img, 0.95)
        self.red2_button = button(380, 380, red2_img, 0.95)

        self.green1_button = button(480, 380, green1_img, 0.95)
        self.green2_button = button(480, 380, green2_img, 0.95)

        self.blue1_button = button(580, 380, blue1_img, 0.95)
        self.blue2_button = button(580, 380, blue2_img, 0.95)

        self.white1_button = button(280, 380, white1_img, 0.95)
        self.white2_button = button(280, 380, white2_img, 0.95)

        self.setscore_button = button(330, 100, setscore_img, 0.85)
        self.pddcolor_button = button(265, 300, paddlecolor_img, 0.85)
        
        self.click = False
        self.flag = 0
        

    def draw(self):
        if self.flag == 0 and self.click == False: # Main menu
            screen.fill((0, 0, 0))
            pygame.draw.line(screen, WHITE, (220, 170), (220, 550), 4)
            pygame.draw.line(screen, WHITE, (680, 170), (680, 550), 4)
            pygame.draw.line(screen, WHITE, (220, 170), (680, 170), 4)
            pygame.draw.line(screen, WHITE, (220, 550), (680, 550), 4)
            self.heading.draw(screen)
            self.play_button.draw(screen)
            self.options_button.draw(screen)
            self.exit_button.draw(screen)

            if self.play_button.hover(screen):
                if self.play_button2.draw(screen):
                    self.click = True
                    self.flag = 10
                    print("game mode menu")
                
            if self.options_button.hover(screen):
                if self.options2_button.draw(screen):
                    self.flag = 11
                    print("options")

            if self.exit_button.hover(screen):
                if self.exit2_button.draw(screen):
                    save_dict_to_file(leaderboard.leaderboard, file_path)
                    pygame.quit()
                    print("exit")

        if self.flag == 10 and self.click == False: # Game mode menu
            screen.fill((0, 0, 0))
            self.classic1_button.draw(screen)
            self.timer_button.draw(screen)
            self.surv_button.draw(screen)
            self.surc1_button.draw(screen)
            self.mm1_button.draw(screen)

            if self.classic1_button.hover(screen):
                if self.classic2_button.draw(screen):
                    self.flag = 100
                    print("classic game mode")

            if self.timer_button.hover(screen):
                if self.timer2_button.draw(screen):
                    self.flag = 101
                    print("time mode")
                    game2.play_game()

            if self.surv_button.hover(screen):
                if self.surv2_button.draw(screen):
                    self.flag = 102
                    print("survival")
                    game3.play_game() 

            if self.surc1_button.hover(screen):
                if self.surc2_button.draw(screen):
                    self.click = True
                    self.flag = 103

            if self.mm1_button.hover(screen):
                if self.mm2_button.draw(screen):
                    self.click = True
                    self.flag = 0
                    print("return to main menu")

        if  self.flag == 103 and self.click == False:
            screen.fill((0, 0, 0))
            text_input.text = ''
            self.play2_button.draw(screen)
            self.leaderboard_button.draw(screen)
            self.back1_button.draw(screen)

            if self.play2_button.hover(screen):
                if self.play2_button2.draw(screen):
                    self.flag = 1030
                    self.click = True
            
            if self.leaderboard_button.hover(screen):
                if self.leaderboard2_button.draw(screen):
                    self.flag = 1031

            if self.back1_button.hover(screen):
                if self.back2_button.draw(screen):
                    self.click = True
                    self.flag = 10
            
        if self.flag == 1030 and self.click == False:
            screen.fill((0, 0, 0))
            self.eyn_button.draw(screen)
            self.back1_button.draw(screen)
            text_input.draw()       

            if self.back1_button.hover(screen):
                if self.back2_button.draw(screen):
                    self.click = True
                    self.flag = 103

        if self.flag == 1031 and self.click == False:
            screen.fill((0, 0, 0))
            self.ldrh_button.draw(screen)
            self.back1_button.draw(screen)

            leaderboard.draw()

            if self.back1_button.hover(screen):
                if self.back2_button.draw(screen):
                    self.click = True
                    self.flag = 103

        if self.flag == 11 and self.click == False: # customization menu
            screen.fill((0, 0, 0))

            self.pddcolor_button.draw(screen)
            self.setscore_button.draw(screen)

            if score1.max_score == 5:
                self.five2_button.draw(screen)
                if self.ten1_button.draw(screen):
                    score1.change_max_score(10)
                if self.fifteen1_button.draw(screen):
                    score1.change_max_score(15)
            elif score1.max_score == 10:
                self.ten2_button.draw(screen)
                if self.five1_button.draw(screen):
                    score1.change_max_score(5)
                if self.fifteen1_button.draw(screen):
                    score1.change_max_score(15)
            elif score1.max_score == 15:
                self.fifteen2_button.draw(screen)
                if self.five1_button.draw(screen):
                    score1.change_max_score(5)
                if self.ten1_button.draw(screen):
                    score1.change_max_score(10)            
            
            if paddle1.color == WHITE:
                self.white2_button.draw(screen)
                if self.red1_button.draw(screen):
                    paddle1.change_color(RED)
                    paddle2.change_color(RED)
                if self.green1_button.draw(screen):
                    paddle1.change_color(GREEN)
                    paddle2.change_color(GREEN)
                if self.blue1_button.draw(screen):
                    paddle1.change_color(BLUE)
                    paddle2.change_color(BLUE)
            elif paddle1.color == RED:
                self.red2_button.draw(screen)
                if self.white1_button.draw(screen):
                    paddle1.change_color(WHITE)
                    paddle2.change_color(WHITE)
                if self.green1_button.draw(screen):
                    paddle1.change_color(GREEN)
                    paddle2.change_color(GREEN)
                if self.blue1_button.draw(screen):
                    paddle1.change_color(BLUE)
                    paddle2.change_color(BLUE)
            elif paddle1.color == GREEN:
                self.green2_button.draw(screen)
                if self.white1_button.draw(screen):
                    paddle1.change_color(WHITE)
                    paddle2.change_color(WHITE)
                if self.red1_button.draw(screen):
                    paddle1.change_color(RED)
                    paddle2.change_color(RED)
                if self.blue1_button.draw(screen):
                    paddle1.change_color(BLUE)
                    paddle2.change_color(BLUE)
            elif paddle1.color == BLUE:
                self.blue2_button.draw(screen)
                if self.white1_button.draw(screen):
                    paddle1.change_color(WHITE)
                    paddle2.change_color(WHITE)
                if self.red1_button.draw(screen):
                    paddle1.change_color(RED)
                    paddle2.change_color(RED)
                if self.green1_button.draw(screen):
                    paddle1.change_color(GREEN)
                    paddle2.change_color(GREEN)

            self.back1_button.draw(screen)
            if self.back1_button.hover(screen):
                if self.back2_button.draw(screen):
                    self.click = True
                    self.flag = 0
                    print("return to main menu")
                      
        if self.flag == 100 and self.click == False: # Classic game mode single player and multiplayer menu
            screen.fill((0, 0, 0))

            self.single1_button.draw(screen)
            self.multi1_button.draw(screen)

            if self.single1_button.hover(screen):
                if self.single2_button.draw(screen):
                    self.flag = 1000
                    print("single player mode")
                    game_ai.play_game()
            
            if self.multi1_button.hover(screen):
                if self.multi2_button.draw(screen):
                    self.flag = 1001
                    print("multiplayer mode")
                    game1.play_game()
        
            self.back1_button.draw(screen)
            if self.back1_button.hover(screen):
                if self.back2_button.draw(screen):
                    self.click = True
                    self.flag = 10
                    print("return to game mode menu")
        
    def update(self):
        self.draw()
        if event.type == pygame.MOUSEBUTTONUP:
            self.click = False

# Create main menu instance
main_menu = main_menu()
    
class text_input():
    def __init__(self):
        self.text = ""
        self.font = pygame.font.Font(None, 32)
        self.input_box = pygame.Rect(400, 270, 300, 30)
        self.color_inactive = WHITE
        self.color_active = (90,90,90)
        self.color = self.color_inactive
        self.active = False

    def draw(self):
        pygame.draw.rect(screen, self.color, self.input_box)
        txt_surface = self.font.render(self.text, True, WHITE)
        screen.blit(txt_surface, (self.input_box.x+5, self.input_box.y+5))
        self.input_box.w = max(100, txt_surface.get_width()+10) 

        

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_box.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key == pygame.K_RETURN:
                    print(self.text)
                    main_menu.flag = 10300
                    game4.play_game()
                else:
                    self.text += event.unicode
        
# Create text input instance
text_input = text_input()

class leaderboard():
    def __init__(self):
        self.leaderboard = loaded_data
        self.font = pygame.font.Font(None, 42)
        self.leaderboard = sorted(self.leaderboard, key=lambda x: x[1], reverse=True)
        self.leaderboard = self.leaderboard[:5]
        self.y = 120
    
    def draw(self):
        for i, (name, score) in enumerate(self.leaderboard):
            text = self.font.render(f"{name}: {score}", True, WHITE)
            screen.blit(text, (300, self.y + i * 50))

    def update(self, name, score):
        self.leaderboard.append((name, score))
        self.leaderboard = sorted(self.leaderboard, key=lambda x: x[1], reverse=True)
        if len(self.leaderboard) > 5:
            self.leaderboard = self.leaderboard[:5]

leaderboard = leaderboard()

# Create text instances
p1_text = text(140, 200, "Player 1 wins!", WHITE, 32)
p2_text = text(560, 200, "Player 2 wins!", WHITE, 32)
play_again_text1 = text(100, 250, "Press SPACEBAR to PLAY AGAIN", WHITE, 20)
play_again_text2 = text(520, 250, "Press SPACEBAR to PLAY AGAIN", WHITE, 20)

# Create main menu buttons instances
main_menu_img1 = button(360,430, return1_img, 0.5)
main_menu_img2 = button(360,430, return2_img, 0.5)

#game class
class game1():
    def __init__(self):
        self.paddle1 = paddle(20, 100, screen)
        self.paddle2 = paddle(865, 100, screen)
        self.score1 = score(400, 10, screen)
        self.score2 = score(485, 10, screen)
        self.ball = ball(450, 300, WHITE, screen,5)
        self.play = False

    def play_game(self):
        self.play = True

    def update(self):
        if self.play:
            screen.fill((0, 0, 0))
            pygame.draw.line(screen, (255, 255, 255), (450, 0), (450, 600), 2)
            paddle1.update()
            paddle2.update()
            self.ball.update()
            score1.update()
            score2.update()
            pygame.display.flip()
            pygame.time.Clock().tick(60)
            self.game_over()

    def reset(self):
        score1.reset_score()
        score2.reset_score()
        self.ball.reset()
        self.play = False

    def game_over(self):
        if score1.score == score1.max_score:
            p1_text.change_text("Player 1 wins!")
            p1_text.update()
            play_again_text1.draw_play_again()
            gameover_sound.play()
            self.reset()
            
            
        elif score2.score == score1.max_score:
            p2_text.change_text("Player 2 wins!")
            p2_text.update()
            play_again_text2.draw_play_again()
            gameover_sound.play()
            self.reset()
            
class game2():
    def __init__(self):
        self.paddle1 = paddle(20, 100, screen)
        self.paddle2 = paddle(865, 100, screen)
        self.score1 = score(400, 10, screen)
        self.score2 = score(485, 10, screen)
        self.ball = ball(450, 300, WHITE, screen,5)
        self.timer = timer(430, 300, screen)
        self.play = False

    def play_game(self):
        self.play = True

    def update(self):
        if self.play:
            screen.fill((0, 0, 0))
            pygame.draw.line(screen, WHITE, (450, 0), (450, 290), 2)
            pygame.draw.line(screen, WHITE, (450, 340), (450, 600), 2)
            paddle1.update()
            paddle2.update()
            self.ball.update()
            score1.update()
            score2.update()
            self.timer.update()
            pygame.display.flip()
            pygame.time.Clock().tick(60)
            self.game_over()

    def reset(self):
        score1.reset_score()
        score2.reset_score()
        self.ball.reset()
        self.timer.reset()
        self.play = False

    def game_over(self):
        if self.timer.j == 0:
            if score1.score > score2.score:
                p1_text.change_text("Player 1 wins!")
                p1_text.update()
                play_again_text1.draw_play_again()
            elif score2.score > score1.score:
                p2_text.change_text("Player 2 wins!")
                p2_text.update()
                play_again_text2.draw_play_again()
            else:
                if self.ball.x <= 450:
                    p2_text.change_text("   It's a tie!")
                    p2_text.update()
                    play_again_text2.draw_play_again()
                else:
                    p1_text.change_text("   It's a tie!")
                    p1_text.update()
                    play_again_text1.draw_play_again()
            gameover_sound.play()
            self.reset()

class game3():
    def __init__(self):
        self.paddle1 = paddle(20, 100, screen)
        self.paddle2 = paddle(865, 100, screen)
        self.ball = ball(450, 300, (255, 255, 255), screen,5)
        self.heart1 = heart(140, 10, screen)
        self.heart2 = heart(570, 10, screen)
        self.play = False

    def play_game(self):
        self.play = True

    def update(self):
        if self.play:
            screen.fill((0, 0, 0))
            pygame.draw.line(screen, (255, 255, 255), (450, 0), (450, 600), 2)
            paddle1.update()
            paddle2.update()
            self.ball.update()
            heart1.update()
            heart2.update()
            pygame.display.flip()
            pygame.time.Clock().tick(60)
            self.game_over()

    def reset(self):
        heart1.reset_hearts()
        heart2.reset_hearts()
        self.ball.reset()
        self.play = False

    def game_over(self):   
        if heart1.hearts == 0:
            p2_text.change_text("Player 2 wins!")
            p2_text.update()
            play_again_text2.draw_play_again()  
            gameover_sound.play() 
            self.reset()            
    
        if heart2.hearts == 0:
            p1_text.change_text("Player 1 wins!")
            p1_text.update()
            play_again_text1.draw_play_again()   
            gameover_sound.play() 
            self.reset()

#game AI     
class GameAI():
    PREDICTION_TOLERANCE = 10

    def __init__(self):
        self.paddle1 = paddle(20, 100, screen)
        self.paddle2 = paddle(865, 100, screen)
        self.score1 = score(400, 10, screen)
        self.score2 = score(485, 10, screen)
        self.ball = ball(450, 300, WHITE, screen, 5)
        self.play = False

    def play_game(self):
        self.play = True

    def update(self):
        if self.play:
            screen.fill((0, 0, 0))
            pygame.draw.line(screen, WHITE, (450, 0), (450, 600), 2)
            paddle1.update()
            paddle2.update()
            self.ball.update()
            self.ai()
            score1.update()
            score2.update()
            pygame.display.flip()
            pygame.time.Clock().tick(60)
            self.game_over()

    def reset(self):
        score1.reset_score()
        score2.reset_score()
        self.ball.reset()
        self.play = False

    def game_over(self):
        if score1.score == score1.max_score:
            p1_text.change_text(" Player wins!")
            p1_text.update()
            play_again_text1.draw_play_again()
            gameover_sound.play()
            self.reset()
            
            
        elif score2.score == score1.max_score:
            p2_text.change_text("    AI wins!")
            p2_text.update()
            play_again_text2.draw_play_again()
            gameover_sound.play()
            self.reset()

    def predict_ball_position(self):
        future_ball_x = self.ball.x
        future_ball_y = self.ball.y
        future_ball_x_direction = self.ball.xdirection
        future_ball_y_direction = self.ball.ydirection
        future_ball_speed = self.ball.speed

        while (future_ball_x_direction > 0 and future_ball_x < self.paddle2.x) or (future_ball_x_direction < 0 and future_ball_x > paddle1.x):
            future_ball_x += future_ball_speed * future_ball_x_direction
            future_ball_y += future_ball_speed * future_ball_y_direction

            # Ball bounces off top or bottom edges
            if future_ball_y <= 10 or future_ball_y >= 590:
                future_ball_y_direction *= -1

        return future_ball_y

    def ai(self):
        predicted_y = self.predict_ball_position()
        if abs(paddle2.y + paddle2.h / 2 - predicted_y) > self.PREDICTION_TOLERANCE:
            if paddle2.y + paddle2.h / 2 < predicted_y:
                paddle2.move("down")
            elif paddle2.y + paddle2.h / 2 > predicted_y:
                paddle2.move("up")

class game4():
    PREDICTION_TOLERANCE = 10

    def __init__(self):
        self.paddle1 = paddle(20, 100, screen)
        self.paddle2 = paddle(865, 100, screen)
        self.timerup = timerup(440, 320, screen)
        self.ball = ball(450, 300, WHITE, screen, 5)
        self.play = False

    def play_game(self):
        self.play = True

    def update(self):
        if self.play:
            screen.fill((0, 0, 0))
            pygame.draw.line(screen, WHITE, (450, 0), (450, 310), 2)
            pygame.draw.line(screen, WHITE, (450, 360), (450, 600), 2)
            paddle1.update()
            paddle2.update()
            self.ball.update()
            self.ai()
            self.timerup.update()
            pygame.display.flip()
            pygame.time.Clock().tick(60)
            self.game_over()

    def reset(self):
        score1.reset_score()
        score2.reset_score()
        self.ball.reset()
        self.timerup.reset()
        self.play = False

    def game_over(self):
        if score1.score == 1:
            p1_text.change_text(" Player wins!")
            p1_text.update()
            play_again_text1.draw_play_again()
            gameover_sound.play()
            self.reset()
            
            
        elif score2.score == 1:
            p2_text.change_text("    AI wins!")
            leaderboard.update(text_input.text, self.timerup.j)
            p2_text.update()
            play_again_text2.draw_play_again()
            gameover_sound.play()
            self.reset()

    def predict_ball_position(self):
        future_ball_x = self.ball.x
        future_ball_y = self.ball.y
        future_ball_x_direction = self.ball.xdirection
        future_ball_y_direction = self.ball.ydirection
        future_ball_speed = self.ball.speed

        while (future_ball_x_direction > 0 and future_ball_x < self.paddle2.x) or (future_ball_x_direction < 0 and future_ball_x > paddle1.x):
            future_ball_x += future_ball_speed * future_ball_x_direction
            future_ball_y += future_ball_speed * future_ball_y_direction

            # Ball bounces off top or bottom edges
            if future_ball_y <= 10 or future_ball_y >= 590:
                future_ball_y_direction *= -1

        return future_ball_y

    def ai(self):
        predicted_y = self.predict_ball_position()
        if abs(paddle2.y + paddle2.h / 2 - predicted_y) > self.PREDICTION_TOLERANCE:
            if paddle2.y + paddle2.h / 2 < predicted_y:
                paddle2.move("down")
            elif paddle2.y + paddle2.h / 2 > predicted_y:
                paddle2.move("up")

# Create game instance
game1 = game1()
game2 = game2()
game3 = game3()
game4 = game4()
game_ai = GameAI()

# Create paddles
paddle1 = paddle(20, 100, screen)
paddle2 = paddle(865, 100, screen)

# Create scores
score1 = score(400, 10, screen)
score2 = score(485, 10, screen)

# Create hearts
heart1 = heart(140, 10, screen)
heart2 = heart(570, 10, screen)

pygame.mixer.Sound.play(background_sound, -1)

# Main loop
flag = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_dict_to_file(leaderboard.leaderboard, file_path)
            running = False
        
        text_input.handle_event(event)

    keys = pygame.key.get_pressed()

    # Control paddles
    if not flag:
        if keys[pygame.K_w]:
            paddle1.move("up")
        if keys[pygame.K_s]:
            paddle1.move("down")
        if keys[pygame.K_UP]:
            paddle2.move("up")
        if keys[pygame.K_DOWN]:
            paddle2.move("down")
    
    if flag:
        if keys[pygame.K_UP]:
            paddle1.move("up")
        if keys[pygame.K_DOWN]:
            paddle1.move("down")

    # Return to main menu
    if (main_menu.flag == 1001 and game1.play == False) or(main_menu.flag == 1000 and game_ai.play == False) or (main_menu.flag == 101 and game2.play == False) or (main_menu.flag == 102 and game3.play == False) or (main_menu.flag == 10300 and game4.play == False):
        main_menu_img1.draw(screen)
        if main_menu_img1.hover(screen):
            if main_menu_img2.draw(screen):
                main_menu.click = True
                main_menu.flag = 0
                game1.reset()
                game2.reset()
                game3.reset()
                game_ai.reset()

        # Play again
        if keys[pygame.K_SPACE]:
            if main_menu.flag == 1001:
                game1.play_game()        
            elif main_menu.flag == 1000:
                game_ai.play_game()
            elif main_menu.flag == 101:
                game2.play_game()
            elif main_menu.flag == 102:
                game3.play_game()
            elif main_menu.flag == 10300:
                game4.play_game()

    # Update main menu
    main_menu.update()

    # Reset game
    if keys[pygame.K_ESCAPE]:
        game1.reset()
        game2.reset()
        game3.reset()
        flag = False
        game_ai.reset()
        game4.reset()
        main_menu.flag = 0

    # Update game
    if game1.play:
        flag = False
        game1.update()

    if game2.play:
        flag = False
        game2.update()

    if game3.play:
        flag = False
        game3.update()  

    if game_ai.play:
        game_ai.update()
        flag = True

    if game4.play:
        game4.update()
        flag = True

    pygame.display.flip()

pygame.quit()