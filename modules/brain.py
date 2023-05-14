"""

- 识别技能(命令、聊天)，返回要回复的字符串
- 进行工作
"""

from enum import Enum
import RPi.GPIO as GPIO
import modules.config as config

class Brain :

    def __init__(self, conversation) :
        self.conversation = conversation

    def Query(self, msg) :
        res = False

        if self.isfan(msg) == True:
            self.dofan(msg)
            res= True
        if self.islight(msg) == True:
            self.dolight(msg)
            res= True
        
        return res

    def isfan(self, msg):
        if "风扇" in msg:
            return True        
        return False
    
    def islight(self, msg):
        if "灯" in msg:
            return True
        return False
    
    def isclock(self, msg):
        if "闹钟" in msg:
            return True
        else:
            return False

    def ismusic(self, msg):
        if "放首" in msg:
            return True
        else:
            return False

    def dofan(self, msg):
        if self.parse_on_off(msg) == 1:
            GPIO.output(config.FAN_PIN, GPIO.LOW)
            self.conversation.doSay("开风扇成功")
        else:
            GPIO.output(config.FAN_PIN, GPIO.HIGH)
            self.conversation.doSay("关风扇成功")

    def dolight(self, msg):
        if self.parse_on_off(msg) == 1:
            GPIO.output(config.LIGHT_PIN, GPIO.LOW)
            self.conversation.doSay("开灯成功")
        else:
            GPIO.output(config.LIGHT_PIN, GPIO.HIGH)
            self.conversation.doSay("关灯成功")


    # 解析开关指令
    def parse_on_off(self, msg):
        if "开" in msg:
            return 1
        if "关" in msg:
            return 0
        
    # 解析时间
    def parse_time(self, msg):
        pass
     
        