import datetime
import os
import xml
import xml.etree.ElementTree as ET
import re

PATH = os.path.abspath(os.curdir) + r"\Notes.xml"


def __check_xml_exist():
    if not os.path.exists(PATH):
        try:
            with open(PATH, 'x') as f:
                pass
        except FileExistsError:
            pass


def write_to_file(note_data):
    __check_xml_exist()

    if note_data[0] is None:  # if we want to add a new note id is None
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
        new_note.set('header', str(note_data[1]))
        new_note.text = note_data[2]

        root.append(new_note)
    else:                     # if we want to edit existing note
        tree = ET.parse(PATH)
        root = tree.getroot()
        note = root.find(f".//note[@id='{note_data[0]}']")
        note.set("header", note_data[1])
        note.text = note_data[2]

    tree.write(PATH, encoding='UTF-8', xml_declaration=True)


def read_xml_file():
    __check_xml_exist()

    try:
        tree = ET.parse(PATH)
        root = tree.getroot()
        return root
    except xml.etree.ElementTree.ParseError:
        pass


def delete_from_file(id_note):
    __check_xml_exist()

    tree = ET.parse(PATH)
    root = tree.getroot()
    note = root.find(f".//note[@id='{id_note}']")
    root.remove(note)
    tree.write(PATH)


def get_note(id_note):

    tree = ET.parse(PATH)
    root = tree.getroot()
    note = root.find(f".//note[@id='{id_note}']")
    return note.get("header"), note.text


def search_note(query):
    if query is None:
        return []
    tree = ET.parse(PATH)
    root = tree.getroot()
    pattern = re.compile(query, flags=re.IGNORECASE)
    results = []
    for note in root.findall('note'):
        content = note.text
        if content and pattern.search(content):
            results.append(note)
    return results

