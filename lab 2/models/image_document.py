from models.document import Document

class ImageDocument(Document):
    def info(self):
        return super().info() + "Dimensions: 512x512\n"