
import streamlit as st
from PIL import Image, ImageOps
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import scipy.ndimage as nd

st.set_page_config(layout="wide", page_title="MY DIP")
st.write("## HW05 백태희")
st.write(":dog:")
st.sidebar.write("## my sidebar")

def process_image(upload):
    image = Image.open(upload)
    col1.write("Input")
    col1.image(image)
    output = image.convert('L')
    col2.write("Output 1: grayscale")
    col2.image(output)
    output = ImageOps.equalize(output)
    col3.write("Output 2: histeq")
    col3.image(output)
    output = np.max(np.array(output)) - np.array(output)
    col4.write("Output 3 : image inversion")
    col4.image(output,clamp=True)

col1, col2, col3, col4 = st.columns(4)
my_upload = st.sidebar.file_uploader("Upload", type=["png","jpg","jpeg"])

if my_upload is not None:
    process_image(upload=my_upload)
else:
    image_path = Path(__file__).resolve().parent / "myphoto.jpg"
    process_image(str(image_path))




import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import scipy.ndimage as nd
from PIL import Image

I = Image.open(imgpath+'/myphoto1105.jpg').convert('L')
f = np.array(I)
plt.imshow(f,cmap='gray')
plt.axis('off')
plt.colorbar()
plt.show()

f_denoised = signal.medfilt2d(f,3)
plt.imshow(f_denoised,cmap='gray')
plt.axis('off')
plt.colorbar()
plt.show()
plt.hist(f_denoised.ravel(), bins=256, range=(0,256), color='gray')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
th_val = 128
f_mask = f_denoised > th_val
plt.imshow(f_mask,cmap='gray')
plt.axis('off')
plt.show()
labels, nums = nd.label(f_mask)
plt.imshow(labels,cmap='Spectral_r')
plt.axis('off')
plt.show()
cc = np.zeros((nums-1,2))
for i in range(1,nums):
  cc[i-1,0] = i
  cc[i-1,1] = np.sum(labels==i)
  print(f'index: {int(cc[i-1,0])}, number of pixels: {int(cc[i-1,1])}')
ind_max = np.argmax(cc[:,1])
print(f'the largest component: index {int(ind_max)}, # of pixels: {int(cc[ind_max,1])}')
ind_min = np.argmin(cc[:,1])
print(f'the smallest component: index {int(ind_min)}, # of pixels: {int(cc[ind_min,1])}')
plt.figure(figsize=(16,9))
plt.subplot(131)
plt.imshow(f,cmap='gray')
plt.axis('off')
plt.title('input image')
plt.subplot(132)
plt.imshow(labels==cc[ind_max,0],cmap='Spectral_r')
plt.axis('off')
plt.title('the largest component')
plt.subplot(133)
plt.imshow(labels==cc[ind_min,0],cmap='Spectral_r')
plt.axis('off')
plt.title('the smallest component')
plt.show()
#smallest component는 왜 안 보이는걸까... -> 픽셀 수가 너무 적어서 눈에 안 띄는 경우 !!
