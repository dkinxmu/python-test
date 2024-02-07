i = 3
running = 1
while running:

    guess = int(input('guess a number between 0~9 :'))
    if guess==i:
        print('U r right\
!')
        running = 0
    elif guess > i:
        print('lower than that')
    else :
        print('higher than that')
