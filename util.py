import pyfiglet
class util():
    def __init__(self):
        pass
    
    def DaggerRoomGraphic(self):
        hellhound= pyfiglet.figlet_format("Dagger")
        print(hellhound)

    def GiantSpiderGraphic(self):
        GiantSpider= pyfiglet.figlet_format("Giant Spider")
        print(GiantSpider)

    def WolfRoomGraphic(self):
        Wolf= pyfiglet.figlet_format("Wolf")
        print(Wolf)

    def HellhoundRoomGraphic(self):
        hellhound= pyfiglet.figlet_format("Hellhound")
        print(hellhound)

    def RatHumanoidGraphic(self):
        ratHumanoid= pyfiglet.figlet_format("RatHumanoid")
        print(ratHumanoid)

    def BatsGraphic(self):
        Bats= pyfiglet.figlet_format("Bats")
        print(Bats)

    def ZombieGraphic(self):
        Zombie= pyfiglet.figlet_format("Zombie")
        print(Zombie)

    def CrawlerGraphic(self):
        Crawler= pyfiglet.figlet_format("Crawler")
        print(Crawler)   
    

    def getIntInput(self, description):        
        inputint=input(description)
        return int(inputint)
    
    def printGameText(self,description):
         print(description)

    def VictoryGraphic(self):
        Victory= pyfiglet.figlet_format("VICTORY")
        print(Victory)
