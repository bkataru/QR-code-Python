from PIL import Image
img = Image.open('test1.jpeg', 'r')
img_w, img_h = img.size

background = Image.open('test2.png', 'r')
bg_w, bg_h = background.size

offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
background.paste(img, offset)
background.save('out.png')