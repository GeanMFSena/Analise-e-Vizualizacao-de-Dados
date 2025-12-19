from random_walk import RandomWalk 
import matplotlib.pyplot as plt 

while True:
    
    # cria um random walk
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use('seaborn-v0_8')

    fig,ax = plt.subplots()

    ax.scatter(rw.x_values, rw.y_values, c=rw.y_values, cmap= plt.cm.Blues , s=25)

    # isso passa para o python que queremos que o tamanho do grafico para x e y fiquem do mesmo tamanho

    ax.set_aspect('equal')

    ax.set_title('Squares', fontsize=24)
    ax.set_xlabel('Values', fontsize=14)
    ax.set_ylabel('Squares', fontsize=14)


    plt.show()
    
    keep_running = input('Make another walk? (y/n): ').lower()

    if keep_running == 'n':
        break
