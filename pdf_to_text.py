#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re


def pdf_to_text(directory):
    PDF_LIST = os.listdir(directory)  # get pdf list data
    PDF_LIST2 = []
    regex = r"(pdf)$"  # regular expression for check .pdf

    for y in PDF_LIST:
        match = re.search(regex, y)
        if match:
            PDF_LIST2.append(y)

    for x in PDF_LIST2:  # Save .txt data converted from .pdf
        path = os.path.join(directory, x)
        name = re.sub(r"(pdf)$", 'txt', os.path.basename(path))
        os.system("pdf2txt.py" + " -o " + name + " " + path)

if __name__ == '__main__':
    pdf_to_text("/home/kazuki/3382")
