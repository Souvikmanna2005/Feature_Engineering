from PIL import Image

image = Image.open(r"C:\Users\SOUVIK MANNA\Downloads\virat.jpg")

flipped_horizontally = image.transpose(Image.FLIP_LEFT_RIGHT)

flipped_horizontally.save('virat.jpg')

image.show()
flipped_horizontally.show()