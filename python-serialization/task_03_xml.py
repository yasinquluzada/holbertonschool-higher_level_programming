import xml.etree.ElementTree as ET


def _python_value_to_type_and_text(value):
    if value is None:
        return "none", ""
    if isinstance(value, bool):
        return "bool", "true" if value else "false"
    if isinstance(value, int) and not isinstance(value, bool):
        return "int", str(value)
    if isinstance(value, float):
        return "float", repr(value)
    return "str", str(value)


def _type_and_text_to_python_value(value_type, text):
    if value_type == "none":
        return None
    if value_type == "bool":
        return str(text).strip().lower() == "true"
    if value_type == "int":
        return int(str(text).strip())
    if value_type == "float":
        return float(str(text).strip())
    return "" if text is None else str(text)


def serialize_to_xml(dictionary, filename):
    if not isinstance(dictionary, dict):
        raise TypeError("dictionary must be a dict")
    root = ET.Element("data")
    for key, value in dictionary.items():
        if not isinstance(key, str):
            raise TypeError("dictionary keys must be strings")
        child = ET.SubElement(root, key)
        value_type, value_text = _python_value_to_type_and_text(value)
        child.set("type", value_type)
        child.text = value_text
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=False)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for child in list(root):
        value_type = child.get("type", "str")
        result[child.tag] = _type_and_text_to_python_value(value_type, child.text)
    return result
