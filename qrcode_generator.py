# install all the lib needed
# create a function that collect a text and convert it to a qr code
# save qr as image
# run the function

import qrcode
import qrcode.constants

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg001.png")


url = input("Enter your url: ")
generate_qrcode(url)    
