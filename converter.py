print("Welcome to AJ's Temperature Converter!")
convert = input("What would you like to convert: C to F or F to C - ")

while True:
    if convert in ('C to F', 'F to C'):
        if convert == 'C to F':
            C = float(input("Enter your tempertature in Celcius: "))
            temp_switch_1 = (C * 9/5) + 32
            print("Fahrenheit converted from", C, "degrees Celcius equals", temp_switch_1, "degrees Fahrenheit")
        if convert == 'F to C':
            F = float(input("Enter your tempertature in Fahrenheit: "))
            temp_switch_2 = (F - 32) * 5/9
            print("Celcius converted from", F, "degrees Fahrenheit equals", temp_switch_2, "degrees Celcius")
        
        next_conversion = input("Let's do another conversion? (yes/no): ")
        if next_conversion == 'yes':
            continue
        if next_conversion == 'no':
            print("Goodbye!")
            break

    else:
        print("Invalid Input")