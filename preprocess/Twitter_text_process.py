import nltk
from ekphrasis.classes.tokenizer import SocialTokenizer
import re


def wsp_tokenizer(text):
    return text.split(" ")

def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

puncttok = nltk.WordPunctTokenizer().tokenize

social_tokenizer = SocialTokenizer(lowercase=False).tokenize

sents = [
    "üôèüò±üíâProof of an ingredient called ‚ÄúLuciferase‚Äù in Moderna Vaccines (satanic?) 1min30sec https://t.co/hjXL7nHn97"
]

import string


for s in sents:
    print(s, '\n')
    s1 = remove_emoji(s)
    tmp = social_tokenizer(s1)
    print(tmp,'\n')
    tmp1 = []
    for t in tmp:
        t1 = "".join(filter(lambda char: char in string.printable, t))
        if len(t1) == 0:
            continue
        tmp1.append(t1)
    print(tmp1, '\n')


#Output
#['Proof', 'of', 'an', 'ingredient', 'called', 'Luciferase', 'in', 'Moderna', 'Vaccines', '(', 'satanic', '?', ')', '1', 'min30sec', 'https://t.co/hjXL7nHn97']
