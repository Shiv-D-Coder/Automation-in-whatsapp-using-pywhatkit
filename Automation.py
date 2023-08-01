import time
import pywhatkit as pw

def MSG():
    recipient_number = "+91769xxxxxxx"  # Replace with the recipient's phone number in international format
    message = "Bruhhhhhhhhhh, WE GO GYM"

    while True:
        pw.sendwhatmsg(recipient_number, message, int(time.strftime("%H")), int(time.strftime("%M")) + 2)
        time.sleep(6)  # Wait for 10 seconds before sending the next message


if __name__ == "__main__":
    MSG()