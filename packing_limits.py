'''packaging limits for different materials'''

import matplotlib.pyplot as plt
import math

R = 18 # mm
A_sa = 0.1834 # m^2


# beryllium copper
def plot1():
    E = 130 * 10**9 # Pa
    yield_strength = 1000 * 10**6 # Pa
    v = 0.3
    x_vals = [18 + n for n in range(162)]
    y_vals_E = []
    y_vals_O = []
    for x_val in x_vals:
        # Equal
        # x_val / R > 1
        if 1 <= x_val / R < 1/v:
            limit_E = (E / (2 * yield_strength)) * ((x_val / R + 1) / 
                                                    ((1 + v) * (x_val / R)))
            t_E = R / limit_E
            y_vals_E.append(t_E)
        else: 
            limit_E = (E / (2 * yield_strength)) * ((x_val / R - v) / 
                                                ((1 - v**2) * (x_val / R )))
            t_E = R / limit_E
            y_vals_E.append(t_E)
        # Opposite
        limit_O = (E / (2 * yield_strength)) * ((x_val / R + v) / 
                                                ((1 - v**2) * (x_val / R )))
        t_O = R / limit_O
        y_vals_O.append(t_O)
    plt.plot(x_vals, y_vals_E, label='Equal-sense Coiling')
    plt.plot(x_vals, y_vals_O, label='Opposite-sense Coiling')
    plt.legend()
    plt.xlabel('Coil Radius (unit: mm)')
    plt.ylabel('Max Thickness (unit: mm)')
    plt.title('Beryllium Copper')
    plt.show()
    
    
# steel
def plot2():
    E = 190 * 10**9 # Pa
    yield_strength = 600 * 10**6 # Pa
    v = 0.28
    x_vals = [18 + n for n in range(162)]
    y_vals_E = []
    y_vals_O = []
    for x_val in x_vals:
        # Equal
        if 1 <= x_val / R < 1/v:
            limit_E = (E / (2 * yield_strength)) * ((x_val / R + 1) / 
                                                    ((1 + v) * (x_val / R)))
            t_E = R / limit_E
            y_vals_E.append(t_E)
        else: 
            limit_E = (E / (2 * yield_strength)) * ((x_val / R - v) / 
                                                ((1 - v**2) * (x_val / R )))
            t_E = R / limit_E
            y_vals_E.append(t_E)
        # Opposite
        limit_O = (E / (2 * yield_strength)) * ((x_val / R + v) / 
                                                ((1 - v**2) * (x_val / R )))
        t_O = R / limit_O
        y_vals_O.append(t_O)
        print(x_val, t_O)
    plt.plot(x_vals, y_vals_E, label='Equal-sense Coiling')
    plt.plot(x_vals, y_vals_O, label='Opposite-sense Coiling')
    plt.legend()
    plt.xlabel('Coil Radius (unit: mm)')
    plt.ylabel('Max Thickness (unit: mm)')
    plt.title('Steel')
    plt.show()
    

# Aluminum
def plot3():
    E = 70 * 10**9 # Pa
    yield_strength = 270 * 10**6 # Pa
    v = 0.33
    x_vals = [18 + n for n in range(162)]
    y_vals_E = []
    y_vals_O = []
    for x_val in x_vals:
        # Equal
        if 1 <= x_val / R < 1/v:
            limit_E = (E / (2 * yield_strength)) * ((x_val / R + 1) / 
                                                    ((1 + v) * (x_val / R)))
            t_E = R / limit_E
            y_vals_E.append(t_E)
        else: 
            limit_E = (E / (2 * yield_strength)) * ((x_val / R - v) / 
                                                ((1 - v**2) * (x_val / R )))
            t_E = R / limit_E
            y_vals_E.append(t_E)
        # Opposite
        limit_O = (E / (2 * yield_strength)) * ((x_val / R + v) / 
                                                ((1 - v**2) * (x_val / R )))
        t_O = R / limit_O
        y_vals_O.append(t_O)
    plt.plot(x_vals, y_vals_E, label='Equal-sense Coiling')
    plt.plot(x_vals, y_vals_O, label='Opposite-sense Coiling')
    plt.legend()
    plt.xlabel('Coil Radius (unit: mm)')
    plt.ylabel('Max Thickness (unit: mm)')
    plt.title('Aluminum')
    plt.show()
    
    
# calculate minimum coil radius of solar sheet
def limit_sheet():
    h = 0.08 # mm, value taken from data sheet
    E = 60 * 10**9 # Pa
    yield_strength = 200 * 10**6 # Pa
    # r = (E * h) / (2 * sigma) 
    r_min = (E * h) / (2 * yield_strength) 
    print('minimum coil radius (mm):', r_min)


# Required length of each array as a function of # of arrays
def length():
    width = 51 * 10 ** (-3) # m
    x_vals = [n + 1 for n in range(4)]
    y_vals = []
    for x in x_vals:
         length = A_sa / (width * x)
         length = round(length, 3)
         y_vals.append(length)
    plt.scatter(x_vals, y_vals)
    for i, j in zip(x_vals, y_vals):
        plt.text(i+0.05, j+0.02, '({}, {})'.format(i, j))
    plt.xlabel('Number of Arrays')
    plt.ylabel('Required length of each array (unit: m)')
    plt.show()


# Packaged radius of each roll as a function of # of arrays.
def packaged_radius():
    width = 51 * 10 ** (-3) # m
    coil_r = 21.6 # mm
    thickness = 0.08 #mm
    x_vals = [n + 1 for n in range(4)]
    y_vals = []
    for x in x_vals:
         length = A_sa / (width * x)
         num = (length * 10 ** 3) / (2 * math.pi * coil_r)
         packed_r = coil_r + num * thickness
         packed_r = round(packed_r, 3)
         y_vals.append(packed_r)
    plt.scatter(x_vals, y_vals)
    for i, j in zip(x_vals, y_vals):
        plt.text(i+0.05, j+0.02, '({}, {})'.format(i, j))
    plt.xlabel('Number of Arrays')
    plt.ylabel('Packaged radius of each roll (unit: mm)')
    plt.show()


# Mass of system as function of # of arrays.
def mass():
    # we use density of steel 7.85 g/cm^3
    cell_mass = A_sa * 50 * 10 # g
    width = 51 * 10 ** (-3) # m
    coil_r = 21.6 # mm
    x_vals = [n + 1 for n in range(4)]
    y_vals = []
    for x in x_vals:
        motor_mass = x * 90 # g
        length = A_sa * 100 / (width * x) # cm
        tape_mass = 2 * x * length * 7.85 * (77.3 / 360) * (math.pi * (18 / 10)
                                                            ** 2 - math.pi * 
                                                            ((18 - 0.08) / 10) 
                                                            ** 2)
        hub_mass = x * (math.pi * (coil_r / 10) ** 2 - math.pi * 
                        ((coil_r - 2) / 10) ** 2) * 10 * 1.2
        total = cell_mass + motor_mass + tape_mass + hub_mass
        print(x, cell_mass, motor_mass, tape_mass, hub_mass)
        y_vals.append(round(total * 1.2))
    plt.scatter(x_vals, y_vals)
    for i, j in zip(x_vals, y_vals):
        plt.text(i+0.05, j+0.02, '({}, {})'.format(i, j))
    plt.xlabel('Number of Arrays')
    plt.ylabel('Mass of system (unit: g)')
    plt.show()

    
if __name__ == '__main__':
    mass()
    