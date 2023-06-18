import pygame
import numpy
import random
pygame.init()

def findMatches(word, anotherWord, currentIndex):
    if currentIndex == 5:
        return 0
    matches = 0
    for j in range(currentIndex+1, 5):
        if word[j:j+1] == anotherWord[j:j+1] and anotherWord[j:j+1] == anotherWord[currentIndex:currentIndex+1]:
            matches += 1
    return matches

def findColored(word, anotherWord, currentIndex, letter):
    letterCount = word.count(letter)
    if not letter.__eq__(anotherWord[currentIndex]) :
        if currentIndex == 0:
            return 0
        return findColored(word,anotherWord,currentIndex-1,letter)
    if currentIndex == 0:
        if word[0] == anotherWord[0]:
            return 1
        elif findMatches(word,anotherWord,0) < letterCount:
            return 1
        else: 
            return 0
    count = 0
    if anotherWord[currentIndex] in word[0:currentIndex]:
        for m in range(currentIndex):
            if anotherWord[m] == anotherWord[currentIndex] and anotherWord[m] == word[m]:
                count += 1
            elif anotherWord[m] == anotherWord[currentIndex] and findColored(word,anotherWord,currentIndex-1,letter) + findMatches(word,anotherWord,currentIndex) < letterCount:
                count += 1
    return count


arrayOfWords = numpy.empty(2500, dtype='U25')
f = open('words.txt')
count = 0
for line in f.readlines():
    arrayOfWords[count] = line.replace('\n','')
    count += 1
f.close()
wordIndex = random.randint(0,2498)          
word = arrayOfWords[wordIndex]  

turn = 0
black = (0,0,0)
green = (0,255,0)
yellow = (255,255,0)
white = (255,255,255)
red = (255,0,0)
font = pygame.font.Font('freesansbold.ttf',56)
WIDTH = 500
HEIGHT = 700
screen = pygame.display.set_mode([WIDTH,HEIGHT])
timer = pygame.time.Clock()
fps = 60
board = [[" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "]]


def draw_board():
    global turn
    global word
    global board

    for col in range(0, 5):
        for row in range(0, 6):            
            pygame.draw.rect(screen, white, [col * 100 + 12, row * 100 + 12, 75, 75], 3, 5)
            if turn > row and board[row][col] in word: 
                guessed = ''
                for j in range(5):
                    guessed += board[row][j]
                numLetters = word.count(board[row][col])
                numColored = findColored(word,guessed,col,guessed[col])
                numMatches = findMatches(word,guessed,col)
                if board[row][col] == word[col]:
                    pygame.draw.rect(screen, green, [col * 100 + 12, row * 100 + 12, 75, 75], 0, 5)
                elif numMatches + numColored < numLetters:
                    pygame.draw.rect(screen, yellow, [col * 100 + 12, row * 100 + 12, 75, 75], 0, 5)            
            piece_text = font.render(board[row][col], True, white)
            screen.blit(piece_text, (col * 100 + 30, row * 100 + 25))            
    pygame.draw.rect(screen, green, [5, turn * 100 + 5, WIDTH - 10, 90], 3, 5)                   

                

game_over = False
letters = 0


running = True
while running:
    timer.tick(fps)
    screen.fill(black)
    text = font.render(word,True,green)
    screen.blit(text,(0,650))
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.TEXTINPUT and letters < 5:
                entry = event.__getattribute__('text')
                if entry != " ":
                    entry = entry.lower()
                    board[turn][letters] = entry
                    letters += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and letters > 0:
                letters -= 1
                board[turn][letters] = ' '
            if event.key == pygame.K_RETURN:
                guess = ''
                for i in range(5):
                    guess += board[turn][i]
                if letters < 5 or guess not in arrayOfWords:
                    count = 0
                    while count < 6:
                        timer.tick(5)
                        count += 1
                        if count % 2 == 0:
                            pygame.draw.rect(screen,black,[5, turn * 100 + 5, WIDTH - 10, 90],3,5)
                        if count % 2 == 1:
                            pygame.draw.rect(screen,red,[5, turn * 100 + 5, WIDTH - 10, 90],3,5)

                        pygame.display.flip()
                elif guess.__eq__(word):
                    count = 0
                    while count < 6:
                        timer.tick(5)
                        screen.fill(black)
                        count += 1
                        if count % 2 == 0:
                            text = font.render('WINNER!', True, green)
                            screen.blit(text,(150,300))
                        if count % 2 == 1:
                            text = font.render('WINNER!', True, white)
                            screen.blit(text,(150,300))

                        pygame.display.flip()
                    running = False
                elif turn == 5:
                    count = 0
                    while count < 6:
                        timer.tick(5)
                        count += 1
                        if count % 2 == 0:
                            for x in range(0,6):
                                pygame.draw.rect(screen, red, [5, x * 100 + 5, WIDTH - 10, 90], 3, 5)
                        if count % 2 == 1:
                            for y in range(0,6):
                                pygame.draw.rect(screen, black, [5, y * 100 + 5, WIDTH - 10, 90], 3, 5)

                        pygame.display.flip()
                    count = 0
                    while count < 6:
                        timer.tick(5)
                        count += 1
                        if count % 2 == 0:
                            text = font.render('LOSER!', True, red)
                            screen.blit(text,(150,300))
                        if count % 2 == 1:
                            text = font.render('LOSER!', True, white)
                            screen.blit(text,(150,300))

                        pygame.display.flip()
                    running = False                        
                    
                else:
                    turn += 1
                    letters = 0
                    
    pygame.display.flip()

pygame.quit()