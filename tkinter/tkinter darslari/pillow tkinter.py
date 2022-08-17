"""Pillow bu pythonda rasimlar bilan ishlash
pip install pillow"""


from PIL import Image

im = Image.open("photo.jpg")
print(im)
im.show()