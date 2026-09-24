from PIL import Image
import numpy as np 

image = Image.open("image.png").convert("RGB")

pixels = np.array(image)

bits = []


for row in pixels :
	for pixel in row :

		r, g, b = pixel 

		r_msb = (r >> 7) & 1
		g_msb = (g >> 7) & 1
		b_msb = (b >> 7) & 1

		bits.extend([r_msb, g_msb, b_msb])

data = bytearray()

for i in range(0, len(bits)-7, 8) :
	byte = bits[i : i+8]

	value = 0

	for bit in byte :
		value = (value << 1) | bit

	data.append(value)

open("extracted", "wb").write(data)



