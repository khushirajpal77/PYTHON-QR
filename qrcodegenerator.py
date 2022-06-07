from matplotlib.pyplot import fill
import qrcode
import image

qr=qrcode.QRCode(
    version=15, #higher the number higher complicated image
    box_size=10, #size of the box
    border=5 #white part of image--border in all four sides with white color
)

data="Heya, Khushi this side."

qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("qrcode.png")