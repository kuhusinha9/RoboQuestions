from steps import translate
from file_handling import get

book= "regelsVanFloor"
doc="Script"
text = get(doc, book)
print(translate(text,"English"))