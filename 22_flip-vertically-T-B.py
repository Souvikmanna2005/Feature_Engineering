from PIL import Image

image = Image.open(r"C:\Users\SOUVIK MANNA\Downloads\virat1.jpg")

flipped_vertically = image.transpose(Image.FLIP_TOP_BOTTOM)

flipped_vertically.save('virat1.jpg')

image.show()
flipped_vertically.show()