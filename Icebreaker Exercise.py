# problem 1
a=float(input("Enter wavelength (in nm): "))

if  a < 380 or a > 750:
    print("Error: wavelength is outside of visible spectrum")
elif a < 450:
    print("Violet")
elif a < 495:
    print(" Blue")
elif a < 570:
    print("Green")
elif a < 590:
    print("Yellow")
elif a < 620:
    print("Orange")
else:
    print(" Red")

#problem 2 


#taking a=frequency
a= float(input("Enter frequency : "))

if a< (3*(10**9)):
    print(" Radio Waves")
elif a < 3*10**12:
    print("Microwaves")
elif a < 4.3*10**14:
    print(" Infrared Light")
elif a < 7.5*10**14:
    print(" Visible Light")
elif a < 3*10**17:
    print("Ultraviolet Light")
elif a <  3*10**19:
    print(" X-Rays")
else:
    print("Gamma Rays")