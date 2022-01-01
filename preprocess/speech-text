
import os
from tqdm import tqdm
import json
import pandas as pd
'''
#yaser's dataset
file_dir = './dataset/yaser/'
files = os.listdir(file_dir)
print(len(files))

i = 0
for file in tqdm(files):
    path = file_dir + file + '/'
    paths1 = os.listdir(path)
    for path1 in paths1:
        if 'mp3' in path1:
            i += 1
print(i)
'''

'''
file33 = os.getcwd()
file_dir = file33 + '/dataset/#booster/'
files = os.listdir(file_dir)

i = 0
j = 0
result = []

for file in tqdm(files):
    path = file_dir + file + '/media/'
    try:
        paths1 = os.listdir(path)
    except:
        continue
    for path1 in paths1:
        if 'mp3' in path1:
            i += 1
            result.append(file)
        if 'mp4' in path1:
            j += 1

print(i, j)
print(result)

'''

'''
tmp_path1 = './dataset_reply/vaccine_v0.json'
with open(tmp_path1, 'r') as f:
    data_replys = json.load(f)


tmp_pat2 = './dataset_reply/vaccine_v1.json'
with open(tmp_pat2, 'r') as f:
    datas = json.load(f)

i = 0
result1 = []

for data in tqdm(datas):
    result1.append(data['id'])

for data in tqdm(data_replys):
    if data['reply_id'] in result1:
        print(data['id'], data['reply_id'])
'''



'''
    if data['reply_id']:
        print(data['reply_id'])
        print(data["twitter_url"])
        i += 1
        if i == 10:
            break
'''
            

'''
result1 = {}
for data in tqdm(datas):
    result1[str(data['id'])] = data['twitter_url']

i = 0
for reply in tqdm(data_replys):
    try:
        tmp1 = str(reply[reply_id])
        tmp = result1[tmp1]
        print("Source:", tmp)
        print('Caption:', reply['twitter_url'])
        print('=============')
        i +=1
        if i == 10:
            break
    except:
        continue
'''


#print(data['extended_entities']['media'][0]['additional_media_info']['source_user']['location'])

#print(data['retweeted_status']['user']['location'])
#print(data['user']['location'])

'''
file33 = os.getcwd()
#filename222 = 'Omicron_Varient'
#file_dir = file33 + '/dataset/#booster/'
filename2222 = file33 + '/dataset/'
filename22222 = os.listdir(filename2222)
'''
#for filename22222_tmp in tqdm(filename22222):
    #filename222 = filename22222_tmp
    #file_dir = filename2222 + filename222 +'/'
'''
file33 = os.getcwd()
filename222 = 'Delta'
file_dir = file33 + '/dataset/'+ filename222 + '/'
files = os.listdir(file_dir)
print(len(files))

result1 = []
result2 = []
result3 = []


i_11 = 0
i_22 = 0

for file in tqdm(files):
    path = file_dir + file + '/media/'
    path_k = file_dir + file + '/analysis/'
    try:
        paths1 = os.listdir(path)
    except:
        continue

    i_1 = 0
    i_2 = 0
    try:
        path_ks = os.listdir(path_k)
        for k in path_ks:
            if 'keyframes' in k:
                i_1 = 1
                i_11 += 1

            if 'transcription' in k:
                i_2 = 1
                i_22 += 1
    except:
        i_1 = 0
        i_2 = 0

    tmp_path = file_dir + file + '/' + file + '.json'
    with open(tmp_path, 'r') as f:
        data_tmp = json.load(f)
    text = data_tmp['tweet_text']
    url = data_tmp['tweet_url']
    video_url = data_tmp['tweet_video_url']

    tmp_path_source = file_dir + file + '/' + file + '_source.json'
    with open(tmp_path_source, 'r') as f:
        data_tmp1 = json.load(f)

    id = data_tmp1['id']
    reply_id = data_tmp1['in_reply_to_status_id']
    user_name = data_tmp1['user']['name']
    user_screen = data_tmp1['user']['screen_name']
    user_profile = data_tmp1['user']['description']
    location = []
    try:
        location.append(data_tmp1['user']['location'])
        location.append(data_tmp1['retweeted_status']['user']['location'])
        location.append(data['extended_entities']['media'][0]['additional_media_info']['source_user']['location'])
    except:
        location.append('')

    retweet_count = data_tmp1['retweet_count']
    favorite_count = data_tmp1['favorite_count']
    in_reply_to_user_id = data_tmp1['in_reply_to_user_id']
    tmp11 = data_tmp1['entities']['hashtags']
    tags = []
    for tmp111 in tmp11:
        tags.append(tmp111['text'])

    for path1 in paths1:
        if 'mp3' in path1:
            # mp3_path
            mp3_path = path + path1
            mp4_path = mp3_path[:-1]
            mp4_path = mp4_path + '4'

            # transcription
            try:
                tmp1_path = file_dir + file + '/analysis/' + file + '_transcription.txt'
                f = open(tmp1_path, "r", encoding="utf-8")
                lines = f.read()
                transcription = lines
            except:
                transcription = ''

            keyframe_path = file_dir + file + '/analysis/keyframes/'

            tmp1 = file_dir + file
            result1.append({'keyword': filename222, 'sample_path': tmp1, 'twitter_url': url, 'video_url': video_url,
                            'keyframe_path': keyframe_path, 'mp4_path': mp4_path, 'mp3_path': mp3_path,
                            'caption': text,
                            'transcription': transcription, 'id': id, 'reply_id': reply_id,
                            'retweet_count': retweet_count,
                            'favorite_count': favorite_count, 'in_reply_to_user_id': in_reply_to_user_id,
                            'tags': tags,
                            'has_keyframefile': i_1, 'has_transcriptionfile': i_2, 'location': location,
                            'user_name': user_name,
                            'user_screen': user_screen, 'user_profile': user_profile})

        if 'mp4' in path1:
            mp4_path = path + path1

            # transcription
            try:
                tmp1_path = file_dir + file + '/analysis/' + file + '_transcription.txt'
                f = open(tmp1_path, "r", encoding="utf-8")
                lines = f.read()
                transcription = lines
            except:
                transcription = ''

            keyframe_path = file_dir + file + '/analysis/keyframes/'

            tmp1 = file_dir + file
            result2.append({'keyword': filename222, 'sample_path': tmp1, 'twitter_url': url, 'video_url': video_url,
                            'keyframe_path': keyframe_path, 'mp4_path': mp4_path, 'mp3_path': '', 'caption': text,
                            'transcription': transcription, 'id': id, 'reply_id': reply_id,
                            'retweet_count': retweet_count,
                            'favorite_count': favorite_count, 'in_reply_to_user_id': in_reply_to_user_id,
                            'tags': tags,
                            'has_keyframefile': i_1, 'has_transcriptionfile': i_2, 'location': location,
                            'user_name': user_name,
                            'user_screen': user_screen, 'user_profile': user_profile})

    if len(paths1) == 1:
        tmp1 = file_dir + file
        result3.append({'keyword': filename222, 'sample_path': tmp1, 'twitter_url': url, 'video_url': video_url,
                        'keyframe_path': '', 'mp4_path': '', 'mp3_path': '', 'caption': text,
                        'transcription': '', 'id': id, 'reply_id': reply_id, 'retweet_count': retweet_count,
                        'favorite_count': favorite_count, 'in_reply_to_user_id': in_reply_to_user_id, 'tags': tags,
                        'has_keyframefile': i_1, 'has_transcriptionfile': i_2, 'location': location,
                        'user_name': user_name,
                        'user_screen': user_screen, 'user_profile': user_profile})

print(len(result1))
print(len(result2))
print(len(result3))
print(i_11, i_22)
output_file1 = './dataset_v1/' + filename222 + '_v2.json'
output_file2 = './dataset_v1/' + filename222 + '_v1.json'
output_file3 = './dataset_v1/' + filename222 + '_v0.json'

with open(output_file1, 'w') as f:
    json.dump(result1, f)

with open(output_file2, 'w') as f:
    json.dump(result2, f)

with open(output_file3, 'w') as f:
    json.dump(result3, f)


'''
'''
file33 = os.getcwd()
filename222 = 'omicron'
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

'''

'''
# Two steps
file_dir = './dataset/#NoVaccinePassports/'
files = os.listdir(file_dir)

result = []

for file in tqdm(files[:10000]):
    paths = file_dir + file + '/'
    files_ = os.listdir(paths)

    for file_ in files_:
        if ('.json' in file_) and ('source' not in file_):
            path2 = paths + file_
            with open(path2, 'r') as f:
                data = json.load(f)
            caption = data['tweet_text']
            url = data['tweet_url']
            if 'RT' not in caption:
                result.append(url)

print(len(files), len(result))
print(result[:30])







'''


'''
result = []

for i in tqdm(range(len(df1))):
    tmp = []
    Tweet_url = df1['Tweet URL'][i]
    Caption = df1['Caption_new'][i]
    Tweet_Id = df1['Tweet Id'][i]
    Source = df1['Source'][i]

    caption = Caption.split(' ')
    for c in caption:
        if '#' in c:
            result.append(c[1:].lower())


print(len(result))

from collections import Counter
result = Counter(result)
result = dict(result)

result2 = []
for key,value in result.items():
    #print(key,value)
    if value < 4:
        result2.append(key)
        #print(key, value)

print(len(result2))
#print(result2)
'''
'''
import string
punc = string.punctuation


result = []

result1 = []
for i in tqdm(range(len(df1))):
    tmp = []
    Tweet_url = df1['Tweet URL'][i]
    Caption = df1['Caption_new'][i].lower()
    Tweet_Id = df1['Tweet Id'][i]
    Source = df1['Source'][i]

    caption = Caption.split(' ')
    caption_new = []
    caption_new1 = []
    j = 0
    k = 0
    for j in range(len(caption)):
        if '#' in caption[j]:
            caption_new1.append(caption[j])
            continue
        caption_new.append(caption[j])
        caption_new1.append(caption[j])

    if len(caption_new) < 2:
        continue

    caption_new = ' '.join(caption_new)
    caption_new1 = ' '.join(caption_new1)

    if caption_new in result1:
        continue

    result1.append(caption_new)

    tmp.append(Tweet_url)
    tmp.append(caption_new1)
    tmp.append(Caption)
    tmp.append(Tweet_Id)
    tmp.append(Source)
    result.append(tmp)

print(len(result))
df = pd.DataFrame(result, columns =['Tweet URL', 'Caption_new', 'Caption_old', 'Tweet Id', 'Source'])

df.to_csv('../dataset_summary/Twitter_full_v7.csv', index=False)
'''






'''
file_dir = './dataset_v1/'

files = os.listdir(file_dir)

url_list = []
result = []
result1 = []
result2= []
result3 = []
i = 0
j = 0

for file in tqdm(files):
    if 'v1' in file:
        tmp = './dataset_v1/' + file
        with open(tmp, 'r') as f:
            datas = json.load(f)

        for data in datas:
            video_url = data['video_url']
            url = data['twitter_url']
            caption = data['caption'][-6:]

            transcription = data['transcription']
            len1 = len(transcription)
            i += 1

            #if video_url == 'https://video.twimg.com/ext_tw_video/1462086422794579975/pu/vid/640x360/Os0p7qGSUkIu5zHM.mp4?tag=12':
                #print(data['twitter_url'], '\n')


            if (video_url in url_list) and (caption in result1):
                result2.append(video_url)
                result3.append(url)
                continue

            #if (video_url in url_list):
                #result3.append(video_url)

            #if video_url not in url_list:

            #if len(data['tags']) >= 5:
                #continue
            url_list.append(video_url)
            result1.append(caption)
            result.append(data)

            #if len1 == 0:
                #j +=1


print(len(url_list), len(result))
print(i, j)

#print(result2[-100])

with open('./dataset_summary/Twitter_dataset_v1.json', 'w') as f:
    json.dump(result, f)


import pandas as pd
result1 = []

for r in tqdm(result):
    tmp = []
    
    tmp.append(r['twitter_url'])
    tmp.append('"' + str(r['id']) + '"')
    tmp.append(r['caption'])
    tmp.append(r['location'])
    tmp.append(r['sample_path'])
    tmp.append(r['user_name'])
    tmp.append(r['tags'])
    tmp.append(r['user_screen'])
    tmp.append(r['user_profile'])
    
    tmp.append(r['twitter_url'])
    tmp.append(r['caption'])
    tmp.append('"' + str(r['id']) + '"')
    tmp.append('Twitter_v1')


    result1.append(tmp)

print(len(result1))
#df = pd.DataFrame(result1, columns =['twitter_url', 'id', 'caption', 'location', 'sample_path', 'user_name', 'tags', 'user_screen', 'user_profile'])
df = pd.DataFrame(result1, columns =['Tweet URL', 'Caption', 'Tweet Id', 'Source'])

df.to_csv('./dataset_summary/Twitter_v2.csv', index=False)


filename1 = './dataset_summary/yaser_v2.csv'
csvfile = open(filename1,encoding='utf-8')
df1 = pd.read_csv(csvfile)

for i in tqdm(range(len(df1))):
    tmp = []
    Tweet_url = df1['Tweet URL'][i]
    Caption = df1['Caption'][i]
    Tweet_Id = df1['Tweet Id'][i]
    Source = df1['Source'][i]
    tmp.append(Tweet_url)
    tmp.append(Caption)
    tmp.append(Tweet_Id)
    tmp.append(Source)
    result1.append(tmp)

print(len(result1))
df = pd.DataFrame(result1, columns =['Tweet URL', 'Caption', 'Tweet Id', 'Source'])

df.to_csv('./dataset_summary/Twitter_full_v2.csv', index=False)



'''










'''
file33 = os.getcwd()
filename222 = 'yaser'
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
    path = file_dir + file + '/'
    try:
        paths1 = os.listdir(path)
    except:
        continue
    for path1 in paths1:

        if 'mp3' in path1:

            #mp3_path
            mp3_path = path + path1
            #mp4_path = mp3_path[:-1]
            mp4_path = ''


            #caption
            tmp_path = file_dir + file + '/'  + 'caption.json'
            with open(tmp_path, 'r') as f:
                data_tmp = json.load(f)
            text = data_tmp[0][0]

            #transcription

            try:
                tmp1_path = file_dir + file + '/transcription.txt'
                f = open(tmp1_path, "r", encoding="utf-8")
                lines = f.read()
                transcription = lines
            except:
                transcription = ''

            #video_url

            tmp33_path = '/fs/vulcan-projects/misc_forensics/DATA_VIDEO/COVID19/'



            keyframe_path = file_dir + file + '/keyframes/'

            tmp1 = file_dir + file
            result1.append({'keyword': filename222, 'id': int(file), 'sample_path': tmp1, 'twitter_url': '', 'video_url': '', 'keyframe_path': keyframe_path, 'mp4_path': mp4_path, 'mp3_path': mp3_path, 'caption': text, 'transcription': transcription})

        if 'keyframe' in path1:

            # mp3_path
            mp3_path = ''
            # mp4_path = mp3_path[:-1]
            mp4_path = ''

            # caption
            tmp_path = file_dir + file + '/' + 'caption.json'
            with open(tmp_path, 'r') as f:
                data_tmp = json.load(f)
            text = data_tmp[0][0]

            # transcription
            try:
                tmp1_path = file_dir + file + '/transcription.txt'
                f = open(tmp1_path, "r", encoding="utf-8")
                lines = f.read()
                transcription = lines
            except:
                transcription = ''

            keyframe_path = file_dir + file + '/keyframes/'

            tmp1 = file_dir + file
            result2.append({'keyword': filename222, 'id': int(file), 'sample_path': tmp1, 'twitter_url': '', 'video_url': '',
                            'keyframe_path': keyframe_path, 'mp4_path': mp4_path, 'mp3_path': mp3_path, 'caption': text,
                            'transcription': transcription})
                            

print(len(result1), len(result2))


print(len(result1))
print(len(result2))
output_file1 = './dataset_summary/' + filename222 + '_v2.json'
output_file2 = './dataset_summary/' + filename222 + '_v1.json'


with open(output_file1, 'w') as f:
    json.dump(result1, f)

with open(output_file2, 'w') as f:
    json.dump(result2, f)
'''



'''
file_dir = './dataset/#handsanitizer/'
files = os.listdir(file_dir)
print('num:', len(files))

result = []
mp4 = 0
mp3 = 0
for file in tqdm(files):
    #file = files[1]
    file_path = file_dir + file +'/'
    files1 = os.listdir(file_path)
    tmp2 = ''
    tmp1 = ''
    #re = 0
    for file1 in files1:
        if 'source' in file1:
            tmp1 = file1.split('_source')[0]
            tmp2 = tmp1 + '.json'

    tmp5 = file_path + 'media/'

    try:
        files2 = os.listdir(tmp5)
        for file2 in files2:
            if 'mp4' in file2:
                mp4 += 1

            if 'mp3' in file2:
                mp3 += 1
    except:
        continue

    #tmp3 = './tmp1/1461567392501284865/1461567392501284865.json'
    path = '/vulcanscratch/fl3es/Twitter_down/dataset/#handsanitizer/' + tmp1 + '/' + tmp2
    with open(path, 'r') as f:
        data = json.load(f)

    if data['tweet_media'] == 1 and data['tweet_media_type'] == 'video':
        result.append(tmp1)
        #print(tmp1)


print(len(result))
print(result[:20])
'''
#print(mp3, mp4)

#import urllib.request
#url_link = 'https://video.twimg.com/ext_tw_video/1461058365455577099/pu/vid/320x568/H5jG4JYYG_nOM-l0.mp4?tag=12'
#urllib.request.urlretrieve(url_link, 'video_name.mp4')

# !/usr/bin/env python

import os
import argparse
import requests
import json
import urllib.parse
import m3u8
from pathlib import Path
import urllib.request
import re
import ffmpeg
import shutil
import copy
# import m3u8_to_mp4
import tweepy
import moviepy.editor as mp
from tweepy import OAuthHandler
import json
import wget
# from IPython.display import clear_output
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
#from keyframes_extract_diff import key_frame_extract


# IBM watson keys
# apikey = 'ADU3J1RXzt9ZZbVOotr2nBCS6Yka4RtMZoPbagh4u78o'
# url = 'https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/391faf6c-3091-498a-9beb-b27b8f15a709'
# https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/391faf6c-3091-498a-9beb-b27b8f15a709


#with open("IBM_speech_to_text_config.json", "r") as json_data_file:
    #IBM_config = json.load(json_data_file)

#apikey = IBM_config["apikey"]

apikey = 'H3P7xGmHVvtuRxNULJQeHMxU-5RqqJUxN5GEAROC4kl2'
#url = IBM_config["url"]
url = 'https://api.us-east.speech-to-text.watson.cloud.ibm.com/instances/7e395764-3129-4746-86b2-e07cfe1fa4c2'
authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(url)


def speech_text(filename, path1):
    # Perform conversion
    text = ''
    #try:
    print('1')
    try:
        with open(filename, 'rb') as f:
            res = stt.recognize(audio=f, content_type='audio/mp3', model='en-US_NarrowbandModel').get_result()

        print('2')
        for result in res['results']:
            text = text + result['alternatives'][0]['transcript'].rstrip()


    except:
        #text = ''
        num4 = ''
        return len(num4)

    print('3')
    transcription_file = path1 + 'transcription.txt'
    with open(transcription_file, 'w') as f:
        f.write(text)
    num4 = len(text)
    return num4


filename1 = '../dataset_summary/Twitter_full_v10.csv'
csvfile = open(filename1, encoding='utf-8')
df_n = pd.read_csv(csvfile)


target_path = '/fs/vulcan-projects/misc_forensics/DATA_FUXIAO/frame_and_transcript/'


num = 0
result = []
j = 0


video_ids = []
for i in tqdm(range(len(df_n))):
    Tweet_Id = df_n['Tweet Id'][i][1:-1]
    video_ids.append(Tweet_Id)
video_ids.reverse()


#for i in tqdm(range(len(df_n))):
    #Tweet_Id = df_n['Tweet Id'][i][1:-1]
for Tweet_Id in tqdm(video_ids):
    path = target_path + Tweet_Id +  "/"
    path_files = os.listdir(path)
    j = 0
    mp3_file = ''
    if Tweet_Id == '1466212381667868674':
        continue
    for f1 in path_files:
        if 'mp3' in f1:
            mp3_file = path + f1
        if 'transcription.txt' in f1:
            path_t = path + f1
            f2 = open(path_t, "r", encoding="utf-8")
            lines = f2.read()
            j = len(lines)
            if j > 0:
                continue

    #if j != 0:
        #num +=1
        #result.append({'id': Tweet_Id})
        #with open('./data10.json', 'w') as f:
            #json.dump(result, f)

    if j == 0:
        print('===========')
        print('id:', Tweet_Id)
        num1 = speech_text(mp3_file, path)
        if num1 > 0:
            print("yes")
            num += 1
            #result.append({'id': Tweet_Id})
            #with open('./data10.json', 'w') as f:
                #json.dump(result, f)

    print('Number of Transcription:', num)






'''
files = os.listdir(target_path)

i = 0
for file in tqdm(files):
    path = target_path + file + '/'
    path_files = os.listdir(path)
    mp3_file = ''
    j = 0
    for f in path_files:
        if 'mp3' in f:
            mp3_file = path + f
        if 'transcription' in f:
            path_t = path + f
            f = open(path_t, "r", encoding="utf-8")
            lines = f.read()
            j = len(lines)

    if j == 0:
        speech_text(mp3_file, path)


'''


'''
import moviepy.editor as mp

filename = './sample.mp4'
my_clip = mp.VideoFileClip(filename)
my_clip.audio.write_audiofile('sample'+".mp3") #,codec='pcm_s16le')


from keyframes_extract_diff import key_frame_extract

key_frame_extract('./sample.mp4','./keyframe/')



target_path = '/fs/vulcan-projects/misc_forensics/DATA_FUXIAO/frame_and_transcript/'
'''
