import xml.etree.ElementTree as et
import os

file_path = os.path.join("ddbb", "animes.xml")
root = et.parse(source=file_path)
main_element = root.getroot()

print(main_element)
