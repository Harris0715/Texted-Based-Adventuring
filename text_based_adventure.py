import random


class Game():

    def __init__(self, life, health):

        self.food_point = 1
        self.insult = random.choice([
            "\nWell done, you abhorrent, churlish son of a griffin!"
            "\n...I hope ye can sense sarcasm.\n",
            "\nYour mother would be proud, you rotten, lazy, pond stain!\n",
            "\nYou are a witless, ignorant baboon!\n",
            "\nWell done, you foul-dried latrine stain!"
            "\n...I hope ye can sense sarcasm.\n",
            "\nWell done, you craven unwashed trout dropping!"
            "\n...I hope ye can sense sarcasm.\n",
            "\nWell done, you mewling, obnoxious pig-dropping!"
            "\n...I hope ye can sense sarcasm.\n"
        ])
        self.hero = {}
        self.life = life
        self.health = health

    def game_over(self):
        print "You are out of health points.  You die a slow, cruel death."
        print self.insult
        quit()

    def credit(self):
        print """

		The rough plot for this story was taken from 
		the free online wiki "Create Your Own Story"

		http://editthis.info/create_your_own_story/Crusader_(an_action-adventure_fantasy)

		accessed on 02/15/2018.
	"""
        quit()

    def death(self, life):
        if self.food_point == 1:
            print """

			You are dead, wandering the bleak emptiness of the netherworld for 
			solace, where you will find none.

			BUT WAIT!!!!!!!!!!!!

			Don't despair, brave %s!  You may consume your morsel of %s and return to 
			fight on!

			DO YOU:

			A) Shove the %s into your mouth and escape from your weary doom.
			B) Nah, that world was a miserable existence anyway, I'd rather 
			wander the underworld for eternity hoping to find some meaning here.
			""" % (self.hero['name'], self.hero['food'], self.hero['food'])

            self.food_point = 0

            while True:
                do_you = raw_input("> ")
                if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                    print "\tYou escape with your life, but lose 5 health points."
                    self.health -= 5
                    getattr(self, life)()
                elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
                    print self.insult
                    print "GAME OVER!  YOU'RE DEAD!"
                    print "____________________________________________"
                    print
                    print
                    return self.credit()

                else:
                    print self.insult
                    print "GAME OVER!  YOU'RE DEAD!"
                    print "____________________________________________"
                    print
                    print
                    return self.credit()


        else:
            return self.insult
            return self.credit()
            quit()

        if self.food_point <= 0:
            return self.credit()

    def begin(self):
        print """
		Play my text-based adventure game below!  Input your responses after the prompts.


		__________________________________________

		You wake up still groggy after a restless night's sleep in the crusader
		barracks.  It seems impossible to sleep lately, as there has been much 
		unrest in your beloved kingdom of Zelanna. 

		Rival kingdoms in the land desire to ravage your territory and 
		challenge your King.  No sooner do you manage to rouse yourself out of
		bed, when a messenger from the king arrives. The king is sending for you.

		"M-m-m me?", you stammer, nervously.  
		You are but a young knight, barely still a squire. 

		It appears that the castle is under attack by a rival lord, 
		who happens to be a necromancer. 

		His armies of undead are destroying the town! The King needs your help
		to destroy this horrid enemy or the kingdom is doomed!

		The royal army has been brutally decimated, and you are the last 
		remaining hope.

		I, the wisest and most respected wizard in all Zelanna, will guide
		you on this quest. 

		But first we must gather some critical information:
		"""

        print "\n\t\tWhat is your name, brave knight?\n"
        self.hero['name'] = raw_input("> ")

        print "\n\t\tWhat is your favorite knightly cuisine?\n"
        self.hero['food'] = raw_input("> ")
        print """
		Very good, and know this!  I will cast a spell of protection
		over a morsel of this %s. You will have one chance to escape death
		by eating it.  Do not lose it, as it may save your very life.
		But be warned, this spell will take you back to the start of your
		journey\n""" % (self.hero['food'])

        print "\t\tWhat weapon do you desire for avenging your King"
        print "\t\tand terrifying the underworld?\n"
        self.hero['weapon'] = raw_input("> ")
        print """

		Aye!  Tis a fair choice, indeed!

		You begin your valiant quest with 100 health points. 

		Keep track of these!!!!

		If you should be so unfortunate as to possess ZERO health points, 
		you will suffer a most undesirable death.

		With haste, valiant %s!  You must be very brave on this journey!
		What is your first move?""" % (self.hero['name'])

        print """
		DO YOU:

		A) Go to the king.
		B) Ignore the king.
		"""

        while True:
            do_you = raw_input("> ")
            if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                return self.go_to_king()
            elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
                return self.ignore_the_king()
            else:
                print "That's not an option, you idiot.  Pick A or B."

    def ignore_the_king(self):
        print """
		Ignoring the king was an unfortunate decision. You are killed by an 
		arrow that that zips past the castles defenses and enters your chest. 
		The king wanted you to help defend the castle from attack.


		THE END.

		Next time you should maintain greater respect for your king's wishes.
		"""

        return self.death("go_to_king")

    def go_to_king(self):
        print "\tYe doth have %d mighty health points left" % (self.health)
        print """

		You enter the king's throne room and learn that the castle is under attack 
		by a rival lord, who happens to be an evil necromancer.

		His armies of undead are destroying the town! The King needs you to help 
		destroy the enemy or the kingdom is doomed!

		Rushing outside, you see all sorts of action. A soldier is screaming 
		for help, trapped under a burning pile of wood. Meanwhile, zombies are killing 
		townspeople, and a horde of children are getting herded by five 
		of the most gruesome zombies of all!

		DO YOU:

		A) Save the soldier.
		B) Kill the zombies.
		"""

        while True:
            do_you = raw_input("> ")
            if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                return self.save_soldier()
            elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
                return self.kill_zombies()
            else:
                print "Hey genius, pick A or B."

    def kill_zombies(self):
        self.health -= 20
        print "\tYe doth have %d mighty health points left" % (self.health)
        print """

		Your sword goes through the zombies like a hot knife through 
		freshly-churned butter, but they wound you...  lose 20 health points!
		"""
        if self.health <= 0:
            return self.game_over()
        else:
            print """
		  Nevertheless, you valiantly push onward and kill the zombies! 
	  	Suddenly, you hear a scream behind a nearby building. 
	  	Without a second thought, you rush to see what it is!

		  A) Investigate the scream.
		  """

            while True:
                do_you = raw_input("> ")
                if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                    return self.investigate_scream()
                else:
                    print "DUMMY!, pick A or B."

    def save_soldier(self):
        print "\tYe doth have %d mighty health points left" % (self.health)
        print """

		The soldier screams for help again, and you answer his plea,
		bravely moving the burning wood off his wounded body. 

		It burns a little, but you don't care, you have saved a fellow soldier
		of the King.  He is still alive!

		To express his humble gratitude, he gives you all that 
		he has within his pocket: 15 gold pieces.

		After freeing the man, you hear a loud scream from behind a building. 
		You rush to see what it is...

		A) Investigate the scream!!
		"""

        while True:
            do_you = raw_input("> ")
            if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                return self.investigate_scream()
            else:
                print "Hey dummy, choose the letter 'A'."

    def investigate_scream(self):
        print "\tYe doth have %d mighty health points left" % (self.health)
        print """

		You see a tall, disfigured man in black robes carrying a staff. 
		He is standing over a dead woman. You rush at him with your sword. 
		The man hears you and swings around, but it's too late.

		You slam into him, knocking him to the ground. Just as you are about to 
		finish him off, he points his staff at you and you fly backwards.

		You are struck with a blow so powerful, you slam right through
		the wall... and into a mysterious black void.

		The black void makes you a bit queasy, before spitting you back 
		out and slamming you into a formidable redwood tree.

		DO YOU:

		A) Brush yourself off and curse.
		B) Shout for someone to help you.
		C) Look around the area.
		"""

        while True:
            do_you = raw_input("> ")
            if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                return self.brush_off_and_curse()
            elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
                return self.shout_help()
            elif "C" in do_you or "c" in do_you or "C)" in do_you or "c)" in do_you:
                return self.look_around_area()
            else:
                print "That's not an option, you idiot.  Pick A, B or C."

    def brush_off_and_curse(self):
        self.health -= 10
        print "\tYe doth have %d mighty health points left" % (self.health)
        print """

		You cower in pain and curse with a mouth so foul it 
		would make even the Evil Dark Lord Gifardus Harduinus blush.

		This word of unholiness has cost you 10 health points."""

        if self.health <= 0:
            return self.game_over()

        else:
            print """

		  Now, you:

	  	A) Shout for someone to help you.
	  	B) Look around the area.
		  """

            while True:
                do_you = raw_input("> ")
                if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                    return self.shout_help()
                elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
                    return self.look_around_area()
                else:
                    print "Did your mom drop you as a baby?  Pick A or B."

    def shout_help(self):
        print "\tYe doth have %d mighty health points left" % (self.health)
        print """

		You stay curled on the ground and touch your 
		injured head gingerly as you shout for help.

		No one replies.

		You shout again, and this time, you hear some cracking through the 
		underbrush. You turn and see a hideous troll-like creature with a large 
		spear coming towards you, although he hasn't apparently spotted you yet. 


		DO YOU:

		A) Stay where you are.
		B) Hide from him.
		"""

        while True:
            do_you = raw_input("> ")
            if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                return self.stay_where_are()
            elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
                return self.hide_from_him()
            else:
                print "That's not an option, you idiot.  Pick A or B."

    def stay_where_are(self):
        print "\tYe doth have %d mighty health points left" % (self.health)
        print """

		The creature sees you lying there. He pokes you with his spear a little, 
		grunts, then turns away and disappears back into the underbrush.

		DO YOU:

		A) Wait for him to come back.
		B) Try to hit him in the back with a spell.
		"""

        while True:
            do_you = raw_input("> ")
            if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                return self.wait_come_back()
            elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
                return self.hit_in_back_spell()
            else:
                print "Hey loser, pick A or B."

    def wait_come_back(self):
        print """
		The creature soon returns, this time accompanied by three similar 
		horrid creatures. 

		You lie down and pretend to be dead. They poke you 
		with spears, and this hurts enough that you cry out.

		They realize you are not dead and stick spears in you until you die.

		GAME OVER!
		"""

        if self.food_point == 1:
            return self.death("stay_where_are")
        else:
            return self.credit()

    def hide_from_him(self):
        print "\tYe doth have %d mighty health points left" % (self.health)
        print """

		You leap into a large bush. The creature looks around, but does not
		uncover your hiding place. He eventually gives up and walks away.

		DO YOU:

		A) Throw a stick at the creature.
		B) Go and attack him.
		"""

        while True:
            do_you = raw_input("> ")
            if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                return self.throw_stick()
            elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
                return self.go_and_attack()
            else:
                print "That's not an option, you idiot.  Pick A or B."

    def hit_in_back_spell(self):
        print "\tYe doth have %d mighty health points left" % (self.health)
        print """

		You shoot a magic arrow spell out of your fingers and hit the creature 
		on the back. You wound the creature, but unfortunately do not kill it, 
		and it limps back towards the place where you are hidden.

		You must now fight it! 

		DO YOU:

		A) Use %s.
		B) Use spell.
		""" % (self.hero['weapon'])

        while True:
            do_you = raw_input("> ")
            if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                return self.vorpal_blade()
            elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
                return self.use_spell()
            else:
                print "I don't think I should need to keep telling you: A or B."

    def throw_stick(self):
        print """
		The stick bounces off the creature's back. 
		It turns and growls but sees no one. 

		Unfortunately for you, you sneeze right at the moment it turns away. 

		The creature runs over to your hiding place. 

		Before you can react, it sticks a spear right into your throat. 

		You die.

		GAME OVER!
		"""
        if self.food_point == 1:
            return self.death("hide_from_him")
        else:
            print self.insult
            return self.credit()

    def go_and_attack(self):
        print "\tYe doth have %d mighty health points left" % (self.health)
        print """

		Since this is a formidable battle, you have 2 choices:

		DO YOU:

		A) Use the mighty %s""" % (self.hero['weapon'])
        print """
		B) Use spell.
		"""

        while True:
            do_you = raw_input("> ")
            if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                return self.vorpal_blade()
            elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
                return self.use_spell()
            else:
                print "That's not an option, you idiot.  Pick A or B."

    def vorpal_blade(self):
        self.health -= 45
        print "\tYe doth have %d mighty health points left" % (self.health)
        print """

		Your powerful %s glows brightly as you face the creature. It growls 
		and raises its spear.

		You swing your %s, and with one stroke, cut the spear in two. 
		The creature spits in rage and draws a sword out of his belt. He fights 
		with great skill; however, he is no match for you in the end. It manages 
		to nick you once, but you finally chop off its head and it falls dead.

		You were quite courageous indeed, but the flesh wound was deeper 
		than it seemed during battle, and this costs you 45 health points."""

        if self.health <= 0:
            return self.game_over()

        else:
            print """
		  NOW, YOU:

		  A) See where the creature came from.
		  B) Search the creature's body.
		  C) Explore the rest of the area.
		  """ % (self.hero['weapon'], self.hero['weapon'])

            while True:
                do_you = raw_input("> ")
                if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                    return self.see_where_creature_came_from()
                elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
                    return self.search_creatures_body()
                elif "C" in do_you or "c" in do_you or "C)" in do_you or "c)" in do_you:
                    return self.explore_rest_area()
                else:
                    print "Are you stupid or something?  Pick A, B or C."

    def spell(self):
        print "\tYe doth have %d mighty health points left" % (self.health)
        print """

		As a young knight, you have learned	
		to perform only but a few spells correctly.

		Alas, as the most powerful wizard in the kingdom 
		I have failed to teach you more suitable magic.  

		Which elementary spell do you choose?:

		A) Lightning.
		B) Bolt of Compression.
		"""

        while True:
            do_you = raw_input("> ")
            if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                return self.lightning()
            elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
                return self.bolt_of_compression()
            else:
                print "Someone put an ignoramus spell on you.  Pick A or B."
                do_you = raw_input("> ")

    def lightning(self):
        print "\tYe doth have %d mighty health points left" % (self.health)
        print """

		You concentrate all your energy, and a huge bolt of lightning 
		shoots from your fingertips and hits the monster straight in the 
		chest. It flies backwards and off a steep cliff. It is dead.

		NOW, YOU:

		A) See where the creature came from.
		B) Search the creature's body.
		C) Explore the rest of the area.
		"""

        while True:
            do_you = raw_input("> ")
            if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                return self.see_where_creature_came_from()
            elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
                return self.search_creatures_body()
            elif "C" in do_you or "c" in do_you or "C)" in do_you or "c)" in do_you:
                return self.explore_rest_area()
            else:
                print "That's not an option, you idiot.  Pick A, B or C."

    def bolt_of_compression(self):
        print "\tYe doth have %d mighty health points left" % (self.health)
        print """

		You aim your powerful spell at the creature's head. 

		An intense blue	bolt flies out of your hand and 
		hits the creature square in the heart!

		Instantly, the creature implodes into a slimy, gelatinous blob and falls 
		to the ground, never to take its true form ever again.

		DO YOU:

		A) See where the creature came from.
		B) Explore the rest of the area.
		"""

        while True:
            do_you = raw_input("> ")
            if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                return self.see_where_creature_came_from()
            elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
                return self.explore_rest_area()
            else:
                print "Someone put an ignoramus spell on you.  Pick A or B."

    def explore_rest_area(self):
        self.health -= 35
        print "\tYe doth have %d mighty health points left" % (self.health)
        print """

		You don't see much else of interest. 
		Lose 35 health points for this waste of precious time."""

        if self.health <= 0:
            return self.game_over()

        else:
            print """
		  You may now:

		  A) Leave the forest.
		  B) See where the creature came from.
		  C) Search the creature's body.
		  """

            while True:
                do_you = raw_input("> ")
                if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                    return self.leave_forest()
                elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
                    return self.see_where_creature_came_from()
                elif "C" in do_you or "c" in do_you or "C)" in do_you or "c)" in do_you:
                    return self.search_creatures_body()
                else:
                    print "That's not an option, you idiot.  Pick A, B or C."

    def see_where_creature_came_from(self):
        print "\tYe doth have %d mighty health points left" % (self.health)
        print """

		You follow the small path the creature made through the forest until 
		a sight makes you stop.

		You are standing outside a huge fortress, which is even more 
		substantial and beautiful than the King's castle itself. 

		Peeking	through some trees, you see a large gate 
		guarded by yet three more of the horrid creatures. 

		They are clearly attuned to their brother's absence...

		DO YOU:

		A) Watch more.
		B) Hail them.
		C) Attack them.
		D) Try to get to the gate.
		"""

        while True:
            do_you = raw_input("> ")
            if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                return self.watch_more()
            elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
                return self.hail_them()
            elif "C" in do_you or "c" in do_you or "C)" in do_you or "c)" in do_you:
                return self.attack()
            elif "D" in do_you or "d" in do_you or "D)" in do_you or "d)" in do_you:
                return self.try_to_get_to_gate()
            else:
                print "Are all the options overwhelming to you? Pick A, B, C or D."

    def watch_more(self):
        print "\tYe doth have %d mighty health points left" % (self.health)
        print """

		You wait to see what the creatures do. They eventually give up 
		looking for their brother and continue to guard the gate.

		You have nothing to learn from watching these creatures, so you:

		A) Hail them.
		B) Attack them.
		C) Try to get to the gate.
		"""

        while True:
            do_you = raw_input("> ")
            if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                return self.hail_them()
            elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
                return self.attack()
            elif "C" in do_you or "c" in do_you or "C)" in do_you or "c)" in do_you:
                return self.try_to_get_to_gate()
            else:
                print "That's not an option, you idiot.  Pick A, B or C."

    def hail_them(self):
        self.health -= 15
        print "\tYe doth have %d mighty health points left" % (self.health)
        print """

		You surprise the creatures, who rush at you with sharp spears. They 
		manage to wound you before you can react, but you are quite brave, 
		and swiftly draw your %s, killing them immediately.

		Lose 15 health points for this unsightly flesh wound."""

        if self.health <= 0:
            return self.game_over()

        else:
            print """Now, the gate is unguarded.

		  DO YOU:

		  A) Go inside.
		  B) Nurse your wounds.
		  """ % (self.hero['weapon'])

            while True:
                do_you = raw_input("> ")
                if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                    return self.go_inside()
                elif do_you == "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
                    return self.nurse_wounds()
                else:
                    print "That's not an option, you idiot.  Pick A or B."

    def try_to_get_to_gate(self):
        print """
		Um, there are still creatures guarding the gate!!! 
		They kill you as you stupidly rush to the door.

		GAME OVER!
		"""
        if self.food_point == 1:
            return self.death("watch_more")
        else:
            print self.insult
            return self.credit()

    def attack(self):
        print "\tYe doth have %d mighty health points left" % (self.health)
        print """

		You catch them off-guard, and desecrate them without taking much damage. 
		However, someone standing on the wall has clearly noticed you, and 
		some arrows are coming down at your position.


		DO YOU:

		A) Try to dodge the arrows.
		B) Try to find some means to fire back.
		C) Run away into the forest.
		"""

        while True:
            do_you = raw_input("> ")
            if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                return self.dodge_arrows()
            elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
                return self.fire_back()
            elif "C" in do_you or "c" in do_you or "C)" in do_you or "c)" in do_you:
                return self.run_into_forest()
            else:
                print "Stupid is as stupid does.  Pick A, B or C."

    def dodge_arrows(self):
        print """
		As you stand there dancing, a small force of skeletons 
		come out of the castle and kill you.

		GAME OVER!  THE END!
		"""
        if self.food_point == 1:
            return self.death("attack")
        else:
            print self.insult
            return self.credit()

    def run_into_forest(self):
        print """
		You run away into the forest and are attacked by thirty MORE creatures 
		just like the ones you just defeated. 

		You fight valiantly but alas, the creatures impale you, and slice 
		your body completely in two. ...ewwww

		GAME OVER!
		"""
        if self.food_point == 1:
            return self.death("attack")
        else:
            print self.insult
            return self.credit()

    def fire_back(self):
        print "\tYe doth have %d mighty health points left" % (self.health)
        print """

		Unfortunately, you do not possess a bow, and you would look pretty 
		ridiculous tossing arrows back at the creatures. 

		You must use a spell if you want to shoot back.

		DO YOU:

		A) Use a spell.
		B) Not use a spell.
		"""

        while True:
            do_you = raw_input("> ")
            if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                return self.use_spell()
            elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
                return self.not_use_spell()
            else:
                print "Did you forget to eat your Wheaties today?  Pick A or B."

    def not_use_spell(self):
        print """
		You don't use a spell, and are trying to flee 
		when an arrow hits you in the back. 

		Your quest ends here.

		GAME OVER, YOU'RE DEAD!
		"""

        if self.food_point == 1:
            return self.death("fire_back")
        else:
            print self.insult
            return self.credit()

    def use_spell(self):
        print "\tYe doth have %d mighty health points left" % (self.health)
        print """

		You use a spell (with an incredibly hard to pronounce name) that 
		redirects the arrows, nailing each of the creatures through the heart! 
		...all but one that is... The remaining creature charges straight at you!!

		DO YOU:

		A) Attack the creature with your sword.
		B) Play dead.
		"""

        while True:
            do_you = raw_input("> ")
            if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                return self.attack_creature_sword()
            elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
                return self.play_dead()
            else:
                print "Stupid is as stupid does.  Pick A or B."

    def play_dead(self):
        print """
		The creature is not fooled.  You are delicious.

		GAME OVER.
		"""
        if self.food_point == 1:
            return self.death("use_spell")
        else:
            print self.insult
            return self.credit()

    def attack_creature_sword(self):
        print "\tYe doth have %d mighty health points left" % (self.health)
        print """

		You have a short but good sword fight with the creature,
		then grow bored and kill it. 

		NOW, YOU:

		A) Go into the castle.
		"""

        while True:
            do_you = raw_input("> ")
            if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                return self.go_in_castle()
            else:
                print "...........you need to choose 'A'......."

    def go_in_castle(self):
        self.health -= 25
        print "\tYe doth have %d mighty health points left" % (self.health)
        print """

		The gate is locked. You must walk around to find another way in.

		Lose 25 health points for this inconvenience."""

        if self.health <= 0:
            return self.game_over()

        else:
            print "A) Walk around the castle to find another way in."

            while True:
                do_you = raw_input("> ")
                if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                    return self.walk_around_castle()
                else:
                    print "............you need to choose 'A'........"

    def walk_around_castle(self):
        print "\tYe doth have %d mighty health points left" % (self.health)

        print """
		The whole stronghold seems well defended. You 
		catch brief glimpses of archers on the walls. 
		However, you are not a target, as they cannot see you.

		The only other way inside appears to be through the fresh water supply. 

		An iron drain lets the water flow in, but keeps intruders
		out. This would be too tremendous of a challenge for the average soldier
		but you are %s the Great! And, using your wit, you can cast a spell. 

		A) Cast a spell at the drain.
		""" % (self.hero['name'])

        while True:
            do_you = raw_input("> ")
            if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                return self.cast_spell_drain()
            else:
                print "Stupid is as stupid does....you need to choose 'A'....."

    def cast_spell_drain(self):
        self.health -= 15
        print "\tYe doth have %d mighty health points left" % (self.health)
        print """

		You cast a huge lightning bolt at the gate, which blasts it open,
		enabling you to easily walk through. 

		But oh no! The guards have heard the noise!  

		Lose 15 health points for your carelessness."""

        if self.health <= 0:
            return self.game_over()
        else:
            print """With haste,

		  DO YOU:

		  A) Go into the main keep.
		  B) Go up onto the wall to explore and kill any guards up there.
		  """

            while True:
                do_you = raw_input("> ")
                if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                    return self.main_keep_and_go_inside()
                elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
                    return self.kill_guards()
                else:
                    print "That's not an option, you idiot.  Pick A or B."

    def main_keep_and_go_inside(self):
        print "\tYe doth have %d mighty health points left" % (self.health)
        print """

		You see a small doorway in a large tower. 
		You carefully open it and walk inside.

		It opens into a small room...with nothing inside except a beautiful, 
		golden-woven tapestry! 	Carefully lifting the tapestry, you see a secret door!

		Clever, aren't you?

		Going through it, you eventually come to a room with a large, grand 
		door on one side and a smaller, more common door on the other. 

		DO YOU:

		A) Go through the large door.
		B) Go through the smaller door.
		C) Investigate this room.
		"""

        while True:
            do_you = raw_input("> ")
            if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                return self.large_door()
            elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
                return self.small_door()
            elif "C" in do_you or "c" in do_you or "C)" in do_you or "c)" in do_you:
                print self.investigate_room()
            else:
                print "Not the sharpest sword in the bunch, are ya?  A, B or C."

    def small_door(self):
        print "\tYe doth have %d mighty health points left" % (self.health)
        print """

		Opening the door, a horrendous smell greets your nostrils. 

		It's a latrine.

		Wondering what a latrine is doing so far inside the castle, you:

		A) Use the latrine.
		B) Destroy the latrine.
		"""

        while True:
            do_you = raw_input("> ")
            if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                return self.use_latrine()
            elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
                return self.destroy_latrine()
            else:
                print "Not the sharpest sword in the bunch, are ya?  Pick A or B."

    def use_latrine(self):
        print "\tYe doth have %d mighty health points left" % (self.health)
        print """

		You sit down and whistle a happy tune as you use the toilet.

		After that, you:


		A) Destroy the latrine.
		B) Investigate this room.
		C) Keep using the latrine.
		"""

        while True:
            do_you = raw_input("> ")
            if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                return self.destroy_latrine()
            elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
                return self.investigate_room()
            elif "C" in do_you or "c" in do_you or "C)" in do_you or "c)" in do_you:
                return self.keep_using_latrine()
            else:
                print "That's not an option, you idiot.  Pick A, B or C."

    def keep_using_latrine(self):
        self.health -= 10
        print "\tYe doth have %d mighty health points left" % (self.health)
        print """

		Man, what did you eat?!  Finish up and investigate the room!

		Lose 10 health points for.... the stink!"""

        if self.health <= 0:
            return self.game_over()

        else:
            print "A) Investigate the room!"

        while True:
            do_you = raw_input("> ")
            if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                return self.investigate_room()
            else:
                print "I guess you're preoccupied with your 'business?'  Pick 'A'."


def destroy_latrine(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		You draw your %s and smash it through the toilet. 

		Because of your brash actions, a geyser of raw sewage erupts, covering you 
		with a foul stench!  

		Alas, you've already destroyed the bucket of water that served as a sink!

		The greenish liquid is nuclear active and you spontaneously burst into flames!

		Quick, quick! Put out the fire!

		A) Swim in the toilet. (eewwwww)
		""" % (self.hero['weapon'])

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.swim_in_toilet()
        else:
            print "It's gross but it will save your life!  Choose 'A'!!"


def swim_in_toilet(self):
    print """
		An unpleasant disease has contaminated the water. You die quickly.

		GAME OVER, THE END!!
		"""
    if self.food_point == 1:
        return self.death("destroy_latrine")
    else:
        print self.insult
        return self.credit()


def investigate_room(self):
    self.health -= 10
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		Nothing of much interest seems to be in here, other than the two doors.

		Lose 10 health points for this fruitless waste of your knightly time."""

    if self.health <= 0:
        return self.game_over()

    else:
        print """A) Go through the large door.
		  B) Go through the smaller door.
	  	"""

        while True:
            do_you = raw_input("> ")
            if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                return self.large_door()
            elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
                return self.small_door()
            else:
                print "Choose a door, man!  A or B."


def nurse_wounds(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		You nurse your wounds before heading to the unguarded gate.  
		(Man, what a sissy, fairy maiden you are!)

		Quickly, run inside!

		A) Go inside.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.main_keep_and_go_inside()
        else:
            print "Choose 'A' before you get caught!"


def kill_guards(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		Sure enough, guards are up there.

		The first three surprise-attacked you, and you took some damage before they died.

		But take heart, the odds are in your favor!  Since not many guards are up there, 
		you destroy the rest with	ease. Now the castle has no guards on the walls.

		DO YOU:

		A) Take valuables from the dead creatures.
		B) Go down the wall.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.take_valuables()
        elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
            return self.go_down_wall()
        else:
            print "That's not an option, you idiot.  Pick A or B."


def take_valuables(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		The guards have misshapen weapons that are of no use to you.

		DO YOU:

		A) Walk along the wall.
		B) Jump down into the courtyard.
		(It looks like a 20 ft jump from here)
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.walk_along_wall()
        elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
            return self.jump_courtyard()
        else:
            print "Choose carefully, A or B?"


def jump_courtyard(self):
    print """
		You fall and break your neck.

		GAME OVER, YOU'RE DEAD!
		"""
    if self.food_point == 1:
        return self.death("take_valuables")
    else:
        print self.insult
        return self.credit()


def walk_along_wall(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		As you walk along the outer wall, you notice only assorted garbage left
		in random piles along the inner edge by the guards, presumably to be 
		collected later.

		Looking out, you see nothing but lush forest surrounding the keep for 
		miles, causing you to idly wonder where you are.

		Feeling slightly refreshed from the walk, you complete the circuit 
		returning to the stairway, and:

		A) Go down the wall.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.go_down_wall()
        else:
            print "It's not that difficult.  Pick 'A'."


def go_down_wall(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		You climb back down the stairway. You can either look at the courtyard 
		or go inside the main keep.

		DO YOU:

		A) Explore the courtyard.
		B) Go into the main keep.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.explore_courtyard()
        elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
            return self.main_keep_and_go_inside()
        else:
            print "That's not an option, you idiot.  Pick A or B."


def explore_courtyard(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		The courtyard is pretty simple. There is a small statue made of marble 
		in the corner, as well as some bushes. But there seems to be no sign of
		any life anywhere.

		A) Go into the main keep.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.main_keep_and_go_inside()
        else:
            print "Pay attention: pick 'A'."


def search_creatures_body(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		You find five gold pieces on its body. You may also take the 
		creature's spear, sword and leather armor with you, if you wish. 

		NOW, YOU:

		A) Explore the rest of the area.
		B) Leave the forest.
		C) See where the creature came from.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.explore_rest_area()
        elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
            return self.leave_forest()
        elif "C" in do_you or "c" in do_you or "C)" in do_you or "c)" in do_you:
            return self.see_where_creature_came_from()
        else:
            print "Not the sharpest sword in the drawer, huh?  Pick A, B or C."


def leave_forest(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		You wander out of the forest until you come to a large grassland. 
		You see a small town way off in the distance. A small river runs into 
		a lake, and an abandoned mill creek by the lake.

		DO YOU:

		A) Go to the town.
		B) Go back into the forest.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.go_to_town()
        elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
            return self.go_back_into_forest()
        else:
            print "Is your mom as dumb as you?  Choose 'A' or 'B'."


def go_back_into_forest(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		Stop wandering back and forth!

		DO YOU:

		A) Leave the forest AGAIN.
		B) Explore the rest of the area.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.leave_forest_again()
        elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
            return self.explore_rest_area()
        else:
            print "Stupid is as stupid does.  Pick A or B."


def leave_forest_again(self):
    print """
		You trip, fall into the stream and...look, you are just being a pest.
		You are going to die on this choice since you keep annoying me.

		GAME OVER!
		"""
    if self.food_point == 1:
        return self.death("go_back_into_forest")
    else:
        print self.insult
        return self.credit()


def look_around_area(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		You stand up and look around. You are certainly not anywhere near the 
		castle.

		You are in a small forest. You look through the trees and see a slab 
		of stone that looks like it might be connected to a structure.

		DO YOU:

		A) Look around some more.
		B) Shout for someone to help you.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.look_around_more()
        elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
            return self.shout_help()
        else:
            print "That's not an option, you idiot.  Pick A or B."


def look_around_more(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		You see nothing else, except a small town outside the forest. You:

		A) Stay in the forest.
		B) Go to the town.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.stay_in_forest()
        elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
            return self.go_to_town()
        else:
            print "That's not an option, you idiot.  Pick A or B."


def stay_in_forest(self):
    print """
		You decide to stay in the forest and wander around.

		Eventually, you come across a huge castle a little way outside the 
		forest.  The castle is heavily protected by guards.  

		Unfortunately, the castle	guards didn't appreciate the intrusion and.... 
		killed you ruthlessly.

		YOU ARE DEAD
		"""
    if self.food_point == 1:
        return self.death("look_around_more")
    else:
        print self.insult
        return self.credit()


def go_to_town(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		You walk into town. Where would you like to visit?

		A) Go to the mage guild.
		B) Go to the Weary Wayfarer.
		C) Leave the town.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.mage_guild()
        elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
            return self.weary_wayfarer()
        elif "C" in do_you or "c" in do_you or "C)" in do_you or "c)" in do_you:
            return self.leave_town()
        else:
            print "Can't you type?  Choose A, B, or C."


def mage_guild(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		The mage there seems happy to see you.

		He offers his special services that he can provide. 
		Each cost several gold pieces, of course. 

		You rummage through your few belongings and find that you have 45 gold pieces.

		A) Teleport (50 gold).
		B) Invisibility spell cast on you (45 gold).
		C) Leave the town.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.teleport()
        elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
            return self.invisibility_spell()
        elif "C" in do_you or "c" in do_you or "C)" in do_you or "c)" in do_you:
            return self.leave_town()
        else:
            print "Are you drunk?!  Pick A, B or C."


def weary_wayfarer(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		The innkeeper is very happy to have a customer, as his little inn has
		been ignored by travelers for a very long time.

		The inn offers hot meals and a drink for 8 gold pieces per meal. 
		A room costs 10 gold.

		DO YOU:

		A) Buy a room.
		B) Buy a meal.
		C) Leave the inn.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.buy_room()
        elif do_you == "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
            return self.buy_meal()
        elif "C" in do_you or "c" in do_you or "C)" in do_you or "c)" in do_you:
            return self.leave_inn()
        else:
            print "You must be the village idiot.  Choose A, B or C."


def leave_town(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		Stealing the teleport, you leave the town and wander around. You see a road 
		leading away from the forest. However, you may also investigate other sites
		of interest near the town.

		DO YOU:

		A) Go back to the town.
		B) Go on the road.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.go_to_town()
        elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
            return self.go_on_road()
        else:
            print "You must be the village idiot.  Pick A or B."


def go_on_road(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		You walk along the road for several hours, until a sight makes you 
		stop.  A small group of buildings on poles are only about 25' off 
		the road. You cannot see what's inside the buildings, nor do you see 
		any guards. 

		DO YOU:

		A) Look around for guards.
		B) Ignore it and continue along the road.
		C) Enter one of the buildings.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.look_around_guards()
        elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
            return self.ignore()
        elif "C" in do_you or "c" in do_you or "C)" in do_you or "c)" in do_you:
            return self.enter_building()
        else:
            print """Roses are red, violets are blue, You're a moron.  
				Choose A, B or C."""


def look_around_guards(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		You carefully scout the area, and see no one. That's strange...

		DO YOU:
		A) Ignore it and continue along the road.
		B) Enter one of the buildings.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.ignore()
        elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
            return self.enter_building()
        else:
            print "That's not an option, you idiot.  Pick A or B."


def enter_building(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		You enter one of the buildings and you see a family of five... octopuses? 

		Suddenly they fade away and sand takes their place. You look down and see that your 
		wrists have been slit, and your voice box no longer exists. You fall over and feel 
		as if you are dead...  you cannot move. 

		Without control of your body you give the wail of a banshee with 
		12 second intervals. You may not be dead, but your mind's been fried. 
		The octopuses and the buildings were a mirage.

		Leave the building, with haste, and see if there's anything else you can do.

		A) Go back to the road.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.ignore()
        else:
            print "Duh, choose 'A' instead of whatever THAT was."


def ignore(self):
    self.health -= 15
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		You continue aimlessly down the road as the hot sun beats down on you. 
		You have no idea where you are, or even how to get home. You vaguely 
		wonder if the kingdom survived the attack. You walk on for miles, 
		seeing nothing but barren grasslands on either side of the road. Hours 
		pass and your body becomes soaked in sweat. You begin to feel dizzy 
		and a sharp pain suddenly pulsates through your head. As you stumble 
		forward, trying to regain control, your vision goes blurry.

		The last thing you see before you pass out is dry grass and the world 
		spinning around you.

		It feels like months later when you awake, but you do not know how much 
		time has passed. 

		Your mind feels hazy, and you keep your eyes closed. You 
		feel warm, but there is still a slight pain in your head. Thoughts 
		spin through your head and you can scarcely remember what happened.

		Lose 15 health points for the ghastly heat exhaustion!"""

    if self.health <= 0:
        return self.game_over()
    else:
        print """
		  DO YOU:

		  A) Slowly open your eyes.
		  B) Keep your eyes closed.
		  """

        while True:
            do_you = raw_input("> ")
            if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
                return self.open_eyes_slowly()
            elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
                return self.close_eyes()
            else:
                print "That's not an option, you idiot.  Pick A or B."


def close_eyes(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		Your mind is still whirling, and you feel slightly dizzy. You keep your 
		eyes closed and try to collect your thoughts, remembering what's 
		happening. With great effort, you feel your thoughts sharpen and finally 
		remember the kingdom, the attack, the passing through a portal, 
		the town... then fainting on the dirt road...

		'I'm not dead...where am I?' you wonder.

		A) Slowly open your eyes
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.open_eyes_slowly()
        else:
            print "Were your eyes closed when you typed that?  Choose 'A'."


def open_eyes_slowly(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		You spot an ugly monster.

		The monster has a humanoid figure, but also has five heads, 16 eyeballs, 
		and slimy skin covered in brown, oozing mucus.	Its fingernails are 
		each more than a foot long, and reek of death and rotting flesh.  

		He attacks you. 

		DO YOU:

		A) Attack it back.
		B) Ask it where you are.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.attack_it_back()
        elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
            return self.ask_where_are()
        else:
            print "EYE ROLLLLL....  Pick A or B."


def attack_it_back(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		Choose your attack strategy wisely!  

		A) Use your sword.
		B) Cast a spell.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.use_sword()
        elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
            return self.cast_spell()
        else:
            print "Did you get hit with the stupidity stick?  Pick A or B"


def ask_where_are(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		Not very bright, he has an ax in his left hand. You've died.

		GAME OVER!
		"""
    if self.food_point == 1:
        return self.death("open_eyes_slowly")
    else:
        print self.insult
        return self.credit()


def cast_spell(self):
    print """
		Unfortunately for you, the monster is immune to magic and 
		tears you apart... slowly... and painfully...............

		YOU'RE DEAD!  GAME OVER!
		"""
    if self.food_point == 1:
        return self.death("attack_it_back")
    else:
        print self.insult
        return self.credit()


def use_sword(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		You fight the ax wielding monster for a few minutes, 
		and eventually kill it. 

		NOW YOU:

		A) Walk down the road.
		B) Find a spell for some reason
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.walk_down_road()
        elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
            return self.find_spell()
        else:
            print "That's not an option, you idiot.  Pick A or B."


def walk_down_road(self):
    print """
		You keep walking until the same events happen over and over again. 
		Caught in a ghastly spell, this continues until you die of old age.

		GAME OVER!
		"""
    if self.food_point == 1:
        return self.death("use_sword")
    else:
        print self.insult
        return self.credit()


def find_spell(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		You check your trusty pocket-book of magic, 
		and indeed, find a strange, mysterious spell. 
		Casting it reveals a large glowing door.

		DO YOU:

		A) Go through the large door.
		B) Continue walking down the path.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.large_door()
        elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
            return self.continue_down_path()
        else:
            print "EYE ROOLLLLLL.  Pick A or B."


def continue_down_path(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		You've been traveling for ages! The glowing door now seems like a 
		good idea, but you turn back and it's no longer there! 

		You must continue walking, on the road to nowhere.  
		In front of you is another door. You run towards but step in
		vile quicksand!  If you do not get out, you'll be dead in just 
		a few short hours.

		Quickly, pull yourself out and look for another way before you die!

		A) Go Back!!!
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.find_spell()
        else:
            print "Uggghhhhh... Choose 'A'!"


def buy_room(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		You are led to a large room upstairs. 
		The bed is neat and small, and you have a good night's sleep.

		When you wake up, you:

		A) Leave the town.
		B) Go to the mage guild.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.leave_town()
        elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
            return self.mage_guild()
        else:
            print "Are you drunk?  Choose 'A' or 'B'."


def buy_meal(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		The meal is a strange, greenish-yellow patty of some kind. 
		It does not taste ideal, but it is nourishing.

		You may now:

		A) Buy a room.
		B) Leave the inn.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.buy_room()
        elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
            return self.leave_inn()
        else:
            print "Did your mother drop you as a baby?  Choose 'A' or 'B'."


def leave_inn(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		This run-down inn has nothing worthwhile to offer. 
		After shaking off the desperate innkeeper, you:

		A) Destroy the inn.
		B) Leave the town.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.destroy_inn()
        elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
            return self.leave_town()
        else:
            print "I can count your brain cells on one hand. Pick 'A' or 'B'."


def destroy_inn(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		You find a lantern and light it, but in your foolish clumsiness you
		drop the lantern to the ground.  Oh no! The ground is covered in dry straw! 
		The inn goes up in flames, and the innkeeper runs out, screaming.

		Riddled with guilt, you surrender.

		A) Let them catch you.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.let_them_catch_you()
        else:
            print "If stupid was a sport you take the gold. Choose 'A'."


def let_them_catch_you(self):
    self.health += 20
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		You let the Town Watch catch you. They throw you in jail, but you GAIN 
		20 health points for your humble surrender. However, this may not be very useful, 
		as you have just been given the death sentence!

		You are moved to a jail for 4 days before you die. 

		DO YOU:

		A) Try to escape.
		B) Stay put in jail.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.try_escape()
        elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
            return self.stay_in_jail()
        else:
            print "I can count your brain cells on one hand.  Pick 'A' or 'B'."


def try_escape(self):
    print """
		You knock out the guard and take his keys. 
		This costs you 15 Crusader points.

		THE END, YOU'RE DEAD! (you have no Crusader points left).
		"""
    return self.death("leave_inn")


def stay_in_jail(self):
    print """
		Bad move!  You die slowly of starvation, alone with the 
		thoughts of your miserable failures.

		THE END!"""
    return self.death("leave_inn")


def teleport(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		You are anxious to get back to the village and protect the people, 
		but unfortunately you don't have enough gold to teleport.

		A) Invisibility spell cast on you (45 gold).
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.invisibility_spell()
        else:
            print "Are you the village drunk?  Choose 'A'."


def invisibility_spell(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		It takes all your gold, but you get the
		mage to turn you (temporarily) invisible!

		A) Take advantage of the opportunity to pick some pockets and cash in!"
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.pick_pockets()
        else:
            print "Do you LIKE being poor?  Choose 'A' to pick some pockets."


def pick_pockets(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		You picked some pockets stealthy enough you now have 50 gold. 

		DO YOU:

		A) Buy the teleport.
		B) Steal the teleport.
		C) Leave the town.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.buy_teleport()
        elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
            return self.steal_teleport()
        elif "C" in do_you or "c" in do_you or "C)" in do_you or "c)" in do_you:
            return self.leave_town()
        else:
            print "You're not too bright, are you? Choose 'A', 'B' or 'C'."


def buy_teleport(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		You find yourself in a completely different area. You're in a small 
		room with torture devices in it, and you're tied to a rack with rusty 
		metal shackles.

		DO YOU:

		A) Look around at the torture-device-filled room.
		B) Try to break the ropes.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.buy_teleport()
        elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
            return self.break_ropes()
        else:
            print "That's not an option, you idiot.  Pick A or B."


def break_ropes(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		You fail to escape, and you go into a long sleep, longer then you expected. 
		You are dead!!  THE END 
		"""
    return self.death("buy_teleport")


def look_around_torture_room(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		You look around, and find a switch to release your shackles, that is 
		conveniently in reach.

		Luckily you still have the %s.  You slay a few monsters 
		before heading out a very large door at the back of the room.

		A) Open the door and leave, quickly!
		""" % (self.hero['weapon'])

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.large_door()
        else:
            print "Do you WANT to die?!  Choose 'A'!!"


def large_door(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		This opens into a magnificent room, with a large throne in it. A 
		creature is sitting on the throne! As you try to take in all the 
		breathtaking details of this ornate room, some guards rush at you! 
		However, you kill them easily!

		Now, you:

		A) Talk to the creature on the throne.
		B) Attack the creature on the throne.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.talk_to_creature_throne()
        elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
            return self.attack_creature_throne()
        else:
            print "Cat got your tongue?  Pick A or B."


def steal_teleport(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		You find yourself in a completely different area. You're in a small 
		room with torture devices in it, and you're tied to a rack with rusty shackles.

		DO YOU:

		A) Look around at the torture-device-filled room.
		B) Try to break the ropes.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return 'look_around_torture_room'
        elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
            return self.break_ropes()
        else:
            print "Not the brightest sword in the drawer, are you? 'A' or 'B'?"


def attack_creature_throne(self):
    self.health += 25
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		Without warning, you rush at the creature in the throne and cut off its arm! 

		The beast points its staff at you with its other arm and unexplainable
		excruciating pain overcomes you.

		Valiantly, you muster the strength to continue fighting the beast!

		Gain 25 health points for your bravery!

		A) Fight with your sword.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.fight_with_sword()
        else:
            print "Hey, Doofus, you want to pick 'A'."


def fight_with_sword(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		You swing your sword over your head, waiting for the creature to make a
		move. It shoots out a bolt of light at you, which you manage to dodge. 
		You rush at it and strike it, then it hits you with its staff. 
		However, you break the staff in two! Then, the creature pulls out a 
		glowing dagger and attacks you again.

		A) Continue to fight with your sword!!
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.continue_sword_fight()
        else:
            print "Fight, man, fight!  Choose 'A'!"


def continue_sword_fight(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		The dagger misses, and you slay the creature easily. Just then, without 
		warning, a dozen creatures, that look just like the last one, rush into the room.

		DO YOU:

		A) Attack the creatures.
		B) Sit down and ponder the meaning of life.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.attack_the_creatures()
        elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
            return self.sit_and_wonder()
        else:
            print "Can't you type?!  Choose 'A' or 'B'"


def attack_the_creatures(self):
    print """
		You fight valiantly, but you are no match for such numbers.
		YOU DIE! (quip)
		THE END.
		"""
    return self.death("large_door")


def sit_and_wonder(self):
    print """
		Um, you haven't been on the ball lately have you, Stupid? IT'S OVER!
		YOU'RE DEAD!!
		"""
    if self.food_point == 1:
        return self.death("large_door")
    else:
        print self.insult
        return self.credit()


def talk_to_creature_throne(self):
    print "\tYe doth have %d mighty health points left" % (self.health)
    print """

		The creature seems oblivious to your presence. Even when you speak, 
		it remains motionless.  You wonder what's wrong with it.

		DO YOU:

		A) Go up and tap it on the shoulder.
		B) Shrug and leave the room.
		C) Chop its head off.
		"""

    while True:
        do_you = raw_input("> ")
        if "A" in do_you or "a" in do_you or "A)" in do_you or "a)" in do_you:
            return self.tap_shoulder()
        elif "B" in do_you or "b" in do_you or "B)" in do_you or "b)" in do_you:
            return self.shrug()
        elif "C" in do_you or "c" in do_you or "C)" in do_you or "c)" in do_you:
            return self.chop_head()
        else:
            print "I can count your brain cells on one hand.. 'A', 'B' or 'C'?"


def tap_shoulder(self):
    print """
		As you walk up to it to say something, it suddenly goes into action!
		It draws a sword and kills you in one swift motion. Nice work.
		THE END, YOU'RE DEAD!
		"""
    if self.food_point == 1:
        return self.death("talk_to_creature_throne")
    else:
        print self.insult
        return self.credit()


def shrug(self):
    print """
		You turn to leave, but have a tingling sensation on your back.  
		Spinning around, you see the creature on the throne standing and 
		grinning at you.  The sensation spreads, it feels like you are caught
		in a thorn bush.  You raise your sword and rush at the creature, but
		move no more than five feet forward when you are reduced to a pile 
		of ashes on the floor.

		YOU'RE DEAD!
		"""
    if self.food_point == 1:
        return self.death("talk_to_creature_throne")
    else:
        print self.insult
        return self.credit()


def chop_head(self):
    print """
		You charge at the creature with all your might, summoning all the magic
		of the great ancestors of the kingdom of Zelanna.  Wielding your %s, you 
		obliterate him, and his guts explode all over the room.

		That was the evil leading necromancer King, and you killed it.
		All its undead creatures are destroyed, you take the castle.  

		Now you are a king.  And there was great rejoicing in the land.

		YOU WON! THE END!
		""" % (self.hero['weapon'])


new = Game("go_to_king", 100)
new.begin()