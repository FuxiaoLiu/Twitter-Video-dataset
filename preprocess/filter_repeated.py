import os
from tqdm import tqdm
import json


file_dir = './dataset_summary/'

files = os.listdir(file_dir)

url_list = []
result = []
result1 = []
result2= []


#After data_2_json.py, this file helps filter out the repeated samples.
i = 0
for file in tqdm(files):
    if 'v1' in file:
    #if 'v2' in file:
        tmp = './dataset_summary/' + file
        with open(tmp, 'r') as f:
            datas = json.load(f)

        for data in datas:
            video_url = data['video_url']
            caption = data['caption'][-3:]

            if (video_url in url_list) and (caption in result1):
                result2.append(video_url)
                continue
            #if video_url not in url_list:
            url_list.append(video_url)
            result1.append(caption)
            result.append(data)

print(len(url_list), len(result))

with open('./dataset_summary/Twitter_dataset_summary_v1.json', 'w') as f:
    json.dump(result, f)
