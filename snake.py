import pygame, sys, time, random
from pygame.locals import *

# dimensioni pannello
X_MAX = 640
Y_MAX = 480

# stato del gioco
gameState = 'started'

# inizializzazione gioco
pygame.init()
# impostazione clock FPS
fpsClock = pygame.time.Clock()
# impostazione display
playSurface = pygame.display.set_mode((X_MAX, Y_MAX))
# titolo finestra
pygame.display.set_caption('SNAKE')

# colori utili
red = pygame.Color(255, 0, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
grey = pygame.Color(150, 150, 150)
green = pygame.Color(0, 255, 0)

# posizione iniziale dello snake
snakePos = [100, 100]
# segmenti iniziali del serpente
snakeSegm = [[100,100],[80,100],[60,100]]
# posizione frutto
raspPos = [300, 300]
# frutto è spawnato o no
raspSpawned = 1
# direzione iniziale
direction = 'right'
# prossima direzione richiesta
changeDirection = 'right'
# punteggio
score = 0

# funzione per terminare il gioco
def terminate():
    pygame.quit()
    sys.exit()

# fonts
font = pygame.font.Font('freesansbold.ttf', 72)
fontSmall = pygame.font.Font('freesansbold.ttf', 36)

# testo-bottone di play
buttonRun = fontSmall.render('Play', True, green)
# testo-bottone di exit
buttonExit = fontSmall.render('Exit', True, green)

# main loop del gioco
while True:
    # event handling
    for event in pygame.event.get():
        # uscita
        if event.type == QUIT:
            terminate()
        # gestione freccie / WASD => imposto la prossima direzione
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT or event.key == ord('d'):
                changeDirection = 'right'
            if event.key == K_LEFT or event.key == ord('a'):
                changeDirection = 'left'
            if event.key == K_UP or event.key == ord('w'):
                changeDirection = 'up'
            if event.key == K_DOWN or event.key == ord('s'):
                changeDirection = 'down'
            # esc metto il gioco in state paused altrimenti running se già pausato
            if event.key == K_ESCAPE:
                if gameState == 'paused':
                    gameState = 'running'
                else:
                    gameState = 'paused'
        # controllo pulsanti
        elif event.type == MOUSEBUTTONDOWN:
            # coordinate click
            mouse_pos = event.pos
            # click sul pulsante di running (le coordinate sono quelle di quando è in pausa)
            if buttonRun.get_rect(center = (X_MAX / 2, Y_MAX / 2 + 80)).collidepoint(mouse_pos):
                gameState = 'running'
            # click sul pulsante di running (le coordinate sono quelle di quando è in gameover)
            elif buttonRun.get_rect(center = (X_MAX / 2 - 60, Y_MAX / 2 + 80)).collidepoint(mouse_pos):
                gameState = 'started'
            # click sul pulsante di exit (le coordinate sono quelle di quando è in pausa)
            elif buttonExit.get_rect(center = (X_MAX / 2 + 60, Y_MAX / 2 + 80)).collidepoint(mouse_pos):
                terminate()

    # gioco appena partito => reset variabili
    if gameState == 'started':
        snakePos = [100, 100]
        snakeSegm = [[100,100],[80,100],[60,100]]
        raspPos = [300, 300]
        raspSpawned = 1
        direction = 'right'
        changeDirection = 'right'
        gameState = 'running'
        score = 0
    # in running
    elif gameState == 'running':
        # controllo che la prossima direzione non sia opposta all'attuale
        if changeDirection == 'right' and not direction == 'left':
            direction = changeDirection
        if changeDirection == 'left' and not direction == 'right':
            direction = changeDirection
        if changeDirection == 'up' and not direction == 'down':
            direction = changeDirection
        if changeDirection == 'down' and not direction == 'up':
            direction = changeDirection

        # sposto la posizione della testa nella direzione voluta tramite le coordinate
        if direction == 'right':
            snakePos[0] += 20
        if direction == 'left':
            snakePos[0] -= 20
        if direction == 'up':
            snakePos[1] -= 20
        if direction == 'down':
            snakePos[1] += 20

        # aggiungo la testa alla coda ...segue
        snakeSegm.insert(0, list(snakePos))

        # ... se ho preso il frutto (stesse coordinate della testa)
        if snakePos[0] == raspPos[0] and snakePos[1] == raspPos[1]:
            # ... aumento il punteggio
            score += 1
            # ... mi segno che è da rispawnare 
            raspSpawned = 0
        else:
            # ... se non l'ho presa allora cavo l'ultimo elemento dalla coda
            snakeSegm.pop()

        # rispawning frutto a random
        if raspSpawned == 0:
            x = random.randrange(1, 32)
            y = random.randrange(1, 24)
            raspPos = [x*20, y*20]
            raspSpawned = 1

        # RENDERING
        # render superficie base
        playSurface.fill(black)
        # rendering di ogni segmento della coda
        for position in snakeSegm:
            pygame.draw.rect(playSurface, white, Rect(position[0], position[1], 20, 20))
        # rendering della testa
        pygame.draw.rect(playSurface, red, Rect(raspPos[0], raspPos[1], 20, 20))

        # controllo se la testa si sta scontrando con la coda
        for snakeBody in snakeSegm[1:]:
            # check di tutti i segmenti della coda
            if snakePos[0] == snakeBody[0] and snakePos[1] == snakeBody[1]:
                gameState = 'gameover'

        # check confini mappa => se esce dai confini lo riporto dall'altra parte
        # della mappa (stile terrapiattisti // pac-man)
        if snakePos[0] > X_MAX:
            snakePos[0] = -20
        elif snakePos[0] < 0:
            snakePos[0] = X_MAX
            
        if snakePos[1] > Y_MAX:
            snakePos[1] = -20
        elif snakePos[1] < 0:
            snakePos[1] = Y_MAX

        # rendering testopunteggio
        scoreText = fontSmall.render(str(score), True, green)
        scoreRect = scoreText.get_rect()
        scoreRect.center = (X_MAX - 30, 30)
        # rendering testo
        playSurface.blit(scoreText, scoreRect)
        # obbligatorio per l'update del display
        pygame.display.flip()
    
    elif gameState == 'paused':
        # se il gioco è in pausa renderizzo il testo di pausa
        surf = font.render('Pause', True, red)
        rect = surf.get_rect()
        rect.center = (X_MAX / 2, Y_MAX / 2)
        runRect = buttonRun.get_rect()
        runRect.center = (X_MAX / 2, Y_MAX / 2 + 80)
        playSurface.blits(blit_sequence=((surf, rect), (buttonRun ,runRect)))
        pygame.display.flip()
        
    elif gameState == 'gameover':
        # se in gameover renderizzo il testo di gameover
        surf = font.render('Game Over', True, grey)
        rect = surf.get_rect()
        rect.center = (X_MAX / 2, Y_MAX / 2)
        runRect = buttonRun.get_rect()
        runRect.center = (X_MAX / 2 - 60, Y_MAX / 2 + 80)
        exitRect = buttonExit.get_rect()
        exitRect.center = (X_MAX / 2 + 60, Y_MAX / 2 + 80)
        playSurface.blits(blit_sequence=((surf, rect), (buttonRun ,runRect), (buttonExit,exitRect)))
        pygame.display.flip()

    # indica la velocità in cui verrà eseguito il main loop del gioco => aumenta a secodna del punteggio corrente
    fpsClock.tick(10 + (score * 0.1))
    
