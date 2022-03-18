from transformers import pipeline
from transformers import RobertaTokenizerFast, RobertaForMaskedLM
from tqdm import tqdm
import json

tokenizer = RobertaTokenizerFast.from_pretrained("amoux/roberta-cord19-1M7k")
model = RobertaForMaskedLM.from_pretrained("amoux/roberta-cord19-1M7k")

fillmask = pipeline("fill-mask", model=model, tokenizer=tokenizer)

data = []
i = 0

#change the filename
input_file = '/fs/vulcan-projects/misc_forensics/DATA_FUXIAO/CLIP_caption_only_transformer2/data_clean_select_key.json'
with open(input_file, 'r') as f:
	datas = json.load(f)

sentence = []
keywords = []
video_ids = []

for data in tqdm(datas):
	sentence.append(data['caption'])
	keywords.append(data['keyword'])
	video_ids.append(data['Video_id'])

print(len(keywords), len(sentence))


false_claim  = []
for i in tqdm(range(len(keywords))):
	claim = sentence[i]
	keyword = keywords[i]
	video_id = video_ids[i]

	i+=1
	if claim[-1] != ".":
		# if there is no . at the end and we are replacing last word, the model will just predict a punctuation mark
		claim = claim +  "."

	masked_text = claim.lower().replace(keyword, tokenizer.mask_token)

	try:
		suggs = fillmask(masked_text, top_k=20) #CHANGED TO 10
		suggs = [sent['sequence'].replace("<s>", "").replace("</s>", "") for sent in suggs]
		suggs = set(suggs)
	except:
		pass

	for sug in suggs:
		if sug != claim.lower():
			if isinstance(sug,list):
				continue
			# ori_caption: original caption
			# caption: generated caption
			false_claim.append({'Video_id': video_id, 'ori_caption':claim, 'caption': sug})

print(len(false_claim))
with open('./data_clean4.json', 'w') as f:
	json.dump(false_claim, f)
