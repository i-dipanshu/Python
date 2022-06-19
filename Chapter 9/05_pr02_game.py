def game():
    return 126 
score = game()
with open('Chapter 9\highscore.txt') as f:
    highscore = f.read()

if highscore == '':
    with open("Chapter 9\highscore.txt", 'w') as f:
        f.write(str(score))

elif int(highscore) < score:
    with open("Chapter 9\highscore.txt", 'w') as f:
        f.write(str(score))
