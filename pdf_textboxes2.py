# -*- coding:utf-8 -*-
import sys
import os
import time
from tqdm import tqdm

from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTContainer, LTTextBox
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage
"""
find /home/2829902373/English/ \( -name ".DS_Store" -or -name "._*" \) -print -exec rm {} ";"
"""

def find_textboxes_recursively(layout_obj):

    if isinstance(layout_obj, LTTextBox):
        return [layout_obj]

    if isinstance(layout_obj, LTContainer):
        boxes = []
        for child in layout_obj:
            boxes.extend(find_textboxes_recursively(child))

        return boxes

    return []


def extract_textboxes(file_path):
    laparams = LAParams(detect_vertical = True)
    resource_manager = PDFResourceManager()
    device = PDFPageAggregator(resource_manager,laparams=laparams)
    interpreter = PDFPageInterpreter(resource_manager,device)
    file = os.path.basename(file_path)
    with open(file_path, 'rb') as f:
        for page in PDFPage.get_pages(f, maxpages=1):
            interpreter.process_page(page)
            layout = device.get_result()

            boxes = find_textboxes_recursively(layout)
            boxes.sort(key=lambda b: (-b.y1, b.x0))

            file_title,file_ext = os.path.splitext(file_path)
            dir_path,file_name = os.path.split(file_path)
            text_path = file_title + '.txt'
            g = open(text_path,'w')
            for box in boxes:
                 pdftext = box.get_text().strip()
                 pdftext_utf8 = pdftext.encode('utf-8')
                 if len(pdftext) > 350:
                    flag = True
                    """
                    if "SMBC NIKKO SECURITIES INC." in pdftext_utf8:
                        flag = False
                    if "APPENDIX FOR ANALYST" in pdftext_utf8:
                        flag = False
                    if "SMBC Nikko Securities Inc." in pdftext_utf8:
                        flag = False
                    if "APPENDIX FOR ANALYST CERTIFICATION" in pdftext_utf8:
                        flag = False
                    if "IMPORTANT" or "ANALYST DISCLOSURES" in pdftext_utf8:
                        flag = False
                    if flag:
                    """
                    g.write(pdftext_utf8)
            g.close()




def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if os.path.exists(file):
                yield os.path.join(root, file)

def print_all_files(directory):
    for file_path in find_all_files(directory):
        if ".pdf" in file_path:
            return file_path

def find_all_dirs(directory):
    for root, dirs,files in os.walk(directory):
        for dir in dirs:
            yield os.path.join(root,dir)

def print_all_dirs(directory):
    for dir_path in find_all_dirs(directory):
        return dir_path

def get_dirs(directory):
    dirs = []
    dirs = os.listdir(directory)
    for dir in dirs:
        dir_path = str(directory) + "/" + str(dir)
        return dir_path

def get_files(directory):
    files = []
    files = os.listdir(directory)
    for file in files:
        file_path = str(directory) + "/" + str(file)
        yield file_path

path = sys.argv[1]
dirs = []
dirs = os.listdir(path)
for dir in tqdm(dirs):
    dir_path = str(path) + "/" + str(dir)
    print dir_path
    files = []
    files = os.listdir(dir_path)
    for file in files:
        file_path = str(dir_path) + "/" + str(file)
        print file_path
        if ".pdf" in file_path:
          extract_textboxes(file_path)
            

        
#get_files(sys.argv[1])
#get_dirs(sys.argv[1])

#extract_textboxes(get_files(sys.argv[1]))
#extract_textboxes(get_files(get_dirs(sys.argv[1])))
#extract_textboxes(print_all_files(sys.argv[1]))
#extract_textboxes(sys.argv[1])
#print_all_files(sys.argv[1])
