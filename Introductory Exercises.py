# problem 1
 


def arithmetic(a, b):
    add = a + b
    sub = a - b
    multi = a * b
    division = a / b
    modulus = a % b

    return add, sub, multi, division, modulus




def conversion(num, unit, target_unit):
    # conversion factors for various units
    if unit == "feet":
        factor = 0.3048
    elif unit == "miles":
        factor = 1609.34
    elif unit == "inches":
        factor = 0.0254
    

    converted_num = num * factor

    return f"{num} {unit} is equal to {converted_num} {target_unit}"





def calculate_earthquake_impact(magnitude):
    # formula to calculate impact based on magnitude
    impact = 10**(1.5*magnitude - 5.75)

    return f"The potential impact of the earthquake is {impact}"





import math

def calculate_wind_factor(wind_speed, temperature):
    # formula to calculate wind chill factor
    factor = 35.74 + 0.6215*temperature - 35.75*math.pow(wind_speed, 0.16) + 0.4275*temperature*math.pow(wind_speed, 0.16)

    return f"The wind chill factor is {factor} degrees Fahrenheit."