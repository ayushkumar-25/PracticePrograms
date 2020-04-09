import math

A = float(input("Enter the lenght of A: "))
B = float(input("Enter the lenght of B: "))

C = math.sqrt(A**2 + B**2)
reqAngle = (math.acos(math.radians((A**2+B**2-C**2)/(2*A*B)))) /2
print(reqAngle)





#angle1 = math.acos(math.radians(A/h))
#angle2 = math.acos(math.radians(B/h))
#angle3 = ((math.radians(180))-(angle1 + angle2))/2

#print(angle1)
#print(angle2)
#print(math.degrees(angle3))

