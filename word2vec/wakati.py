# coding : utf-8

import MeCab
import sys

input_path  = 'resources/yume_juya.txt'
output_path = 'resources/yume_juya_wakati.txt'

tagger = MeCab.Tagger('-F\s%f[6] -U\s%m -E\\n')

fi = open(input_path,  'r')
fo = open(output_path, 'w')

line = fi.readline()
while line:
    result = tagger.parse(line)
    fo.write(result[1:])
    line = fi.readline()

fi.close()
fo.close()
