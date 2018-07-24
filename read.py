from pyzbar.pyzbar import decode
from PIL import Image
result = decode(Image.open('img.png'))
print(result[0].data)