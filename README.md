# Image MSB Extractor

A simple Python script for extracting data stored in the **Most Significant Bits (MSB)** of RGB image pixels.

This project was created while learning image steganography and digital forensics.

## How it works

For every pixel in the image, the script reads the Red, Green, and Blue channel values.

Each RGB channel is an 8-bit value:

```text
R = 10110110
G = 01100101
B = 11001010
```

The script extracts the most significant bit, which is the leftmost bit:

```text
R MSB = 1
G MSB = 0
B MSB = 1
```

The extracted bits from all pixels are collected sequentially.

Every 8 bits are then converted into one byte:

```text
bits → byte → output data
```

The recovered bytes are written to a binary file named:

```text
extracted
```

## Requirements

- Python 3
- Pillow
- NumPy

Install the required libraries with:

```bash
pip install pillow numpy
```

## Usage

Place the image you want to analyze in the same directory as the script and name it:

```text
image.png
```

Run:

```bash
python extract_msb.py
```

The extracted data will be saved in:

```text
extracted
```

You can then inspect the recovered file using tools such as:

```bash
file extracted
```

```bash
xxd extracted
```

```bash
strings extracted
```

## Purpose

This project is mainly intended for learning:

- Image steganography
- MSB manipulation
- Bitwise operations
- Digital forensics
- CTF forensics challenges

## Author

Created as part of my cybersecurity and digital forensics learning journey.
