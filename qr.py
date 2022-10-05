
from io import BytesIO
import streamlit as st
import pandas as pd
import qrcode #  qrcode[pil]
import qrcode.image.svg
import pyqrcode

from math import trunc
import numpy as np
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from  PIL import ImageEnhance


uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  print(df.to_string())
  st.write(df)
  data = df['DEVICE'] 
  data = df['DEVICE'] 
  # texts = "you,you"
  # image = pyqrcode.create(texts)
  # image.svg("QR.svg", scale="5")
  # st.image('image.svg')

for index, values in df.iterrows(): 
  DEVICE = values["DEVICE"]
# st.download_button(
#     label="Download Image",
#     data=image.jpg,
#     file_name="imagename.svg",
#     mime="image/svg"
# )

# Create qr code instance
  qr = qrcode.QRCode(
    version = 2,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 4,
    border = 4,
  )

 
  imgext = '.png'
  # Add data
  qr.add_data(f"{DEVICE}")
  qr.make(fit=True)
  

  # Create an image from the QR Code instance
  img = qr.make_image()
  img = img.convert("RGB")


  draw = ImageDraw.Draw(img)
  font = ImageFont.truetype("fonts/HelveticaBold.ttf", 26)

  draw.text((10,0),(f"{DEVICE}") ,fill=(0,0,0), font=font)
  
  img.save (f"{DEVICE}.png")
  # image = pyqrcode.create(data)
  #         image.svg(f"{v['DEVICE']}.svg", scale="5")

  st.image(img)

  # Add data
  qr.add_data(data)
  qr.make(fit=True)


  # Create an image from the QR Code instance
  st.img = qr.make_image()

  img = qrcode.make(data)

  # Save it somewhere, change the extension as needed:
  # img.save("image.png")
  # img.save("image.bmp")
  # img.save("image.jpeg")
  st.img.save("image.jpg")



st.title("QR code generator")
