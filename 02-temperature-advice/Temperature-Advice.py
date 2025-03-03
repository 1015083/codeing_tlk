# Prompt the user to enter the current temperature in Celsius
temperature = int(input("Enter the temperature in Celsius: "))

#if the temperature is 10: 'print it's cold outside == wear a jacket'

if temperature < 10:
    print("it is cold outside 🥶🧊= Wear a jacket!")

#if temperature is more than 10 degree : 'print it is a nice weather'

elif 10 <= temperature <= 25:
    print("It's a nice day. Wear short-sleeves!")

#if the temperature is more than 25: 'print it's hot outside 😰'
else:
    print("It's hot outside. Stay cool!")
