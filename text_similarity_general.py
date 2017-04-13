from sklearn.feature_extraction.text import TfidfVectorizer
import os

'''
cosine similarity betwen two text files

This can easily be expanded to loop through pairs of files.

Params:
input_file1 - input file name, must be pure text file
input_file2 - input file name to compare, must be pure text file
outfile - name of similairty outputfile
id1 - id for file 1
id2 - id for file 2
'''

input_file1 = ""
input_file2 = ""
outfile = ""
id1 = ""
id2 = ""
bad_files = []
with open(outfile, "a") as out:
    out.write("id_1,id_2,similarity\n") # header
    with open(input_file1) as f1:
        text_data = [line.strip() for line in f1]
        text1 = " ".join(text_data)
    with open(input_file2) as f2:
        text_data = [line.strip() for line in f2]
        text2 = " ".join(text_data)
    try:
        print "trying to compute similarity..."
        documents = [text1, text2]
        tfidf = TfidfVectorizer().fit_transform(documents)
        cos_sim = ((tfidf * tfidf.T).A)[0,1]
        out.write(",".join((id1,id2,str(cos_sim)))+"\n")
    except:
        print "bad file, logging..."
        bad_files.append((id1,id2))
        with open("bad_file.log", "a") as err:
            [err.write(",".join(p)+"\n") for p in bad_files]
