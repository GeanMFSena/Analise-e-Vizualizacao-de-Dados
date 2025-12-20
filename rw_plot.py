from random_walk import RandomWalk 
import matplotlib.pyplot as plt 

while True:
    
    # cria um random walk
    rw = RandomWalk(100_000)
    rw.fill_walk()

    # plt.style.use('seaborn-v0_8')
    plt.style.use('classic')
    fig,ax = plt.subplots(figsize =(10,6), dpi=124)
    
    point_numbers = range(rw.num_points)    

    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap= plt.cm.Blues ,edgecolors='none', s=1)
    # ax.scatter(0,0, c='green',edgecolors='none', s=100)
    # ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    
    # remove os eixos x e y
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    # isso passa para o python que queremos que o tamanho do grafico para x e y fiquem do mesmo tamanho
    ax.set_aspect('equal')

    ax.set_title('Squares', fontsize=24)
    ax.set_xlabel('Values', fontsize=14)
    ax.set_ylabel('Squares', fontsize=14)

    plt.show()
    
    keep_running = input('Make another walk? (y/n): ').lower()

    if keep_running == 'n':
        break
