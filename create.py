import pyqrcode
qr = pyqrcode.create('Unladden swallow')
qr.png('img.png', scale=10, background=(0xff, 0xff, 0xff, 00))