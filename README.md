# Automation-in-whatsapp-using-pywhatkit

This is a Python script that sends a gym reminder message to a recipient's phone number using the pywhatkit library. The script is designed to run indefinitely, sending the message every 6 seconds with a 2-minute delay after each message.

Requirements
Before running the script, you need to have the following installed:

Python 3.x
pywhatkit library (you can install it using pip install pywhatkit)
How to Use
Install the required libraries (if not already installed) by running the following command:

pip install pywhatkit
Replace the placeholder recipient_number with the recipient's phone number in international format (e.g., "+91769xxxxxxx").

Customize the message to your liking by modifying the message variable.

Run the script using the following command:

python script_name.py
Important Note
Make sure to provide the correct recipient's phone number and use this script responsibly and with the recipient's consent.

The script will continue to run indefinitely until manually stopped by the user. To stop the script, you can press CTRL + C in the terminal.

The script sends the message every 6 seconds to the recipient's phone number. Adjust the time.sleep(6) value if you want to change the interval between messages.
