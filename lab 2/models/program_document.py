from models.document import Document

class ProgramDocument(Document):
    def read_content(self):
        with open(self.filename, 'r') as f:
            return f.readlines()
        
    def count_lines(self):
        return len(self.read_content())

    def count_classes(self):
        count = 0
        for line in self.read_content():
            line = line.strip()
            if line.startswith('class ') or line.startswith('public class'):
                count += 1
        return count

    def count_methods(self):
        count = 0
        for line in self.read_content():
            line = line.strip()
            if line.startswith('def '):
                count += 1
            elif line.startswith('public ') or line.startswith('private ') or line.startswith('protected '):
                if '(' in line and ')' in line:
                    count += 1
        return count

    def info(self):
        return (super().info() +  f"Lines: {self.count_lines()}, Classes: {self.count_classes()}, Methods: {self.count_methods()}\n")
