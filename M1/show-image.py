from PIL import Image

image_path = "C:/Users/fatha/Downloads/FWVKStCVUAAPTjS.png"
with Image.open(image_path) as im:
    im.show()