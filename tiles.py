﻿from game import play
import items, enemies, actions, world
from util import util
from sounds import sounds

 
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sounds =sounds()
        self.util = util()
    def intro_text(self):
        raise NotImplementedError()
 
    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves
 
    def available_actions(self, player):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        
 
        return moves


class StartingRoom(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        self.sounds.GameBeginSound()
        return """
        You find yourself in a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

class StartingJungle(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        self.sounds.GameBeginSound()
        return """
        Welcome to the Jungle. You have to kill the giants of the jungle
        Take care these animals are dangerous, in the end you will find the highway.
        Take a lift in the end.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

class StartingSanAndreas(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        self.sounds.GameBeginSound()
        return """
        Zoombies have attacked SanAndreas city, there are Zombies all around the city
        The Virus is spreading, kill the Zombies, take the chemical form the lab.
        And go to the outer city.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        self.beenThere = False
        super().__init__(x, y)
 
    def add_loot(self, player):
        player.inventory.append(self.item)
 
    def modify_player(self, player):
        self.add_loot(player)

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
 
    def modify_player(self, the_player):
        if self.enemy.is_alive():
            self.sounds.HitSound()
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self, player):
        if self.enemy.is_alive(): 
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy), 
            actions.Status(player=player), actions.Heal(player=player),
            actions.Equip(player=player)]
        else:
            return self.adjacent_moves()

class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
        Another unremarkable part of the cave. You must forge onwards.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass
 
class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())
 
    def intro_text(self):
        if self.enemy.is_alive():
            self.util.GiantSpiderGraphic()
            self.sounds.GiantSpiderSound()
            return """
            A giant spider jumps down from its web in front of you!
            """
        else:
            self.sounds.KillSound()
            return """
            The corpse of a dead spider rots on the ground.
            """


class WolfRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Wolf())

    def intro_text(self):
        if self.enemy.is_alive():
            self.util.WolfRoomGraphic()
            self.sounds.WolfSound()
            return """
             A wolf jumps down in front of you!
             """
        else:
            self.sounds.KillSound()
            return """
             The corpse of a dead wolf is on the ground.
             """


class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())
 
    def intro_text(self):
        if self.beenThere:
            return """
                You have been here before...
                This is where you found a dagger!
            """
        else:
            self.util.DaggerRoomGraphic()
            return """
            Your notice something shiny in the corner.
            It's a dagger! You pick it up.
            """

class HellhoundRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Hellhound())
 
    def intro_text(self):
        if self.enemy.is_alive():
            self.util.HellhoundRoomGraphic()
            self.sounds.HellHoundSound();                                 
            return """
             A massive flaming dog growls angrily as you enter his lair!
             """
        else:
            self.sounds.KillSound()
            return """
             The Hellhound corpse. You killed it.
             """

class RatHumanoidRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.RatHumanoid())
 
    def intro_text(self):
        if self.enemy.is_alive():
            self.util.RatHumanoidGraphic()
            self.sounds.RatHumanoidSound();                                 
            return """
             A ugly but dangerous looking Rathumanoid is standing in front of you!
             """
        else:
            self.sounds.KillSound()
            return """
            You killed the impossible rathumanoid.
             """

class BatsRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Bats())
 
    def intro_text(self):
        if self.enemy.is_alive():
            self.util.BatsGraphic()
            self.sounds.BatSound();                                 
            return """
             A dark bad Bats are in this room!
             """
        else:
            self.sounds.KillSound()
            return """
            You killed the bats.
             """

class ZombieRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Zombie())
 
    def intro_text(self):
        if self.enemy.is_alive():
            self.util.ZombieGraphic()
            self.sounds.ZombieSound();                                 
            return """
             The impossible to kill zombie is in the room!
             """
        else:
            self.sounds.KillSound()
            return """
            You killed the Zombie.
             """

class CrawlerRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Crawler())
 
    def intro_text(self):
        if self.enemy.is_alive():
            self.util.CrawlerGraphic()
            self.sounds.ZombieSound();                                 
            return """
             Careful, save yourself a Crawler in the room!
             """
        else:
            self.sounds.KillSound()
            return """
            You crushed the crawler.
             """

class Elephant(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Elephant())
 
    def intro_text(self):
        if self.enemy.is_alive():
            self.util.ElephantGraphic()
            self.sounds.ElephantSound();                                 
            return """
             The mighty elephant is in front of you, he will break your skull in minutes, be brave!
             """
        else:
            self.sounds.KillSound()
            return """
            You killed the elephant.
             """

class Bear(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Bear())
 
    def intro_text(self):
        if self.enemy.is_alive():
            self.util.BearGraphic()
            self.sounds.BearSound()                                 
            return """
             The forecul Bear is here. watch it!
             """
        else:
            self.sounds.KillSound()
            return """
            The Bear is dead!.
             """
        
class Snake(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Snake())
 
    def intro_text(self):
        if self.enemy.is_alive():
            self.util.SnakeGraphic()
            self.sounds.SnakeSound()                                 
            return """
             The poisoneous Snake is in the room. it may bite you!
             """
        else:
            self.sounds.KillSound()
            return """
            The Snake is dead!.
             """

class TigerHerd(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.TigerHerd())
 
    def intro_text(self):
        if self.enemy.is_alive():
            self.util.TigerGraphic()
            self.sounds.TigerSound();                                 
            return """
             The king of the jungle, Tiger is here be careful and show your might!
             """
        else:
            self.sounds.KillSound()
            return """
            You killed the King of the jungle.
             """

class Lion(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Lion())
 
    def intro_text(self):
        if self.enemy.is_alive():
            self.util.LionGraphic()
            self.sounds.LionSound();                                 
            return """
             The king of the jungle, Lion is here be careful and show your might!
             """
        else:
            self.sounds.KillSound()
            return """
            You killed the King of the jungle.
             """


class Dragon(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Dragon())
 
    def intro_text(self):
        if self.enemy.is_alive():
            self.util.DragonGraphic()
            self.sounds.DragonSound();                                 
            return """
             The ancient Dragon, Dragon may burn you!
             """
        else:
            self.sounds.KillSound()
            return """
            You killed the scary Dragon.
             """

class ClimbMountain(MapTile):
    def intro_text(self):
        return """
        This mountain in the jungle. Climb it. You will find your way towards your victory.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

class OpenGround(MapTile):
    def intro_text(self):
        return """
        Another open ground in the jungle. pass it. You will find your way towards your victory.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

class WolfPack(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Wolf())

    def intro_text(self):
        if self.enemy.is_alive():
            self.util.WolfRoomGraphic()
            self.sounds.WolfSound()
            return """
             A pack of wolves is hungry, you are passing them!
             """
        else:
            self.sounds.KillSound()
            return """
             The corpses of a dead wolves are on the ground.
             """

class Highway(MapTile):
    def intro_text(self):
        self.util.VictoryGraphic()
        self.sounds.VictorySound()
        return """
        You see the shining highway in the distance...
        ... you see moving vehicles, go hop on one of them!
 
 
        Victory is yours!
        """        
        
    def modify_player(self, player):        
        player.victory = True

class Downtown(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Zombie())

    def intro_text(self):
        if self.enemy.is_alive():
            self.util.ZombieGraphic()            
            self.sounds.ZombieSound()
            self.sounds.ScreamSound()
            return """
             You are in the downtown of the SaenAndreas city...
             ... The residents are fearfull for their life save them from the Zombies!
             """
        else:
            self.sounds.KillSound()
            return """
             The downtown is clear, Zombies are dead in the downtown.
        """

class Lab(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Zombie())

    def intro_text(self):
        if self.enemy.is_alive():
            self.util.LabGraphic()
            self.sounds.LabSound()
            self.sounds.ZombieSound()
            return """
             You are in the Lab, Kill the Zombie...
             ... You will find the chemical to treat people from Zombie virus, take it with you!
             """
        else:
            self.sounds.KillSound()
            return """
             The Lab is clear, Zombies are dead in the Lab. You have the treatment chemical.
        """


class Goldenbridge(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Zombie())

    def intro_text(self):
        if self.enemy.is_alive():
            self.util.GoldenBridgeGraphic()
            self.sounds.FootStepTweSound()
            self.sounds.ZombieSound()           
            return """
             You are in the iconic Goldenbridge, Kill the Zombie...
             ... Clear the Goldenbridge from the Zombies!
             """
        else:
            self.sounds.KillSound()
            return """
             The Goldenbridge is clear for ferrying people out of SeanAndreas city.
        """

class Volleyballground(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Zombie())

    def intro_text(self):
        if self.enemy.is_alive():
            self.util.VolleyballgroundGraphic()
            self.sounds.ImpactTwoSound()
            self.sounds.ZombieSound()           
            return """
             You are on the volleyball ground... The ground is empty Zombie is round the corner
             ... Clear the Volleyball ground from the Zombies!
             """
        else:
            self.sounds.KillSound()
            return """
             The Volleyball ground is good to go to the next target, quick.
        """

class Baseballground(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Zombie())

    def intro_text(self):
        if self.enemy.is_alive():
            self.util.BaseballgroundGraphic()
            self.sounds.ImpactSound()
            self.sounds.ZombieSound()           
            return """
             You are on the baseball ground... The ground is empty Zombie is round the corner
             ... Clear the baseball ground from the Zombies!
             """
        else:
            self.sounds.KillSound()
            return """
             The baseball ground clear go to the next target, quick.
        """


class Financetower(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Zombie())

    def intro_text(self):
        if self.enemy.is_alive():
            self.util.FinanceTowerGraphic()
            self.sounds.FootStepSound()
            self.sounds.ZombieSound()           
            return """
             You are in the SeanAndreas city Finance tower...There are Zombies
             ... Kill them and move for the next target!
             """
        else:
            self.sounds.KillSound()
            return """
             The Finance tower is clear go to the next target, quick.
        """


class River(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Zombie())

    def intro_text(self):
        if self.enemy.is_alive():
            self.util.RiverGraphic()
            self.sounds.RiverSound()
            self.sounds.ZombieSound()           
            return """
             You need to cross the river to reach the outer city...There are Zombies
             ... Kill them and get victory over this game!
             """
        else:
            self.sounds.KillSound()
            return """
             You killed the zombie near the river, you are one step away from victory.
        """

class OuterCity(MapTile):
    def intro_text(self):
        self.util.VictoryGraphic()
        self.sounds.VictorySound()
        return """
        You clear the SanAndreas City...
        ... YOu have the chemical to treat the patients from Zombie virus, soon SeanAndreas will rejuvenate!
 
 
        Victory is yours!
        """
 
    def modify_player(self, player):
        player.victory = True

class LeaveCaveRoom(MapTile):
    def intro_text(self):
        self.util.VictoryGraphic()
        self.sounds.VictorySound()
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!
 
 
        Victory is yours!
        """
 
    def modify_player(self, player):
        player.victory = True