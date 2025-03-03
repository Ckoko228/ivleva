
import json
import xml.etree.ElementTree as ET

def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    return tree.getroot()

def xml_to_dict(element):
    return {child.tag: xml_to_dict(child) for child in element} if element else element.text

def save_json(data, json_file):
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def xml_to_json(xml_file, json_file):
    try:
        root = parse_xml(xml_file)
        data = {root.tag: xml_to_dict(root)}
        save_json(data, json_file)
        print(f"JSON-файл '{json_file}' создан.")
    except Exception as e:
        print(f"Ошибка: {e}")


xml_to_json("231.xml", "1234.json")

