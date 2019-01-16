import gzip, shutil, sys, glob, nltk, string
from lxml import etree

def load_files(files):
    xml_files = list()
    for gz_file in files:
        outfile = gz_file[:-3]
        xml_files.append(outfile)
        with gzip.open(gz_file, 'r') as f_in, open(outfile, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    return xml_files

def get_sentences(unzipped_file):
    xpath = '//DOC[@type="story"]/TEXT/P/text()'
    root = etree.parse(unzipped_file)
    return root.xpath(xpath)

def remove_newlines(sentences):
    sentences = [sentence.replace('\n', ' ') for sentence in sentences]
    return " ".join(sentences)

def tokenize_sentences(sentences):
    tokenized = nltk.sent_tokenize(sentences)
    return tokenized

def remove_punctuation(tokens):
    punctuation_set = set(string.punctuation)
    no_punct_tokens = [t for t in tokens if t not in punctuation_set]
    return no_punct_tokens

def capitalize(tokens):
    tokens  = [token.upper() for token in tokens]
    return tokens

def tokenized_corpus(input_corpus):
    pass

xml_files = load_files(glob.glob(sys.argv[1]))
words = list()
for xml_file in xml_files:
    words.append(" ".join(get_sentences(xml_file)))
print(*words)


#sentences = tokenize_sentences(remove_newlines(get_sentences(sys.argv[1])))
#words = [nltk.word_tokenize(sentence) for sentence in sentences]
#words = [remove_punctuation(tokens) for tokens in words]
#words = [capitalize(tokens) for tokens in words]
#print(len(words))

#files = glob.glob(sys.argv[1])
#xml_files = list()
#for gz_file in files:
#    outfile = gz_file[:-3]
 #   xml_files.append(outfile)
#    with gzip.open(gz_file, 'r') as f_in, open(outfile, 'wb') as f_out:
#        shutil.copyfileobj(f_in, f_out)

#for xml_file in xml_files:
#    result += get_sentences(xml_file)


