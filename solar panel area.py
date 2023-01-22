import matplotlib.pyplot as plt
import math

AU = 1.50 * (10 ** 11)  # unit: m
L = 15 # years
P = 150 # W
delta = 0.0275
n = 0.3
Id = 0.65
theta_max = 25 * (math.pi / 180)

def BOL(ds_in_AU, n, Id, theta_max):
    flux = 1368 * (1 / ds_in_AU ** 2)  # unit: W/m^2
    P_0 = n * flux
    # n = solar cell efficiency
    P_BOL = P_0 * Id * math.cos(theta_max)
    # Id = inherent degradation, theta_max = worst-case solar angle in radians
    return P_BOL  # unit: W/m^2


def EOL(P_BOL, L, delta):
    L_d = (1 - delta) ** L
    # delta = degredation per year, L = mission length
    P_EOL = L_d * P_BOL
    return P_EOL  # unit: W/m^2
 

def area(P, P_EOL):
    A_sa = P / P_EOL
    # P = required power
    return A_sa  # unit: m^2


# plot A_sa as a function of distance from Sun
def plot1():
    step = 0.99375
    # ds_in_AU in range (0.25, 40)
    x_vals = [0.25 + step * i for i in range(41)]
    y_vals = []
    for x_val in x_vals:
        P_BOL = BOL(x_val, n, Id, theta_max)
        P_EOL = EOL(P_BOL, L, delta)
        A_sa = area(P, P_EOL)
        y_vals.append(A_sa)
    # plot the graph
    plt.plot(x_vals, y_vals)
    # x-axis
    plt.xlabel('Distance from the Sun (unit: AU)')
    # y_axis
    plt.ylabel('Required Solar Array Size (unit: m^2)')
    # I think the labels are self-explanatory enough to not use a plot title
    plt.show()


# This function is used solely for calculation purposes
def calc(ds_in_AU):
    P_BOL = BOL(ds_in_AU, n, Id, theta_max)
    P_EOL = EOL(P_BOL, L, delta)
    A_sa = area(P, P_EOL)
    print('The required solar array size at', ds_in_AU, 'is', A_sa, 'm^2.')
    
    
# plot EOL as a function of mission lifetime
def plot2():
    # lifetime 0 to 30
    x_vals = [i for i in range(31)]
    y_vals = []
    for lifetime in x_vals:
        P_BOL = BOL(1, n, Id, theta_max)
        P_EOL = EOL(P_BOL, lifetime, delta)
        y_vals.append(P_EOL)
    plt.plot(x_vals, y_vals)
    plt.xlabel('Mission Lifetime (unit: year)')
    plt.ylabel('EOL Power Density (unit: W/m^2)')
    plt.show()
        

# plot A_sa as a function of mission lifetime
def plot3():
    x_vals = [i for i in range(31)]
    y_vals = []
    for lifetime in x_vals:
        P_BOL = BOL(1, n, Id, theta_max)
        P_EOL = EOL(P_BOL, lifetime, delta)
        A_sa = area(P, P_EOL)
        y_vals.append(A_sa)
    plt.plot(x_vals, y_vals)
    plt.xlabel('Mission Lifetime (unit: year)')
    plt.ylabel('Required Solar Array Size (unit: m^2)')
    plt.show()


if __name__ == '__main__':
    
    