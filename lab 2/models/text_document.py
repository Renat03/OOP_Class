from models.document import Document

class TextDocument(Document):
    def info(self):
        with open(self.filename, 'r') as file:
            content = file.read()
            line_count = len(content.splitlines())
            word_count = len(content.split())
            char_count = len(content)
        return (super().info() + 
                f"Lines: {line_count}, Words: {word_count}, Characters: {char_count}\n")