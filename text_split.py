# -*- coding:utf-8 -*-

import os
import re
import sys

f = open("sample6.txt")
data = f.readlines()
x = []
for line in data:
    if "LTTextBox" in line:
        x.append(line)
        for y in x:
            if len(y) > 1000:
                print y
f.close()
