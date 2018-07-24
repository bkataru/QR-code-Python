import pyqrcode
qr = pyqrcode.create('Unladden swallow')
qr.png('img.png', scale=10)