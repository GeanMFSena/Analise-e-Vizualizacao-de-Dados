import random as rd

class Die:
    '''classe que gera um dado de dois lados'''

    def __init__(self,num_side=6):
        self.num_sides = num_side
        
    def roll(self):
        '''retorna um valor aleatorio entre um e o numero de lados'''
        return rd.randint(1,self.num_sides)