#!/usr/bin/env python3

import os
import shutil
import subprocess
import sys

if shutil.which('scanprep') is None:
    sys.exit('You need to install `scanprep`: pip3 install scanprep')

if shutil.which('ocrmypdf') is None:
    sys.exit('You need to install `ocrmypdf`: sudo apt install ocrmypdf')

if shutil.which('tesseract') is None:
    sys.exit('You need to install `tesseract`: sudo apt install tesseract-ocr-deu')

# We use the CWD as the base directory for the scans
data_dir = os.getcwd()

tmp_dir = data_dir + '/tmp/'
out_dir = data_dir + '/out/'

if not os.path.exists(tmp_dir):
    print(sys.stderr, 'Creating tmp directory')
    os.mkdir(tmp_dir)
if not os.path.exists(out_dir):
    print(sys.stderr, 'Creating out directory')
    os.mkdir(out_dir)

# Loop over all PDFs in the data directory
pdfs = [(f.name, f.path) for f in os.scandir(data_dir)
        if f.is_file() and f.name.endswith(".pdf")]

for (i, (file_name, input_pdf_path)) in enumerate(pdfs):
    print(f"Processing PDF {i+1}/{len(pdfs)}: {file_name}")

    tmp_file = tmp_dir + "0-" + file_name

    subprocess.run(["scanprep", "--blank-removal", input_pdf_path, tmp_dir],
                   check=True)
    subprocess.run(["ocrmypdf", "-l", "deu", "--deskew", tmp_file, out_dir + file_name],
                   check=True)

    os.remove(tmp_file)

print(os.getcwd())
