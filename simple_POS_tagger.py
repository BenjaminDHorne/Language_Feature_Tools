import nltk
from nltk import tokenize
import os

def fix(text): # unicode hack
    text = text.replace("\r", "").replace('\n', "").replace("\ufffd'", "")
    text = text.decode("ascii", "ignore")
    return text

path = ""
outpath = ""
outfilename = ""
for fn in os.listdir(path):
        print "processing", fn
        tid = fn.split("_")[0]
        with open(path+fn) as data:
            text_content = [line.strip() for line in data]
            text = " ".join(text_content)
            text = fix(text)
        sents = tokenize.sent_tokenize(text)
        for sent in sents:
            words = sent.strip(".").split()
            tags = nltk.pos_tag(words)
            strtags = ["/".join((wt[0],wt[1])) for wt in tags]
            with open(outpath+tid+outfilename, "a") as out:
                out.write(" ".join(strtags)+" ")
                
            
