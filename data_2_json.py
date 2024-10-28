import json
import base64
import xml.etree.ElementTree as ET
import csv
import io

def detect_data_type(data):
    if isinstance(data, str):
        if data.startswith('data:image'):
            return 'image'
        elif data.startswith('data:video'):
            return 'video'
        elif data.startswith('data:audio'):
            return 'sound'
        else:
            return 'text'
    elif isinstance(data, dict):
        return 'json'
    elif isinstance(data, list):
        return 'json'
    elif isinstance(data, ET.Element):
        return 'xml'
    elif isinstance(data, io.StringIO):
        return 'csv'
    else:
        raise ValueError("Unsupported data type")

def parse_text(data):
    return {"text": data}

def parse_image(data):
    if data.startswith('data:image'):
        data = data.split(',')[1]
    return {"image": data}

def parse_video(data):
    if data.startswith('data:video'):
        data = data.split(',')[1]
    return {"video": data}

def parse_sound(data):
    if data.startswith('data:audio'):
        data = data.split(',')[1]
    return {"sound": data}

def parse_json(data):
    return data

def parse_xml(data):
    root = ET.fromstring(data)
    return {root.tag: {child.tag: child.text for child in root}}

def parse_csv(data):
    reader = csv.DictReader(data)
    return [row for row in reader]

def convert_to_structured_json(data):
    data_type = detect_data_type(data)
    
    if data_type == 'text':
        return parse_text(data)
    elif data_type == 'image':
        return parse_image(data)
    elif data_type == 'video':
        return parse_video(data)
    elif data_type == 'sound':
        return parse_sound(data)
    elif data_type == 'json':
        return parse_json(data)
    elif data_type == 'xml':
        return parse_xml(data)
    elif data_type == 'csv':
        return parse_csv(data)
    else:
        raise ValueError("Unsupported data type")

# Example usage
if __name__ == "__main__":
    # Text
    text_data = "Hello, World!"
    structured_json_text = convert_to_structured_json(text_data)
    print(f"Structured JSON (Text): {json.dumps(structured_json_text, indent=2)}")

    # Image (Base64 encoded)
    image_data = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA..."
    structured_json_image = convert_to_structured_json(image_data)
    print(f"Structured JSON (Image): {json.dumps(structured_json_image, indent=2)}")

    # Video (Base64 encoded)
    video_data = "data:video/mp4;base64,AAAAIGZ0eXBtcDQyAAAAAG1wNDJpc29tYXZj..."
    structured_json_video = convert_to_structured_json(video_data)
    print(f"Structured JSON (Video): {json.dumps(structured_json_video, indent=2)}")

    # Sound (Base64 encoded)
    sound_data = "data:audio/mpeg;base64,AAAAIGZ0eXBtcDQyAAAAAG1wNDJpc29tYXZj..."
    structured_json_sound = convert_to_structured_json(sound_data)
    print(f"Structured JSON (Sound): {json.dumps(structured_json_sound, indent=2)}")

    # JSON
    json_data = {"name": "John", "age": 30, "city": "New York"}
    structured_json_json = convert_to_structured_json(json_data)
    print(f"Structured JSON (JSON): {json.dumps(structured_json_json, indent=2)}")

    # XML
    xml_data = "<root><name>John</name><age>30</age><city>New York</city></root>"
    structured_json_xml = convert_to_structured_json(xml_data)
    print(f"Structured JSON (XML): {json.dumps(structured_json_xml, indent=2)}")

    # CSV
    csv_data = io.StringIO("name,age,city\nJohn,30,New York\nJane,25,Los Angeles")
    structured_json_csv = convert_to_structured_json(csv_data)
    print(f"Structured JSON (CSV): {json.dumps(structured_json_csv, indent=2)}")
