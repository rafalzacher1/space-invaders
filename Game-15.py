import Vector
import sys
import random

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Game:
    def __init__(self):
        self.missiles = set()
        self.lasers = set()
        self.enemies = set()
        self.enemymissiles = set()
        self.WIDTH = 600
        self.HEIGHT = 400
        self.CANVAS_DIMS = (self.WIDTH, self.HEIGHT)
        self.missileVelocity = Vector.Vector(0, -1)
        self.missileDamage = 5
        self.laserVelcocity = 2
        self.shipLeftVelocity = Vector.Vector(-1.5, 0)
        self.shipRightVelocity = Vector.Vector(1.5, 0)
        self.misLev = 1
        self.lasLev = 1
        self.difficulty = 0.1
        self.first = True
        self.death = False

        """ These variables are for the spaceships available for the player """
        # These variables are for the original starting ship
        self.shipIMG = simplegui.load_image(
            'http://personal.rhul.ac.uk/zhac/109/SHIP-01.png')
        self.shipIMG_CENTRE = (144, 222)
        self.shipIMG_DIMS = (288, 443)

        # These variables are for the first ship that can be purchased
        self.shipIMG1 = simplegui.load_image(
            'http://personal.rhul.ac.uk/zhac/109/SHIP-02.png')
        self.shipIMG1_CENTRE = (144, 221.5)
        self.shipIMG1_DIMS = (288, 443)

        # These variables are for the second ship that can be purchased
        self.shipIMG2 = simplegui.load_image(
            'http://personal.rhul.ac.uk/zhac/109/SHIP-03.png')
        self.shipIMG2_CENTRE = (93, 107)
        self.shipIMG2_DIMS = (186, 214)

        # These variables are for the third ship that can be purchased
        self.shipIMG3 = simplegui.load_image(
            'http://personal.rhul.ac.uk/zhac/109/SHIP-04.png')
        self.shipIMG3_CENTRE = (68, 93.5)
        self.shipIMG3_DIMS = (136, 187)

        # These variables are for the fourth ship that can be purchased
        self.shipIMG4 = simplegui.load_image(
            'http://personal.rhul.ac.uk/zhac/109/SHIP-05.png')
        self.shipIMG4_CENTRE = (46, 71)
        self.shipIMG4_DIMS = (92, 142)

        # These variables are for the ships dimensions and position
        self.img_dest_dim = (50, 50)
        self.img_pos = Vector.Vector(self.CANVAS_DIMS[0] / 2, self.CANVAS_DIMS[1] - 50)
        self.shipIMG_HEIGHT_DEST = (80, 100)

        """"""

        """ These variables are for the rockets and lasers available for the player """
        # These variables are for the original rocket
        self.rocketIMG = simplegui.load_image(
            'http://personal.rhul.ac.uk/zhac/109/missile-01.png')
        self.rocketIMG_CENTRE = (4.5, 21)
        self.rocketIMG_DIMS = (9, 42)

        # These variables are for the first missile that can be purchased
        self.rocketIMG1 = simplegui.load_image(
            'http://personal.rhul.ac.uk/zhac/109/missile-01.png')
        self.rocketIMG1_CENTRE = (4.5, 21)
        self.rocketIMG1_DIMS = (9, 42)

        # These variables are for the second missile that can be purchased
        self.rocketIMG2 = simplegui.load_image(
            'http://personal.rhul.ac.uk/zhac/109/missile-02.png')
        self.rocketIMG2_CENTRE = (4.8, 21)
        self.rocketIMG2_DIMS = (9, 42)

        # These variables are for the third missile that can be purchased
        self.rocketIMG3 = simplegui.load_image(
            'http://personal.rhul.ac.uk/zhac/109/missile-03.png')
        self.rocketIMG3_CENTRE = (8, 35)
        self.rocketIMG3_DIMS = (16, 70)

        # These variables are for the first laser that can be purchased
        self.laserIMG1 = simplegui.load_image(
            'http://personal.rhul.ac.uk/zhac/109/laser-01.png')
        self.laserIMG1_CENTRE = (7.5, 9)
        self.laserIMG1_DIMS = (15, 18)

        # These variables are for the second laser that can be purchased
        self.laserIMG2 = simplegui.load_image(
            'http://personal.rhul.ac.uk/zhac/109/laser-02.png')
        self.laserIMG2_CENTRE = (7.5, 9)
        self.laserIMG2_DIMS = (15, 18)

        # These variables are for the third laser that can be purchased
        self.laserIMG3 = simplegui.load_image(
            'http://personal.rhul.ac.uk/zhac/109/laser-03.png')
        self.laserIMG3_CENTRE = (7.5, 9)
        self.laserIMG3_DIMS = (15, 18)

        # These variables are for the fourth laser that can be purchased
        self.laserIMG4 = simplegui.load_image(
            'http://personal.rhul.ac.uk/zhac/109/laser-04.png')
        self.laserIMG4_CENTRE = (7.5, 9)
        self.laserIMG4_DIMS = (15, 18)

        # These variables are for the dimensions and position
        self.misDEST_DIMS = (9, 42)
        self.rocketIMG_POS = self.img_pos.copy()
        self.rocketIMG_HEIGHT_DEST = (18, 84)
        
        self.laserIMG_CENTRE = (7.5, 9)
        self.laserIMG_DIMS = (15, 18)
        self.laserIMG_HEIGHT_DEST = (20, 104)

        """"""

        # This variable is for the background image
        self.spaceIMG = simplegui.load_image(
            'http://personal.rhul.ac.uk/zhac/109/Space.png')

        self.enemy_img = simplegui.load_image(
            'http://personal.rhul.ac.uk/zhac/109/enemyShip.png')
        self.enemy_DIMS = (106, 145)
        self.enemy_center = (53, 72.5)
        self.kbd = Keyboard(self)
        self.player = Player(Vector.Vector(self.WIDTH / 2, self.HEIGHT - 40), self)

        self.shop = Shop(self.shipIMG1, self)
        self.shop = Shop(self.shipIMG2, self)
        self.shop = Shop(self.shipIMG3, self)
        self.shop = Shop(self.shipIMG4, self)

        self.inter = Interaction(self.player, self.kbd, self.shop, self)
        self.score = 0

        # These variables are used to indicate if a menu button has been shot
        self.pressed = False
        self.playShot = False
        self.shopShot = False
        self.shipsShot = False
        self.lasersShot = False
        self.rocketsShot = False
        self.contShot = False
        self.gameScreen = False

        # These variables indicate which ship is used
        self.originalShip = True
        self.shipOne = False
        self.shipTwo = False
        self.shipThree = False
        self.shipFour = False

        # These variables indicate which laser is used
        self.laserOne = False
        self.laserTwo = False
        self.laserThree = False
        self.laserFour = False

        # These variables indicate which rocket is used
        self.originalRocket = True
        self.rocketOne = False
        self.rocketTwo = False
        self.rocketThree = False
        self.rocketFour = False

        # These variables are for the buttons that can be shot in the menus
        self.playButtonPos = Vector.Vector(self.WIDTH / 4, self.HEIGHT / 2)
        self.exitButtonPos = Vector.Vector(self.WIDTH / 1.5, self.HEIGHT / 2)
        self.shipsButtonPos = Vector.Vector(self.WIDTH / 12, self.HEIGHT / 2)
        self.lasersButtonPos = Vector.Vector(self.WIDTH / 3.5, self.HEIGHT / 2)
        self.rocketsButtonPos = Vector.Vector(self.WIDTH / 2, self.HEIGHT / 2)
        self.contButtonPos = Vector.Vector(self.WIDTH / 1.35, self.HEIGHT / 2)
        self.shopButtonPos = Vector.Vector(self.WIDTH / 2.25, self.HEIGHT / 2)
        self.returnButtonPos = Vector.Vector(self.WIDTH / 1.2, self.HEIGHT / 2)
        self.playButtonLen = 0
        self.shopButtonLen = 0
        self.exitButtonLen = 0
        self.contButtonLen = 0
        self.shipsButtonLen = 0
        self.lasersButtonLen = 0
        self.rocketsButtonLen = 0
        self.returnButtonLen = 0

        # These variables are for the space ships
        self.shipOnePos = Vector.Vector(self.WIDTH / 13, self.HEIGHT / 2.25)
        self.shipTwoPos = Vector.Vector(self.WIDTH / 3.6, self.HEIGHT / 2.25)
        self.shipThreePos = Vector.Vector(self.WIDTH / 2.25, self.HEIGHT / 2.25)
        self.shipFourPos = Vector.Vector(self.WIDTH / 1.58, self.HEIGHT / 2.25)
        self.shipOneLen = 0
        self.shipTwoLen = 0
        self.shipThreeLen = 0
        self.shipFourLen = 0

        # These variable are for the lasers
        self.laserOnePos = Vector.Vector(self.WIDTH / 10, self.HEIGHT / 2.25)
        self.laserTwoPos = Vector.Vector(self.WIDTH / 3.5, self.HEIGHT / 2.25)
        self.laserThreePos = Vector.Vector(self.WIDTH / 2.1, self.HEIGHT / 2.25)
        self.laserFourPos = Vector.Vector(self.WIDTH / 1.5, self.HEIGHT / 2.25)
        self.laserOneLen = 0
        self.laserTwoLen = 0
        self.laserThreeLen = 0
        self.laserFourLen = 0

        # These variables are for the rockets
        self.rocketOnePos = Vector.Vector(self.WIDTH / 9.5, self.HEIGHT / 2.25)
        self.rocketTwoPos = Vector.Vector(self.WIDTH / 3.6, self.HEIGHT / 2.25)
        self.rocketThreePos = Vector.Vector(self.WIDTH / 2.15, self.HEIGHT / 2.25)
        self.rocketOneLen = 0
        self.rocketTwoLen = 0
        self.rocketThreeLen = 0

    def draw(self, canvas):
        self.inter.update(canvas)
        self.player.update()
        self.player.draw(canvas)
        self.inter.draw(canvas)

    def play(self):
        frame = simplegui.create_frame('Game', self.WIDTH, self.HEIGHT)
        frame.set_canvas_background('White')
        frame.set_draw_handler(self.draw)
        frame.set_keydown_handler(self.kbd.keyDown)
        frame.set_keyup_handler(self.kbd.keyUp)

        # These variables are for the buttons on the menus
        self.playButtonLen = frame.get_canvas_textwidth('Play', 28)
        self.shopButtonLen = frame.get_canvas_textwidth('Shop', 28)
        self.exitButtonLen = frame.get_canvas_textwidth('Exit', 28)
        self.contButtonLen = frame.get_canvas_textwidth('Continue', 28)
        self.shipsButtonLen = frame.get_canvas_textwidth('Ships', 28)
        self.lasersButtonLen = frame.get_canvas_textwidth('Lasers', 28)
        self.rocketsButtonLen = frame.get_canvas_textwidth('Rockets', 28)
        self.returnButtonLen = frame.get_canvas_textwidth('Return', 28)

        # These variables are for the ships
        self.shipOneLen = frame.get_canvas_textwidth('Battlecruiser', 12)
        self.shipTwoLen = frame.get_canvas_textwidth('Battleship', 12)
        self.shipThreeLen = frame.get_canvas_textwidth('Spacecruiser', 12)
        self.shipFourLen = frame.get_canvas_textwidth('Light Spaceship', 12)

        # These variables are for the lasers
        self.laserOneLen = frame.get_canvas_textwidth('LCB-10', 12)
        self.laserTwoLen = frame.get_canvas_textwidth('MCB-25', 12)
        self.laserThreeLen = frame.get_canvas_textwidth('MCB-50', 12)
        self.laserFourLen = frame.get_canvas_textwidth('RSB-75', 12)

        # These variables are for the rockets
        self.rocketOneLen = frame.get_canvas_textwidth('R310', 12)
        self.rocketTwoLen = frame.get_canvas_textwidth('PLT-2021', 12)
        self.rocketThreeLen = frame.get_canvas_textwidth('PLT-3030', 12)
        frame.start()

    def populateEnemies(self, multiplier):#the multiplier passed determines the number of rows of enemies
        formation = random.randint(1, 3)
        if (formation == 1):
            #FORMATION X    X    X
            #            X    X
            i = 0
            while (i < multiplier):
                if (i%2 == 0):
                    game.enemies.add(Enemy(Vector.Vector(self.WIDTH / 3,  -(i * 100)), game.difficulty, game))
                    game.enemies.add(Enemy(Vector.Vector((2 * self.WIDTH / 3), -(i * 100)), game.difficulty, game))
                else:
                    game.enemies.add(Enemy(Vector.Vector(self.WIDTH / 4, -(i * 100)), game.difficulty, game))
                    game.enemies.add(Enemy(Vector.Vector((2 * self.WIDTH) / 4, -(i * 100)), game.difficulty, game))
                    game.enemies.add(Enemy(Vector.Vector((3 * self.WIDTH) / 4, -(i * 100)), game.difficulty, game))
                i += 1
        elif (formation == 2):
            #FORMATION X       X
            #              X   
            #          X       X
            i = 0
            while (i < multiplier):
                game.enemies.add(Enemy(Vector.Vector((3 * self.WIDTH) / 4, -(i * 50)), game.difficulty, game))
                game.enemies.add(Enemy(Vector.Vector(self.WIDTH / 4, (i * 50)), game.difficulty, game))
                if (i%2 != 0):
                    game.enemies.add(Enemy(Vector.Vector((2 * self.WIDTH) / 4, -(i * 50) - 5), game.difficulty, game))
                i = i + 1		
        else:
            #FORMATION X X X X X
            i = 0
            while (i < (multiplier / 2)):
                game.enemies.add(Enemy(Vector.Vector((self.WIDTH / 6), -(i * 50)), game.difficulty, game))
                game.enemies.add(Enemy(Vector.Vector(((2*self.WIDTH) / 6), -(i * 50)), game.difficulty, game))
                game.enemies.add(Enemy(Vector.Vector(((3*self.WIDTH) / 6), -(i * 50)), game.difficulty, game))
                game.enemies.add(Enemy(Vector.Vector(((4*self.WIDTH) / 6), -(i * 50)), game.difficulty, game))
                game.enemies.add(Enemy(Vector.Vector(((5*self.WIDTH) / 6), -(i * 50)), game.difficulty, game))
                i = i + 1
                
    def loadNextWave(self, difficulty): #a difficulty multiplier is passed which determines how many rows of enemies are spawned
        self.difficulty = difficulty #difficulty should increase by 0.1 after every successful wave
        if (difficulty < 0.5):
            self.populateEnemies(5) #5 rows will be spawned
        elif (difficulty < 1):
            self.populateEnemies(8) #8 rows will be spawned
        elif (difficulty < 2):
            self.populateEnemies(12) #12 rows will be spawned
        elif (difficulty < 4):
            self.populateEnemies(15) #15 rows
        else:
            self.populateEnemies(30) #30 rows
        
class Player:
    def __init__(self, pos, game):
        self.pos = pos
        self.vel = Vector.Vector()
        self.health = 3
        self.game = game

    def draw(self, canvas):
        if game.originalShip == True:
            canvas.draw_image(game.shipIMG, game.shipIMG_CENTRE, game.shipIMG_DIMS, self.pos.get_p(), game.img_dest_dim,
                              3.15)

        if game.shipOne == True:
            canvas.draw_image(game.shipIMG1, game.shipIMG1_CENTRE, game.shipIMG1_DIMS, self.pos.get_p(),
                              game.img_dest_dim, 3.15)

        if game.shipTwo == True:
            canvas.draw_image(game.shipIMG2, game.shipIMG2_CENTRE, game.shipIMG2_DIMS, self.pos.get_p(),
                              game.img_dest_dim, 3.15)

        if game.shipThree == True:
            canvas.draw_image(game.shipIMG3, game.shipIMG3_CENTRE, game.shipIMG3_DIMS, self.pos.get_p(),
                              game.img_dest_dim, 3.15)

        if game.shipFour == True:
            canvas.draw_image(game.shipIMG4, game.shipIMG4_CENTRE, game.shipIMG4_DIMS, self.pos.get_p(),
                              game.img_dest_dim, 3.15)

    def update(self):
        self.pos = game.img_pos


class Keyboard:
    def __init__(self, game):
        self.right = False
        self.left = False
        self.up = False
        self.space = False
        self.game = game

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['right']:  # if right key pressed return true
            self.right = True
        if key == simplegui.KEY_MAP['left']:
            self.left = True
        if key == simplegui.KEY_MAP['up']:
            self.up = True
        if key == simplegui.KEY_MAP['space']:
            self.space = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right']:  # when right key released return true
            self.right = False
        if key == simplegui.KEY_MAP['left']:
            self.left = False
        if key == simplegui.KEY_MAP['up']:
            self.up = False
            game.pressed = False
        if key == simplegui.KEY_MAP['space']:
            self.space = False


class Interaction:
    def __init__(self, player, keyboard, shop, game):
        self.player = player
        self.keyboard = keyboard
        self.shop = shop
        self.game = game
        self.foo = game.missiles.copy()
        self.moo = game.enemies.copy()
        self.zoo = game.enemymissiles.copy()
        self.boo = game.lasers.copy()
        
    def update(self, canvas):
        if self.keyboard.right:  # if right key pressed, move 1 to the right
            self.player.pos.add(game.shipRightVelocity)
        if self.keyboard.left:
            self.player.pos.add(game.shipLeftVelocity)
        if self.keyboard.up:  ##if up arrow pressed
            if (not game.pressed):  ##if isn't being held down
                game.missiles.add(Missile(self.player.pos.copy(), True, game))  # create new missile
                game.pressed = True  # is now being held down
        if self.keyboard.space:
            if self.keyboard.right:
                game.lasers.add(Laser(self.player.pos.copy(), 2, game.lasLev, game))
            elif self.keyboard.left:
                game.lasers.add(Laser(self.player.pos.copy(), -2, game.lasLev, game))
            else:
                game.lasers.add(Laser(self.player.pos.copy(), 0, game.lasLev, game))
        for missile in self.foo:  ##update all the missiles
            if(missile.pos.get_p()[1] <= 0):
                explosion = Spritesheet(missile.pos, img, 9, 9, 74)
                game.missiles.remove(missile)
            missile.update()
        for enemy in self.moo:
            if(enemy.pos.get_p()[1] >= (game.player.pos.get_p()[1] - 37.5)):
                explosion = Spritesheet(enemy.pos, img, 9, 9, 74)
                game.enemies.remove(enemy)
                game.player.health = game.player.health - 1
            enemy.update()
        for missile in self.zoo:
            missile.update()
        for laser in self.boo:
            if(laser.pos.get_p()[1] <= 0):
                game.lasers.remove(laser)
            laser.update()
        self.foo = game.missiles.copy()
        self.moo = game.enemies.copy()
        self.zoo = game.enemymissiles.copy()
        self.boo = game.lasers.copy()
            

    def draw(self, canvas):
        self.update(canvas)

        if game.death:
            game.first = True
            game.player.health = 3
            canvas.draw_text("YOU DIED", (game.WIDTH / 2, game.HEIGHT / 4), 40, 'Black', 'sans-serif')
            canvas.draw_text("Continue", (game.WIDTH / 2, game.HEIGHT / 3), 32, 'Black', 'sans-serif')
            for missile in self.foo:
                if self.textHit(missile, Vector.Vector(game.WIDTH / 2, game.HEIGHT / 3), game.contButtonLen):
                    game.playShot = False
                    game.death = False
                    game.missiles.clear()
                else:
                    missile.draw(canvas)
        if game.playShot == False:  # if the play button hasn't been shot (ie still on the start menu)
            canvas.draw_text("Space Shooters", (game.WIDTH / 3, game.HEIGHT / 4), 32, 'Black', 'sans-serif')
            canvas.draw_text("Play", game.playButtonPos.get_p(), 28, 'Black', 'sans-serif')
            canvas.draw_text("Exit", game.exitButtonPos.get_p(), 28, 'Black', 'sans-serif')  # draw the start menu
            game.gameScreen = True
            
            for missile in self.foo:  # for all missiles
                if self.textHit(missile, game.exitButtonPos, game.exitButtonLen):  # if it hits the exit button
                    sys.exit(0)  # sys.exit(0) when not in codeskulptor ##exits the game

                if self.textHit(missile, game.playButtonPos, game.playButtonLen):  # if play button is hit
                    game.playShot = True  # don't draw the start menu any more
                    game.gameScreen = True
                    game.missiles.clear()#stop drawing this missile

                else:
                    missile.draw(canvas)  # if doesn't hit any, draw it

        else:
            canvas.draw_text("Score: " + str(game.score), (0, 32), 32, 'Black', 'sans-serif')
            canvas.draw_text("Lives: " + str(game.player.health), (0, game.WIDTH-40), 32, 'Black', 'sans-serif')

            # Checks which menu has been shot
            if game.shopShot == True:
                game.shopShot == False
                self.shop.shopMenu(canvas)
                for missile in self.foo:
                    if self.textHit(missile, game.shipsButtonPos, game.shipsButtonLen):
                        game.playShot = True
                        game.shipsShot = True
                        game.missiles.clear()
                    elif self.textHit(missile, game.lasersButtonPos, game.lasersButtonLen):
                        game.playShot = True
                        game.lasersShot = True
                        game.missiles.clear()
                    elif self.textHit(missile, game.rocketsButtonPos, game.rocketsButtonLen):
                        game.playShot = True
                        game.rocketsShot = True
                        game.missiles.clear()
                    elif self.textHit(missile, game.contButtonPos, game.contButtonLen):
                        game.shopShot = False
                        game.gameScreen = True
                        game.missiles.clear()
                    else:
                        missile.draw(canvas)

            # Checks which ship has been purchased
            if game.shipsShot == True:
                game.shopShot = False
                self.shop.shipsMenu(canvas)

                for missile in self.foo:
                    if self.textHit(missile, game.returnButtonPos, game.returnButtonLen):
                        game.shipsShot = False
                        game.shopShot = True
                        game.missiles.clear()

                    # Ship one is purchased
                    if self.textHit(missile, game.shipOnePos, game.shipOneLen):
                        if game.score >= 200:
                            game.score -= 200
                            
                            game.shipLeftVelocity = Vector.Vector(-1.75, 0)
                            game.shipRightVelocity = Vector.Vector(1.75, 0)
                            self.player.health = self.player.health + 1

                            game.orginalShip = False
                            game.shipOne = True
                            game.shipTwo = False
                            game.shipThree = False
                            game.shipFour = False

                            game.shipsShot = False
                            game.shopShot = True
                            game.missiles.clear()

                    # Ship two is purchased
                    if self.textHit(missile, game.shipTwoPos, game.shipTwoLen):
                        if game.score >= 400:
                            game.score -= 400
                            
                            game.shipLeftVelocity = Vector.Vector(-2, 0)
                            game.shipRightVelocity = Vector.Vector(2, 0)
                            self.player.health = self.player.health + 1

                            game.orginalShip = False
                            game.shipOne = False
                            game.shipTwo = True
                            game.shipThree = False
                            game.shipFour = False

                            game.shipsShot = False
                            game.shopShot = True
                            game.missiles.clear()

                    # Ship three is purchased
                    if self.textHit(missile, game.shipThreePos, game.shipThreeLen):
                        if game.score >= 600:
                            game.score -= 600
                            
                            game.shipLeftVelocity = Vector.Vector(-2.25, 0)
                            game.shipRightVelocity = Vector.Vector(2.25, 0)
                            self.player.health = self.player.health + 1

                            game.orginalShip = False
                            game.shipOne = False
                            game.shipTwo = False
                            game.shipThree = True
                            game.shipFour = False

                            game.shipsShot = False
                            game.shopShot = True
                            game.missiles.clear()

                    # Ship four is purchased
                    if self.textHit(missile, game.shipFourPos, game.shipFourLen):
                        if game.score >= 800:
                            game.score -= 800
                            
                            game.shipLeftVelocity = Vector.Vector(-2, 0)
                            game.shipRightVelocity = Vector.Vector(2, 0)
                            self.player.health = self.player.health + 1

                            game.orginalShip = False
                            game.shipOne = False
                            game.shipTwo = False
                            game.shipThree = False
                            game.shipFour = True

                            game.shipsShot = False
                            game.shopShot = True
                            game.missiles.clear()

                    else:
                        missile.draw(canvas)

            # Checks which laser has been purchased
            if game.lasersShot == True:
                game.shopShot = False
                self.shop.lasersMenu(canvas)

                for missile in self.foo:
                    if self.textHit(missile, game.returnButtonPos, game.returnButtonLen):
                        game.lasersShot = False
                        game.shopShot = True
                        game.missiles.clear()

                    # Laser one has been purchased
                    if self.textHit(missile, game.laserOnePos, game.laserOneLen):
                        if game.score >= 1000:
                            game.score -= 1000
                            
                            game.laserVelocity = -2.25
                            
                            game.laserOne = True
                            game.laserTwo = False
                            game.laserThree = False
                            game.laserFour = False
                            
                            game.lasLev = 1
                            
                            game.lasersShot = False
                            game.shopShot = True
                            game.missiles.clear()

                    # Laser two has been purchased
                    if self.textHit(missile, game.laserTwoPos, game.laserTwoLen):
                        if game.score >= 1500:
                            game.score -= 1500
                            
                            game.laserVelocity = -2.5
                            
                            game.laserOne = False
                            game.laserTwo = True
                            game.laserThree = False
                            game.laserFour = False
                            
                            game.lasLev = 2
                            
                            game.lasersShot = False
                            game.shopShot = True
                            game.missiles.clear()

                    # Laser three has been purchased
                    if self.textHit(missile, game.laserThreePos, game.laserThreeLen):
                        if game.score >= 2000:
                            game.score -= 2000
                            
                            game.laserVelocity = -2.75
                            
                            game.laserOne = False
                            game.laserTwo = False
                            game.laserThree = True
                            game.laserFour = False
                            
                            game.lasLev = 3
                            
                            game.lasersShot = False
                            game.shopShot = True
                            game.missiles.clear()

                    # Laser four has been purchased
                    if self.textHit(missile, game.laserFourPos, game.laserFourLen):
                        if game.score >= 3000:
                            game.score -= 4000
                            
                            game.laserVelocity = -3
                            
                            game.laserOne = False
                            game.laserTwo = False
                            game.laserThree = False
                            game.laserFour = True
                            
                            game.lasLev = 4
                            
                            game.lasersShot = False
                            game.shopShot = True
                            game.missiles.clear()

                    else:
                        missile.draw(canvas)

            # Checks which rocket has been purchased
            if game.rocketsShot == True:
                game.shopShot = False
                self.shop.rocketsMenu(canvas)

                for missile in self.foo:
                    if self.textHit(missile, game.returnButtonPos, game.returnButtonLen):
                        game.rocketsShot = False
                        game.shopShot = True
                        game.missiles.clear()

                    # Rocket one has been purchased
                    if self.textHit(missile, game.rocketOnePos, game.rocketOneLen):
                        if game.score >= 200:
                            game.score -= 200
                            
                            game.missileVelocity = Vector.Vector(0, -1.15)
                            game.missileDamage = 10
                            
                            game.originalMissile = False
                            game.rocketOne = True
                            game.rocketTwo = False
                            game.rocketThree = False
                            
                            game.rocketsShot = False
                            game.shopShot = True
                            game.missiles.clear()

                    # Rocket two has been purchased
                    if self.textHit(missile, game.rocketTwoPos, game.rocketTwoLen):
                        if game.score >= 400:
                            game.score -= 400
                            
                            game.missileVelocity = Vector.Vector(0, -1.27)
                            game.missileDamage = 15
                            
                            game.originalMissile = False
                            game.rocketOne = False
                            game.rocketTwo = True
                            game.rocketThree = False
                            
                            
                            game.rocketsShot = False
                            game.shopShot = True
                            game.missiles.clear()

                    # Rocket three has been purchased
                    if self.textHit(missile, game.rocketThreePos, game.rocketThreeLen):
                        if game.score >= 700:
                            game.score -= 700
                            
                            game.missileVelocity = Vector.Vector(0, -1.4)
                            game.missileDamage = 20
                            
                            game.originalMissile = False
                            game.rocketOne = False
                            game.rocketTwo = False
                            game.rocketThree = True
                            
                            game.rocketsShot = False
                            game.shopShot = True
                            game.missiles.clear()

                    else:
                        missile.draw(canvas)

            if game.gameScreen == True:  # if no longer on start menu
                if(game.player.health <= 0):
                    game.death = True
                    game.gameScreen = False
                    game.enemies.clear()
                    game.missiles.clear()
                if game.first == True:
                    game.playShot = True
                    game.first = False
                    game.loadNextWave(game.difficulty)
                elif(len(game.enemies) != 0):
                    for enemy in self.moo:
                        enemy.draw(canvas)
                        enemy.shoot()
                    for missile in self.zoo:
                        missile.draw(canvas)
                        if self.hit(missile, self.player):
                            game.enemymissiles.remove(missile)
                            game.player.health = game.player.health - 1
                            if(game.player.health <= 0):
                                game.death = True
                                game.gameScreen = False
                                game.enemies.clear()
                                game.missiles.clear()
                    for missile in self.foo:
                            missile.draw(canvas)
                            for enemy in self.moo:
                                if self.hit(missile, enemy):
                                    game.missiles.remove(missile)
                                    enemy.health = enemy.health - missile.damage
                                    if enemy.health <= 0:
                                        game.score += enemy.score
                                        game.enemies.remove(enemy)
                        
                else:
                    canvas.draw_text("Shop", game.shopButtonPos.get_p(), 28, 'Black', 'sans-serif')
                    canvas.draw_text("Continue", game.returnButtonPos.get_p(), 28, 'Black', 'sans-serif')
                    for missile in self.foo:
                        if self.textHit(missile, game.shopButtonPos, game.shopButtonLen):
                            game.shopShot = True
                            game.gameScreen = False
                            game.missiles.clear()
                        elif self.textHit(missile, game.returnButtonPos, game.returnButtonLen):
                            game.first = True
                            game.missiles.clear()
                        else:
                            missile.draw(canvas)  ##draw missile (This is where the hit checking for the enemies will go

    def textHit(self, missile, textPos, textLen):  # checks if hit text
        return textPos.get_p()[1] >= missile.pos.get_p()[1] and textPos.get_p()[0] <= missile.pos.get_p()[0] and \
               textPos.get_p()[0] + textLen >= missile.pos.get_p()[0]  # if the missile is to the left of the right of the text (ie if it will hit the text)
    
    def hit(self, missile, ship):
        if(missile.playen == True):
            return missile.pos.get_p()[0] >= ship.pos.get_p()[0]-37.5 and missile.pos.get_p()[0] <= ship.pos.get_p()[0]+37.5 \
                    and missile.pos.get_p()[1] <= ship.pos.get_p()[1]
        else:
            return missile.pos.get_p()[0] >= ship.pos.get_p()[0]-37.5 and missile.pos.get_p()[0] <= ship.pos.get_p()[0]+37.5 \
                    and missile.pos.get_p()[1] >= ship.pos.get_p()[1]

class Missile:
    def __init__(self, pos, playen, game):
        self.pos = pos
        self.playen = playen
        if self.playen: #if a missile shot by the player
            self.permVel = game.missileVelocity
            self.damage = game.missileDamage
        else:
            self.permVel = Vector.Vector(0, 2)
            self.damage = 1
        self.game = game

    def draw(self, canvas):
        if self.playen == False:
            canvas.draw_image(game.rocketIMG, game.rocketIMG_CENTRE, game.rocketIMG_DIMS, self.pos.get_p(), game.rocketIMG_DIMS, 216.5)    
        if self.playen == True:
            if game.originalRocket == True:
               canvas.draw_image(game.rocketIMG, game.rocketIMG_CENTRE, game.rocketIMG_DIMS, self.pos.get_p(),
                                 game.rocketIMG_DIMS, 3.15)
            if game.rocketOne == True:
                canvas.draw_image(game.rocketIMG1, game.rocketIMG1_CENTRE, game.rocketIMG1_DIMS, self.pos.get_p(),
                                  game.rocketIMG1_DIMS, 3.15)

            if game.rocketTwo == True:
                canvas.draw_image(game.rocketIMG2, game.rocketIMG2_CENTRE, game.rocketIMG2_DIMS, self.pos.get_p(),
                                  game.rocketIMG2_DIMS, 3.15)

            if game.rocketThree == True:
                canvas.draw_image(game.rocketIMG3, game.rocketIMG3_CENTRE, game.rocketIMG3_DIMS, self.pos.get_p(),
                                  game.rocketIMG3_DIMS, 3.15)

    def update(self):
        self.pos.add(self.permVel)

    def changeVel(self, multiplier):
        game.missileVelocity = game.missileVelocity.mulitply(multiplier)

    def resetVel(self):
        game.missileVelocity = self.perVel

class Laser:
    def __init__(self, pos, vel, lasLev, game):
        self.pos = pos
        self.velocity = Vector.Vector(vel, game.laserVelocity)
        self.permVel = self.velocity
        self.level = lasLev
        self.damage = self.level*5
        self.game = game
        
    def draw(self, canvas):
        if game.laserOne == True:
            canvas.draw_image(game.laserIMG1, game.laserIMG1_CENTRE, game.laserIMG1_DIMS, self.pos.get_p(),
                              game.laserIMG1_DIMS, 3.15)

        if game.laserTwo == True:
            canvas.draw_image(game.laserIMG2, game.laserIMG2_CENTRE, game.laserIMG2_DIMS, self.pos.get_p(),
                              game.laserIMG2_DIMS, 3.15)

        if game.laserThree == True:
            canvas.draw_image(game.laserIMG3, game.laserIMG3_CENTRE, game.laserIMG3_DIMS, self.pos.get_p(),
                              game.laserIMG3_DIMS, 3.15)

        if game.laserFour == True:
            canvas.draw_image(game.laserIMG4, game.laserIMG4_CENTRE, game.laserIMG4_DIMS, self.pos.get_p(),
                              game.laserIMG4_DIMS, 3.15)
        
    def update(self):
        self.pos.add(self.velocity)
        
    def changeVel(self, multiplier):
        self.velocity = self.velocity.mulitply(multiplier)
        
    def resetVel(self):
        self.velocity = self.perVel        
    
    def bounce(self):
        self.vel.reflect(normal)
        
class Enemy:
    def __init__(self, pos, difficulty, game):
        self.pos = pos
        self.vel = Vector.Vector(0,0.5)
        self.health = difficulty * 10
        self.score = 1000 * difficulty
        self.game = game

    def shoot(self):
        i = random.randint(1, 1000)
        if i == 1:
            game.enemymissiles.add(Missile(self.pos.copy(), False, self.game))
        
    def update(self):
        self.pos.add(self.vel)
        
    def draw(self, canvas):
        canvas.draw_image(game.enemy_img, game.enemy_center, game.enemy_DIMS,
                       self.pos.get_p(), game.img_dest_dim, 93.15)

        
class Shop:
    """
    This class is to show the available menus that the player can use to buy better ships, upgrade their rockets and
    upgrade to lasers
    """

    def __init__(self, shipIMG, game):
        """ This is the constructor """
        self.shipIMG = shipIMG
        self.game = game

    def shopMenu(self, canvas):
        """ This function is to show the available menus for the player """
        canvas.draw_text("Welcome to The Galactic Shop", (game.WIDTH / 3.3, game.HEIGHT / 6), 20, 'Black', 'sans-serif')
        canvas.draw_text("Ships", game.shipsButtonPos.get_p(), 28, 'Black', 'sans-serif')
        canvas.draw_text("Lasers", game.lasersButtonPos.get_p(), 28, 'Black', 'sans-serif')
        canvas.draw_text("Rockets", game.rocketsButtonPos.get_p(), 28, 'Black', 'sans-serif')
        canvas.draw_text("Continue", game.contButtonPos.get_p(), 28, 'Black', 'sans-serif')

    def shipsMenu(self, canvas):
        """ This function is to display the different available ships that the player can purchase with their score """
        canvas.draw_text("Ships", (game.WIDTH / 15, game.HEIGHT / 6), 28, 'Black', 'sans-serif')
        canvas.draw_text("Return", game.returnButtonPos.get_p(), 28, 'Black', 'sans-serif')

        canvas.draw_image(game.shipIMG1, game.shipIMG1_CENTRE, game.shipIMG1_DIMS, (80, 120), game.shipIMG_HEIGHT_DEST)
        canvas.draw_text("Battlecruiser", game.shipOnePos.get_p(), 12, 'Black', 'sans-serif')

        canvas.draw_image(game.shipIMG2, game.shipIMG2_CENTRE, game.shipIMG2_DIMS, (193, 120), game.shipIMG_HEIGHT_DEST)
        canvas.draw_text("Battleship", game.shipTwoPos.get_p(), 12, 'Black', 'sans-serif')

        canvas.draw_image(game.shipIMG3, game.shipIMG3_CENTRE, game.shipIMG3_DIMS, (306, 120), game.shipIMG_HEIGHT_DEST)
        canvas.draw_text("Spacecruiser", game.shipThreePos.get_p(), 12, 'Black', 'sans-serif')

        canvas.draw_image(game.shipIMG4, game.shipIMG4_CENTRE, game.shipIMG4_DIMS, (420, 120), game.shipIMG_HEIGHT_DEST)
        canvas.draw_text("Light Spaceship", game.shipFourPos.get_p(), 12, 'Black', 'sans-serif')

    def lasersMenu(self, canvas):
        """ This function is to display the different available lasers that the player can purchase with their score """
        canvas.draw_text("Lasers", (game.WIDTH / 15, game.HEIGHT / 6), 28, 'Black', 'sans-serif')
        canvas.draw_text("Return", game.returnButtonPos.get_p(), 28, 'Black', 'sans-serif')

        canvas.draw_image(game.laserIMG1, game.laserIMG1_CENTRE, game.laserIMG1_DIMS, (80, 120), game.laserIMG_HEIGHT_DEST)
        canvas.draw_text("LCB-10", game.laserOnePos.get_p(), 12, 'Black', 'sans-serif')

        canvas.draw_image(game.laserIMG2, game.laserIMG2_CENTRE, game.laserIMG2_DIMS, (193, 120), game.laserIMG_HEIGHT_DEST)
        canvas.draw_text("MCB-25", game.laserTwoPos.get_p(), 12, 'Black', 'sans-serif')

        canvas.draw_image(game.laserIMG3, game.laserIMG3_CENTRE, game.laserIMG3_DIMS, (306, 120), game.laserIMG_HEIGHT_DEST)
        canvas.draw_text("MCB-50", game.laserThreePos.get_p(), 12, 'Black', 'sans-serif')

        canvas.draw_image(game.laserIMG4, game.laserIMG4_CENTRE, game.laserIMG4_DIMS, (420, 120), game.laserIMG_HEIGHT_DEST)
        canvas.draw_text("RSB-75", game.laserFourPos.get_p(), 12, 'Black', 'sans-serif')

    def rocketsMenu(self, canvas):
        """ This function is to display the different available rockets that the player can purchase with their score """
        canvas.draw_text("Rockets", (game.WIDTH / 15, game.HEIGHT / 6), 28, 'Black', 'sans-serif')
        canvas.draw_text("Return", game.returnButtonPos.get_p(), 28, 'Black', 'sans-serif')

        canvas.draw_image(game.rocketIMG1, game.rocketIMG1_CENTRE, game.rocketIMG1_DIMS, (80, 120), game.rocketIMG_HEIGHT_DEST)
        canvas.draw_text("R310", game.rocketOnePos.get_p(), 12, 'Black', 'sans-serif')

        canvas.draw_image(game.rocketIMG2, game.rocketIMG2_CENTRE, game.rocketIMG2_DIMS, (193, 120), game.rocketIMG_HEIGHT_DEST)
        canvas.draw_text("PLT-2021", game.rocketTwoPos.get_p(), 12, 'Black', 'sans-serif')

        canvas.draw_image(game.rocketIMG3, game.rocketIMG3_CENTRE, game.rocketIMG3_DIMS, (306, 120), game.rocketIMG_HEIGHT_DEST)
        canvas.draw_text("PLT-3030", game.rocketThreePos.get_p(), 12, 'Black', 'sans-serif')


img = simplegui.load_image("http://personal.rhul.ac.uk/zhac/109/explosion-spritesheet.png")
frame_index = [0, 0]
game_clock = 0


class Spritesheet():
    def __init__(self, pos, sprite, columns, rows, num_frames):
        self.pos = pos
        self.sprite = sprite
        self.columns = columns
        self.rows = rows
        self.width = sprite.get_width()
        self.height = sprite.get_height()
        self.frame_width = self.width / columns
        self.frame_height = self.height / rows
        self.frame_centre_x = self.frame_width / 2
        self.frame_centre_y = self.frame_height / 2
        self.num_frames = num_frames
    
    def next_frame(self):
        global frame_index
        
        frame_index[0] = (frame_index[0] + 1) % self.columns
        if frame_index[0] == 0:
            frame_index[1] = (frame_index[1] + 1) % self.rows
        
    def draw(self, canvas):
        global frame_index, frame_width, frame_height, frame_centre_x, frame_centre_y
        
        self.next_frame()
        
        source_centre = (self.frame_width * frame_index[0] + self.frame_centre_x,
                        self.frame_height * frame_index[1] + self.frame_centre_y)
        
        source_size = (self.frame_width, self.frame_height)
        
        dest_centre = pos
        
        dest_size = (100, 100)

        canvas.draw_image(self.sprite,
                          source_centre,
                          source_size,
                          dest_centre,
                          dest_size)    


class Clock:
    def __init__(self, time):
        self.time = time
        
    def tick(self):
        global game_clock
        game_clock += 1
        
    def transition(self):
        global game_clock
        
        self.tick()
        
        if game_clock % self.time == 0:
            return True
        else:
            return False

clock = Clock(10)

def draw(canvas):
    running_man.draw(canvas)
    if clock.transition():
        running_man.next_frame()

game = Game()
game.play()
