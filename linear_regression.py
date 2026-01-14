import matplotlib.pyplot as plt
import numpy as np

xs = [1, 2, 3, 5, 7, 9]
ys = [2, 4, 5, 9, 15, 21]

x  = np.linspace(0, 10, 100) #Define intervalo início-fim e reparte no número de pontos

#======================================================================================
def erro_medio(a, b):
    erro = 0
    for i in range(len(xs)):
        y_prev = a*xs[i] + b
        erro += (ys[i] - y_prev)**2

    erro = erro/(len(xs))

    return erro

#======================================================================================
melhor_erro = float("inf")
melhor_a = 0
melhor_b = 0

for a in [i/100 for i in range(-200, 400)]:
    for b in [j/100 for j in range(-200, 400)]:
        e = erro_medio(a,b)
        if(e<melhor_erro):
            melhor_erro = e
            melhor_a = a
            melhor_b = b

print(melhor_erro)

#======================================================================================
m = 2.3
b = -1.

print(f"Melhor erro manual: {erro_medio(m,b)}")

#======================================================================================

y = m*x + b

melhor_y = (melhor_a)*x + melhor_b


#======================================================================================
#Plotagem

plt.plot(x, y, label=f'y = {m}x + {b}', color='blue') #Plota a reta
plt.plot(x, melhor_y, label=f'best_y = {melhor_a}x + {melhor_b}', color='green')

for i in range(len(xs)):
    plt.plot(xs[i], ys[i], marker = "o", markersize = 5, color="red")

plt.legend()
plt.grid(True)
plt.show()
#======================================================================================