from PIL import Image

image_path = "./FWVKStCVUAAPTjS.png"
with Image.open(image_path) as im:
    im.show()