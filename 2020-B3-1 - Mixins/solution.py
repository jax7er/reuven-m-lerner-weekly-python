import csv
import json
import pickle as pkl
import xml.etree.ElementTree as ET


class Serializable:
    def dump(self, file_name: str):
        with open(file_name, "wb") as file:
            pkl.dump(vars(self), file)

    def load(self, file_name: str):
        with open(file_name, "rb") as file:
            vars(self).update(pkl.load(file))


class JSONMixin:
    def dump(self, file_name: str):
        with open(file_name, "w") as file:
            json.dump(vars(self), file)

    def load(self, file_name: str):
        with open(file_name) as file:
            vars(self).update(json.load(file))


class XMLMixin:
    def dump(self, file_name: str):
        tree = ET.Element(
            "root", 
            {attr: str(val) for attr, val in vars(self).items()}
        )

        with open(file_name, "wb") as file:
            file.write(ET.tostring(tree))

    def load(self, file_name: str):
        with open(file_name, "rb") as file:
            tree = ET.parse(file)

        for attr, value in tree.getroot().attrib.items():
            for T in (int, float, str):
                try:
                    setattr(self, attr, T(value))
                    break
                except ValueError:
                    pass


class CSVMixin:
    def dump(self, file_name: str):
        self_dict = vars(self)
        
        with open(file_name, "w") as file:
            writer = csv.writer(file, lineterminator="\n")
            writer.writerow(self_dict.keys())
            writer.writerow(self_dict.values())

    def load(self, file_name: str):
        with open(file_name) as file:
            reader = csv.reader(file)
            attrs = next(reader)
            values = next(reader)

            for attr, value in zip(attrs, values):
                setattr(self, attr, value)


# class Book(CSVMixin, Serializable):
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price

# b = Book("Practice Makes Python", "Reuven Lerner", 39)
# b.dump('book.csv')      # book is now stored on disk, in CSV format

# b2 = Book('blah title', 'blah author', 100)
# b2.load('book.csv')     # title, author, and price now reflect disk file