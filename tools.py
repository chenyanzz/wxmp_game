import werobot
import werobot.client


robot = None

def prn_obj(obj): 
  print ('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))

#@param msg: 用户的msg类
def createImageReply(msg, pic_path):
    ret = robot.client.upload_media("image",open(pic_path, mode='rb'))
    pic_id = ret["media_id"]
    return werobot.replies.ImageReply(msg,media_id=pic_id)

#@param msg: 用户的msg类
def createVoiceReply(msg, rec_path):
    ret = robot.client.upload_media("voice",open(rec_path, mode='rb'))
    rec_id = ret["media_id"]
    return werobot.replies.VoiceReply(msg,media_id=rec_id)


# from PIL import Image, ImageDraw, ImageFont
# 处理我也不知道啥图片：加文自
# def IDontKnow():
#   image = Image.open('m.jpg')

#   font = ImageFont.truetype('./华文行楷.ttf', 136)
#   # 创建Draw对象:
#   draw = ImageDraw.Draw(image)

#   draw.text((100, 100), "喵喵喵！", font=font, fill=(125,23,80))

#   image.save('out.jpg', 'jpeg')