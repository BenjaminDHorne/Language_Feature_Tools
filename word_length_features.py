import os

def fix(text): # Unicode Hack for python 2
    text = text.replace("\r", "").replace('\n', "").replace("\ufffd'", "")
    text = text.decode("ascii", "ignore")
    return text

def get_stopwords():
    with open("./stopwords.txt") as data:
        stopwords = [w.strip() for w in data]
    return set(stopwords)

if __name__ == "__main__":
    path = ""
    outpath = ""
    outfilename = ""
    stopwords = get_stopwords()
    for fn in os.listdir(path):
        tid = fn.split("_")[0]
        with open(outpath+"_word_feats_title.csv", "a") as out:
             out.write("id,avg_word_len,percent_stopwords\n")
        with open(path+fn) as data:
            text_content = [line.strip() for line in data]
            text = " ".join(text_content)
            text = fix(text)
        words = text.split(" ")
        stopwords_in_text = [s for s in words if s in stopwords]
        percent_sws = float(len(stopwords_in_text))/len(words)
        lengths = [len(w) for w in words if w not in stopwords]
        word_len_avg = float(sum(lengths))/len(lengths)
        with open(outpath+outfilename, "a") as out:
            outarr = [str(tid),str(word_len_avg),str(percent_sws)]
            out.write(",".join(outarr)+"\n")
