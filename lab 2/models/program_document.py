from models.document import Document

class ProgramDocument(Document):
    def info(self):
        return super().info() + "Lines: 100, Classes: 3, Methods: 10\n"