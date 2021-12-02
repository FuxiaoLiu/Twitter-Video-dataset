import os
from tqdm import tqdm
import json
import pandas as pd


#Given the downloaded data from Twitter in ./dataset/, This file is use to filer out the samples without videos and audios. The output file is json.

file33 = os.getcwd()
filename222 = 'work_from_home'
#file_dir = file33 + '/dataset/#booster/'

file_dir = file33 + '/dataset/' + filename222 +'/'
#file_dir = './dataset/#booster/'
files = os.listdir(file_dir)
print(len(files))

i = 0
j = 0
k = 0
result1 = []
result2 = []
result3 = []
o = 0
for file in tqdm(files):
    path = file_dir + file + '/media/'
    try:
        paths1 = os.listdir(path)
    except:
        continue
    for path1 in paths1:
        if 'mp3' in path1:

            #mp3_path
            mp3_path = path + path1
            mp4_path = mp3_path[:-1]
            mp4_path = mp4_path + '4'


            #caption
            tmp_path = file_dir + file + '/' + file + '.json'
            with open(tmp_path, 'r') as f:
                data_tmp = json.load(f)
            text = data_tmp['tweet_text']
            url = data_tmp['tweet_url']
            video_url = data_tmp['tweet_video_url']

            #transcription
            try:
                tmp1_path = file_dir + file + '/analysis/' + file + '_transcription.txt'
                f = open(tmp1_path, "r", encoding="utf-8")
                lines = f.read()
                transcription = lines
            except:
                transcription = ''

            keyframe_path = file_dir + file + '/analysis/keyframes/'

            tmp1 = file_dir + file
            result1.append({'keyword': filename222, 'sample_path': tmp1, 'twitter_url': url, 'video_url': video_url, 'keyframe_path': keyframe_path, 'mp4_path': mp4_path, 'mp3_path': mp3_path, 'caption': text, 'transcription': transcription})


        if 'mp4' in path1:

            mp4_path = path + path1

            #caption
            tmp_path = file_dir + file + '/' + file + '.json'
            with open(tmp_path, 'r') as f:
                data_tmp = json.load(f)
            text = data_tmp['tweet_text']
            url = data_tmp['tweet_url']
            video_url = data_tmp['tweet_video_url']

            #transcription
            try:
                tmp1_path = file_dir + file + '/analysis/' + file + '_transcription.txt'
                f = open(tmp1_path, "r", encoding="utf-8")
                lines = f.read()
                transcription = lines
            except:
                transcription = ''

            keyframe_path = file_dir + file + '/analysis/keyframes/'

            tmp1 = file_dir + file
            result2.append({'keyword': filename222, 'sample_path': tmp1, 'twitter_url': url, 'video_url': video_url, 'keyframe_path': keyframe_path, 'mp4_path': mp4_path, 'mp3_path': '', 'caption': text, 'transcription': transcription})


print(len(result1))
print(len(result2))
output_file1 = './dataset_summary/' + filename222 + '_v2.json'
output_file2 = './dataset_summary/' + filename222 + '_v1.json'


with open(output_file1, 'w') as f:
    json.dump(result1, f)

with open(output_file2, 'w') as f:
    json.dump(result2, f)
