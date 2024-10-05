#conversion variables
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

#conversion functions
def convert_to_celsius(fahrenheit):
    return(fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return(celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

#User interaction 
def main():
    temperature = input("Enter the temperature to convert: ")
    try:
        temperature = float(temperature)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    
    #create an input using the variable unit
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    while unit not in ['C','F']:
        unit = input("Invalid unit. Please enter C for celcius or F for fahrenheit: ").strip().upper()

    #conversion
    if unit == 'F':
        converted_temperature = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temperature}°C")
    elif unit == 'C':
        converted_temperature = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temperature}°F")
    
if __name__ == "__main__":
    main()