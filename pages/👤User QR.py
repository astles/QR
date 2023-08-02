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
Wp, Hp = (200,200)
qrsize = 5
qrborder = 4
labelsize = (730, 143)
Wt, Ht = (165, 165)
textloc = (155,30)
textsize = 10
textOnQr = 20
zipObj = ZipFile('myfile.zip', 'w')
W, H = (300,300)

# qrsize = (W, H)
# user_input = st.text_input("Enter User Name",)

# im = Image.new("RGB",(W,H,"yellow"))
# draw = ImageDraw.Draw(im)
# w, h = draw.textsize(name)
# qrTxtPos = ((W-w)/2,(H-h)/2)


## HORIZONTAL ALING TEST---
# font_size = 60
# text = 'your text'
# rgb_color = (255,255,255)

# img = Image.open('your-image.jpg')
# draw = ImageDraw.Draw(img)

# font = ImageFont.truetype('your-font.ttf', font_size)

# w, h = draw.textsize(text, font)

# left = (img.width - w) / 2
# top = 22

st.title("🏁USER - QR code generator")
uploaded_file = st.file_uploader("Choose a file. Make sure your header is USER in your table")

name = st.text_input("User Name for QR")
email = st.text_input("User Email")



# if not name:
#   st.warning("Please Input user Name ")
if name is not None:

  # Create qr code instance
  qru = qrcode.QRCode(
    version = 2,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = qrsize,
    border = qrborder,
  )
  print(email)



## CREATE NEW IMAGE
  msg = "STest Name "
  pic = Image.new("RGB", (Wp, Hp), "white")

  draw = ImageDraw.Draw(pic)
  wp, hp = draw.textsize("msg")
  font = ImageFont.truetype("fonts/HelveticaBold.ttf", textOnQr)
  _, _, wp, hp = draw.textbbox((0, 0), msg, font=font)
  draw.text(((Wp-wp)/2,0),msg, fill="black",anchor= "la", align='left',  font=font)
  draw.text(((Wp-wp)/2,30),msg, fill="black",anchor= "la", align='left',  font=font)
  
  # st.image(pic)


  imgext = '.png'
  # Add data
  qru.add_data(f"{email}")
  qru.make(fit=True)


  # Create an image from the QR Code instance
  imgqru = qru.make_image()
  imgqru = imgqru.convert("RGB")
  # imgqru = ImageChops.invert(imgqru)

  

  #QR TEXT
  drawtxt = ImageDraw.Draw(imgqru)
 
  # GET IMAGE SIZE
  print(imgqru.size)
  Himg, Wimg = imgqru.size
  print(Himg)
  ##TEXT SPLIT UP
  namebrake = (f"{name}")
  #split string by single space

  chunks = namebrake.split(' ')
  topname = chunks[0]
  botname = chunks[1]

  print(botname)

  font = ImageFont.truetype("fonts/HelveticaBold.ttf", textOnQr)
  w, h = drawtxt.textsize(f"{name}")
  _, _, wpt, hp = draw.textbbox((0, 0), topname, font=font)
  _, _, wpb, hp = draw.textbbox((0, 0), botname, font=font)
  ## Single Line Name Text
  # drawtxt.text(((Wt-wp)/2, 0),(f"{name}") ,fill=(0,0,0),anchor= "la", align='center',  font=font)

  drawtxt.text(((Wimg-wpt)/2, 0), topname ,fill=(0,0,0),anchor= "la", align='center',  font=font)
  drawtxt.text(((Wimg-wpb)/2, (Himg-20)), botname ,fill=(0,0,0),anchor= "la", align='center',  font=font)
  # drawtxt.text((0,0),(f"{name}") ,fill=(0,0,0), font=font)
  # drawtxt.text((qrTxtPos), name, fill="black", font=font)


  #IMAGE DISPLAYED IN STREAMLIT
  st.image(imgqru)


#----------------------
  # bkrnd = Image.new("RGB", (Wt, Ht), "white")
  # draw = ImageDraw.Draw(bkrnd)
  # w, h = draw.textsize(f"{USER}")
  # # draw.text(textloc,(f"{USER}") ,fill=(0,0,0), font=font)
  # draw.text(((Wt-w)/2,(Ht-h)/2),(f"{USER}") ,fill=(0,0,0), font=font)
  # bkrnd1 = bkrnd.copy()
  # bkrnd1.paste(qrimg)




#-------------------------








  from io import BytesIO
  buf = BytesIO()
  imgqru.save(buf, quality=100, dpi=(200, 200), format="png")
  byte_im = buf.getvalue()

  #DOWNLOAD INDIVIDUAL
  btn2 = st.download_button(
    label="Download Image",
    data=byte_im,
    file_name=f"{email}.png",
    # mime="image/png",
    mime="k",
  )

##-----------TABLE INPUT-----------------------------------------------------------##

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  print(df.to_string())
  df = df[df.notnull().all(1)]
  expander = st.expander("SEE TABLE DATA")
  expander.write(df)
  # st.write(df)

  data = df['USER'] 

  data = df['USER'] 
    



  for index, values in df.iterrows(): 
    USER = values["USER"]


  # Create qr code instance
    qr = qrcode.QRCode(
      version = 1,
      error_correction = qrcode.constants.ERROR_CORRECT_H,
      box_size = qrsize,
      border = qrborder,
    )

  
    imgext = '.png'
    # Add data
    qr.add_data(f"{USER}")
    qr.make(fit=True)
    

    # Create an image from the QR Code instance
    img = qr.make_image()
    img = img.convert("RGB")
    img = ImageChops.invert(img)


    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("fonts/HelveticaBold.ttf", textsize)
    #QR TEXT
    #draw.text((10,10),(f"{USER}") ,fill=(0,0,0), font=font)
    
    # img.save (f"{USER}.png")
    # image = pyqrcode.create(data)
    #         image.svg(f"{v['USER']}.svg", scale="5")
    #single QR CODE
    #st.image(img)

    qrimg = (img)

    bkrnd = Image.new("RGB", (Wt, Ht), "white")
    draw = ImageDraw.Draw(bkrnd)
    w, h = draw.textsize(f"{USER}")
    # draw.text(textloc,(f"{USER}") ,fill=(0,0,0), font=font)
    draw.text(((Wt-w)/2,(Ht-h)/2),(f"{USER}") ,fill=(0,0,0), font=font)
    bkrnd1 = bkrnd.copy()
    bkrnd1.paste(qrimg)


    ##Backup
    # bkrnd = Image.new("RGB", labelsize, "white")
    # draw = ImageDraw.Draw(bkrnd)
    # draw.text(textloc,(f"{USER}") ,fill=(0,0,0), font=font)
    # bkrnd1 = bkrnd.copy()
    # bkrnd1.paste(qrimg)



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
    # img.save (f"{USER}.png")


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

    with open(f"{USER}.png", 'wb') as f: 
       f.write(byte_im)
        
    zipObj.write(f"{USER}.png")
    
    # DOWNLOAD INDIVIDUAL
    # btn = st.download_button(
    #     label="Download Image",
    #     data=byte_im,
    #     file_name=f"{USER}.png",
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

