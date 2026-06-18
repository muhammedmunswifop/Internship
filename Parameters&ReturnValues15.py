"""15.Write a function that accepts a temperature in Celsius and returns Fahrenheit."""
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

tempc = float(input("Enter temperature in Celsius: "))
tempf = celsius_to_fahrenheit(tempc)

print("Temperature in Fahrenheit:", tempf)