import json
import xml.etree.ElementTree as ET

def xml_to_json(xml_file, json_file):
    try:
        root = ET.parse(xml_file).getroot()
        
        data = {root.tag: [child.text for child in root]}
        
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"JSON файл '{json_file}' успешно создан.")

    except Exception as e:
        print(f"Ошибка при обработке файла: {e}")

xml_to_json("231.xml", "filename.json")
