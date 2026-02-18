import numpy as np
from math import acos, degrees

print("welcome to the vector calculator")
x=np.array([int(input("x1: ")), int(input("x2: "))])
y=np.array([int(input("y1: ")), int(input("y2: "))])
s=np.dot(x,y)
lenx=np.linalg.norm(x)
leny=np.linalg.norm(y)
print(f"your vectors: x={x}, y={y}")
print(f"sum= {x+y}")
print(f"subtraction= {x-y}")
print(f"scalar multiplication= {s}")
print(f"lengths: len(x)= {lenx}; len(y)={leny}")
if lenx==0 or leny==0:
    print("angle undefined for zero vector")
else:
    cos_value = s / (lenx * leny)
    cos_value = max(min(cos_value, 1), -1)
    angle = acos(cos_value)
    print(f"angle between them= {degrees(angle)} degrees")