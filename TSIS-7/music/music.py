import pygame

pygame.init()
song_list = [
   "Dragula.mp3"
    ]
song_names = [
   "Dragula.mp3"
    ]
screen = pygame.display.set_mode((1662,1664))
pygame.display.set_caption('÷')

font = pygame.font.SysFont('sf', 24)
clock = pygame.time.Clock()
running = True

index = 0
pygame.mixer.music.load(song_list[index])
pygame.mixer.music.play()
song_name = song_names[index]
text = font.render("Currently playing:  ", True, ('black'))
text1 = font.render(song_name, True, ('black'))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        index -= 1
        pygame.mixer.music.load(song_list[index])
        song_name = song_names[index]
        text = font.render("Currently playing:  ", True, ('black'))
        text1 = font.render(song_name, True, ('black'))
        pygame.mixer.music.play()
    if pressed[pygame.K_SPACE]: pygame.mixer.music.stop()
    if pressed[pygame.K_UP]: pygame.mixer.music.pause()
    if pressed[pygame.K_DOWN]: pygame.mixer.music.unpause()
    if pressed[pygame.K_RIGHT]: 
        index += 1
        pygame.mixer.music.load(song_list[index])
        song_name = song_names[index]
        text = font.render("Currently playing:  ", True, ('black'))
        text1 = font.render(song_name, True, ('black'))
        pygame.mixer.music.play()
    if index == len(song_list) - 1:
        index = -1


    screen.fill((255, 255, 255))
    screen.blit(pygame.image.load('Rob_Z.png'), (0, 0))
    screen.blit(text, (400, 535))
    screen.blit(text1, text1.get_rect(center = (470,565)))
    pygame.display.flip()
    clock.tick(5.75)