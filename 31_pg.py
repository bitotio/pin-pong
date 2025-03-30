import pygame
pygame.init()




FPS = 120

clock = pygame.time.Clock()
screen = pygame.display.set_mode((640, 480))

screen_rect = screen.get_rect()

MAIN_BACKGROUND_COLOR = (255, 255, 255)
MISSILE_COLOR = (255, 0, 0)
SHIP_COLOR = (0, 0, 255)
GAME_OVER_COLOR = (0, 0, 0)
WIN_COLOR = (0, 255, 0)

background_color = MAIN_BACKGROUND_COLOR

ship = pygame.Rect(300, 200, 50, 100)
ship.right = screen_rect.right

ship.centery = screen_rect.centery

missile = pygame.Rect(50, 50, 10, 10)

missile.left = screen_rect.left

missile.centery = screen_rect.centery

missile_speed_x = 0
missile_speed_y = 0

ship_speed_y = 1

ship_alive = True
missile_alive = True

missile_launched = False

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE and not missile_launched:

                missile_launched = True
                missile_speed_y = 0
                missile_speed_x = 3




            # если нажата клавиша W и торпеда не запущена
            elif event.key == pygame.K_w and not missile_launched:

                missile_speed_y = -2


            # если нажата клавиша S и торпеда не запущена
            elif event.key == pygame.K_s and not missile_launched:

                missile_speed_y = 2

        # если торпеда жива
        if missile_alive:
            # сдвигаем торпеду на величину скорости по горизонтали и
            missile.move_ip(missile_speed_x, missile_speed_y)
            # если торпеда не пересекается с экраном, значит вылетела
            if not missile.colliderect(screen_rect):
                # устанавливаем флаг жизни торпеды в False
                missile_alive = False
                # меняем цвет фона на черный
                background_color = GAME_OVER_COLOR

            # если торпеда столкнулась с кораблем
            if ship_alive and missile.colliderect(ship):
                # устанавливаем флаги жизни торпеды и корабля в False
                missile_alive = False
                ship_alive = False
                background_color = WIN_COLOR
if ship_alive:
    # сдвигаем корабль на величину скорости по вертикали
    ship.move_ip(0, ship_speed_y)
    # если нижняя кромка корабля вышла за нижнюю границу экрана или

    if ship.bottom > screen_rect.bottom or ship.top < screen_rect.top:
        ship_speed_y = -ship_speed_y

    screen.fill(background_color)

    if ship_alive:

        pygame.draw.rect(screen, SHIP_COLOR, ship)

    if missile_alive:
        pygame.draw.rect(screen, MISSILE_COLOR, missile)
    # обновляем дисплей
    pygame.display.flip()
    # задерживаем цикл на нужное время для достижения FPS=60
    clock.tick(FPS)
    # выходим из рудате
pygame.quit()
