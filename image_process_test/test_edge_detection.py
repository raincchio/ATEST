from PIL import Image, ImageFilter

img = Image.open(r"C:\Users\chenxing\Desktop\2019561005.jpg")

# Converting the image to grayscale, as Sobel Operator requires
# input image to be of mode Grayscale (L)
img = img.convert("L")

# Calculating Edges using the passed laplican Kernel
final = img.filter(ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 8,
                                               -1, -1, -1, -1), 1, 0))
final.show()
# final.save("EDGE_sample.png")