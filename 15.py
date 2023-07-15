"""
Leia um ângulo em radianos e apresente-o convertido em graus.π=3.14
"""
import math

r = float(input())

pi = math.pi

g = r * 180 / pi

print(f'{g:.2f} graus')