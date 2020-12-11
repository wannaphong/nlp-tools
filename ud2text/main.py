import codecs
import re
from conllu import parse
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-ud", "--udfile", help="path conllu from ud",type=str)
args = parser.parse_args()

with codecs.open(args.udfile, 'r',encoding='utf-8-sig') as f:
  t=f.read()
s=re.split('\n\n',re.sub('\# (.*)\n','',t))
text = str()

sentences = parse(t)
for i in sentences:
    _t =[]
    for j in i:
        _t.append(j['form'])
    text+='|'.join(_t)+'\n'
"""
for t in s:
    sentence = parse(t)
    for i in sentence:
        _t =[]
        for j in i:
            _t.append(j['form'])
        text+='|'.join(_t)+'\n'
"""
with open(args.udfile+'.txt','w',encoding='utf-8') as f:
    f.write(text)