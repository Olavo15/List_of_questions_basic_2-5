"""
Leia um ângulo em graus e apresente-o convertido em radianos,π=3.14
"""
import math
g = float(input())

pi = math.pi

r= (g * pi)/180

print(f"{r:.2f} radianos")