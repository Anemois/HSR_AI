import pyautogui as pg
import time

class MouseController():
    def __init__(self):
        self.scrX, self.scrY = pg.size()
        self.initPos()

    def initPos(self):
        def initUltPos():
            self.ultPos = [[self.scrX*277//1920, self.scrY*895//1080], 
                        [self.scrX*505//1920, self.scrY*895//1080], 
                        [self.scrX*729//1920, self.scrY*895//1080], 
                        [self.scrX*955//1920, self.scrY*895//1080]]

        def initBasicPos():
            self.basicPos = [self.scrX*1645//1920, self.scrY*920//1080]

        def initSkillPos():
            self.skillPos = [self.scrX*1800//1920, self.scrY*840//1080]
        
        def initAutoPos():
            self.autoPos = [self.scrX*1760//1920, self.scrY*50//1080]

        initBasicPos()
        initSkillPos()
        initUltPos()
        initAutoPos()

    def changeTarget(self, target = None):
        for i in range(5):
            pg.press('a')
        for i in range(target):
            pg.press('d')

    def click(self, button = None):
        if(button == "basic"):
            pg.click(x=self.basicPos[0], y=self.basicPos[1])
            pg.click(x=self.basicPos[0], y=self.basicPos[1])
        elif(button == "skill"):
            pg.click(x=self.skillPos[0], y=self.skillPos[1])
            pg.click(x=self.skillPos[0], y=self.skillPos[1])
        elif("ult" in button):
            i = int(button[3])-1
            pg.click(x=self.ultPos[i][0], y=self.ultPos[i][1])
            pg.press(' ')
            time.sleep(1.5)
            for i in range(20):
                pg.press(' ')
                time.sleep(0.2)
            
