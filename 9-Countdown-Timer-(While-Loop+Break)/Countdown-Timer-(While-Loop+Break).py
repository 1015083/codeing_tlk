# Program Name: countdown_timer.py
# Purpose: Countdown from 10 to 1, allowing the user to stop it
# Creator: Nehayesh Sayedzada
# Date: 2025-03-13

# Initialize countdown
count = 10

# Loop until count reaches 0
while count > 0:
    print(count)
    user_input = input('Enter "stop" to cancel or press Enter to continue: ')
    if user_input.lower() == "stop":
        print("Countdown stopped!")
        break
    count -= 1

# If the countdown reaches 0 without being stopped
if count == 0:
    print("Countdown finished!")
