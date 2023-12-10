# pdf-scan-preprocessor

Postprocessing of scanned pages in a PDF.
It first calls a blank page removal.
Then it performs OCR.

## Dependencies

```sh
sudo apt install ocrmypdf tesseract-ocr-deu
snap install scanprep
```

## Usage

```sh
chmod +x postprocess-scans.py
./postprocess-scans.py
```

This works through all PDFs in the current folder and creates the folder `out` for the results.
