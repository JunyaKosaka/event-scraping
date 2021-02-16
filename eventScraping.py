import json
import requests

datas = []

url = 'https://eventon.jp/api/events.json'
response = requests.get(url)
response.raise_for_status()

event_data = json.loads(response.text)

for e in event_data['events']:
    event_data_dict = {}
    # print(event_data['events'])
    event_data_dict["title"] = e['title']
    event_data_dict["startAt"] = e['started_at']
    event_data_dict["endAt"] = e['ended_at']
    event_data_dict["address"] = e['address']
    event_data_dict["imageUrl"] = e['image_path']
    
    datas.append(event_data_dict)

datas = sorted(datas, key=lambda d: d['startAt'])
print(datas)