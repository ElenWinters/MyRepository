from turtle import *
from random import randrange
from gamebase import playerSquare
import pygame
from trypygame import load_audio

def play_audio(file_name):
    sound = load_audio(file_name)
    sound.play()

# 设置屏幕
screen = Screen()
screen.title("Kill that greedy snake!")
screen.setup(840, 840)
screen.tracer(False)

player_x = randrange(-40, 40) * 10
player_y = randrange(-40, 40) * 10
playerSquare(player_x,player_y,10,"red")
p_aim_x = 10
p_aim_y = 0

snake = [[0,0],[10,0],[20,0],[30,0]]
aim_x = 10
aim_y = 0

def changes(x,y):
    global aim_x,aim_y
    aim_x = x
    aim_y = y
def isBiteItself():
    for n in range(len(snake) - 1):
        if snake[-1][0] == snake[n][0] and snake[-1][1] == snake[n][1]:
            return True
    return False
def changeAim():
    dx = snake[-1][0] - player_x - 10
    dy = snake[-1][1] - player_y - 10

    if dx < 0 and dy < 0 and dx < dy:
        if aim_x == 0 and aim_y == 10 or aim_x == 10 and aim_y == 0 or aim_x == 0 and aim_y == -10:
            changes(10,0)
        elif aim_x == -10 and aim_y == 0:
            changes(0,10)
    elif dx < 0 and dy > 0 and -dx > dy:
        if aim_x == 0 and aim_y == 10 or aim_x == 10 and aim_y == 0 or aim_x == 0 and aim_y == -10:
            changes(10,0)
        elif aim_x == -10 and aim_y == 0:
            changes(0,-10)
    elif dx < 0 and dy < 0 and dx > dy:
        if aim_x == 0 and aim_y == 10 or aim_x == 10 and aim_y == 0 or aim_x == -10 and aim_y == 0:
            changes(0,10)
        elif aim_x == 0 and aim_y == -10:
            changes(10,0)
    elif dx > 0 and dy < 0 and dx < -dy:
        if aim_x == 0 and aim_y == 10 or aim_x == 10 and aim_y == 0 or aim_x == -10 and aim_y == 0:
            changes(0,10)
        elif aim_x == 0 and aim_y == -10:
            changes(-10,0)
    elif dx > 0 and dy < 0 and dx > -dy:
        if aim_x == -10 and aim_y == 0 or aim_x == 0 and aim_y == 10 or aim_x == 0 and aim_y == -10:
            changes(-10,0)
        elif aim_x == 10 and aim_y == 0:
            changes(0,10)
    elif dx > 0 and dy > 0 and dx > dy:
        if aim_x == -10 and aim_y == 0 or aim_x == 0 and aim_y == 10 or aim_x == 0 and aim_y == -10:
            changes(-10,0)
        elif aim_x == 10 and aim_y == 0:
            changes(0,-10)
    elif dx > 0 and dy > 0 and dx < dy:
        if aim_x == 0 and aim_y == -10 or aim_x == 10 and aim_y == 0 or aim_x == -10 and aim_y == 0:
            changes(0,-10)
        elif aim_x == 0 and aim_y == 10:
            changes(-10,0)
    elif dx < 0 and dy > 0 and -dx < dy:
        if aim_x == 0 and aim_y == -10 or aim_x == 10 and aim_y == 0 or aim_x == -10 and aim_y == 0:
            changes(0,-10)
        elif aim_x == 0 and aim_y == 10:
            changes(10,0)

def changep(x, y):
    global p_aim_x, p_aim_y
    p_aim_x = x
    p_aim_y = y

def move_player():
    global player_x, player_y
    hideturtle()
    player_x += p_aim_x
    player_y += p_aim_y
    ontimer(move_player, 150) # 每100毫秒移动一次
    screen.update() # 更新屏幕显示

def gameLoop():
    global player_x,player_y
    snake.append([snake[-1][0] + aim_x,snake[-1][1] + aim_y])
    if isBiteItself():
        print("The Greedy Snake is DEAD NOW!!!")
        print(f"What you paid for killing the greedy snake:{len(snake) - 5}")
        for n in range(len(snake)):
            playerSquare(snake[n][0], snake[n][1], 10, "red")
        return
    if snake[-1][0] != player_x or snake[-1][1] != player_y:
        snake.pop(0)
    else:
        player_x = randrange(-20, 20) * 10
        player_y = randrange(-20, 20) * 10
    n = 0
    clear()
    for n in range(len(snake)):
        playerSquare(snake[n][0],snake[n][1],10,"black")
    changeAim()
    playerSquare(player_x, player_y, 10, "red")
    ontimer(gameLoop,100)
    update()

# 监听键盘事件
screen.listen()
screen.onkey(lambda: changep(0, 10), "w")
screen.onkey(lambda: changep(0, -10), "s")
screen.onkey(lambda: changep(10, 0), "d")
screen.onkey(lambda: changep(-10, 0), "a")

# 开始移动玩家
play_audio("Croatian Rhapsody-Maksim Mrvica.wav")
if __name__ == "__main__":
    pygame.init()
    running = True
    while running:
        gameLoop()
        move_player()
        screen.mainloop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()