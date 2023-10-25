import os
import datetime

class Document:
    def __init__(self, filename):
        self.filename = filename
        self.extension = os.path.splitext(filename)[1]
        self.created_at = datetime.datetime.now()
        self.updated_at = None
        self.snapshot_time = None

    def info(self):
        return (f'''
Filename: {self.filename}
Extension: {self.extension}
Created time: {self.created_at}
Updated time: {self.updated_at}
''')

    def has_changed(self):
        last_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(self.filename))
        
        if not self.snapshot_time or last_modified_time > self.snapshot_time:
            self.updated_at = last_modified_time
            return True
        return False


    def commit(self):
        self.snapshot_time = datetime.datetime.now()