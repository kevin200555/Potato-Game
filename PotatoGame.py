from time import *
from graphics import *
from button import Button
class clicker():
    def __init__(self,perClick,percentBoost):
        self.perClick = perClick
        self.percentBoost = percentBoost
    def getperClick(self):
        return self.perClick
    def percentBoost(self):
        return self.percentBoost
    def changeperClick(self,x):
        self.perClick = x
    def changepercentBoost(self,x):
        self.percentBoost = x
        
class buildings():
    """
    Plant      (1)
    Field      (50)
    Farm       (10000)
    Plantation (500000)
    GreenHouse (1000000000)
    """
    def __init__(self,plantNum,fieldNum,farmNum,platNum,greNum,plantBoost,fieldBoost,farmBoost,platBoost,greBoost):
        self.plantNum = plantNum
        self.fieldNum = fieldNum
        self.farmNum = farmNum
        self.platNum = plantNum
        self.greNum = greNum
        self.totalNum = plantNum + fieldNum + farmNum + platNum + greNum
        
        self.plantBoost = plantBoost
        self.fieldBoost = fieldBoost
        self.farmBoost = farmBoost
        self.platBoost = platBoost
        self.greBoost = greBoost

        self.plantPerSec = plantNum * plantBoost
        self.fieldPerSec = (fieldNum * 50) * fieldBoost
        self.farmPerSec = (farmNum * 10000) * farmBoost
        self.platPerSec = (platNum * 500000) * platBoost
        self.grePerSec = (greNum * 1000000000) * greBoost

        self.potatoPerClick = 1 + (plantNum + (fieldNum * 5) + (farmNum * 100) + (platNum * 5000) + (greNum * 10000000))
        
    def updatebuildings(self):
        self.plantPerSec = self.plantNum * self.plantBoost
        self.fieldPerSec = (self.fieldNum * 50) * self.fieldBoost
        self.farmPerSec = (self.farmNum * 10000) * self.farmBoost
        self.platPerSec = (self.platNum * 500000) * self.platBoost
        self.grePerSec = (self.greNum * 1000000000) * self.greBoost
        
    def getPlantCost(self):
        if self.plantNum == 0:
            return 1
        return round(self.plantNum * 1.1 * 1)
    def getFieldCost(self):
        if self.fieldNum == 0:
            return 50
        return round(self.fieldNum * 1.1 * 50)
    def getFarmCost(self):
        if self.farmNum == 0:
            return 10000
        return round(self.farmNum * 1.1 * 10000)
    def getPlatCost(self):
        if self.platNum == 0:
            return 500000
        return round(self.platNum * 1.1 * 500000)
    def getGreCost(self):
        if self.greNum == 0:
            return 1000000000
        return round(self.greNum * 1.1 * 1000000000)
    def getPotatoPerClick(self):
        return 1 + (self.plantNum + (self.fieldNum * 5) + (self.farmNum * 100) + (self.platNum * 5000) + (self.greNum * 10000000))
    def getTotalPerSec(self):
        self.Total = self.plantPerSec + self.fieldPerSec + self.farmPerSec + self.platPerSec + self.grePerSec
        return self.Total
    def save(self):
        return [self.plantNum,self.fieldNum,self.farmNum,self.platNum,self.greNum,self.plantBoost,self.fieldBoost,self.farmBoost,self.platBoost,self.greBoost]
class PotatoGame():
    def __init__(self,name,Potatos):
        self.name = name
        self.Potatos = Potatos
        self.saveFile = []
    def getName(self):
        return self.name
    def getPotatos(self):
        return self.Potatos
    def changePotatos(self,x):
        self.Potatos = x
    def save(self):
        return [self.name,int(self.Potatos)]

def shortenNumber(number):
    num = float(number)
    if num > 1000000000000000:
        num = round(num / 1000000000000000,2)
        return str(num) + "Q"
    elif num > 1000000000000:
        num = round(num / 1000000000000,2)
        return str(num) + "T"
    elif num > 1000000000:
        num = round(num / 1000000000,2)
        return str(num) + "B"
    elif num > 1000000:
        num = round(num / 1000000,2)
        return str(num) + "M"
    elif num > 1000:
        num = round(num / 1000,2)
        return str(num) + "K"
    return number
def main():
    win = GraphWin("Potato Game",750,750)
    win.setCoords(0, 0, 75, 75)
    win.setBackground("light green")
    Build = buildings(0,0,0,0,0,1,1,1,1,1)
    Game = PotatoGame("Name",0)

    nameText = Text(Point(20,25),Game.getName() + "'s Potato Paradise")
    ppsText = Text(Point(20,20),str(Build.getTotalPerSec()) + " Potatos Per Second")
    Potatos = Text(Point(55,70),str(Game.getPotatos()) + " Potatos")
    
    nameText.setStyle("bold")
    ppsText.setStyle("bold")
    Potatos.setStyle("bold")

    nameText.setSize(18)
    ppsText.setSize(18)
    Potatos.setSize(30)
    
    nameText.draw(win)
    ppsText.draw(win)
    Potatos.draw(win)

    #big potato
    bigPotato = Oval(Point(5,70),Point(35,35))
    bigPotato.setFill(color_rgb(255,212,80))

    bigPotato.setWidth(3)
    bigPotato.draw(win)

    potatoI = Circle(Point(25,65),.5)
    potatoI.setWidth(3)
    potatoI.draw(win)

    potatoI2 = Circle(Point(20,54),.5)
    potatoI2.setWidth(3)
    potatoI2.draw(win)

    potatoI3 = Circle(Point(11,62),.5)
    potatoI3.setWidth(3)
    potatoI3.draw(win)

    potatoI4 = Circle(Point(30,51),.5)
    potatoI4.setWidth(3)
    potatoI4.draw(win)

    potatoI5 = Circle(Point(7,48),.5)
    potatoI5.setWidth(3)
    potatoI5.draw(win)
    
    potatoI6 = Circle(Point(17,46),.5)
    potatoI6.setWidth(3)
    potatoI6.draw(win)

    potatoI7 = Circle(Point(23,38),.5)
    potatoI7.setWidth(3)
    potatoI7.draw(win)

    potatoButton = Button(win,Point(20,52.5),30,35,"")
    potatoButton.hide()
    
    quitButton = Button(win,Point(72.5,2.5),5,5,"Quit")
    quitButton.activate()

    saveButton = Button(win,Point(72.5,7.5),5,5,"Save")
    saveButton.activate()
    
    loadButton = Button(win,Point(72.5,12.5),5,5,"Load")
    loadButton.activate()

    plantButton = Button(win,Point(50,50),20,5,"Plant")
    fieldButton = Button(win,Point(50,45),20,5,"Field")
    farmButton = Button(win,Point(50,40),20,5,"Farm")
    platButton = Button(win,Point(50,35),20,5,"Plantation")
    greButton = Button(win,Point(50,30),20,5,"Greenhouse")

    plantButton.activate()
    fieldButton.activate()
    farmButton.activate()
    platButton.activate()
    greButton.activate()

    buildingText = Text(Point(67,55),"# of Buildings:")
    buildingText.setSize(17)
    buildingText.draw(win)
    buildingCostMessage = Text(Point(43.5,20),"Plant cost:\nField cost:\nFarm cost:\n        Plantation cost:\n            Greenhouse cost:" )
    buildingCostMessage.draw(win)
    buildingCost = Text(Point(62.5,20),"")
    buildingCost.draw(win)
    numOfBuildings = Text(Point(67,40),"0\n\n0\n\n0\n\n0\n\n0")
    numOfBuildings.setSize(17)
    numOfBuildings.draw(win)
    potatoPerClickMessage = Text(Point(20,33),"0 potatos per click")
    potatoPerClickMessage.draw(win)
    tickSpeed = 1
    while(True):
        Build.updatebuildings()
        Game.changePotatos(Game.getPotatos() + (Build.getTotalPerSec())*.0125)
        Potatos.setText(shortenNumber(str(round(Game.getPotatos()))) + " Potatos")
        ppsText.setText(shortenNumber(str(round(Build.getTotalPerSec(),2))) + " Potatos Per Second")
        potatoPerClickMessage.setText(shortenNumber(str(round(Build.getPotatoPerClick(),2))) + " potatos per click")
        numOfBuildings.setText(str(Build.plantNum) + "\n\n" + str(Build.fieldNum) + "\n\n" + str(Build.farmNum) + "\n\n" + str(Build.platNum) + "\n\n" + str(Build.greNum))
        buildingCost.setText(str(Build.getPlantCost()) + "\n" + str(Build.getFieldCost()) + "\n" + str(Build.getFarmCost()) + "\n" + str(Build.getPlatCost()) + "\n" + str(Build.getGreCost()))
        sleep(.01)
        pClick = win.checkMouse()
        if pClick is not None:
            if quitButton.clicked(pClick):
                win.close()
            elif saveButton.clicked(pClick):
                saveMenu = GraphWin("save file",200,100)
                saveMessage = Text(Point(100,25),"Enter Name: ")
                enterButton = Button(saveMenu,Point(75,75),50,20,"Enter")
                enterButton.activate()
                exitButton = Button(saveMenu,Point(125,75),50,20,"Exit")
                exitButton.activate()
                saveMessage.draw(saveMenu)
                saveEntry = Entry(Point(100,50),10)
                saveEntry.draw(saveMenu)
                while(True):
                    sClick = saveMenu.checkMouse()
                    if sClick is not None:
                        if exitButton.clicked(sClick):
                            saveMenu.close()
                            break
                        elif enterButton.clicked(sClick):
                            try:
                                fileName = saveEntry.getText()
                                newFile = open(f"{fileName}.txt","w")
                                tempGame = Game.save()
                                tempBuild = Build.save()
                                for i in tempGame:
                                   newFile.write(str(i)+"\n")
                                for x in tempBuild:
                                    newFile.write(str(x)+"\n")
                                newFile.close()
                                saveMessage.setText("File successfully saved")
                                sleep(1)
                                saveMenu.close()
                                break
                            except:
                                saveMessage.setText("Enter a Valid File Name")
                                sleep(1)
                                saveMenu.close()
                                break

            elif loadButton.clicked(pClick):
                loadMenu = GraphWin("load file",200,400)
                loadMessage = Text(Point(100,25),"Enter Name: ")
                enterButton = Button(loadMenu,Point(75,75),50,20,"Enter")
                enterButton.activate()
                exitButton = Button(loadMenu,Point(125,75),50,20,"Exit")
                exitButton.activate()
                loadMessage.draw(loadMenu)
                loadEntry = Entry(Point(100,50),10)
                loadEntry.draw(loadMenu)

                while(True):
                    lClick = loadMenu.checkMouse()
                    if lClick is not None:
                        if exitButton.clicked(lClick):
                            loadMenu.close()
                            break
                        elif enterButton.clicked(lClick):
                            fileName = loadEntry.getText()
                            info = []
                            while(True):
                                try:
                                    with open(f"{fileName}.txt","r") as file:
                                        for line in file:
                                            info.append(line.replace("\n", ""))
                                    Game = PotatoGame(info[0],int(info[1]))
                                    Build = buildings(int(info[2]),int(info[3]),int(info[4]),int(info[5]),int(info[6]),float(info[7]),float(info[8]),float(info[9]),float(info[10]),float(info[11]))
                                    sleep(1)
                                    loadMenu.close()
                                    print(Build.getTotalPerSec())
                                    break
                                except:
                                    loadMessage.setText("File not found")
                        break

            elif plantButton.clicked(pClick) and Game.getPotatos() >= Build.getPlantCost():
                Game.Potatos = Game.Potatos - Build.getPlantCost()
                Build.plantNum += 1
                
            elif fieldButton.clicked(pClick) and Game.getPotatos() >= Build.getFieldCost():
                Game.Potatos = Game.Potatos - Build.getFieldCost()
                Build.fieldNum += 1
                
            elif farmButton.clicked(pClick) and Game.getPotatos() >= Build.getFarmCost():
                Game.Potatos = Game.Potatos - Build.getFarmCost()
                Build.farmNum += 1
                
            elif platButton.clicked(pClick) and Game.getPotatos() >= Build.getPlatCost():
                Game.Potatos = Game.Potatos - Build.getPlatCost()
                Build.platNum += 1
                
            elif greButton.clicked(pClick) and Game.getPotatos() >= Build.getGreCost():
                Game.Potatos = Game.Potatos - Build.getGreCost()
                Build.greNum += 1

            elif potatoButton.clicked(pClick):
                Game.Potatos = Game.Potatos  + Build.getPotatoPerClick()
                
main()
"""
GameStates
1: Start Screen, ask to load file
2: playing game part, has clicker, potatos go up here
3: Buying, clicking is paused, buildings may be paused, buy buildings here

Windows:
1: main window, has game, play game here
2: building shop menu, buy and sell buildings
3: upgrade menu, buy upgrades
main()
"""
