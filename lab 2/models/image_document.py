from models.document import Document
from PIL import Image

class ImageDocument(Document):
    def get_image_dimensions(self):
        with Image.open(self.filename) as img:
            return img.width, img.height
        
    def info(self):
        width, height = self.get_image_dimensions()
        return super().info() + f"Dimensions: {width}x{height}\n"