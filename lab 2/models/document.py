import os
from datetime import datetime

class Document:
    def __init__(self, filename):
        self.filename = filename
        self.extension = os.path.splitext(filename)[1]
        self.created_at = datetime.fromtimestamp(os.path.getctime(filename))
        self.updated_at = datetime.fromtimestamp(os.path.getmtime(filename))

    def info(self):
        return (f'''
Filename: {self.filename}
Extension: {self.extension}
Created time: {self.created_at}
Updated time: {self.updated_at}
''')
