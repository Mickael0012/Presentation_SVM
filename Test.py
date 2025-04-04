import random
import matplotlib.pyplot as plt
import numpy as np
import math

def generate_data_simple(dimension=2, pop=30, coeffs=(1,1)):

    groupe1 = []
    groupe2 = []
    for i in range(pop):
        g1 = [random.randint(0,100)*coeffs[c] for c in range(dimension)]
        g2 = [random.randint(150,250)*coeffs[c] for c in range(dimension)]

        groupe1.append(np.array(g1))
        groupe2.append(np.array(g2))

    return groupe1,groupe2


def generate_data_polaire(dimension=2, pop=30, coeffs=(1,1)):

    groupe1 = []
    groupe2 = []
    for i in range(pop):
        r = random.randint(0,100)
        v = random.uniform(-math.pi,math.pi)
        g1 = [math.cos(v)*r,math.sin(v)*r]
        

        groupe1.append(np.array(g1))

    return groupe1


def separate_coords(groupe_points):
    return [point[0] for point in groupe_points], [point[1] for point in groupe_points]


def moyenne_points(groupe_points):
    somme = [0]*len(groupe_points[0])
    for point in groupe_points:
        somme += point

    return somme/len(groupe_points)


def calcul_vect_opti(groupe1,groupe2):
    m1 = moyenne_points(groupe1)
    m2 = moyenne_points(groupe2)
    return m2-m1


# TEST =======================================================

g1 = generate_data_polaire(pop=300)

data = g1
print(len(data))
print(data)

x, y = separate_coords(data)
plt.scatter(x,y)
plt.axis((-100,100,-100,100))
plt.show()