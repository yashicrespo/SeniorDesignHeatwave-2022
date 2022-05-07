#!/usr/bin/python
import re
s_strs = 'oneXXXtwoYYYthreeZZZfourXXXtwoXXXfive'

cat =re.split('XXX|YYY|ZZZ', s_strs)

sam="{'temp' : 23.323 , 'frame' : [2,3,454,232]}"

sam = re.findall(r"[^\]\[]*|\[[^\]\[]*?\]", sam)


print(sam[2])