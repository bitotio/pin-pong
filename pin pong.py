import pygame

pygame.init()

# Частота кадров
FPS = 120

clock = pygame.time.Clock()
screen = pygame.display.set_mode((640, 480))

screen_rect = screen.get_rect()

# Цвета
MAIN_BACKGROUND_COLOR = (255, 255, 255)
MISSILE_COLOR = (255, 0, 0)
SHIP_COLOR = (0, 0, 255)
GAME_OVER_COLOR = (0, 0, 0)
WIN_COLOR = (0, 255, 0)

# Фон
background_color = MAIN_BACKGROUND_COLOR

# Создание корабля
ship = pygame.Rect(300, 200, 50, 100)
ship.right = screen_rect.right
ship.centery = screen_rect.centery

# Создание ракеты
missile = pygame.Rect(50, 50, 10, 10)
missile.left = screen_rect.left
missile.centery = screen_rect.centery

# Скорости
missile_speed_x = 0
missile_speed_y = 0
ship_speed_y = 1

# Флаги состояния
ship_alive = True
missile_alive = True
missile_launched = False

running = True

while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not missile_launched:
                missile_launched = True
                missile_speed_x = 3  # Запуск ракеты вперед
                missile_speed_y = 0

            elif event.key == pygame.K_w and not missile_launched:
                missile_speed_y = -2  # Движение ракеты вверх

            elif event.key == pygame.K_s and not missile_launched:
                missile_speed_y = 2  # Движение ракеты вниз

    # Логика игры (вынесена из обработки событий)

    if missile_alive:
        missile.move_ip(missile_speed_x, missile_speed_y)

        # Если ракета вышла за пределы экрана
        if not screen_rect.contains(missile):
            missile_alive = False
            background_color = GAME_OVER_COLOR  # Игра окончена (проигрыш)

        # Если ракета столкнулась с кораблем
        if ship_alive and missile.colliderect(ship):
            missile_alive = False
            ship_alive = False
            background_color = WIN_COLOR  # Победа

    # Движение корабля вверх-вниз
    if ship_alive:
        ship.move_ip(0, ship_speed_y)
        if ship.bottom > screen_rect.bottom or ship.top < screen_rect.top:
            ship_speed_y = -ship_speed_y  # Меняем направление

    # Отрисовка
    screen.fill(background_color)

    if ship_alive:
        pygame.draw.rect(screen, SHIP_COLOR, ship)

    if missile_alive:
        pygame.draw.rect(screen, MISSILE_COLOR, missile)

    pygame.display.flip()

    # Ограничение FPS
    clock.tick(FPS)

pygame.quit()
