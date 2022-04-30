import emoji
from random import seed
from random import random
from random import randint

from emoji.core import emojize

x = (randint(1, 10))
y = (randint(1, 25))

print(emojize("(user2) ,(sender) quer quicar em você... aceitas? :flushed: (1)Sim (2)Não",use_aliases=True))

quicada = int(input("Quicar?"))

if (quicada == 1):

    print(f'(sender) você quicou {x} vezes e o (user2) aguentou {y} minutos! CUMMIES')

elif (quicada == 2):

    print('(sender) você não quicou em (user2). D:')

else:

    print('Ou quica ou vaza!!!')
