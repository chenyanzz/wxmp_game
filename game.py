# -*- coding: utf-8 -*-  


import conf
import texts
import tools
import time
import re

handler_list = []

# 有顺序的！
def GameHandler(fn):
    handler_list.append(fn)

InputAnythingToGo = "\n\n【回复任意文字以继续】"
InputAnswerToGo = "\n\n【回复答案以继续，请使用阿拉伯数字】"
AnsRight = "【正确，继续游戏】\n\n"
AnsWrong = "【回答错误请重试】"

@GameHandler
def newGameHandler(msg, session):
    if msg.Content != "第七个人":
        return "输入'第七个人'开始游戏哦。"
    session["phase"] += 1
    return '''
    输入姓名以开始游戏<第七个人>！
    (如输入错误，游戏中随时输入‘重新开始’以改过自新)

    Program By 顾晓cy
    Directed By 七朵金花
    '''

@GameHandler
def inputNameHandler(msg, session):
    name = msg.Content
    session["name"] = name
    session["phase"] += 1
    session["start_time"] = time.time()

    return "欢迎进入游戏，%s！"%name + InputAnythingToGo

@GameHandler
def Act1_1_handler(msg, session):
    session["phase"] += 1
    return "【第一幕  一审】" + InputAnythingToGo

@GameHandler
def Act1_1_handler(msg, session):
    session["phase"] += 1
    return texts.Act_1_1 + InputAnythingToGo

@GameHandler
def Act1_2_handler(msg, session):
    session["phase"] += 1
    return texts.Act_1_2 + InputAnythingToGo

@GameHandler
def Act1_3_handler(msg, session):
    session["phase"] += 1
    return texts.Act_1_3 + InputAnythingToGo

@GameHandler
def Act1_4_handler(msg, session):
    session["phase"] += 1
    return texts.Act_1_4 + InputAnythingToGo

@GameHandler
def Act1_5_handler(msg, session):
    session["phase"] += 1
    return texts.Act_1_5 + InputAnythingToGo

@GameHandler
def Act1_6_handler(msg, session):
    session["phase"] += 1
    return texts.Act_1_6+ InputAnythingToGo

@GameHandler
def Act1_7_handler(msg, session):
    session["phase"] += 1
    return texts.Act_1_7 + InputAnythingToGo

@GameHandler
def Act1_8_handler(msg, session):
    session["phase"] += 1
    return texts.Act_1_8 + InputAnythingToGo

@GameHandler
def Act1_9_handler(msg, session):
    session["phase"] += 1
    return texts.Act_1_9 + InputAnythingToGo

@GameHandler
def Act2_handler(msg, session):
    session["phase"] += 1
    return "【第二幕  搜证】" + InputAnythingToGo

@GameHandler
def Act2_1_handler(msg, session):
    session["phase"] += 1
    return texts.Act_2_1 + InputAnythingToGo

# 题目1-提问
@GameHandler
def Act2_2_handler(msg, session):
    session["phase"] += 1
    return texts.Act_2_2 + InputAnswerToGo + "\n【PS：你还有%d次输入“不会”的跳过机会】"%session["skip_times_left"]

# 题目1-解答
@GameHandler
def Act2_3_a_handler(msg, session):
    ans = msg.Content
    if ans == "不会" :
        if session["skip_times_left"] > 0:
            session["skip_times_left"] -= 1
            ans = "3"
        else:
            return "跳过机会用尽！"

    if ans == "3" :
        session["phase"] += 1
        return texts.Act_2_3_a + InputAnythingToGo
    else:
        return AnsWrong

@GameHandler
def Act2_3_v1_handler(msg, session):
    session["phase"] += 1
    return tools.createVoiceReply(msg,"./rc/Act2_3_v1.mp3")

@GameHandler
def Act2_3_b_handler(msg, session):
    session["phase"] += 1
    return texts.Act_2_3_b+ InputAnythingToGo

@GameHandler
def Act2_3_v2_handler(msg, session):
    session["phase"] += 1
    return tools.createVoiceReply(msg,"./rc/Act2_3_v2.mp3")

@GameHandler
def Act2_3_c_handler(msg, session):
    session["phase"] += 1
    return texts.Act_2_3_c+ InputAnythingToGo

@GameHandler
def Act2_3_v3_handler(msg, session):
    session["phase"] += 1
    return tools.createVoiceReply(msg,"./rc/Act2_3_v3.mp3")

@GameHandler
def Act2_3_d_handler(msg, session):
    session["phase"] += 1
    return texts.Act_2_3_d+ InputAnythingToGo

@GameHandler
def Act2_4_handler(msg, session):
    session["phase"] += 1
    return texts.Act_2_4+ InputAnythingToGo

# 题目2-提问
@GameHandler
def Act2_5_handler(msg, session):
    session["phase"] += 1
    return texts.Act_2_5 + InputAnswerToGo + "\n【PS：你还有%d次输入“不会”的跳过机会】"%session["skip_times_left"]

# 题目2-解答
@GameHandler
def Act2_6_a_handler(msg, session):
    ans = msg.Content
    if ans == "不会" :
        if session["skip_times_left"] > 0:
            session["skip_times_left"] -= 1
            ans = "9:20"
        else:
            return "跳过机会用尽！"
    
    result = re.match(r"(\d+)[:：](\d+)",ans)
    h = m = 0
    if result!=None:
        h = int(result.group(1))
        m = int(result.group(2))

    if h==9 and m in range(31):
        session["phase"] += 1
        return texts.Act_2_6_a + InputAnythingToGo
    else:
        return AnsWrong

@GameHandler
def Act2_6_v1_handler(msg, session):
    session["phase"] += 1
    return tools.createVoiceReply(msg,"./rc/Act2_6_v1.mp3")

@GameHandler
def Act2_6_b_handler(msg, session):
    session["phase"] += 1
    return texts.Act_2_6_b+ InputAnythingToGo

@GameHandler
def Act2_6_v2_handler(msg, session):
    session["phase"] += 1
    return tools.createVoiceReply(msg,"./rc/Act2_6_v2.mp3")

# 题目3-提问
@GameHandler
def Act2_7_handler(msg, session):
    session["phase"] += 1
    return texts.Act_2_7 + "【PS：你还有%d次输入“不会”的跳过机会】"%session["skip_times_left"]

# 题目3-解答
# 题目4-提问
@GameHandler
def Act2_8_handler(msg, session):
    ans = msg.Content
    if ans == "不会" :
        if session["skip_times_left"] > 0:
            session["skip_times_left"] -= 1
            ans = "留"
        else:
            return "跳过机会用尽！"

    if ans == "留" :
        session["phase"] += 1
        return texts.Act_2_8 + InputAnswerToGo + "\n【PS：你还有%d次输入“不会”的跳过机会】"%session["skip_times_left"]
    else:
        return AnsWrong

# 题目4-解答
# 题目5-提问
@GameHandler
def Act2_9_handler(msg, session):
    ans = msg.Content
    if ans == "不会" :
        if session["skip_times_left"] > 0:
            session["skip_times_left"] -= 1
            ans = "0.25"
        else:
            return "跳过机会用尽！"

    if ans in ("0.25", "1/4", "25%") :
        session["phase"] += 1
        return texts.Act_2_9 + InputAnswerToGo + "\n【PS：你还有%d次输入“不会”的跳过机会】"%session["skip_times_left"]
    else:
        return AnsWrong

# 题目5-解答
# 题目6-提问
@GameHandler
def Act2_10_a_handler(msg, session):
    ans = msg.Content
    if ans == "不会" :
        if session["skip_times_left"] > 0:
            session["skip_times_left"] -= 1
            ans = "能"
        else:
            return "跳过机会用尽！"

    if ans == "能" :
        session["phase"] += 1
        return texts.Act_2_10_a + InputAnythingToGo
    else:
        return AnsWrong

@GameHandler
def Act2_10_v_handler(msg, session):
    session["phase"] += 1
    return tools.createVoiceReply(msg,"./rc/Act2_10_v.mp3")

@GameHandler
def Act2_10_b_handler(msg, session):
    session["phase"] += 1
    return texts.Act_2_10_b + InputAnswerToGo + "\n【PS：你还有%d次输入“不会”的跳过机会】"%session["skip_times_left"]

# 题目6-解答
# 题目7-提问
@GameHandler
def Act2_11_handler(msg, session):
    ans = msg.Content
    if ans == "不会" :
        if session["skip_times_left"] > 0:
            session["skip_times_left"] -= 1
            ans = "是"
        else:
            return "跳过机会用尽！"

    if ans == "是" :
        session["phase"] += 1
        return texts.Act_2_11 + InputAnswerToGo + "\n【PS：你还有%d次输入“不会”的跳过机会】"%session["skip_times_left"]
    else:
        return AnsWrong

# 题目7-解答
# 题目8-提问
@GameHandler
def Act2_12_handler(msg, session):
    ans = msg.Content
    if ans == "不会" :
        if session["skip_times_left"] > 0:
            session["skip_times_left"] -= 1
            ans = "75"
        else:
            return "跳过机会用尽！"

    if ans in ("75", "75分") :
        session["phase"] += 1
        return texts.Act_2_12 + InputAnswerToGo + "\n【PS：你还有%d次输入“不会”的跳过机会】"%session["skip_times_left"]
    else:
        return AnsWrong

# 题目8-解答
# 题目9-提问
@GameHandler
def Act2_13_a_handler(msg, session):
    ans = msg.Content
    if ans == "不会" :
        if  session["skip_times_left"] > 0:
            session["skip_times_left"] -= 1
            ans = "2"
        else:
            return "跳过机会用尽！"

    if ans == "2" :
        session["phase"] += 1
        return texts.Act_2_13_a + InputAnythingToGo
    else:
        return AnsWrong

@GameHandler
def Act2_13_v_handler(msg, session):
    session["phase"] += 1
    return tools.createVoiceReply(msg,"./rc/Act2_13_v.mp3")

@GameHandler
def Act2_13_b_handler(msg, session):
    session["phase"] += 1
    return texts.Act_2_13_b + InputAnswerToGo + "\n【PS：你还有%d次输入“不会”的跳过机会】"%session["skip_times_left"]

# 题目9-解答
# 题目10-提出
@GameHandler
def Act2_14_a_handler(msg, session):
    ans = msg.Content
    if ans == "不会" :
        if session["skip_times_left"] > 0:
            session["skip_times_left"] -= 1
            ans = "2"
        else:
            return "跳过机会用尽！"

    if ans == "2" :
        session["phase"] += 1
        return texts.Act_2_14_a + InputAnythingToGo
    else:
        return AnsWrong

@GameHandler
def Act2_14_v_handler(msg, session):
    session["phase"] += 1
    return tools.createVoiceReply(msg,"./rc/Act2_14_v.mp3")

@GameHandler
def Act2_14_b_handler(msg, session):
    session["phase"] += 1
    return texts.Act_2_14_b + InputAnswerToGo + "\n【PS：你还有%d次输入“不会”的跳过机会】"%session["skip_times_left"]

# 题目10-图片
@GameHandler
def Act2_15_handler(msg, session):
    session["phase"] += 1
    return tools.createImageReply(msg,"./rc/T11.jpg")

# 题目10-解答
# 题目11-提出
@GameHandler
def Act2_16_a_handler(msg, session):
    ans = msg.Content
    if ans == "不会" :
        if session["skip_times_left"] > 0:
            session["skip_times_left"] -= 1
            ans = "24"
        else:
            return "跳过机会用尽！"

    if ans == "24" :
        session["phase"] += 1
        return texts.Act_2_16_a + InputAnythingToGo
    else:
        return AnsWrong

@GameHandler
def Act2_16_v1_handler(msg, session):
    session["phase"] += 1
    return tools.createVoiceReply(msg,"./rc/Act2_16_v1.mp3")

@GameHandler
def Act2_16_b_handler(msg, session):
    session["phase"] += 1
    return texts.Act_2_16_b+ InputAnythingToGo

@GameHandler
def Act2_16_v2_handler(msg, session):
    session["phase"] += 1
    return tools.createVoiceReply(msg,"./rc/Act2_16_v2.mp3")

@GameHandler
def Act2_16_c_handler(msg, session):
    session["phase"] += 1
    return texts.Act_2_16_c+ InputAnythingToGo

@GameHandler
def Act2_16_v3_handler(msg, session):
    session["phase"] += 1
    return tools.createVoiceReply(msg,"./rc/Act2_16_v3.mp3")

@GameHandler
def Act2_16_d_handler(msg, session):
    session["phase"] += 1  
    return texts.Act_2_16_d + InputAnswerToGo + "\n【PS：你还有%d次输入“不会”的跳过机会】"%session["skip_times_left"]

# 题目11-图片
@GameHandler
def Act2_17_handler(msg, session):
    session["phase"] += 1
    return tools.createImageReply(msg,"./rc/T12.jpg")

# 题目11-解答
@GameHandler
def Act2_18_handler(msg, session):
    ans = msg.Content
    if ans == "不会" :
        if session["skip_times_left"] > 0:
            session["skip_times_left"] -= 1
            ans = "45"
        else:
            return "跳过机会用尽！"

    if ans == "45" :
        session["phase"] += 1
        return texts.Act_2_18 + InputAnythingToGo
    else:
        return AnsWrong

@GameHandler
def Act3_handler(msg, session):
    session["phase"] += 1
    return "【第三幕  二审】" + InputAnythingToGo

@GameHandler
def Act3_1_handler(msg, session):
    session["phase"] += 1
    return texts.Act_3_1 + InputAnythingToGo

@GameHandler
def Act3_2_handler(msg, session):
    session["phase"] += 1
    return texts.Act_3_2 + InputAnythingToGo

@GameHandler
def Act3_3_handler(msg, session):
    session["phase"] += 1
    return texts.Act_3_3 + InputAnythingToGo

@GameHandler
def Act3_4_handler(msg, session):
    session["phase"] += 1
    return texts.Act_3_4 + InputAnythingToGo

@GameHandler
def Act3_5_handler(msg, session):
    session["phase"] += 1
    return texts.Act_3_5 + InputAnythingToGo

@GameHandler
def Act3_6_handler(msg, session):
    session["phase"] += 1
    return texts.Act_3_6 + InputAnythingToGo

@GameHandler
def Act3_7_handler(msg, session):
    session["phase"] += 1
    return texts.Act_3_7 + InputAnythingToGo

@GameHandler
def Act3_8_handler(msg, session):
    session["phase"] += 1
    return texts.Act_3_8 + InputAnythingToGo

@GameHandler
def Act3_8_v_handler(msg, session):
    session["phase"] += 1
    return tools.createVoiceReply(msg,"./rc/Act3_8_v.mp3")

@GameHandler
def Act3_9_handler(msg, session):
    session["phase"] += 1
    return texts.Act_3_9 + InputAnythingToGo

@GameHandler
def Act3_10_handler(msg, session):
    session["phase"] += 1
    return texts.Act_3_10 + InputAnythingToGo

@GameHandler
def Act3_11_handler(msg, session):
    session["phase"] += 1
    return texts.Act_3_11 + InputAnythingToGo

@GameHandler
def Act3_12_handler(msg, session):
    session["phase"] += 1
    return texts.Act_3_12 + InputAnythingToGo

@GameHandler
def Act3_13_handler(msg, session):
    session["phase"] += 1
    return texts.Act_3_13 + InputAnythingToGo

@GameHandler
def Ans_1_handler(msg, session):
    session["phase"] += 1
    return '''
    恭喜你完成剧情，下面请给出你的猜测：
    （回复完以下四个问题才算成功哦。）
    
    你猜测的凶手是：
    '''

@GameHandler
def Ans_2_handler(msg,session):
    session["phase"] += 1
    session["ans.killer"] = msg.Content
    return '''
    作案动机：
    '''

@GameHandler
def Ans_2_handler(msg,session):
    session["phase"] += 1
    session["ans.motivation"] = msg.Content
    return '''
    杀人手法（包括但不限于时间线，作案方法，或者如何排除其他人的嫌疑）：
    '''

@GameHandler
def Ans_3_handler(msg,session):
    session["phase"] += 1
    session["ans.method"] = msg.Content
    return '''
    其他（你的建议，意见，什么都可以）：
    '''

@GameHandler
def Ans_4_handler(msg,session):
    session["phase"] += 1
    session["ans.advice"] = msg.Content

    ans = {
        "name" : session["name"],
        "killer" : session["ans.killer"],
        "motivation" : session["ans.motivation"],
        "method" :  session["ans.method"],
        "advice" : session["ans.advice"],
        "used_time" : time.time()-session["start_time"],
    }


    import json
    json_str = json.dumps(ans, indent=4, ensure_ascii=False)
    file = open("./ans/%s.json"%msg.FromUserName, "w", encoding='utf-8')
    file.write(json_str)
    file.close()

    return  '''
    恭喜完成游戏！
    撒花✿✿
    '''

@GameHandler
def End_handler(msg,session):
    return '''
    恭喜完成游戏！
    撒花✿✿
    '''

def nullHandler(msg, session):
    return "owchhhh系统出错了"

def printPhaseId():
    print("phases of game:")
    for phase in range(len(handler_list)):
        print("phase[%d] : %s"%(
            phase,handler_list[phase].__name__
        ))

printPhaseId()

def onUserReply(msg, session):
    uid = msg.FromUserName
    text = msg.Content

    m = re.match(r"GOTO (\d+)", text, re.IGNORECASE)

    if None != m:
        session["phase"] = int(m.group(1))


    if text=="重新开始":
        session.clear()

    if "phase" not in session:
        session["phase"] = 0
        session["uid"] = uid
        session["skip_times_left"] = conf.MaxSkipTimes
    
    phase = session["phase"]
    if phase > 1:
        name = session["name"]
        print("==== %s @ %s :%s ===="%(
            name, handler_list[phase].__name__, text
        ))

    handler = nullHandler
    if phase < len(handler_list):
        handler = handler_list[phase]
        
    return handler(msg, session)
