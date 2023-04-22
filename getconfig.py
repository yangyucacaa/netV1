import requests
import json

# Convert keys to snake_case
def snake_case(key):
    return ''.join(['_'+i.lower() if i.isupper() else i for i in key]).lstrip('_')

# Recursively convert keys to snake_case
def convert_keys_to_snake_case(data):
    if isinstance(data, dict):
        new_data = {}
        for key, value in data.items():
            new_key = snake_case(key)
            new_value = convert_keys_to_snake_case(value)
            new_data[new_key] = new_value
        return new_data
    elif isinstance(data, list):
        return [convert_keys_to_snake_case(item) for item in data]
    else:
        return data

# 访问a.com并获取JSON数据
response = requests.get('https://a.com')
json_data = response.json()

# 修改JSON数据
modified_json_data = convert_keys_to_snake_case(json_data)

# 输出修改后的JSON数据
print(json.dumps(modified_json_data, ensure_ascii=False, indent=2))

# 输出修改后的JSON数据到文件
with open('data.json', 'w') as f:
    json.dump(modified_json_data, f, ensure_ascii=False, indent=2)
