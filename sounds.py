from playsound import playsound
import os
import time

from enemies import RatHumanoid
class sounds():
         
    def __init__(self):      
        self.dirname = os.path.dirname(os.getcwd())
        pass

    def WolfSound(self):        
        wolfsoundpath=self.dirname.strip()+'\wolfsund.wav'       
        
        time.sleep(1)
        playsound(wolfsoundpath)

    def HellHoundSound(self):
        hellhoundsoundpath=self.dirname.strip()+'\dogsund.wav'
        time.sleep(1)
        playsound(hellhoundsoundpath)

    def RatHumanoidSound(self):
        RatHumanoidsoundpath=self.dirname.strip()+'\_ratsund.wav'
        time.sleep(1)
        playsound(RatHumanoidsoundpath)

    def BatSound(self):
        BatSoundpath=self.dirname.strip()+'\_brdsund.wav'
       
        time.sleep(1)        
        playsound(BatSoundpath)

    def ZombieSound(self):
        zombiesoundpath=self.dirname.rstrip()+'\lughsund.wav'
        playsound(zombiesoundpath)

    def CrawlerSound(self):
        crawlersoundpath=self.dirname.rstrip()+'\hornsund.wav'
        time.sleep(1)
        playsound(crawlersoundpath)

    def errorSound(self):
        errorsoundpath=self.dirname.rstrip()+'\_buzsund.wav'
        time.sleep(1)
        playsound(errorsoundpath)

    def drinkSound(self):
        drinksoundpath=self.dirname.rstrip()+'\watrsund.wav'
        time.sleep(1)
        playsound(drinksoundpath)
    
    def GiantSpiderSound(self):
        GiantSpiderSoundpath=self.dirname.rstrip()+'\_spysund.wav'
        time.sleep(1)
        playsound(GiantSpiderSoundpath)

    def TigerSound(self):
        TigerSoundpath=self.dirname.rstrip()+'\_tgersund.wav'
        time.sleep(1)
        playsound(TigerSoundpath)


    def ElephantSound(self):
        ElephantSoundpath=self.dirname.rstrip()+'\_elfsund.mp3'
        time.sleep(1)
        playsound(ElephantSoundpath)

    def SnakeSound(self):
        SnakeSoundpath=self.dirname.rstrip()+'\snakesund.mp3'
        time.sleep(1)
        playsound(SnakeSoundpath)
    
    def LionSound(self):
        LionSoundpath=self.dirname.rstrip()+'\lionsund.mp3'
        time.sleep(1)
        playsound(LionSoundpath)
    
    def DragonSound(self):
        DragonSoundpath=self.dirname.rstrip()+'\_drgsund.mp3'
        time.sleep(1)
        playsound(DragonSoundpath)

    def BearSound(self):
        BearSoundpath=self.dirname.rstrip()+'\_bersund.mp3'
        time.sleep(1)
        playsound(BearSoundpath)
