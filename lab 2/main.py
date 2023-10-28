import os
import datetime
from models.image_document import ImageDocument
from models.program_document import ProgramDocument
from models.text_document import TextDocument


class FolderMonitor:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.documents = self.load_documents()
        self.committed_documents = self.documents.copy()
        self.last_snapshot_time = None

    def load_documents(self):
        docs = []
        for filename in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, filename)
            if os.path.isfile(file_path):
                ext = os.path.splitext(filename)[1]
                if ext in ['.txt']:
                    docs.append(TextDocument(file_path))
                elif ext in ['.png', '.jpg', '.jpeg']:
                    docs.append(ImageDocument(file_path))
                elif ext in ['.py', '.java']:
                    docs.append(ProgramDocument(file_path))
        return docs

    def commit(self):
        self.last_snapshot_time = datetime.datetime.now()
        self.committed_documents = self.documents.copy()

    def status(self):
        current_files = set(os.listdir(self.folder_path))
        last_snapshot_files = {doc.filename.split('\\')[-1] for doc in self.committed_documents}

        added_files = set(current_files - last_snapshot_files)
        removed_files = set(last_snapshot_files - current_files)

        if added_files:
            for filename in added_files:
                file_path = os.path.join(self.folder_path, filename)
                ext = os.path.splitext(filename)[1]
                if ext in ['.txt']:
                    self.documents.append(TextDocument(file_path))
                elif ext in ['.png', '.jpg', '.jpeg']:
                    self.documents.append(ImageDocument(file_path))
                elif ext in ['.py', '.java']:
                    self.documents.append(ProgramDocument(file_path))

        if removed_files:
            self.documents = [doc for doc in self.documents if doc.filename.split('\\')[-1] not in removed_files]

        print(f"\nCreated Snapshot at: {self.last_snapshot_time}") if self.last_snapshot_time else print("\nNo snapshots taken yet.")

        for name in added_files:
            print(f"{name} - Added")
        for name in removed_files:
            print(f"{name} - Removed")
        for doc in self.documents:
            name = doc.filename.split('\\')[-1]
            if name not in added_files:
                current_updated_at = datetime.datetime.fromtimestamp(os.path.getmtime(doc.filename))
                status = 'Changed' if current_updated_at > doc.updated_at else 'No Change'
                doc.updated_at = current_updated_at
                print(f"{name} - {status}")
        print('')

    def info(self, filename):
        for doc in self.documents:
            if doc.filename.split('\\')[-1] == filename:
                doc.updated_at = datetime.datetime.fromtimestamp(os.path.getmtime(doc.filename))
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

