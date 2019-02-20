import json

json_dict = {"one": "1", "two": "2", "three": "3"}
for k, v in json_dict.items():
    print(k, v)

# json str --> dict
# json decode
json_dump = json.dumps(json_dict)
json_dict = json.loads(json_dump)
print("json_dump type %s: " % type(json_dump), json_dump)
print("json_dict type %s: " % type(json_dict), json_dict)


info_dict = {
"translateResult":[[{"tgt":"你好","src":"hello"}]],
"errorCode": 0, 
"type": "en2zh-CHS",
"smartResult":{
    "entries": ["","n. 表示问候, 惊奇或唤起注意时的用语\r\n", "int. 喂; 哈罗\r\n", "n. (Hello)人名; (法)埃洛\r\n"],
    "type": 1
    }
}

json_encoder = json.JSONEncoder(ensure_ascii=False)
info_json = json_encoder.encode(info_dict["smartResult"])
print(info_json)
