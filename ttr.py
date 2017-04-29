import os

def fix(text): # unicode hack
    text = text.replace("\r", "").replace('\n', "")
    text = text.decode("ascii", "ignore")
    return text

if __name__ == "__main__":
    path = ""
    outpath = ""
    outfilename = ""
    with open(outpath+outfilename,"a") as out:
        out.write("id,ttr\n")
    for fn in os.listdir(path):
        tid = fn.split("_")[0].split(".")[0]
        with open(path+fn) as data:
            text_content = [line.strip() for line in data]
            text = " ".join(text_content)
            text = fix(text)
        words = text.split()
        dif_words = len(set(words))
        tot_words = len(words)

        with open(outpath+outfilename,"a") as out:
            out.write(",".join((str(tid),str(float(dif_words)/tot_words)))+"\n")
