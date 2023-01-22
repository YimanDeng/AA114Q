''' origami dimensions'''

import matplotlib.pyplot as plt
import math


# length change (L / L_0) as a function of beta
def length_change():
    x_vals = [n for n in range(91)]
    alphas = [70, 74, 78, 82, 86, 90]
    lists = [[] for alpha in alphas]
    for beta in x_vals:
        for alpha in alphas:
            rad_alpha = math.radians(alpha)
            rad_beta = math.radians(beta)
            len_change = math.sqrt(1 - math.sin(rad_alpha)**2 * math.sin(rad_beta)**2)
            lists[alphas.index(alpha)].append(len_change)
    for i in range(len(lists)):
        plt.plot(x_vals, lists[i], label='alpha: ' + str(alphas[i]))
    plt.legend()
    plt.xlabel('Deployment Angle (Beta)')
    plt.ylabel('Length Change (L / L_0)')
    plt.show()


# width change (S / S_0) as a function of beta
def width_change():
    x_vals = [n for n in range(91)]
    alphas = [70, 74, 78, 82, 86, 90]
    lists = [[] for alpha in alphas]
    for beta in x_vals:
        for alpha in alphas:
            rad_alpha = math.radians(alpha)
            rad_beta = math.radians(beta)
            wid_change = math.cos(rad_beta) / (math.cos(rad_alpha) * 
                                               math.sqrt(1 + math.tan(rad_alpha)**2
                                                         * math.cos(rad_beta)**2))
            lists[alphas.index(alpha)].append(wid_change)
    for i in range(len(lists)):
        plt.plot(x_vals, lists[i], label='alpha: ' + str(alphas[i]))
    plt.legend()
    plt.xlabel('Deployment Angle (Beta)')
    plt.ylabel('Width Change (S / S_0)')
    plt.show()


# width change (S / S_0) as a function of beta
def height():
    x_vals = [n for n in range(91)]
    alphas = [70, 74, 78, 82, 86, 90]
    lists = [[] for alpha in alphas]
    for beta in x_vals:
        for alpha in alphas:
            rad_alpha = math.radians(alpha)
            rad_beta = math.radians(beta)
            h = 5 * (math.sin(rad_alpha) * math.sin(rad_beta))
            lists[alphas.index(alpha)].append(h)
    for i in range(len(lists)):
        plt.plot(x_vals, lists[i], label='alpha: ' + str(alphas[i]))
    plt.legend()
    plt.xlabel('Deployment Angle (Beta)')
    plt.ylabel('Height (H, unit: cm)')
    plt.show()
   
    
# Dimensions of parallelograms (a, b) as a function of # of unit cells across each panel
def dimensions(): 
    # n * 2 * a = boom_length
    # n * 2 * b * math.cos(alpha) = boom_length
    boom_length = 0.3 # m
    alpha = math.radians(65)
    x_vals = [n + 1 for n in range(10)]
    a_vals = []
    b_vals = []
    for n in x_vals:
        a_vals.append(boom_length / (2 * n))
        b_vals.append(boom_length / (2 * n * math.sin(alpha)))
    plt.scatter(x_vals, a_vals, label='a')
    plt.scatter(x_vals, b_vals, label='b')
    plt.legend()
    plt.xlabel('Number of Unit Cells across Each Panel')
    plt.ylabel('Dimension of a, b (unit: m)')
    plt.show()
    
    
# Packaged height of a single array as a function of # of unit cells across each panel
def height2():
    boom_length = 0.3 # m
    x_vals = [n + 1 for n in range(10)]
    alpha = math.radians(65)
    beta = math.radians(90)
    h_vals = []
    for n in x_vals:
        h = (boom_length / (2 * n)) * (math.sin(alpha) * math.sin(beta))
        h_vals.append(h)
        if h < 0.05:
            print(n)
    plt.scatter(x_vals, h_vals)
    plt.xlabel('Number of Unit Cells across Each Panel')
    plt.ylabel('Packaged Height (unit: m)')
    plt.show()
    

# Packaged length of a single array as a function of # of unit cells across each panel
def length2():
    boom_length = 0.3 # m
    x_vals = [n + 1 for n in range(10)]
    alpha = math.radians(85)
    beta = math.radians(90)
    l_vals = []
    for n in x_vals:
        len_change = math.sqrt(1 - math.sin(alpha)**2 * math.sin(beta)**2)
        a = boom_length / (2 * n)
        b = boom_length / (2 * n * math.sin(alpha))
        l = n * (2 * len_change * a) + b
        l_vals.append(l) 
        if l < 0.05:
            print(n)
    plt.scatter(x_vals, l_vals)
    plt.xlabel('Number of Unit Cells across Each Panel')
    plt.ylabel('Packaged Length (unit: m)')
    plt.show()


if __name__ == '__main__':
    length2()