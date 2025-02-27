import requests

# There is a simple sql server that takes in heartrates and can be gotten at 
# https://atown.pythonanywhere.com/get_all_heartrates or /get_single_heartrate
URL = "https://atown.pythonanywhere.com/add_heartrate"

"""
This is a script to take in input such as "85" + Enter in the command line and then
send it to an sql server.
When code from hb-monitor presses keyboard keys, it is meant to be inputted in here
to be sent to URL.

This code from hb-monitor:
#try to send bpm to pc as a keyboard
#layout.write(str(average_bpm)", delay=.05)
#kbd.press(Keycode.ENTER)
#kbd.release_all()

This should also work in a spreadsheet (types number and then presses ENTER key)

When using this it might be smarter to get averages for longer periods of time,
so they are more accurate and send less requests to the server.
"""
while True:
    try:
        heart_rate = input("Waiting for heart rate: ").strip()

        # Check if input is valid (only numbers)
        if not heart_rate.isdigit():
            print("Invalid input. Please enter a number.")
            continue  # Skip to the next loop iteration

        # Convert to integer
        heart_rate = int(heart_rate)
        
        # Send a POST request with the heart rate
        response = requests.post(URL, data={"heartrate": heart_rate})

        print(f"Sent heart rate: {heart_rate} | Server response: {response.status_code}")

    except KeyboardInterrupt:
        print("\nIssue")
        break