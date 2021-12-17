from game import play
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
        return """
        You find yourself in a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
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
            return """
            You crushed the crawler.
             """

class LeaveCaveRoom(MapTile):
    def intro_text(self):
        self.util.VictoryGraphic()
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!
 
 
        Victory is yours!
        """
 
    def modify_player(self, player):
        player.victory = True