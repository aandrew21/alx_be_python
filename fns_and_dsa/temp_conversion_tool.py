# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """
    Main function to prompt user input and perform temperature conversion.
    """
    try:
        # Get temperature from user
        temperature_input = input("Enter the temperature to convert: ")
        
        # Ensure input is numeric
        if not temperature_input.replace('.', '', 1).isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        temperature = float(temperature_input)

        # Get the temperature unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == 'F':
            # Convert from Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature:.1f}\u00b0F is {converted_temp:.2f}\u00b0C")
        elif unit == 'C':
            # Convert from Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature:.1f}\u00b0C is {converted_temp:.2f}\u00b0F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
