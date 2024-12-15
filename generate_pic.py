from PIL import Image,ImageDraw,ImageFont

image=Image.new('RGB',(500,500),color='white')

draw=ImageDraw.Draw(image)
# draw.rectangle([100,100,400,400],fill='blue')
font_path="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
font_large=ImageFont.truetype(font_path,size=80)
draw.text((150,200),"Hi",fill='black',font=font_large)

image.save('uploads/output_image.jpg')