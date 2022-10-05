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
from PIL import ImageChops

st.title("QR code generator")
uploaded_file = st.file_uploader("Choose a file")
#df=NULL
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  print(df.to_string())
  st.write(df)
  data = df['DEVICE'] 
  data = df['DEVICE'] 
  

for index, values in df.iterrows(): 
  DEVICE = values["DEVICE"]


# Create qr code instance
  qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 4,
    border = 1,
  )

 
  imgext = '.png'
  # Add data
  qr.add_data(f"{DEVICE}")
  qr.make(fit=True)
  

  # Create an image from the QR Code instance
  img = qr.make_image()
  img = img.convert("RGB")


  draw = ImageDraw.Draw(img)
  font = ImageFont.truetype("fonts/HelveticaBold.ttf", 50)
  #QR TEXT
  #draw.text((10,10),(f"{DEVICE}") ,fill=(0,0,0), font=font)
  
  img.save (f"{DEVICE}.png")
  # image = pyqrcode.create(data)
  #         image.svg(f"{v['DEVICE']}.svg", scale="5")
  #single QR CODE
  #st.image(img)

  qrimg = (img)

  bkrnd = Image.new("RGB", (270, 90), "white")
  draw = ImageDraw.Draw(bkrnd)
  draw.text((100,20),(f"{DEVICE}") ,fill=(0,0,0), font=font)
  bkrnd1 = bkrnd.copy()
  bkrnd1.paste(qrimg)


  # Add data
  qr.add_data(data)
  qr.make(fit=True)
  im = bkrnd1

  # Passing the image object to invert() 
  # inv_img = ImageChops.invert(img)
 
  im_invert = ImageChops.invert(im)
  #IMAGE DISPLAYED IN STREAMLIT
  st.image(bkrnd1)
  #IMAGE INVERTED
  st.image(im_invert)


  # Save it 
  # img.save("image.png")
  # img.save("image.bmp")
  # img.save("image.jpeg")
#   st.img.save("image.png")
  buf = BytesIO()
  img.save(buf, format="png")
  byte_im = buf.getvalue()
  
  # DOWNLOAD BUTTON
  from io import BytesIO
  buf = BytesIO()
  img.save(buf, format="png")
  byte_im = buf.getvalue()
  btn = st.download_button(
      label="Download Image",
      data=byte_im,
      file_name=f"{DEVICE}.png",
      mime="image/png",
      )

  
  #btn = st.download_button( label="Download ZIP", data=st.img, file_name="myfile.zip", mime="application/zip" )


