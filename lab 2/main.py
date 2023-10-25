import os
import datetime
from models.image_document import ImageDocument
from models.program_document import ProgramDocument
from models.text_document import TextDocument


class FolderMonitor:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.documents = self.load_documents()
        self.last_snapshot_time = None

    def load_documents(self):
        docs = []
        for filename in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, filename)
            if os.path.isfile(file_path):
                ext = os.path.splitext(filename)[1]
                if ext in ['.txt']:
                    docs.append(TextDocument(file_path))
                elif ext in ['.png', '.jpg', 'jpeg']:
                    docs.append(ImageDocument(file_path))
                elif ext in ['.py', '.java']:
                    docs.append(ProgramDocument(file_path))
        return docs

    def commit(self):
        for doc in self.documents:
            doc.commit()
        self.last_snapshot_time = datetime.datetime.now()

    def status(self):
        print(f"\nCreated Snapshot at: {self.last_snapshot_time}") if self.last_snapshot_time else print("\nNo snapshots taken yet.")
        for doc in self.documents:
            status = 'Changed' if doc.has_changed() else 'No Change'
            name = doc.filename.split('\\')[-1]
            print(f"{name} - {status}")
        print('')

    def info(self, filename):
        for doc in self.documents:
            if doc.filename.split('\\')[-1] == filename:
                print(doc.info())
                break

    def start(self):
        command = ''
        while command != 'quit':
            command = input("Enter a command (commit, status, info <filename>, quit): ")
            if command == 'commit':
                self.commit()
            elif command == 'status':
                self.status()
            elif command.startswith('info'):
                filename = command.split()[1]
                self.info(filename)
            elif command != 'quit':
                print('Invalid command!')


if __name__ == '__main__':
    monitor = FolderMonitor(r"C:\Users\PС\Desktop\oop\lab 2\files")
    monitor.start()
