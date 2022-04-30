from random import seed
from random import random
from random import randint

seed()
value = random()

a = (randint(1,5))

if(value<0.5):
    print(f'Você tragou {a} vezes e se engasgou.')

else:
    print(f'Você deu {a} tragadas e não engasgou!') 
