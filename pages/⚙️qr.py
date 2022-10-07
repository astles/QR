from cProfile import label
from ctypes.wintypes import SIZE
from io import BytesIO
import streamlit as st
import pandas as pd
import qrcode #  qrcode[pil]
import qrcode.image.svg
import pyqrcode
#IMPORT ZIP FILE
from zipfile import ZipFile
from math import trunc
import numpy as np
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from  PIL import ImageEnhance
from PIL import ImageChops
# from PIL import tempfile



##-----------VARIABLES-------------------

qrsize = 5
qrborder = 2
labelsize = (730, 143)
textloc = (155,30)
textsize = 100
zipObj = ZipFile('myfile.zip', 'w')



st.title("🏁DEVICE - QR code generator")
uploaded_file = st.file_uploader("Choose a file. Make sure your header is DEVICE in your table")
#df=NULL



# #user_input = st.text_input("Enter User Name",)
# name = st.text_input("User Name for QR")
# if not name:
#   st.warning("Please Input user Name ")




  
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  print(df.to_string())
  expander = st.expander("SEE TABLE DATA")
  expander.write(df)
  # st.write(df)
  
  data = df['DEVICE'] 
  data = df['DEVICE'] 
  



  for index, values in df.iterrows(): 
    DEVICE = values["DEVICE"]


  # Create qr code instance
    qr = qrcode.QRCode(
      version = 1,
      error_correction = qrcode.constants.ERROR_CORRECT_H,
      box_size = qrsize,
      border = qrborder,
    )

  
    imgext = '.png'
    # Add data
    qr.add_data(f"{DEVICE}")
    qr.make(fit=True)
    

    # Create an image from the QR Code instance
    img = qr.make_image()
    img = img.convert("RGB")
    img = ImageChops.invert(img)


    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("fonts/HelveticaBold.ttf", textsize)
    #QR TEXT
    #draw.text((10,10),(f"{DEVICE}") ,fill=(0,0,0), font=font)
    
    # img.save (f"{DEVICE}.png")
    # image = pyqrcode.create(data)
    #         image.svg(f"{v['DEVICE']}.svg", scale="5")
    #single QR CODE
    #st.image(img)

    qrimg = (img)

    bkrnd = Image.new("RGB", labelsize, "white")
    draw = ImageDraw.Draw(bkrnd)
    draw.text(textloc,(f"{DEVICE}") ,fill=(0,0,0), font=font)
    bkrnd1 = bkrnd.copy()
    bkrnd1.paste(qrimg)


    # Add data
    qr.add_data(data)
    qr.make(fit=True)
    im = bkrnd1

    # Passing the image object to invert() 
    # inv_img = ImageChops.invert(img)
  
    im_invert = ImageChops.invert(im)
    # im_invert = Image.open(f"./Images/UsersImages/001.png")
    im_invert = im_invert.resize(labelsize) ### EDITED LINE
    # im_invert.show()





    #IMAGE DISPLAYED IN STREAMLIT
    st.image(bkrnd1)
    #IMAGE INVERTED
    # st.image(im_invert)
    # img.save (f"{DEVICE}.png")


    # Save it 
    # img.save("image.png")
    # img.save("image.bmp")
    # img.save("image.jpeg")
    # st.img.save("image.png")
    buf = BytesIO()
    bkrnd.save(buf, quality=100, dpi=(500, 500), format="png")
    #tee = (bkrnd.save(buf, format="png"))
    byte_im = buf.getvalue()
    
    # DOWNLOAD BUTTON
    from io import BytesIO
    buf = BytesIO()
    bkrnd1.save(buf, quality=100, dpi=(500, 500), format="png")
    byte_im = buf.getvalue()

    with open(f"{DEVICE}.png", 'wb') as f: 
       f.write(byte_im)
        
    zipObj.write(f"{DEVICE}.png")
    
    # DOWNLOAD INDIVIDUAL
    # btn = st.download_button(
    #     label="Download Image",
    #     data=byte_im,
    #     file_name=f"{DEVICE}.png",
    #     # mime="image/png",
    #     mime="application/zip",
    #   )
  

  zipObj.close()
  with open("myfile.zip", "rb") as fp:
    btn = st.download_button(
        label="Download zip",
        data=fp,
        file_name="myfile.zip",
        mime="application/zip"
    )

