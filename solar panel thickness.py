import matplotlib.pyplot as plt
import math

PANELS = 10
GAP = 2 # mm
DENSITY = 0.05 #g/cm^2

# plot packaged stack height of each wing as a function of panel thickness
def plot1():
    x_vals = [0.1 + 0.1 * i for i in range(35)]
    y_vals = []
    for x_val in x_vals:
        h_stack = (PANELS * (x_val + GAP)) / 10 # mm to cm
        y_vals.append(h_stack)
    plt.plot(x_vals, y_vals)
    plt.xlabel('Panel Thickness (unit: mm)')
    plt.ylabel('Packaged Stack Height (unit: cm)')
    plt.title('Packaged Stack Height of Each Wing as a Function of Panel Thickness')
    plt.show()

# plot the mass of each wing as a function of panel thickness
def plot2():
    x_vals = [0.1 + 0.1 * i for i in range(35)]
    y_vals = []
    for x_val in x_vals:
        mass = 1.85*10*((x_val/10)*10*10) + (PANELS)*7 + 90 + 1.2*0.9 + DENSITY*10*10
        # mass = PCB panels + hinges + actuation motor + cables + solar cells
        y_vals.append(mass / 1000) # kg
        # print(x_val, mass * 1.2 / 1000)
    min_vals = [0.8 * y_val for y_val in y_vals]
    max_vals = [1.2 * y_val for y_val in y_vals]
    plt.plot(x_vals, y_vals, label='true mass')
    plt.plot(x_vals, max_vals, label='+20% margin')
    plt.plot(x_vals, min_vals, label='-20% margin')
    plt.legend()
    plt.xlabel('Panel Thickness (unit: mm)')
    plt.ylabel('Mass (unit: kg)')
    plt.title('Mass of Each Wing as a Function of Panel Thickness')
    plt.show()

# plot fundamental frequency of each wing as a function of panel thickness
def plot3():    
    x_vals = [0.1 + 0.1 * i for i in range(35)]
    y_vals = []
    for x_val in x_vals:
        # second moment of area in deployed state
        I = (0.1 * (x_val/1000) ** 3) / 12
        # I = (w * t^3) / 12
        mass = 1.2 * (1.85*10*((x_val/10)*10*10) + (PANELS)*7 + 90 + 1.2*0.9 + DENSITY*10*10)
        mass = mass / 1000
        fund_f = (1/(2*math.pi)) * math.sqrt(3*(20*10**9)*I/(mass * 1**3))
        y_vals.append(fund_f)
    plt.plot(x_vals, y_vals)
    plt.xlabel('Panel Thickness (unit: mm)')
    plt.ylabel('Fundamental Frequency (unit: Hz)')
    plt.title('Fundamental Frequency of Each Wing as a Function of Panel Thickness')
    plt.show()


if __name__ == '__main__':
    # I'm trying to find the minimum thickness to satisfy fund_f requirements
    x_vals = [0.01 + 0.01 * i for i in range (350)]
    for x_val in x_vals:
        mass = 1.2 * (1.85*10*((x_val/10)*10*10) + (PANELS)*7 + 90 + 1.2*0.9 + DENSITY*10*10)
        mass = mass / 1000
        I = (0.1 * (x_val/1000) ** 3) / 12
        fund_f = (1/(2*math.pi)) * math.sqrt(3*(20*10**9)*I/(mass * 1**3))
        if fund_f > 0.1:
            print(x_val, fund_f)