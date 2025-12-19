import random as rd 

class RandomWalk:
    '''criando uma classe de passeio aleatorio '''
    
    def __init__(self,num_points=5000):
        self.num_points = num_points 
    
    def fill_walk(self):
        '''Calcula todos os pontos do passeio'''
        
        self.x_values = [0]
        self.y_values = [0]
        
        # continua dando passos ate que o passeio atinja a distancia desejada
        while len(self.x_values) < self.num_points:
            
            # decide qual decisao tomar, e ate onde 
            x_direction = rd.choice([1,-1])
            x_distance = rd.choice([0,1,2,3,4])
            x_step = x_direction * x_distance
            
            y_direction = rd.choice([1,-1])
            y_distance = rd.choice([0,1,2,3,4])
            y_step = y_direction * y_distance
            
            # rejeita movimentos que nao vao a lugar nenhum 
            
            if x_step == 0 and y_step == 0:
                continue
            
            # calcula a nova posicao 
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            
            self.x_values.append(x)
            self.y_values.append(y)
            
            