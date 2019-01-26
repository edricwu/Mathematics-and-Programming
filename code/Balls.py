from random import *

def balls(black,white):
    x = ['black']*black + ['white']*white
    shuffle(x)
    while len(x)>1:
        balls = sample(x,2)
        ball_1 = balls[0]
        ball_2 = balls[1]
        if ball_1 == 'black' or ball_2 == 'black':
            x.remove('black')
            shuffle(x)
        else:
            x.remove('white')
            x.remove('white')
            x.append('black')
            shuffle(x)
    return x[0]

print (balls(150,75))
