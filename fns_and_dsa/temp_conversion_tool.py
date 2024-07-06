FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32 
    return fahrenheit 

def calculate_temperature():
    temperature = input("Enter the temperature to convert:")
    try:
        int_temperature = int(temperature)
        is_integer = True 
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return 
    type = input("Is this temperature in Celsius or Fahrenheit? (C/F):").strip().lower()
    if type == "c":
        #convert celsius to fahrenheit
        result = convert_to_fahrenheit(int_temperature)
        print(f"{int_temperature}°C is {result}°F")
    elif type == "f":
        #convert fahrenheit to celsius
        result = convert_to_celsius(int_temperature)
        print(f"{int_temperature}°F is {result}°C")
    else:
        print("Enter a valid type C or F")

calculate_temperature()