from playsound import playsound
import os
import time

from enemies import RatHumanoid
class sounds():
         
    def __init__(self):      
        self.dirname = os.path.dirname(os.getcwd())
        pass

    def WolfSound(self):        
        wolfsoundpath=self.dirname.strip()+'\wolfsund.mp3'       
        
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

    def HighwaySound(self):
        HighwaySoundpath=self.dirname.rstrip()+'\motrsund.wav'
        time.sleep(1)
        playsound(HighwaySoundpath)

    def RiverSound(self):
        RiverSoundpath=self.dirname.rstrip()+'\_rvrsund.wav'
        time.sleep(1)
        playsound(RiverSoundpath)

    def FootStepSound(self):
        FootStepSoundpath=self.dirname.rstrip()+'\_futsund.wav'
        time.sleep(1)
        playsound(FootStepSoundpath)

    def ImpactSound(self):
        ImpactSoundpath=self.dirname.rstrip()+'\imptsund.wav'
        time.sleep(1)
        playsound(ImpactSoundpath)

    def ImpactTwoSound(self):
        ImpactTwoSoundpath=self.dirname.rstrip()+'\impt2sund.wav'
        time.sleep(1)
        playsound(ImpactTwoSoundpath)
    
    def SirenSound(self):
        SirenSoundpath=self.dirname.rstrip()+'\sirensund.wav'
        time.sleep(1)
        playsound(SirenSoundpath)

    def ScreamSound(self):
        ScreamSoundpath=self.dirname.rstrip()+'\screamsund.wav'
        time.sleep(1)
        playsound(ScreamSoundpath)
    
    def LabSound(self):
        LabSoundpath=self.dirname.rstrip()+'\labsund.wav'
        time.sleep(1)
        playsound(LabSoundpath)
        playsound(LabSoundpath)

    def FootStepTweSound(self):
        FootStepTweSoundpath=self.dirname.rstrip()+'\_foot2sund.wav'
        time.sleep(1)
        playsound(FootStepTweSoundpath)

    def PunchSound(self):
        PunchSoundSoundpath=self.dirname.rstrip()+'\punchsund.wav'
        time.sleep(1)
        playsound(PunchSoundSoundpath)
    
    def DaggerSound(self):
        DaggerSoundpath=self.dirname.rstrip()+'\_daggersund.mp3'
        time.sleep(1)
        playsound(DaggerSoundpath)
    
    def PillowSound(self):
        PillowSoundpath=self.dirname.rstrip()+'\pillowsund.wav'
        time.sleep(1)
        playsound(PillowSoundpath)
    
    def ProjectileSound(self):
        ProjectileSoundpath=self.dirname.rstrip()+'\_prjtilsund.wav'
        time.sleep(1)
        playsound(ProjectileSoundpath)
    
    def CrossbowSound(self):
        CrossbowSoundpath=self.dirname.rstrip()+'\crosbowsund.wav'
        time.sleep(1)
        playsound(CrossbowSoundpath)

    def MoltovSound(self):
        MoltovSoundpath=self.dirname.rstrip()+'\moltovsund.wav'
        time.sleep(1)
        playsound(MoltovSoundpath)
    
    def RevolverSound(self):
        RevolverSoundpath=self.dirname.rstrip()+'\_rvolersund.wav'
        time.sleep(1)
        playsound(RevolverSoundpath)
    
    def SlingshotSound(self):
        SlingshotSoundpath=self.dirname.rstrip()+'\slinhotsund.wav'
        time.sleep(1)
        playsound(SlingshotSoundpath)
    
    def SwordSound(self):
        SwordSoundpath=self.dirname.rstrip()+'\swordsund.wav'
        time.sleep(1)
        playsound(SwordSoundpath)

    def KillSound(self):
        KillSoundpath=self.dirname.rstrip()+'\killsund.wav'
        time.sleep(1)
        playsound(KillSoundpath)
    
    def VictorySound(self):
        VictorySoundpath=self.dirname.rstrip()+'\_victrsund.wav'
        time.sleep(1)
        playsound(VictorySoundpath)
    
    def HitSound(self):
        HitSoundpath=self.dirname.rstrip()+'\_hitsund.wav'
        time.sleep(1)
        playsound(HitSoundpath)
    
    def GameBeginSound(self):
        GameBeginSoundpath=self.dirname.rstrip()+'\_gamsund.wav'#os.path.dirname(__file__) + '\_gamsund.wav'         
        time.sleep(1)        
        playsound(GameBeginSoundpath)
