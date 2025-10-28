#1. Use map() para converter Celsius →
#Fahrenheit

celsius = [0, 10, 20, 30, 40]

fahrenheit = list(map(lambda c: (c * 1.8) + 32, celsius))

print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)
