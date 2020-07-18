import pygame

play = True
speed = 15 # Скорость движения кораблика

pygame.init()
pygame.display.set_caption('spaceships battle')

W = 700 # Размеры окна
H = 400
COLOR = (0, 0, 0) # Цвет фона экрана

FPS = 30
start1_y = 20 # Стартовая позиция 1st кораблика
start2_y = 375 # Стартовая позиция 2st корбалика

# класс летающих корабликов для создания спрайта лемонад
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, group): # функция создания объекта Spaceship
        pygame.sprite.Sprite.__init__(self) # конструктор класса Sprite
        self.image = pygame.image.load(filename).convert_alpha() 
        self.rect = self.image.get_rect(center=(x, y))
        self.add(group) # добавляю объект в группoу

# класс пулек
class Lazer:
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        
sc = pygame.display.set_mode((W, H))

ships = pygame.sprite.Group() # группа спрайтов корабликов

first_ship = Spaceship(20, start1_y, '1st.png', ships) # Создаю 1st кораблик
second_ship = Spaceship(680 ,start2_y, '2st.png', ships)

lazer1_X = 40
lazer2_X = 665

first_HP = 3 # броня первого кораблика
second_HP = 3 # броня второго кораблика

hit = pygame.mixer.Sound('hit.wav')
shot = pygame.mixer.Sound('shot.wav')

while play:
    lazer1 = Lazer(-5, -5, 'lazer1.png')
    lazer2 = Lazer(-5, -5, 'lazer2.png')
    for i in pygame.event.get():
        if i.type ==  pygame.QUIT: # Выход из программы
            exit()

    keys = pygame.key.get_pressed() # Управление 1st игрока
    if keys[pygame.K_q] and first_ship.rect.y > 10:
        first_ship.rect.y -= speed 
    elif keys[pygame.K_a] and first_ship.rect.y < 360:
        first_ship.rect.y += speed 
    elif keys[pygame.K_s]:
        shot.play()
        lazer1_Y = first_ship.rect[1] + 11 
        lazer1 = Lazer(lazer1_X, lazer1_Y, 'lazer1.png')
        lazer1_X += 65
        if lazer1_X > W:
            lazer1_X = 40

        if pygame.sprite.spritecollideany(lazer1, ships):
            hit.play()
            print('boom 2st')
            second_HP -= 1
            print('у 2st осталось ', second_HP, ' брони')
            pygame.display.update()

    keys = pygame.key.get_pressed() # Управление 2st игрока
    if keys[pygame.K_UP] and second_ship.rect.y > 5:
        second_ship.rect.y -= speed
    elif keys[pygame.K_DOWN] and second_ship.rect.y < 360:
        second_ship.rect.y += speed
    elif keys[pygame.K_LEFT]:
        shot.play()
        lazer2_Y = second_ship.rect[1] + 11
        lazer2 = Lazer(lazer2_X, lazer2_Y, 'lazer2.png')
        lazer2_X -= 65
        if lazer2_X < 0:
             lazer2_X = 665

        if pygame.sprite.spritecollideany(lazer2, ships):
             hit.play()
             print('boom 1st')
             first_HP -= 1
             print('у 1st осталось ', first_HP, ' брони')
             pygame.display.update()

    sc.fill(COLOR)
    sc.blit(first_ship.image, first_ship.rect) #1 кораблик
    sc.blit(second_ship.image, second_ship.rect) # 2 кораблик
    sc.blit(lazer1.image, lazer1.rect)
    sc.blit(lazer2.image, lazer2.rect)

    if first_HP == -1:
        print('Победа 2st!')
        exit()
    elif second_HP == -1:
        print('Победа 1st!')
        exit()
   
    pygame.display.update()
    pygame.time.delay(0)

    pygame.time.delay(FPS)
