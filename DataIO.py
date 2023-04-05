import datetime
import os
import xml
import xml.etree.ElementTree as ET
import time

PATH = r".\Notes.xml"


def __check_xml_exist():
    if not os.path.exists(PATH):
        try:
            with open(PATH, 'x') as f:
                pass
        except FileExistsError:
            pass


def write_to_file(header, string_to_append):

    __check_xml_exist()

    try:
        tree = ET.parse(PATH)
    except xml.etree.ElementTree.ParseError:
        new_root = ET.Element("root")
        new_tree = ET.ElementTree(new_root)
        new_tree.write(PATH)
        tree = ET.parse(PATH)

    root = tree.getroot()

    new_note = ET.Element('note')
    new_note.set('time', str(datetime.datetime.now().strftime("%d.%m.%Y %H:%M")))
    new_note.set('id', str(len(root) + 1))
    new_note.set('header', str(header))
    new_note.text = string_to_append

    root.append(new_note)

    tree.write(PATH, encoding='UTF-8', xml_declaration=True)
