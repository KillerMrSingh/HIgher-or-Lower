import pygame
import random

pygame.font.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Higher or Lower")
clock = pygame.time.Clock()
c = 160, 32, 240

T_font = pygame.font.SysFont('comicsans', 40)
# Use a smaller font size
T_font2 = pygame.font.SysFont('comicsans', 20)

def Draw(ball, num1, num2, t, Time, rand1, rand2, pScore, game_over):
    if not game_over:
        WIN.fill(c)
        pygame.draw.rect(WIN,(0,0,0),(150,575,500,25))
        pygame.draw.line(WIN,(0,0,0),(150,575),(135,560), width = 2)
        pygame.draw.line(WIN, (0, 0, 0), (135, 560), (135, 600), width=2)
        pygame.draw.line(WIN, (0, 0, 0), (650, 575), (665, 560), width=2)
        pygame.draw.line(WIN, (0, 0, 0), (665, 560), (665, 600), width=2)
        pygame.draw.circle(WIN, (255,255,255),(ball.x,550),22) #x = 400
        pygame.draw.rect(WIN, (0, 0, 0), (200, num1.y, 50, 50))
        pygame.draw.rect(WIN, (0, 0, 0), (550, num2.y, 50, 50))
        Time =  T_font.render(str(t), 1, (255,255,255))
        WIN.blit(Time,(400 - Time.get_width() - 10,25))

        # Render and display text on falling rectangles
        num1_text_surface = T_font2.render(str(rand1), 1, (255, 255, 255))  # Replace "Text1" with your desired text
        WIN.blit(num1_text_surface, (num1.x + 10, num1.y + 10))  # Adjust the position as needed

        num2_text_surface = T_font2.render(str(rand2), 1, (255, 255, 255))  # Replace "Text2" with your desired text
        WIN.blit(num2_text_surface, (num2.x + 10, num2.y + 10))  # Adjust the position as needed

        Score = T_font.render("Score:"+str(pScore), 1, (255, 255, 255))
        WIN.blit(Score, (400 - Time.get_width() - 350, 5))
    else:
        WIN.fill(c)
        Score = T_font.render("Final Score: " + str(pScore), 1, (255, 255, 255))
        press_right = T_font2.render("Press Right to Continue or", 1, (255, 255, 255))
        press_enter = T_font2.render("Press Enter to Quit", 1, (255, 255, 255))
        WIN.blit(Score, (WIDTH // 2 - Score.get_width() // 2, HEIGHT // 2 - Score.get_height() // 2))
        WIN.blit(press_right, (300, 200))
        WIN.blit(press_enter, (300, 225))

    pygame.display.update()
    Time = T_font.render(str(Time), 1, (255, 255, 255))
    WIN.blit(Time, (400 - Time.get_width() - 10, 25))



def main():
    pScore = 0
    rand1 = random.randint(1, 10)
    rand2 = random.randint(1, 10)
    t = 5
    Time = T_font.render(str(t), 1, (255, 255, 255))
    ball = pygame.Rect(400, 553, 22, 22)
    num1 = pygame.Rect(200, 0, 50, 50)
    num2 = pygame.Rect(550, 0, 50, 50)
    clock = pygame.time.Clock()
    timer_event = pygame.USEREVENT + 1
    num1_collided = False  # Flag to track collision with num1
    num2_collided = False  # Flag to track collision with num2
    pygame.time.set_timer(timer_event, 1000)  # Timer event to decrement the timer every second
    game_over = False
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == timer_event:
                t -= 1
                if t <= 0:
                    game_over = True
                pass
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and ball.x - 1 > 150:
            ball.x -= 10
        elif keys_pressed[pygame.K_RIGHT] and ball.x + 1 < 650:
            ball.x += 10
        num1.y += 4 # Velocity of Squares
        num2.y += 4

        # Check if rectangles have reached the bottom
        if num1.y > HEIGHT:
            num1.y = -50  # Reset the rectangle position to the top
            rand1 = random.randint(1,10)
            num1_collided = False
        if num2.y > HEIGHT:
            rand2 = random.randint(1, 10)
            num2.y = -50  # Reset the rectangle position to the top
            num2_collided = False
            # ball collison
        if ball.colliderect(num1) and not num1_collided:
            if rand1 > rand2:
                pScore += 1
            num1_collided = True
        elif ball.colliderect(num2) and not num2_collided:
            if rand2 > rand1:
                pScore += 1
            num2_collided = True


        Draw(ball, num1, num2, t, Time, rand1, rand2, pScore, game_over)
        if game_over:
            break
            # Once the game is over, run the final score screen
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_KP_ENTER]:
            pygame.quit()
            return
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # new feature is press right to restart or enter to kill game
                running = False
            elif event.key == pygame.K_RIGHT:
                Draw(ball, num1, num2, t, Time, rand1, rand2, pScore, game_over)
                main()
                running = False

        # Draw the final score screen
        Draw(ball, num1, num2, t, Time, rand1, rand2, pScore, game_over)





if __name__ == '__main__':
    main()
