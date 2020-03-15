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