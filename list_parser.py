import pandas as pd
import nltk, json, sys, traceback, platform, os
from collections import Counter
import nltk
from collections import Counter
import nltk
import io, pprint
from pprint import pprint



class Colors:
    reset = "\033[0m"

    # Black
    fgBlack = "\033[30m"
    fgBrightBlack = "\033[30;1m"
    bgBlack = "\033[40m"
    bgBrightBlack = "\033[40;1m"

    # Red
    fgRed = "\033[31m"
    fgBrightRed = "\033[31;1m"
    bgRed = "\033[41m"
    bgBrightRed = "\033[41;1m"

    # Green
    fgGreen = "\033[32m"
    fgBrightGreen = "\033[32;1m"
    bgGreen = "\033[42m"
    bgBrightGreen = "\033[42;1m"

    # Yellow
    fgYellow = "\033[33m"
    fgBrightYellow = "\033[33;1m"
    bgYellow = "\033[43m"
    bgBrightYellow = "\033[43;1m"

    # Blue
    fgBlue = "\033[34m"
    fgBrightBlue = "\033[34;1m"
    bgBlue = "\033[44m"
    bgBrightBlue = "\033[44;1m"
    # Magenta
    fgMagenta = "\033[35m"
    fgBrightMagenta = "\033[35;1m"
    bgMagenta = "\033[45m"
    bgBrightMagenta = "\033[45;1m"
    # Cyan
    fgCyan = "\033[36m"
    fgBrightCyan = "\033[36;1m"
    bgCyan = "\033[46m"
    bgBrightCyan = "\033[46;1m"
    # White
    fgWhite = "\033[37m"
    fgBrightWhite = "\033[37;1m"
    bgWhite = "\033[47m"
    bgBrightWhite = "\033[47;1m"
###########
color = Colors()
yellow = color.fgYellow
red = color.fgRed
blue = color.fgBlue
bblue = color.fgBrightBlue
cyan = color.fgCyan
bg_background = color.bgBlack
reset = color.reset
###########

class TextBuffer():
    def __init__(self):
        super(TextBuffer, self).__init__()
        self.os = os; self.io = io; self.json = json
        self.list_count = 0
        self._args = _args = []
        self.text_data = []
        self.current_platform = platform.platform
        self.io.DEFAULT_BUFFER_SIZE = io.DEFAULT_BUFFER_SIZE
        self.text_len = []
        print(f'[+] {self.current_platform} :: {self.io.DEFAULT_BUFFER_SIZE}')
        self.text_file = input('')
        self.text_file = str(self.text_file)
        self.cwd = self.os.getcwd()
        self.text_loc = str(self.cwd) + f'/{self.text_file}'
        self.text_str = f'[SYSTEM]** Dump The Text Data To: [{self.text_file}] ** [SYSTEM]'

    def __str__(self):
        return '{}({})'.format(type(self).__name__, ', '.join(repr(getattr(self, a)) for a in self._args))  ## guidelines for res
    def __repr__(self):
        return '{}({})'.format(type(self).__name__,', '.join(str(getattr(self, a)) for a in self._args))

    ### website_list = [x.strip() for x in content]   ####
    ### ADD LOGIC TO COUNT NUMBERS                    ####
    def text_file_len(self):
        with open(self.text_loc) as f:
            for href in open(self.text_loc):
                self.text_data = f.readlines(self.list_count)
                index = 0
                self.list_count += 1
                for iterate in self.text_len:
                    if index < self.list_count:
                        print(f'[SYS]** ADDED {iterate}')
                    else:
                        break
                global text_len
                text_len = self.list_count
                print(f'[SYSTEM] Found {self.list_count} items in .txt')
                break

    ### CHEAP GENERATOR ###
    def cheap_generator(self):
        def toOpen():
            n = 0
            while n <= int(self.text_len):
                yield sq


    def start_Buffer(self):
        buffer_append = []
        matching_string = []
        with open('file.csv', buffering=200000, '', 'r', -1) as f:
            for line in f:
                print(line)
                buffer_append.append(line)
        if str(line) in buffer_append:
            print('{red}[-] -[System Found Matching String]- [-]')
        print('{yellow}[+]\t\t -[SCANNING-SYSTEM]- \t\t[+]{reset}')
        return line

try:
    def main():
        print('[+] --- [+]')
        print()
        with TextBuffer() as TB:
            lins, count = TB.start_buffer()
            print(f'[+] Found [{count}] similar strings in the text doc')
            for i in lins:
                pprint.pprint(i)
    if __name__ == '__main__':
        main()
except Exception as e:
    print(str(e))
    print(traceback.format_exc())
    print(sys.exc_info()[2])
    pass



def training(self):
    self. .split()
    tokens = nltk.word_tokenize(text)
    print(tokens)
    tag = nltk.pos_tag(tokens)
    print(tag)
    grammar = "NP: {<DT>?<JJ>*<NN>}"
    cp = nltk.RegexpParser(grammar)
    result = cp.parse(tag)
    print(result)
    result.draw()  # It will draw the pattern graphically which can be seen in Noun Phrase chunking

    print(f'[+] Please enter the message you would like to encrypt')
    message = input('')
    message = message.split() ## to conver cars to lower case

    ### serialize json
    data = json.loads(message)
    results = []
    for chunk in pd.read_csv():
        results.append(sum(chunk['X']))
    total = sum(results)
    print(total)

    nltk.download()
    def topten():
        yield 1
        yield 2
        yield 3
        yield 4

    values = topten()
    print(values.__next__())
    print(values.__next__())

    for i in values:
        print(i)

    ###  LOADING THE DATA
    ## 1 TOKENIZ
    sentence = """At eight o'clock on Thursday morning
    ... Arthur didn't feel very good."""
    tokens = nltk.word_tokenize(sentence)
    tokens

    ['At', 'eight', "o'clock", 'on', 'Thursday', 'morning',
     'Arthur', 'did', "n't", 'feel', 'very', 'good', '.']
    tagged = nltk.pos_tag(tokens)
    tagged[0:6]
    [('At', 'IN'), ('eight', 'CD'), ("o'clock", 'JJ'), ('on', 'IN'),
     ('Thursday', 'NNP'), ('morning', 'NN')]

    # 2 display enetitites

    entities = nltk.chunk.ne_chunk(tagged)
    entities
    ## count pos tags
    text = "Guru99 is one of the best sites to learn WEB, SAP, Ethical Hacking and much more online."
    lower_case = text.lower()
    tokens = nltk.word_tokenize(lower_case)
    tags = nltk.pos_tag(tokens)
    counts = Counter(tag for word, tag in tags)
    print(counts)

    ### COUNTING POS TAGS

    text = "Guru99 is one of the best sites to learn WEB, SAP, Ethical Hacking and much more online."
    lower_case = text.lower()
    tokens = nltk.word_tokenize(lower_case)
    tags = nltk.pos_tag(tokens)
    counts = Counter(tag for word, tag in tags)
    print(counts)

    #  from nltk.corpus import treebank
    t = treebank.parsed_sents('wsj_0001.mrg')[0]
    t.draw()

    ## produces graphicsal of dispalyed words s
    a = "Gase     visit the site guru99.com and much more."
    words = nltk.tokenize.word_tokenize(a)
    fd = nltk.FreqDist(words)
    fd.plot()





