import sys
import os

from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTContainer, LTTextBox
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage


def find_textboxes_recursively(layout_obj):

    if isinstance(layout_obj, LTTextBox):
        return [layout_obj]

    if isinstance(layout_obj, LTContainer):
        boxes = []
        for child in layout_obj:
            boxes.extend(find_textboxes_recursively(child))

        return boxes

    return []


laparams = LAParams(detect_vertical=True)
resource_manager = PDFResourceManager()
device = PDFPageAggregator(resource_manager, laparams=laparams)
interpreter = PDFPageInterpreter(resource_manager, device)


def extract_textboxes(pdf_file):
    with open(pdf_file, 'rb') as f:
        for page in PDFPage.get_pages(f, maxpages=1):
            interpreter.process_page(page)
            layout = device.get_result()

            boxes = find_textboxes_recursively(layout)
            boxes.sort(key=lambda b: (-b.y1, b.x0))

            for box in boxes:
                if len(box) > 30:
                    pdftext = box.get_text().strip()
                    g = open(text_name, 'w')
                    g.writelines(pdftext)
                    g.close()


def check_dir(path):
    dirs = []
    files = []
    for x in dirs:
        if os.path.isdir(x):


def get_dir(path):
    path = sys.argv[1]
    dirs = []
    for directory in os.listdir(path):
        path2 = os.path.join(path + directory)
        if os.path.isdir(path2):
            dirs.append(directory)
            for dire in dirs:
                if not os.path.isdir(dire):
                    files.append(


def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        yield dirs
        for file in files:
            yield os.path.join(root, file)

def print_all_files(directory):
    for file in find_all_files(directory):
        print file
