# Player vars
define player = Character("[playerName]")
define playerSubjectPronoun = "they"
define playerObjectPronoun = "them"
define playerDepPossesivePronoun = "their"

# Player character vars
define playerCharacter = Character("[playerUsername]")
default playerCharacterSubjectPronoun = "they"
default playerCharacterObjectPronoun = "them"
default playerCharacterDepPossesivePronoun = "their"
define playerUsername = ""
define playerPassword = ""
define playerID = ""

# Characters
define friendA = Character("Brogan", image="Friend01")
define friendB = Character("Cynthia", image="Friend02")
define startBoss = Character("Ignis the Conqueror", image="Boss01")
define iceBoss = Character("Iceclops", image="Boss02")
define gameLog = Character("GameLog")
define hacker = Character("[hackerName]")

# BG IMG
image Game Tavern = "bg_GW_GameTavern.png"
image Game World Arena 01 = "bg_GW_GameWorldArena01.png"
image Game World Arena 02 = "bg_GW_GameWorldArena02.png"
image Generic Game Env = "bg_GW_GenericGameEnvironment.png"
image Forest = "bg_GW_forest.png"
image Hacker Space = "bg_GW_HackerSpace.png"
image Bedroom = "bg_RW_Bedroom.png"
image City = "bg_RW_City.png"
image Prison = "bg_RW_Prison.png"
image Hallway = "bg_RW_Hallway.png"
image crash = "bg_GW_crash.png"
image logInScreen = "bg_GW_login.png"
image Forest Snow = "bg_GW_SnowForest.png"
image Prison Closed = "bg_RW_Prison.png"
image Prison Open = "bg_RW_Prison_Door_Open.png"
image Prison Alert:
    "bg_RW_Prison_Red.png"
    0.5
    "bg_RW_Prison.png"
    0.5
    "bg_RW_Prison_Red.png"
    0.5
    "bg_RW_Prison.png"
    0.5
    "bg_RW_Prison_Red.png"
    0.5
    "bg_RW_Prison_Steam1.png"
    0.25
    "bg_RW_Prison_Steam2.png"
    0.25
    "bg_RW_Prison_Steam1.png"
    0.25
    "bg_RW_Prison_Steam2.png"
    0.25
    repeat
image doorWedge1 = "bg_RW_Prison_Door_Wedge01.png"
image doorWedge2 = "bg_RW_Prison_Door_Wedge02.png"
image doorWedge3 = "bg_RW_Prison_Door_Wedge03.png"
image doorWedge4 = "bg_RW_Prison_Door_Wedge04.png"
image doorWedge5 = "bg_RW_Prison_Door_Wedge05.png"
image doorWedge6 = "bg_RW_Prison_Door_Wedge06.png"
image doorWedge7 = "bg_RW_Prison_Door_Wedge07.png"
image doorWedge8 = "bg_RW_Prison_Door_Wedge08.png"

# Char IMG
image Boss01 angry = "ch_GW_Boss01_angry.png"
image Boss01 neutral:
    "ch_GW_Boss01_neutral1.png"
    0.33
    "ch_GW_Boss01_neutral2.png"
    0.33
    "ch_GW_Boss01_neutral3.png"
    0.33
    "ch_GW_Boss01_neutral2.png"
    0.33
    repeat
image Boss02 neutral = "ch_GW_Boss02_neutral.png"
image Boss02 possessed = "ch_GW_Boss02_POSSESSED.png"
image Friend01 angry = im.Crop("ch_GW_Friend01_angry.png", (100, 0, 520, 720))
image Friend01 happy = im.Crop("ch_GW_Friend01_happy.png", (100, 0, 520, 720))
image Friend01 neutral = im.Crop("ch_GW_Friend01_neutral.png", (100, 0, 520, 720))
image Friend01 sad = im.Crop("ch_GW_Friend01_sad.png", (100, 0, 520, 720))
image Friend02 angry = im.Crop("ch_GW_Friend02_angry.png", (100, 0, 520, 720))
image Friend02 happy = im.Crop("ch_GW_Friend02_happy.png", (100, 0, 520, 720))
image Friend02 neutral = im.Crop("ch_GW_Friend02_neutral.png", (100, 0, 520, 720))
image Friend02 sad = im.Crop("ch_GW_Friend02_sad.png", (100, 0, 520, 720))
image GWHacker:
    "ch_GW_Medusa1.png"
    0.15
    "ch_GW_Medusa2.png"
    0.15
    "ch_GW_Medusa3.png"
    0.15
    "ch_GW_Medusa4.png"
    0.15
    repeat
image RWHacker neutral = "ch_RW_Hacker_neutral.png"
image CorpGuy neutral = im.Crop("ch_RW_CorpGuy_neutral.png", (200, 0, 420, 720))
image CorpGuy angry = im.Crop("ch_RW_CorpGuy_angry.png", (200, 0, 420, 720))

# Item IMG
image hacker item = im.Scale("item_hackerItem.png", 360, 360)

# Other IMG
image HP = im.Scale("boss_hp.png", 360, 90)
image redBar = im.Scale("boss_hp_bar.png", 360, 90)
image campfire:
    im.Scale("bg_GW_campfire1.png", 360, 360)
    0.15
    im.Scale("bg_GW_campfire2.png", 360, 360)
    0.15
    im.Scale("bg_GW_campfire3.png", 360, 360)
    0.15
    im.Scale("bg_GW_campfire4.png", 360, 360)
    0.15
    repeat
image darkOverlay = "bg_forest_darkoverlay.png"
image snowTree1 = "bg_GW_snowtree1.png"
image snowTree2 = "bg_GW_snowtree2.png"
image snowTree3 = "bg_GW_snowtree3.png"

# Other game vars
define digitalWorld = "NeuralScape"
define gameWorld = "Hero's Fantasy Online"
define corporation = "Noodle Bowl Industries Inc. Corp"

# Non game vars
image credit = Text(creditText, text_align=0.5)
image Rice Bowl = Composite((525, 314), (121, 0), "rice_bowl_studios_PLACEHOLDER.png")

# Other vars
define noFlashing = True

label splashscreen:
    $ renpy.pause (0)
    scene whitedrop with None
    if config.developer:
        "{cps=0}DEBUG MODE ENABLED{/cps}"
    show Rice Bowl:
        xalign 0.5
        ypos -0.7
        parallel:
            easeout 3.0 ypos 1.3
        parallel:
            linear 3.0 rotate 480
    $ renpy.pause(4.0)
    scene black with fade
    return

label main_menu:
    return

label start:
    $ suppress_overlay = False
    if config.developer:
        "{cps=0}GAME START{/cps}"
    menu: 
        "{cps=0}{font=Kenney Rocket.ttf}This game has flashing and strobing, which can cause seizures. Would you like to disable them?{/font}{/cps}"
        "{font=Kenney Rocket.ttf}Yes{/font}":
            $ noFlashing = True
        "{font=Kenney Rocket.ttf}No{/font}":
            $ noFlashing = False
    python:
        while playerUsername == "":
            playerUsername = renpy.input("{font=Kenney Rocket.ttf}Username:{/font}", length=36)
            playerUsername = playerUsername.strip()
        while playerPassword == "":
            playerPassword = renpy.input("{font=Kenney Rocket.ttf}Password:{/font}", length=16)
            playerPassword = playerPassword.strip()
        playerID = "#" + generateHex(8)
    "{font=Kenney Rocket.ttf}[gameLog]{/font}" """
    {font=Kenney Rocket.ttf}Launching [gameWorld]{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}{/font}{nw}
    
    {font=Kenney Rocket.ttf}We did not find a character with that login info.{/font}
    
    {font=Kenney Rocket.ttf}Launching character creation{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}{/font}{nw}
    """
    $ gameWorld = "HFO"
    menu:
        "{cps=0}{font=Kenney Rocket.ttf}What are your character's pronouns?{/font}{/cps}"
        "{font=Kenney Rocket.ttf}He/Him/His{/font}":
            python:
                playerCharacterSubjectPronoun = "he"
                playerCharacterObjectPronoun = "him"
                playerCharacterDepPossesivePronoun = "his"
        "{font=Kenney Rocket.ttf}She/Her/Hers{/font}":
            python:
                playerCharacterSubjectPronoun = "she"
                playerCharacterObjectPronoun = "her"
                playerCharacterDepPossesivePronoun = "her"
        "{font=Kenney Rocket.ttf}They/Them/Their{/font}":
            python:
                playerCharacterSubjectPronoun = "they"
                playerCharacterObjectPronoun = "them"
                playerCharacterDepPossesivePronoun = "their"
        "{font=Kenney Rocket.ttf}Other{/font}":
            python:
                playerCharacterSubjectPronoun = renpy.input("{font=Kenney Rocket.ttf}Subject Pronoun (ex. he, she, they):{/font}", length=24)
                playerCharacterSubjectPronoun = playerCharacterSubjectPronoun.strip()
                if not playerCharacterSubjectPronoun:
                    playerCharacterSubjectPronoun = "they"
                playerCharacterObjectPronoun = renpy.input("{font=Kenney Rocket.ttf}Object Pronoun (ex. him, her, them):{/font}", length=24)
                playerCharacterObjectPronoun = playerCharacterObjectPronoun.strip()
                if not playerCharacterObjectPronoun:
                    playerCharacterObjectPronoun = "them"
                playerCharacterDepPossesivePronoun = renpy.input("{font=Kenney Rocket.ttf}Dependent Possessive Pronoun (ex. his, her, their):{/font}", length=24)
                playerCharacterDepPossesivePronoun = playerCharacterDepPossesivePronoun.strip()
                if not playerCharacterDepPossesivePronoun:
                    playerCharacterDepPossesivePronoun = "their"
    python:
        playerName = ""
        while playerName == "":
            playerName = renpy.input("{font=Kenney Rocket.ttf}Real Name:{/font}", length=36)
            playerName = playerName.strip()

label startBossFight:
    if config.developer:
        menu:
            "Where to jump to?"
            "Scene 1":
                pass
            "Scene 2":
                jump startHackerSpace
            "Scene 3":
                jump scene3Start
            "Scene 4":
                jump scene4Start
            "Scene 5":
                jump scene5Start
            "Scene 6":
                jump scene6Start
            "More":
                menu:
                    "Where to jump to?"
                    "Scene 7 Orange":
                        jump scene7Orange
                    "Scene 7 Purple":
                        jump scene7Purple
                    "Scene 8":
                        jump scene8Start
                    "Scene 9":
                        jump scene9Start
                    "Scene 10":
                        jump scene10Start
                    "End":
                        jump kill
                    "Back":
                        jump startBossFight
    # TODO: music 1.1.1 boss fight music
    scene Game World Arena 01
    show Boss01 neutral at right
    show Friend01 angry at left:
        xzoom -1.0
    show HP at top with easeintop
    show redBar at top:
        size (0, 90)
        linear 1.5 size (360, 90)
    python:
        playerCharacterSubjectPronoun = playerCharacterSubjectPronoun.lower()
        if playerCharacterSubjectPronoun == "they":
            tmpChosen = "are"
        else:
            tmpChosen = "is"
    friendA "Ugh! Why's this taking so long? Where the heck [tmpChosen] [playerCharacterSubjectPronoun]?"
    startBoss "HAHAHAHA THERE IS NO HOPE FOR YOU PUNY MORTAL!"
    play sound "audio/mirror_shattering.wav"
    show Boss01 neutral with vpunch
    friendA "Damn, my weapon's almost broken! I can't stay here much longer."
    "{font=Kenney Rocket.ttf}[gameLog]{/font}" "{font=Kenney Rocket.ttf}[playerCharacter] has entered the area.{/font}"
    show Friend01 happy
    friendA "There you are! It's about time! Wasn't the plan to ambush this boss like 30 minutes ago?"
    menu:
        "Sorry I'm late. I fell asleep.":
            pass
        "I'm here now. Let's do this.":
            pass
    friendA "Well come on! You know, if we don't beat this <insulting nickname for boss> tonight, [friendB]'s never gonna let us forget it."
    "You and [friendA] draw your weapons."
    startBoss "YOU PATHETIC CREATURES REALLY THINK YOU CAN DEFEAT ME?"
    show Friend01 angry
    friendA "I'm going in. Cover me!"
    menu:
        "Attack 1":
            pass
        "Attack 2":
            pass
    show Friend01 angry:
        ease 0.25 zoom 1.1
        ease 0.25 xalign 0.75
    $ renpy.pause(0.5)
    show Boss01 neutral:
        ease 0.05 zoom 0.9 xoffset 100
        ease 0.1 zoom 1.0 xoffset 0
    $ renpy.pause(0.15)
    play sound "audio/swordMetal6.ogg"
    show redBar:
        linear 0.25 size (360 * 3 / 4, 90)
    show Friend01 angry:
        ease 0.35 xalign 0.0
        ease 0.25 zoom 1.0
    "[friendA]'s weapon shatters into a million pieces."
    friendA "Shit!"
    friendA "I don't get it, our level is way higher than his. Shouldn't this fight be easy?"
    menu:
        "Yeah, it's kind of weird.":
            pass
        "Maybe you're just bad.":
            friendA "Very funny coming from the one who almost missed the whole fight."
    friendA "I don't know if we can win this, [playerCharacter]."
    $ tmpFlag = False

label startBossAttackChoice:
    menu:
        "Attack":
            play sound "audio/swordMetal6.ogg"
            show Boss01 neutral:
                ease 0.1 zoom 0.9 xoffset 100
            $ renpy.pause(0.1)
            show redBar:
                linear 0.25 size (360 * 2 / 4, 90)
            show Boss01 neutral:
                ease 0.1 zoom 1.0 xoffset 0
            "{font=Kenney Rocket.ttf}[gameLog]{/font}" "{font=Kenney Rocket.ttf}Critical Hit!{/font}"
            friendA "Nice!"
        "Run Away" if not tmpFlag:
            $ tmpFlag = True
            show Boss01 angry:
                ease 0.25 zoom 1.1
            startBoss "HAHAHA YOU FOOLS CAN'T ESCAPE ME"
            show Boss01 neutral:
                ease 0.25 zoom 1.0
            jump startBossAttackChoice

label startBossAttackChoice2:
    menu:
        "Attack":
            play sound "audio/swordMetal6.ogg"
            show Boss01 neutral:
                ease 0.1 zoom 0.9 xoffset 100
            $ renpy.pause(0.1)
            show redBar:
                linear 0.25 size (360 / 4, 90)
            show Boss01 neutral:
                ease 0.1 zoom 1.0 xoffset 0
            "{font=Kenney Rocket.ttf}[gameLog]{/font}" "{font=Kenney Rocket.ttf}Critical Hit!{/font}"
            friendA "Wow!"
        "Run Away" if not tmpFlag:
            $ tmpFlag = True
            show Boss01 angry:
                ease 0.25 zoom 1.1
            startBoss "YOU WON'T GET AWAY THAT EASY"
            show Boss01 neutral:
                ease 0.25 zoom 1.0
            jump startBossAttackChoice2

label startBossAttackChoice3:
    menu:
        "Attack":
            play sound "audio/swordMetal6.ogg"
            show Boss01 angry:
                ease 0.1 zoom 0.9 xoffset 100
            $ renpy.pause (0.1)
            show redBar:
                linear 0.25 size (0, 90)
            "{font=Kenney Rocket.ttf}[gameLog]{/font}" "{font=Kenney Rocket.ttf}Critical Hit!{/font}"
            friendA "What the-"
        "Run Away" if not tmpFlag:
            $ tmpFlag = True
            show Boss01 angry:
                ease 0.25 zoom 1.1
            startBoss "WHO SAYS YOU CAN RUN?"
            show Boss01 neutral:
                ease 0.25 zoom 1.0
            jump startBossAttackChoice3
    startBoss "AAAARRRGGGGHHHHH HOW COULD THIS HAPPEN???"
    hide Boss01 with zoomout
    hide redBar
    hide HP with easeouttop
    # TODO: music 1.1.2 post boss fight music
    show Friend01 happy
    friendA "That was awesome!"
    menu:
        "I know":
            pass
        "I just got lucky":
            pass
    friendA "Let's see what kind of loot we got!"
    friendA "Woah is that a-"
    show Friend01 neutral
    friendA "Oh wait... never mind."
    friendA "Ooo maybe this is-"
    friendA "Nah, I got nothing. How about you? Anything good?"
    "Only one item appears on your screen."
    show hacker item at truecenter with zoomin
    $ tmpGlitchText = glitchText(16)
    "{font=Kenney Rocket.ttf}[gameLog]{/font}" "{font=Kenney Rocket.ttf}[tmpGlitchText] was added to your inventory{/font}"
    friendA "That's all you got? God, [friendB]'s gonna get a kick outta this one."
    friendA "Hey wait. What's up with it's name? I can't read it on my screen. Can you?"
    playerCharacter "No."
    friendA "Huh, weird. Well, maybe [friendB] knows something about it-{w=0.4}{nw}"
    stop music fadeout 0.5
    show screen tear()
    # TODO: play sfx 01 glitching
    $ renpy.pause(1.0)
    hide screen tear
    play sound "audio/computer_error_alert.wav"
    scene black
    show crash at truecenter with vpunch
    $ renpy.pause(1.5)
    hide crash with zoomout

label startRealWorld:
    # TODO: music 1.1.3 hanging out in room
    scene Bedroom with fade
    player """
    [gameWorld] seems to have crashed.
    
    My headset is burning hot.
    
    What {i}was{/i} that weird bracelet item.
    """
    $ renpy.music.set_pause(True)
    play sound "<to 2.5>audio/phone_ringing.wav"
    $ renpy.pause(2)
    $ renpy.music.set_pause(False)
    player "It's [friendB]."
    friendB "Hey [player] where are you two? I thought you and [friendA] were gonna come over after you took down [startBoss]."
    menu:
        "About that…":
            friendB "Ha! You seriously fell asleep? Here I was thinking [friendA] was the stupid one."
        "I'll be there in a few minutes.":
            friendB "Alright. Are you still with [friendA]?"
    friendB "Oh, here he is now. I’ll see you in a bit. Bye."
    player "I'd better try logging back in."
    "You put your headset back on."
    stop music fadeout 1.0
    scene logInScreen
    image passwordHintText = ParameterizedText(xalign=0.5, yalign=0.5)
    image passwordText = ParameterizedText()
    image playerIdText = ParameterizedText(xalign=1.0)
    show text "{color=#000}[playerUsername]{/color}":
        zoom 1.5
        anchor (0, 0)
        pos (300, 400)
    show playerIdText "{color=#7e7e7e}[playerID]{/color}":
        zoom 1.5
        pos (990, 400)
    show passwordHintText "{color=#000}[playerPassword]{/color}":
        transform_anchor True
        rotate -15
        pos (130, 125)
    python:
        tmpPassword = renpy.input("Password:")
        tmpPassword = tmpPassword.strip()
    while tmpPassword != playerPassword:
        play sound "audio/error2.ogg"
        "{font=Kenney Rocket.ttf}[gameLog]{/font}" "{font=Kenney Rocket.ttf}Incorrect Login.{/font}"
        python:
            tmpPassword = renpy.input("Password:")
            tmpPassword = tmpPassword.strip()
    window hide
    $ tmpChosen = ""
    while len(tmpChosen) < len(tmpPassword):
        $ renpy.pause(0.15)
        $ tmpChosen += "*"
        show passwordText "{color=#000}[tmpChosen]{/color}":
            zoom 1.5
            anchor (0, 0)
            pos (300, 525)
    $ renpy.pause(0.5)
    scene black with fade
    "..."
    # TODO: music 1.1.4 trying to log back on
    """
    {i}???{/i}
    
    {i}My headset is getting hot again{/i}.

    You try to remove your headset
    """
    scene black with pulse(6, "#f00", 0.7, 1.2, 0.1, 0.1, 0.25, 2.0)
    """
    {i}I can't lift my arm{/i}.

    {i}It feels like something's grabbing my wrist{/i}.

    {i}I can't get the headset off with my arm stuck like this{/i}.

    {i}The heat is getting unbearable{/i}...
    """
    stop music fadeout 1.0

label startHackerSpace:
    # TODO: music 1.2.1 hacker space
    scene Hacker Space with fade
    "Where am I?"
    show GWHacker at center with easeinbottom
    $ hackerName = "{b}redacted{/b}"
    "{font=Kenney Rocket.ttf}[hacker]{/font}" "{font=Kenney Rocket.ttf}Good question. From what I can see, I'm pretty sure you're in a bedroom.{/font}"
    $ tmpChosen = -1
    menu:
        "Who are you?":
            $ tmpChosen = 0
            "{font=Kenney Rocket.ttf}[hacker]{/font}" "{font=Kenney Rocket.ttf}That's kind of complicated. Could we start with the easy questions please?{/font}"
        "Did you just read my mind?":
            $ tmpChosen = 1
            "{font=Kenney Rocket.ttf}[hacker]{/font}" """
            {font=Kenney Rocket.ttf}Oh, if only it were that simple! What do I look like? Some kind of fortune teller?{/font}
            
            {font=Kenney Rocket.ttf}Let's just say I made an extremely educated guess{/font}
            """
        "How did you know that?":
            $ tmpChosen = 2
            "{font=Kenney Rocket.ttf}[hacker]{/font}" """
            {font=Kenney Rocket.ttf}Um... I'm actually a psychic.{/font}
            
            {font=Kenney Rocket.ttf}No, a genie!{/font}
            
            {font=Kenney Rocket.ttf}Or maybe I'm your conscience! Hehe, spooky, right?{/font}
            """
    menu:
        "Who are you?" if tmpChosen != 0:
            pass
        "Did you just read my mind?" if tmpChosen != 1:
            pass
        "How did you know that?" if tmpChosen != 2:
            pass
    "{font=Kenney Rocket.ttf}[hacker]{/font}" "{font=Kenney Rocket.ttf}Okay, I think that's enough questioning for today.{/font}"
    "You try to speak, but nothing comes out. It feels as though you are underwater."
    "{font=Kenney Rocket.ttf}[hacker]{/font}" """
    {font=Kenney Rocket.ttf}Right, now where was I? Let's see, plant the thing, dramatic entrance, obligatory exposition...{/font}
    
    {font=Kenney Rocket.ttf}Ah of course{/font}
    
    {font=Kenney Rocket.ttf}{i}*ahem*{/i}{/font}
    """
    if playerName != playerUsername:
        "{font=Kenney Rocket.ttf}[hacker]{/font}" """
        {font=Kenney Rocket.ttf}Welcome to my world, [playerCharacter]! Or should I say [player].{/font}
        
        {font=Kenney Rocket.ttf}Which would you prefer?{/font}
        """
        $ tmpFlag = True
    else:
        "{font=Kenney Rocket.ttf}[hacker]{/font}" "{font=Kenney Rocket.ttf}Welcome to my world, [player].{/font}"
        python:
            preferredName = playerName
            preferredSubjectPronoun = playerSubjectPronoun
            preferredObjectPronoun = playerObjectPronoun
            preferredDepPossesivePronoun = playerDepPossesivePronoun
        jump afterHackerSpaceNameChoice

label hackerSpaceNameChoice:
    menu:
        "Call me [playerCharacter]":
            python:
                preferredName = playerUsername
                preferredSubjectPronoun = playerCharacterSubjectPronoun
                preferredObjectPronoun = playerCharacterObjectPronoun
                preferredDepPossesivePronoun = playerCharacterDepPossesivePronoun
        "Call me [player]":
            python:
                preferredName = playerName
                preferredSubjectPronoun = playerSubjectPronoun
                preferredObjectPronoun = playerObjectPronoun
                preferredDepPossesivePronoun = playerDepPossesivePronoun
        "How do you know my name?" if tmpFlag:
            $ tmpFlag = False
            show screen tear()
            play sound "audio/error2.ogg"
            $ renpy.pause(0.5)
            hide screen tear
            "{font=Kenney Rocket.ttf}[hacker]{/font}" "{font=Kenney Rocket.ttf}Hey, what did I say about asking questions?{/font}"
            jump hackerSpaceNameChoice
    
label afterHackerSpaceNameChoice:
    if playerName != playerUsername:
        "{font=Kenney Rocket.ttf}[hacker]{/font}" "{font=Kenney Rocket.ttf}Ya know, I'm so glad you're here [preferredName]. I was really starting to think {i}nobody{/i} would show up to my little party.{/font}"
    else:
        "{font=Kenney Rocket.ttf}[hacker]{/font}" "{font=Kenney Rocket.ttf}Ya know, I'm so glad you're here. I was really starting to think {i}nobody{/i} would show up to my little party.{/font}"
    "{font=Kenney Rocket.ttf}[hacker]{/font}" "{font=Kenney Rocket.ttf}But then, right when I was about to call it off, you came along and found my invitation!{/font}"
    show hacker item at truecenter with zoomin
    $ tmpGlitchText = glitchText(16, False, True)
    """
    The mysterious figure gestures toward the [tmpGlitchText], which is now fastened to your wrist
    
    {i}How did that get there?{/i}
    """
    hide hacker item with zoomout
    "{font=Kenney Rocket.ttf}[hacker]{/font}" """
    {font=Kenney Rocket.ttf}And guess what. The best part is{w=3.0}: it's yours to keep! Consider it a party favor from your new best friend.{/font}
    
    {font=Kenney Rocket.ttf}Oh, that reminds me,{w=1.0} I haven't introduced myself yet! {size=-5}Gosh, what kind of friend doesn't even know their friend's name?{/size}{/font}
    
    {font=Kenney Rocket.ttf}Sorry, it's been a while since I've actually talked to someone for real like this.{/font}
    
    {font=Kenney Rocket.ttf}Hmmm...{w=0.5} where do I begin?{w=1.0} I've gone by a LOT of names in the past, <name1>{w=0.5}, <name2>{w=0.5}, <name3>{w=1.0}, {size=-5}<embarrassing name>{w=0.5}... I don't know what I was thinking with that one{/size}...{/font}
    
    {font=Kenney Rocket.ttf}Anything ring a bell? You've probably heard of me before, right? I mean - I'm {i}kind of{/i} a big deal.{/font}
    """
    "..."
    "{font=Kenney Rocket.ttf}[hacker]{/font}" """
    {font=Kenney Rocket.ttf}...{/font}
    
    {font=Kenney Rocket.ttf}?{/font}
    
    {font=Kenney Rocket.ttf}Nothing?{w=1.0} Seriously? {size=-5}Wow, have I really fallen off that hard?{/size}{/font}
    """
    $ hackerName = "Medusa"
    "{font=Kenney Rocket.ttf}[hacker]{/font}" """
    {font=Kenney Rocket.ttf}Well, whatever, since we're friends you can call me [hacker]{/font}
    
    {font=Kenney Rocket.ttf}So.. I'm sure you're probably wondering why I invited you here today. Well you see, I actually noticed you and your friends are pretty into that game.{/font}
    
    {font=Kenney Rocket.ttf}What was it called again?{w=2.0} You know, the one you've been playing {i}literally{/i} non-stop. {size=-5}Like seriously don't you have a job or something?{/size}{/font}
    
    {font=Kenney Rocket.ttf}Anyways, I've got a game of my own going on{w=0.5} -so to speak-, and it's {i}really{/i} important{/font}
    
    {font=Kenney Rocket.ttf}But you see, the thing is, I kind of need some help getting to the end of it.{/font}
    
    {font=Kenney Rocket.ttf}And you know...{/font}
    
    {font=Kenney Rocket.ttf}I just thought...{/font}
    
    {font=Kenney Rocket.ttf}{i}Since we are friends,{/i}{/font}
    
    {font=Kenney Rocket.ttf}You could lend me a hand!{/font}
    """
    menu:
        "ok...?":
            $ tmpFlag = False
        "Hell no!":
            $ tmpFlag = True
    "{font=Kenney Rocket.ttf}[hacker]{/font}" "{font=Kenney Rocket.ttf}Awesome! I knew I could count on you [preferredName]!{w=1.0} I mean, what are friends for, right?{/font}"
    if tmpFlag:
        "{font=Kenney Rocket.ttf}[hacker]{/font}" "{font=Kenney Rocket.ttf}{size=-10}Totally doesn't bother me that you don't really want to help.{/size}{/font}"
    "{font=Kenney Rocket.ttf}[hacker]{/font}" """    
    {font=Kenney Rocket.ttf}And don't worry! I promise that when we beat my little game, there's gonna be a special reward just for you.{w=1.0} Oh! And I can even help you with your game too!{/font}
    
    {font=Kenney Rocket.ttf}Alright, [preferredName], it's been a pleasure chatting with you tonight.{/font}
    
    {font=Kenney Rocket.ttf}However, I now have a very important train to catch.{w=1.0} I'll be contacting you with more info on our deal pretty soon, so be on the lookout!{/font}
    
    {font=Kenney Rocket.ttf}Alright, now back to your regularly scheduled programming.{/font}

    {font=Kenney Rocket.ttf}Anyways, [hacker] out!{/font}
    """
    stop music fadeout 1.0
    scene black with pixellate
    "{i}What was that?{/i}"

label scene3Start:
    # TODO: music 1.1.2
    scene Forest
    show Friend01 neutral at right
    show Friend02 angry at left
    friendB "There you are. [friendA] was about to tell me about the big fight, specifically the part where he somehow {i}lost{/i} the weapon I gave him?"
    friendA """
    Right...
    
    About that...
    """
    menu:
        "Something really weird just happened":
            pass
        "Did anyone else see that?":
            pass
    show Friend01 happy
    show Friend02 happy
    friendA "Oh yeah, did your game crash too?"
    friendB "You had a crash? I didn't even think that was possible anymore."
    menu:
        "Well yeah, but there was...":
            pass
        "No, it was something else...":
            pass
    show Friend01 neutral at right
    show Friend02 angry at left with fade
    friendA "..."
    friendB "..."
    # TODO: music 1.3.1
    show Friend01 neutral
    show Friend02 neutral
    friendA "{i}Seriously?{/i}"
    friendB "Hold on, so you're telling me somebody just showed up and starting talking to you on the [digitalWorld]? And you didn't know who it was or where you were?"
    $ digitalWorld = "N-Scape"
    friendA "That doesn't make any sense. Are you sure you weren't just on some weird night time TV channel? Sometimes I'll fall asleep on the [digitalWorld], and then I wake up with no idea how I got there? It's {i}freaky{/i}."
    $ playerCharacterObjectPronoun = playerCharacterObjectPronoun.lower()
    friendB "Um I doubt [playerCharacterSubjectPronoun]'s had that happen to [playerCharacterObjectPronoun]. Or anyone but you for that matter, like-{w=0.5} what the heck?"
    friendB "Hmm, maybe it was some kind of glitch in [gameWorld]? That would explain the crash, and I've heard there might still be some bugs left behind from before [gameWorld] was ported to [digitalWorld]."
    friendA "Or {i}maybe{/i} [playerCharacterSubjectPronoun] got hacked!"
    friendB "Wow, you really have been watching too much TV. You know the [digitalWorld] runs on the most powerful super computer in the world. It can't be hacked."
    friendB "You said your headset overheated right? Maybe you passed out and it was all some weird dream."
    menu:
        "I think it has something to do with this bracelet.":
            pass
        "The person put this thing on my wrist":
            pass
    friendA "Oh yeah, I forgot about that; after [playerCharacter] killed [startBoss], [playerCharacterSubjectPronoun] picked up that weird item. [friendB], have you ever seen anything like it?"
    show hacker item at truecenter with zoomin
    friendB "No. It looks just like any normal accessory, but it has no name and {w=0.5} wait, that's strange."
    friendB "It's identified as a quest item?"
    friendA "If it's a quest item, then it must be important! You really haven't seen it before [friendB]? I thought you knew everything there is to know about [gameWorld]."
    friendB "Well... not everything. I do have a life you know."
    hide hacker item with zoomout
    friendA "I didn't mean it that way. I just figured... well you know, if there really is some crazy quest that involves whatever the heck just happened to [playerCharacter], you would have heard about it."
    friendB "Yeah, I'm pretty shocked myself."
    # TODO: music 1.1.2
    friendA "Well, I say we go see what this mystery quest is all about! I bet we'll find some rare loot along the way too. {size=-5}maybe even some stuff [friendB] doesn't have{/size}"
    friendB "Are you serious? You can't just charge headfirst into a quest you know nothing about. You're not even level 50 yet."
    friendA "You're right..."
    friendA "That's why you're coming with me!"
    friendB "I would be lying if I said I wasn't a little interested. But just so we're clear, I am not here to babysit you two."
    friendA "Yes!"
    friendA "How about you [playerCharacter]?"
    playerCharacter "..."
    $ renpy.music.set_pause(True)
    $ tmpGlitchText = glitchText(16)
    """
    You feel the [tmpGlitchText] pulling at your arm.
    
    You try to speak, but nothing comes out.
    
    Your hand raises into a thumbs-up position.
    """
    $ renpy.music.set_pause(False)
    play music "audio/Mission Plausible.ogg" # TODO: remove
    $ playerCharacterDepPossesivePronoun = playerCharacterDepPossesivePronoun.lower()
    friendA "Great! It's the perfect team: Me as our fearless leader, [friendB] as our game expert/bodyguard, and [playerCharacter] and [playerCharacterDepPossesivePronoun] weird bracelet thing as our guide through the unknown."
    friendA "Together, we'll be unstoppable!"
    friendB "You know, [friendA], you may be the least qualified {i}fearless leader{/i} I know, but I'm actually pretty excited about this."
    friendA "I'll take that as a compliment"
    friendB "So, when are we starting our grand adventure?"
    friendA "How about same time tomorrow? But no falling asleep this time!"
    friendB "Fine by me."
    menu:
        "Ok.":
            pass
        "I'm not so sure about this.":
            friendA """
            Look, I know you're freaked out about what you saw, but the only way to figure it out is to go on this quest.
            
            {size=-5}also we kinda need you since you've got the quest item and all.{/size}
            """
            "{i}He's right. I need to find out what's going on here{/i}."
    "You nod your head affirmatively, agreeing to come along."
    friendA "Great. In that case, I think I'll be signing off for the night. We've got a big day ahead of us after all"
    friendB "Ok. I'm gonna head out too. See you tomorrow."
    stop music fadeout 1.0
    scene Bedroom with fade
    "This is all so strange."
    "I'd better go to sleep for now"
    scene black with fade
    $ renpy.pause(2.0)

label scene4Start:
    # TODO: music 1.2.1
    scene Hacker Space with fade
    "Am I... dreaming?"
    show GWHacker at right with easeinright
    "{font=Kenney Rocket.ttf}[hacker]{/font}" "{font=Kenney Rocket.ttf}Sort of. Depends on where you draw the line between dream and reality.{/font}"
    "What are you talking about?"
    "{font=Kenney Rocket.ttf}[hacker]{/font}" """
    {font=Kenney Rocket.ttf}Do you want the short answer, or the technical one?{w=1.0} Ah, screw it, I'll give you both. {size=-5}I do love hearing the sound of my own voice after all{/size}{/font}

    {font=Kenney Rocket.ttf}[preferredName], I don't know what they taught you in school about [digitalWorld],{/font}
    
    {font=Kenney Rocket.ttf}But I'm assuming it was some kind of pretentious spiel about \"the world's most powerful super computer\"{/font}
    
    {font=Kenney Rocket.ttf}\"A new era of digital communication\", generously brought to you by [corporation]{/font}

    {font=Kenney Rocket.ttf}Which honestly isn't far off in some aspects{/font}

    {font=Kenney Rocket.ttf}{i}But my god, there is so much more to it than that.{/i}{/font}

    {font=Kenney Rocket.ttf}Don't get me wrong. I love our education system just as much as the next person, but let me tell you a secret.{/font}
    
    {font=Kenney Rocket.ttf}Your 8th grade history teacher has no idea what's actually going on under the hood of [corporation]'s little simulation.{/font}
    
    {font=Kenney Rocket.ttf}In fact, {i}nobody does{/i}.{/font}

    {font=Kenney Rocket.ttf}Hold on, did I say \"nobody\"?{w=0.5} Ha!{w=0.25} {i}They wish.{/i}{/font}

    {font=Kenney Rocket.ttf}You see, what [corporation] doesn't want you to know about their fancy \"super computer\" is that most of its design was actually {i}stolen{/i}.{/font}

    {font=Kenney Rocket.ttf}Don't believe me? Look no further than the first thought you had when I brought you here today.{/font}
    """
    "I thought I was in a dream..."
    "{font=Kenney Rocket.ttf}[hacker]{/font}" """
    {font=Kenney Rocket.ttf}Exactly! Let me explain...{/font}

    {font=Kenney Rocket.ttf}Believe it or not, the suits and ties at [corporation] are pretty clever.{/font}
    
    {font=Kenney Rocket.ttf}You see, their so-called \"super computer\" isn't much of a computer at all.{/font}
    
    {font=Kenney Rocket.ttf}It's actually emulating something much more akin to what goes on in our brains when we fall asleep.{/font}
    
    {font=Kenney Rocket.ttf}A dream, essentially.{/font}
    """
    menu:
        "Are we dreaming right now?":
            pass
        "Is everyone on [digitalWorld] dreaming?":
            pass
    "{font=Kenney Rocket.ttf}[hacker]{/font}" """
    {font=Kenney Rocket.ttf}Well, not exactly. It's more like one person {size=-5}the computer{/size} is having some kind of comatose fever-dream, and everyone else,{/font}
    
    {font=Kenney Rocket.ttf}{size=-5}including you and your weird friends,{/size} gets to show up and whisper in the dreamer's ear.{/font}

    {font=Kenney Rocket.ttf}With enough whispering, you can make an imprint on their subconscious, and then the dream can be whatever you want.{/font}

    {font=Kenney Rocket.ttf}In short, they made a super advanced dream machine. Super cool!{/font}

    {font=Kenney Rocket.ttf}And super {i}creepy{/i}.{/font}

    {font=Kenney Rocket.ttf}I mean, do you have any idea how much raw data is constantly flowing straight from your brain to the [digitalWorld] all the time?{/font}
    """
    "[preferredName]" "..."
    "{font=Kenney Rocket.ttf}[hacker]{/font}" "{font=Kenney Rocket.ttf}Neither do I! Nobody does! But I have a theory that it's a lot.{/font}"
    menu:
        "Why are you telling me all of this":
            "{font=Kenney Rocket.ttf}[hacker]{/font}" "{font=Kenney Rocket.ttf}You know if you'd just hold on a minute, I was getting there.{/font}"
        "How do you know all of this?":
            "{font=Kenney Rocket.ttf}[hacker]{/font}" "{font=Kenney Rocket.ttf}Oh [preferredName], I'm so glad you asked!{/font}"
    "{font=Kenney Rocket.ttf}[hacker]{/font}" """
    {font=Kenney Rocket.ttf}In case you haven't noticed, I'm kind of a genius when it comes to the [digitalWorld], {size=-5}and everything else for that matter{/size}.{/font}
    
    {font=Kenney Rocket.ttf}And believe it or not, me and [corporation] actually go way back.{/font}

    {font=Kenney Rocket.ttf}My relationship with them is...{w=0.5} complicated, to say the least. I hack them...{w=0.5} they catch me...{/font}
    
    {font=Kenney Rocket.ttf}I disappear for a while...{w=0.5} and then I come back and do it again!{/font}

    {font=Kenney Rocket.ttf}And so on.{/font}

    {font=Kenney Rocket.ttf}But things changed when [corporation] launched the [digitalWorld].{/font}
    
    {font=Kenney Rocket.ttf}{i}The New Digital Frontier{/i}, as they like to call it, was supposed to be totally secure. Unhackable! Foolproof!{/font}

    {font=Kenney Rocket.ttf}Can you believe that? {size=-5}So arrogant, even by my standards{/size}.{/font}

    {font=Kenney Rocket.ttf}They're not wrong though. There's no other system like <super computer>,{/font}
    
    {font=Kenney Rocket.ttf}so even if you were somehow able to intercept its data, the actual hardware you'd need to read it doesn't exist.{/font}

    {font=Kenney Rocket.ttf}I'm an exception of course. When it comes to the [digitalWorld], I can see {i}everything{/i}.{/font}
    
    {font=Kenney Rocket.ttf}From the contents of your inventory, to the actual thought data flowing through your headset.{/font}
    """
    menu:
        "How are you able to do that?":
            pass
        "What makes you so special?":
            pass
    "{font=Kenney Rocket.ttf}[hacker]{/font}" """
    {font=Kenney Rocket.ttf}To be honest, I got {i}really{/i} lucky.{w=0.5} Like I said before, the folks at [corporation] are a pretty clever bunch.{/font}

    {font=Kenney Rocket.ttf}So clever in fact, that when they launched the [digitalWorld], they actually created a whole new security system just for me! {size=-5}Flattering, I know.{/size}{/font}

    {font=Kenney Rocket.ttf}For certain {i}personal reasons{/i}, I won't be going into detail on how exactly [corporation] decided to deal with me. {size=-5}Sorry, we are not that close yet{/size}.{/font}

    {font=Kenney Rocket.ttf}But what's more important is that their plan backfired{w=0.5} - Well, not entirely. It's more like a double edged sword.{/font}

    {font=Kenney Rocket.ttf}{i}And my side is sharper{/i}.{/font}

    {font=Kenney Rocket.ttf}You see, what [corporation] hasn't realized yet about their \"expert security plan\" is that,{/font}
    
    {font=Kenney Rocket.ttf}it just so happens to double as an all-exclusive backdoor to the [digitalWorld].{/font}

    {font=Kenney Rocket.ttf}And that's what allows me to do all the cool stuff I do!{/font}

    {font=Kenney Rocket.ttf}{i}And{/i} how I'll get my revenge{/font}
    """
    menu:
        "Revenge?":
            pass
        "What exactly are you planning?":
            "{font=Kenney Rocket.ttf}[hacker]{/font}" """
            {font=Kenney Rocket.ttf}Hehe, piqued your interest have I? Sorry but you'll just have to wait and see.{/font}
            
            {font=Kenney Rocket.ttf}Wouldn't want to ruin the surprise after all.{/font}
        """
    "{font=Kenney Rocket.ttf}[hacker]{/font}" """
    {font=Kenney Rocket.ttf}Let's just say, [corporation] is hiding something about the [digitalWorld].{w=1.0} {i}Something big{/i}.{/font}

    {font=Kenney Rocket.ttf}And I'm gonna be the one to expose it!{/font}

    {font=Kenney Rocket.ttf}But...{w=0.5} I need some help. {size=-5}Lame, I know.{/size} That's where you come in [preferredName]{/font}
    """
    menu:
        "What do you need me for?":
            pass
        "Is this going to be illegal?":
            "{font=Kenney Rocket.ttf}[hacker]{/font}" "{font=Kenney Rocket.ttf}Pfft... no! No... haha... why would you thing that?{w=0.25} I mean, I don't know...{w=0.25} maybe...{w=0.25} {size=-5}it could be.{w=0.25} Do you want it to be?{/size}{/font}"
    "{font=Kenney Rocket.ttf}[hacker]{/font}" """
    {font=Kenney Rocket.ttf}You see [preferredName], before I can make my next big move, I need you to hurry up and finish your quest.{/font}

    {font=Kenney Rocket.ttf}Sorry. I don't mean to sound ungrateful or anything, but there's something really important hiding at the end of that quest I gave you, and I need it ASAP.{/font}
    """
    menu:
        "Why don't you just get it yourself?":
            "{font=Kenney Rocket.ttf}[hacker]{/font}" """
            {font=Kenney Rocket.ttf}In case you haven't noticed, I can't actually enter the [digitalWorld] myself.{/font}

            {font=Kenney Rocket.ttf}If I were to be detected by [corporation], everything I've done up until now would be pointless.{/font}

            {font=Kenney Rocket.ttf}Also, I'm kind of busy with my own adventure right now.{/font}

            {font=Kenney Rocket.ttf}Here, take a look.{/font}
            """
        "What is it?":
            "{font=Kenney Rocket.ttf}[hacker]{/font}" """
            {font=Kenney Rocket.ttf}{size=-5}Hmmm...{w=0.25} how should I explain this{/size}?{/font}

            {font=Kenney Rocket.ttf}It's a key (sort of?) to the heart of the [digitalWorld].{/font}

            {font=Kenney Rocket.ttf}Once I have it, I'll finally be able to expose [corporation]'s secret, and take back what they stole from me.{/font}

            {font=Kenney Rocket.ttf}Exciting stuff, right? Anyways, I didn't just bring you here today just to monologue about me master plan.{/font}

            {font=Kenney Rocket.ttf}I actually wanted to take you on a little field trip...{/font}
            """
    scene City with pixellate
    "{font=Kenney Rocket.ttf}[hacker]{/font}" "{font=Kenney Rocket.ttf}Look familiar?{/font}"
    "[preferredName]" "It looks like the city I live in. Although I don't think I've been to this particular area."
    "{font=Kenney Rocket.ttf}[hacker]{/font}" """
    {font=Kenney Rocket.ttf}This is the energy district. Unless you're into nuclear physics or radiation poisoning, you've probably never been here.{/font}

    {font=Kenney Rocket.ttf}And this guy definitely doesn't fall into either of those categories.{/font}
    """
    show CorpGuy neutral at left with easeinleft # TODO: ATL to get him to fit in the scene
    menu:
        "Who is he?":
            "{font=Kenney Rocket.ttf}[hacker]{/font}" """
            {font=Kenney Rocket.ttf}I'm wondering the same thing.{/font}

            {font=Kenney Rocket.ttf}From what I've gathered, he's definitely connected to [corporation].{/font}

            {font=Kenney Rocket.ttf}But that alone doesn't explain the data coming from his headset.{/font}

            {font=Kenney Rocket.ttf}There's something off about it. It's unlike any I've seen before.{/font}
            """
        "Why are you here?":
            "{font=Kenney Rocket.ttf}[hacker]{/font}" """
            {font=Kenney Rocket.ttf}Oh, I'm not actually {i}here{/i} [preferredName]. I'm just borrowing the local cameras.{/font}
            
            {font=Kenney Rocket.ttf}But to answer your question, I'm here to keep an eye on our sophisticated friend here.{/font}

            {font=Kenney Rocket.ttf}From what I've gathered, this particular individual is without a doubt part of [corporation]. And from the looks of his fancy getup, I'd say he's a pretty important one at that.{/font}
            """
    "{font=Kenney Rocket.ttf}[hacker]{/font}" """
    {font=Kenney Rocket.ttf}But that alone doesn't explain the data coming from his headset. There's something seriously off about it.{/font}

    {font=Kenney Rocket.ttf}You see, I've been tracking him for a couple days now, but whenever I try and see what's going on inside his head, I get all this weird junk data.{/font}

    {font=Kenney Rocket.ttf}It's like there's some kind of noise machine in his headset, drowning out all the real stuff with a bunch of nonsense.{/font}

    {font=Kenney Rocket.ttf}I can't get any kind of read on what he's thinking, or doing in [digitalWorld]. It's unlike anything I've ever seen before, and honestly, it kind of freaks me out.{/font}

    {font=Kenney Rocket.ttf}Anyways, I've got a sneaking suspicion this guy may know something about what I'm looking for, so I'm gonna follow him until I find it.{/font}
    """
    # TODO: animate (?) corpguy
    hide CorpGuy
    "The man heads inside a large office building."
    "{font=Kenney Rocket.ttf}[hacker]{/font}" """
    {font=Kenney Rocket.ttf}!{/font}

    {font=Kenney Rocket.ttf}Did you see that [preferredName]? The building he just went in must be one of [corporation]'s secret labs! Oh my god, this could be it!{/font}

    {font=Kenney Rocket.ttf}Hmm... I've gotta figure out how to get inside there, and fast. Their security cams are definitely well protected so that's a no-go.{/font}

    {font=Kenney Rocket.ttf}Shoot! If I don't figure out something soon, I'm gonna miss my chance! Sorry [preferredName], but I've gotta run. This is just too important to miss.{/font}

    {font=Kenney Rocket.ttf}[hacker] out!{/font}
    """
    stop music fadeout 1.0
    scene Bedroom with pixellate
    """
    {i}What the heck is she planning?{/i}
    
    {i}It's almost time to meet up with [friendA] and [friendB]. We're starting [hacker]'s quest today...{/i}
    """

label scene5Start:
    # TODO:  music 2.5.1
    scene Forest Snow with fade
    show Friend01 happy at right
    show Friend02 happy at left
    friendB "Hey [playerCharacter], today's the day."
    friendA "Oh man, I'm so pumped! Aren't you excited."
    menu:
        "Yeah.":
            friendA "Awesome. So what do we have to do first?"
        "Not really.":
            show Friend01 neutral
            friendB "I don't really blame you. I mean, what {i}are{/i} we doing anyways?"
    "{i}The <hacker item> is pointing toward the forest region{/i}."
    "{font=Kenney Rocket.ttf}[gameLog]{/font}" "{font=Kenney Rocket.ttf}Current Objective: Inside <forest>.{/font}"
    show Friend01 neutral
    $ treePos = generateTreePos()
    friendB """
    Huh? How is that supposed to be a challenge?
    
    I didn't think there was much to see over there.
    """
    friendA "Well then, what are we waiting for? Let's go!"
    scene Forest Snow with fade
    show Boss02 neutral:
        alpha 0.0
    show snowTree1:
        zoom treePos[0][0]
        pos (treePos[0][1][0], treePos[0][1][1])
    show snowTree2:
        zoom treePos[1][0]
        pos (treePos[1][1][0], treePos[1][1][1])
    show snowTree3:
        zoom treePos[2][0]
        pos (treePos[2][1][0], treePos[2][1][1])
    show Friend01 neutral at right:
        zoom 0.75
    show Friend02 neutral at left:
        zoom 0.75
    $ treePos = generateTreePos()
    friendA "Alright. We're in the forest. Now what?"
    "{font=Kenney Rocket.ttf}[gameLog]{/font}" "{font=Kenney Rocket.ttf}Current Objective: Inside <forest>.{/font}"
    friendA "Ok... let's just start looking around I guess."
    friendB "Wait, hold on. Do you see that?"
    friendA """
    ...

    No?
    """
    friendB "Over there."
    show Boss02 neutral:
        zoom 0.7
        align (0.5, 0.5)
        ypos 0.25
        linear 0.25 alpha 1.0
    "{i}There appears to be a large monster standing deeper in the woods{/i}."
    friendA "What is that thing? It's huge."
    friendB "If it's what I think it is, then this is really bad news."
    friendA "Why? Can't we just kill it and move on?"
    friendB """
    That right there is a [iceBoss], one of the most powerful enemies in the game.
    
    Fighting it head on would be suicide.
    """
    friendA "We have to get past it somehow, don't we? What should we do?"
    friendB "The only thing I can think of is trying to sneak past it, but even that's pretty risky."
    friendA "Well, if that's our only option, I say we go for it."
    friendB "If you say so.{w=1.0} Ok{w=0.5}, follow my lead."
    "You slowly follow [friendB] deeper into the forest. No one makes a sound."
    friendB "{size=-5}Ok, were close to the [iceBoss] now.{/size}"
    friendA "{size=-5}Hey, [friendB].{/size}"
    friendB "{size=-5}Shhh.{/size}"
    friendA "{size=-5}I just wanted to ask you-{/size}{size=-1}Wa-{/size} {size=-2}woah{/size} {size=2}-Ahh!{/size}"
    # TODO: twig snap SFX
    "[friendA] slips and falls."
    show Boss02 possessed
    iceBoss "?"
    stop music fadeout 0.5
    friendB "{size=-5}You've got to be kidding me.{/size}"
    hide Boss02
    show Boss02 possessed:
        zoom 0.7
        align (0.5, 0.5)
        ypos 0.25
        linear 0.5 zoom 1 ypos 0.5
    "{i}The [iceBoss] is heading right towards us. This is not good.{/i}"
    # I hate myself for doing this, but it's kind of funny
    iceBoss "rawr uwu" # TODO: replace with roar SFX
    friendB "New plan. Everybody run!"
    scene Forest Snow with fade
    show snowTree1:
        zoom treePos[0][0]
        pos (treePos[0][1][0], treePos[0][1][1])
    show snowTree2:
        zoom treePos[1][0]
        pos (treePos[1][1][0], treePos[1][1][1])
    show snowTree3:
        zoom treePos[2][0]
        pos (treePos[2][1][0], treePos[2][1][1])
    $ treePos = generateTreePos()
    """
    {i}I think I'm safe here, but now I'm totally lost.{/i}

    {i}I need to find [friendA] and [friendB]{/i}
    """
    show snowTree1:
        zoom treePos[0][0]
        pos (treePos[0][1][0], treePos[0][1][1])
    show snowTree2:
        zoom treePos[1][0]
        pos (treePos[1][1][0], treePos[1][1][1])
    show snowTree3:
        zoom treePos[2][0]
        pos (treePos[2][1][0], treePos[2][1][1])
    $ treePos = generateTreePos()
    """
    {i}...{/i}
    
    {i}Am I going the right way?{/i}
    """
    show snowTree1:
        zoom treePos[0][0]
        pos (treePos[0][1][0], treePos[0][1][1])
    show snowTree2:
        zoom treePos[1][0]
        pos (treePos[1][1][0], treePos[1][1][1])
    show snowTree3:
        zoom treePos[2][0]
        pos (treePos[2][1][0], treePos[2][1][1])
    $ treePos = generateTreePos()
    "{i}This forest feels endless{/i}."
    show snowTree1:
        zoom treePos[0][0]
        pos (treePos[0][1][0], treePos[0][1][1])
    show snowTree2:
        zoom treePos[1][0]
        pos (treePos[1][1][0], treePos[1][1][1])
    show snowTree3:
        zoom treePos[2][0]
        pos (treePos[2][1][0], treePos[2][1][1])
    $ treePos = generateTreePos()
    "{i}Have I been this way before?{/i}"
    show snowTree1:
        zoom treePos[0][0]
        pos (treePos[0][1][0], treePos[0][1][1])
    show snowTree2:
        zoom treePos[1][0]
        pos (treePos[1][1][0], treePos[1][1][1])
    show snowTree3:
        zoom treePos[2][0]
        pos (treePos[2][1][0], treePos[2][1][1])
    $ treePos = generateTreePos()
    "{i}I think I'm going in circles{/i}."
    "{font=Kenney Rocket.ttf}[hacker]{/font}" "{font=Kenney Rocket.ttf}I think I'm going in circles.{/font}"
    # TODO: music 1.2.1
    show Hallway:
        alpha 0.0
        zoom 0.5
        linear 15.0 alpha 0.1
    "{i}?{/i}"
    "{font=Kenney Rocket.ttf}[hacker]{/font}" """
    {font=Kenney Rocket.ttf}You know, when I imagined finding this place in my head, it was a lot cooler.{/font}

    {font=Kenney Rocket.ttf}I mean, who would hae thought I'd be infiltrating the world;s most top secret facility using a sanitation bot?{/font}

    {font=Kenney Rocket.ttf}Whatever. Desperate times call for desperate measures, I guess.{/font}
    """
    show snowTree1:
        zoom treePos[0][0]
        pos (treePos[0][1][0], treePos[0][1][1])
    show snowTree2:
        zoom treePos[1][0]
        pos (treePos[1][1][0], treePos[1][1][1])
    show snowTree3:
        zoom treePos[2][0]
        pos (treePos[2][1][0], treePos[2][1][1])
    $ treePos = generateTreePos()
    "{i}Where am I?{/i}"
    "{font=Kenney Rocket.ttf}[hacker]{/font}" "{font=Kenney Rocket.ttf}Come on...{w=0.5} Where is it?{/font}"
    show Hallway:
        linear 10 alpha 0.6
    show snowTree1:
        zoom treePos[0][0]
        pos (treePos[0][1][0], treePos[0][1][1])
    show snowTree2:
        zoom treePos[1][0]
        pos (treePos[1][1][0], treePos[1][1][1])
    show snowTree3:
        zoom treePos[2][0]
        pos (treePos[2][1][0], treePos[2][1][1])
    $ treePos = generateTreePos()
    "{font=Kenney Rocket.ttf}[hacker]{/font}" "{font=Kenney Rocket.ttf}I've got to hurry before somebody sees me.{/font}"
    "[preferredName]" "I'm so freaking lost."
    "{font=Kenney Rocket.ttf}[hacker]{/font}" "{font=Kenney Rocket.ttf}I'm so freaking lost.{/font}"
    show Hallway:
        linear 2.5 alpha 1.0
    "{font=Kenney Rocket.ttf}[hacker]{/font}" "{font=Kenney Rocket.ttf}How big can this place be? I must be close. I have to be.{/font}"
    show Hallway:
        alpha 1.0
        align (0.525, 0.51)
        easeout_quad 10.0 zoom 2.5
    "{font=Kenney Rocket.ttf}[hacker]{/font}" "{font=Kenney Rocket.ttf}Yes! This is it! After so many years. Finally...{/font}"
    "Before [hacker] reaches the door, it begins to open from the other side."
    # TODO: maybe play the solid snake alert sound?
    "{font=Kenney Rocket.ttf}[hacker]{/font}" """
    {font=Kenney Rocket.ttf}{b}!{/b}{/font}
    
    {font=Kenney Rocket.ttf}Not good.{/font}
    """
    stop music
    hide Hallway
    hide Boss02
    hide snowTree1
    hide snowTree2
    hide snowTree3
    scene Forest Snow
    show snowTree1:
        zoom treePos[0][0]
        pos (treePos[0][1][0], treePos[0][1][1])
    show snowTree2:
        zoom treePos[1][0]
        pos (treePos[1][1][0], treePos[1][1][1])
    show snowTree3:
        zoom treePos[2][0]
        pos (treePos[2][1][0], treePos[2][1][1])
    $ del(treePos)
    show Boss02 possessed
    "{i}!{/i}"
    iceBoss "rawr xD" # TODO: replace with roar SFX
    # pause for roar
    show HP at top with easeintop:
        size (1280, 90)
    show redBar at top:
        size (0, 90)
        linear 1.0 size (1280, 90)
    "{i}Not good!{/i}"
    # TODO: music 1.1.1
    menu:
        "Fight":
            pass
        "Run Away":
            "{i}I'm completely cornered. It looks like I have no choice but to fight{/i}."
    menu:
        "Attack 1":
            pass
        "Attack 2":
            pass
    show redBar:
        linear 0.25 size (1280 * 95 / 100, 90)
    "[iceBoss] attacks."
    menu:
        "Attack 1":
            pass
        "Attack 2":
            pass
    show redBar:
        linear 0.25 size (1280 * 90 / 100, 90)
    "[iceBoss] attacks."
    """
    {i}This is really bad. I won't survive another attack like that{/i}.

    {i}I guess this is it{/i}...
    """
    show hacker item # TODO: positioning and anim (glowing loop?)
    iceBoss "..."
    playerCharacter "?"
    "The [iceBoss] looks at you with a blank stare, and then wanders off into the forest." # ATL the boss out
    image hpComb = Composite((1280, 90), (0, 0), im.Scale("boss_hp.png", 1280, 90), ((1280 - (1280 * 90 / 100)) / 2, 0), im.Scale("boss_hp_bar.png", 1280 * 90 / 100, 90))
    show hpComb at top
    hide redBar
    hide HP
    hide hpComb with easeouttop
    hide Boss02 with zoomout
    hide hacker item
    """
    {i}What just happened?{/i}
    
    {i}I'd better get out of here and go find the others{/i}.
    """
    if config.developer:
        "END SCENE 5"

label scene5HalfStart:
    # TODO: music 1.1.2
    scene Forest
    show Friend01 neutral at right
    show Friend02 angry at left
    show campfire:
        alpha 0.0
    show darkOverlay:
        alpha 0.0
    friendA "[playerCharacter]! You made it!"
    friendB "We got split up after the [iceBoss] found us. You didn't find anything, did you?"
    playerCharacter "No."
    friendA """
    Ugh, what kind of quest doesn't even give you a real objective?
    
    I mean, what the heck are we supposed to be looking for in that empty forest?

    Whatever, I guess we'd better set up camp for now. We can look some more later.
    """
    show darkOverlay with fade:
        alpha 1.0
    show campfire:
        align (0.52, 0.95)
        alpha 0.0
        linear 0.1 alpha 1.0
    friendB "Um, I don't know about you, but I am {i}not{/i} going back in there with that [iceBoss] prowling around. Especially not after what you just pulled."
    friendA "Look, I said I was sorry alright? How was I supposed to know there was ice there?"
    friendB """
    {i}Maybe{/i} if you'd just pay more attention...{w=0.5} Ugh never mind.
    
    Anyways, it's super easy to get lost in there too. It wouldn't be smart to go back without a map at least.
    """
    friendA "That's true. Actually, is it just me, or does the forest seem way bigger from the inside than it does from here?"
    menu:
        "Yeah, it is kind of weird":
            pass
        "I don't think so.":
            pass
    friendA "Well, if we're not going back in, what should we do next?"
    friendB "Maybe we could..."
    show screen tear()
    $ renpy.pause(0.4)
    hide screen tear

label scene6Start:
    # TODO: music 1.2.1
    scene Hacker Space with pixellate
    show GWHacker at center:
        alpha 0.0
        linear 0.5 alpha 1.0
    "{font=Kenney Rocket.ttf}[hacker]{/font}" """
    {font=Kenney Rocket.ttf}Now {i}that{/i} was a close call.{/font}
    
    {font=Kenney Rocket.ttf}You're welcome by the way.{/font}
    """
    menu:
        "For what?":
            "{font=Kenney Rocket.ttf}[hacker]{/font}" """
            {font=Kenney Rocket.ttf}For saving you just new, duh. {size=-5}You should probably be used to it by now, if we're being honest.{/size}{/font}

            {font=Kenney Rocket.ttf}Whatever. You can thank me later. Right now, I have a question.{/font}
            """
        "What was that door?":
            "{font=Kenney Rocket.ttf}[hacker]{/font}" """
            {font=Kenney Rocket.ttf}Door? You{w=0.5} saw that?{w=0.5}{size=-5}Weird. I guess things are working out quicker than I thought.{/size}{/font}

            {font=Kenney Rocket.ttf}That was part of [corporation]'s lab.{/font}

            {font=Kenney Rocket.ttf}You know, the one I showed you earlier.{/font}

            {font=Kenney Rocket.ttf}Sorry for leaving you on a cliffhanger there. I just got a little overexcited.{/font}

            {font=Kenney Rocket.ttf}For good reason, though!{/font}

            {font=Kenney Rocket.ttf}I found something, but before I tell you, I have a question.{/font}
            """
    "{font=Kenney Rocket.ttf}[hacker]{/font}" """
    {font=Kenney Rocket.ttf}[preferredName], be honest{/font}
    
    {font=Kenney Rocket.ttf}What do {i}you{/i} think about hte whole [digitalWorld]?{/font}
    """
    $ tmpFlag = False
    menu:
        "I like it.":
            "{font=Kenney Rocket.ttf}[hacker]{/font}" """
            {font=Kenney Rocket.ttf}You know, if I wasn't in my current position, I think I might really love this place.{/font}

            {font=Kenney Rocket.ttf}I mean, a whole world where you can see your friends all the time, and have the same freedom as a dream?{/font}

            {font=Kenney Rocket.ttf}Sounds pretty nice to me.{/font}
            """
        "I hate it.":
            "{font=Kenney Rocket.ttf}[hacker]{/font}" """
            {font=Kenney Rocket.ttf}I get that, there's so much about the [digitalWorld] that even I don't know.{/font}

            {font=Kenney Rocket.ttf}I mean, imagine if somebody else could do what I can. They'd be able to get away with whatever they want.{/font}
            """
        "Why do you ask?":
            $ tmpFlag = True
            "{font=Kenney Rocket.ttf}[hacker]{/font}" """
            {font=Kenney Rocket.ttf}Just curious.{/font}

            {font=Kenney Rocket.ttf}I don't really get out of the house much, so I wonder how normal people like you must feel about it.{/font}

            {font=Kenney Rocket.ttf}You know, if I wasn't in my current position, I think I'd really love this place.{/font}

            {font=Kenney Rocket.ttf}A whole world where you can see your friends all the time, adn have the same amount of freedom as a dream?{/font}

            {font=Kenney Rocket.ttf}Doesn't sound so bad to me.{/font}

            {font=Kenney Rocket.ttf}But at the same time, it's kind of scary, isn't it?{/font}

            {font=Kenney Rocket.ttf}I mean, there's so much about the [digitalWorld] that even I still don't know.{/font}

            {font=Kenney Rocket.ttf}Imagine if somebody else was able to do what I can.{/font}

            {font=Kenney Rocket.ttf}They could get away with whatever they want.{/font}

            {font=Kenney Rocket.ttf}Sorry [preferredName], you don't have to answer the question if you don't want to.{/font}
            """
    if tmpFlag:
        menu:
            "I love the [digitalWorld].":
                pass
            "I hate the [digitalWorld].":
                pass
            "I'd prefer not to say.":
                pass
        "{font=Kenney Rocket.ttf}[hacker]{/font}" "{font=Kenney Rocket.ttf}I can understand that. One way or another, I hope we find some answers at the end of this.{/font}"
    "{font=Kenney Rocket.ttf}[hacker]{/font}" """
    {font=Kenney Rocket.ttf}Anyways [preferredName], I've {i}finally{/i} found what I'm looking for. Which means we're almost at the end of our little quest.{/font}

    {font=Kenney Rocket.ttf}I have to warn you, from here on out, what we're doing is {i}not{/i} a game.{/font}
    """
    "[preferredName]" "..."
    "{font=Kenney Rocket.ttf}[hacker]{/font}" """
    {font=Kenney Rocket.ttf}I'm serious, what [corporation]'s been doing in that lab is...{/font}

    {font=Kenney Rocket.ttf}It's just really not cool! Alright?{/font}

    {font=Kenney Rocket.ttf}Look, all I need now is for you to finish your quest in [gameWorld]. OK?{/font}

    {font=Kenney Rocket.ttf}{size=-5}Then maybe, just maybe, I'll be able to fix this.{/size}{/font}
    """
    menu:
        "What is [corporation] doing exactly?":
            "{font=Kenney Rocket.ttf}[hacker]{/font}" """
            {font=Kenney Rocket.ttf}I-{/font}

            {font=Kenney Rocket.ttf}They-{/font}

            {font=Kenney Rocket.ttf}...{/font}

            {font=Kenney Rocket.ttf}*Sigh*{/font}

            {font=Kenney Rocket.ttf}Listen [preferredName]. I know I have some explaining to do. I just...{/font}

            {font=Kenney Rocket.ttf}I need you to trust me right now, OK?{/font}

            {font=Kenney Rocket.ttf}It'll all make sense once you finish the quest. I promise.{/font}
            """
            menu:
                "OK, what do I have to do?":
                    jump scene6PurpleCont
                "No. Tell me what's going on {i}{b}now{/b}{/i}":
                    "{font=Kenney Rocket.ttf}[hacker]{/font}" """
                    {font=Kenney Rocket.ttf}I-{w=0.5} I...{w=0.5} Listen, I don't have time for this!{/font}
                    
                    {font=Kenney Rocket.ttf}Are you gonna help me or not?{/font}
                    """
            menu:
                "I guess.":
                    jump scene6PurpleCont
                "No way!":
                    "{font=Kenney Rocket.ttf}[hacker]{/font}" """
                    {font=Kenney Rocket.ttf}Ugh, {i}fine{/i}. Sorry [preferredName], I tried playing nice, but this might be my only change.{/font}

                    {font=Kenney Rocket.ttf}And I am {i}not{/i} going to miss it!{/font}
                    """
                    if config.developer:
                        "END SCENE 6"
                    jump scene7Orange
        "OK.":
            jump scene6PurpleCont

label scene6PurpleCont:
    "{font=Kenney Rocket.ttf}[hacker]{/font}" """
    {font=Kenney Rocket.ttf}Great! All you have to do is go back into the forest, and you should find what you're looking for pretty fast.{/font}
    
    {font=Kenney Rocket.ttf}Oh, and this time, don't bring any of your pesky friends with you! {size=-5}Sorry, but this last part is single-player only.{/size}{/font}

    {font=Kenney Rocket.ttf}Alright? You'd better hurry. Good luck [preferredName]!{/font}

    {font=Kenney Rocket.ttf}I'll be waiting for you on the other side.{/font}
    """
    if config.developer:
        "END SCENE 6"

label scene7Purple:
    scene Forest
    show Friend01 neutral at right
    show Friend02 angry at left
    show campfire:
        alpha 0.0
    show darkOverlay:
        alpha 0.0
    show darkOverlay:
        alpha 1.0
    show campfire:
        align (0.52, 0.95)
        alpha 0.0
        linear 0.1 alpha 1.0
    friendA "Hey [playerCharacter], are you even listening?"
    friendB "Looks like [playerCharacterSubjectPronoun] zoned out pretty hard there."
    friendA """
    We've got to figure out what to do next.
    
    All we found in that dumb forest was a freaking [iceBoss].
    """
    "{font=Kenney Rocket.ttf}[gameLog]{/font}" "{font=Kenney Rocket.ttf}Current Objective: Inside <forest>.{/font}"
    "{i}Right. I've got to go back{/i}."
    playerCharacter "I'm gonna go get some more firewood."
    friendA "OK."
    friendB "Don't go too far. The [iceBoss] could still be around."
    $ treePos = generateTreePos()
    scene Forest Snow with fade
    show snowTree1:
        zoom treePos[0][0]
        pos (treePos[0][1][0], treePos[0][1][1])
    show snowTree2:
        zoom treePos[1][0]
        pos (treePos[1][1][0], treePos[1][1][1])
    show snowTree3:
        zoom treePos[2][0]
        pos (treePos[2][1][0], treePos[2][1][1])
    $ treePos = generateTreePos()
    "{font=Kenney Rocket.ttf}[gameLog]{/font}" "{font=Kenney Rocket.ttf}Current Objective: Inside <forest>.{/font}"
    show snowTree1:
        zoom treePos[0][0]
        pos (treePos[0][1][0], treePos[0][1][1])
    show snowTree2:
        zoom treePos[1][0]
        pos (treePos[1][1][0], treePos[1][1][1])
    show snowTree3:
        zoom treePos[2][0]
        pos (treePos[2][1][0], treePos[2][1][1])
    $ treePos = generateTreePos()
    "{i}This place makes no sense{/i}."
    show snowTree1:
        zoom treePos[0][0]
        pos (treePos[0][1][0], treePos[0][1][1])
    show snowTree2:
        zoom treePos[1][0]
        pos (treePos[1][1][0], treePos[1][1][1])
    show snowTree3:
        zoom treePos[2][0]
        pos (treePos[2][1][0], treePos[2][1][1])
    $ treePos = generateTreePos()
    "{i}What am I even looking for?{/i}"
    show hacker item at truecenter
    "{i}The <hacker item> is pulling at my arm...{/i}"
    show snowTree1:
        zoom treePos[0][0]
        pos (treePos[0][1][0], treePos[0][1][1])
    show snowTree2:
        zoom treePos[1][0]
        pos (treePos[1][1][0], treePos[1][1][1])
    show snowTree3:
        zoom treePos[2][0]
        pos (treePos[2][1][0], treePos[2][1][1])
    $ treePos = generateTreePos()
    "{i}I guess I should follow it{/i}."
    show snowTree1:
        zoom treePos[0][0]
        pos (treePos[0][1][0], treePos[0][1][1])
    show snowTree2:
        zoom treePos[1][0]
        pos (treePos[1][1][0], treePos[1][1][1])
    show snowTree3:
        zoom treePos[2][0]
        pos (treePos[2][1][0], treePos[2][1][1])
    $ treePos = generateTreePos()
    """
    {i}I've been walking for a long time now{/i}.
    
    {i}This forest feels never-ending{/i}.
    """
    # TODO: add more trees and then manually pos them to make a path
    "{i}Is that...?{/i}"
    $ tmpGlitchText = glitchText(128)
    "{font=Kenney Rocket.ttf}[gameLog]{/font}" "{font=Kenney Rocket.ttf}Current Objective:{w=1.0} [tmpGlitchText]{/font}"
    $ tmpFlag = False
    if config.developer:
        "END SCENE 7"
    jump scene8Start

label scene7Orange:
    scene Forest
    show Friend01 neutral at right
    show Friend02 angry at left
    show campfire:
        alpha 0.0
    show darkOverlay:
        alpha 0.0
    show darkOverlay:
        alpha 1.0
    show campfire:
        align (0.52, 0.95)
        alpha 0.0
        linear 0.1 alpha 1.0
    friendA """
    So what should we do now?

    All we found in the forest was a freaking [iceBoss]
    """
    friendA """
    ?

    What the...
    """
    show Friend01 angry
    $ tmpGlitchText = glitchText(32, False, True)
    friendA "[tmpGlitchText]"
    $ tmpGlitchText = glitchText(64, True, True)
    friendA "[tmpGlitchText]"
    $ tmpGlitchText = glitchText(128, True, True)
    friendA "{b}{vert}[tmpGlitchText]{/vert}{/b}"
    friendB "What's going on?"
    python:
        if random.randint(0,2) == 0:
            tmpGlitchText = glitchText(32, False, True)
            tmpGlitchText1 = glitchText(32, True, True)
        else:
            tmpGlitchText = glitchText(32, True, True)
            tmpGlitchText1 = glitchText(32, False, True)
    menu:
        "[tmpGlitchText]":
            pass
        "[tmpGlitchText1]":
            pass
    $ tmpFlag = True
    if config.developer:
        "END SCENE 7"

label scene8Start:
    scene black with fade
    "{i}Where am I?{/i}"
    "{i}I can't feel my body{/i}"
    # TODO: music 1.2.1
    "{font=Kenney Rocket.ttf}[hacker]{/font}" """
    {font=Kenney Rocket.ttf}This is it [player]. Before we continue{w=1.0}, I have to apologize. I haven't been 100 percent honest with you.{/font}

    {font=Kenney Rocket.ttf}You may already know by now, but the truth is, <forest> was never supposed to be part of the game.{/font}
    
    {font=Kenney Rocket.ttf}In fact, it’s barely part of the [digitalWorld] at all.{/font}

    {font=Kenney Rocket.ttf}It's part of {i}me{/i}.{/font}
    """
    playerCharacter "?"
    "{font=Kenney Rocket.ttf}[hacker]{/font}" "{font=Kenney Rocket.ttf}And now that you've found it, I fear we're both in terrible danger.{/font}"
    playerCharacter "???"
    $ tmpChosen = "Look"
    menu:
        "What kind of danger?":
            pass
        "What do you mean the <forest> is {i}part of you?{/i}":
            pass
        "What happened to the [digitalWorld]? To my friends?" if tmpFlag:
            "{font=Kenney Rocket.ttf}[hacker]{/font}" """
            {font=Kenney Rocket.ttf}Sorry, when you refused to finish the quest, I got desperate.{/font}

            {font=Kenney Rocket.ttf}But don't worry! Your friends will be fine.{w=1.0} {size=-5}Probably.{/size}{/font}
            """
            $ tmpChosen = "Anyways"
    "{font=Kenney Rocket.ttf}[hacker]{/font}" """
    {font=Kenney Rocket.ttf}[tmpChosen], I don't have much time, but I promise everything will make sense soon.{/font}
    
    {font=Kenney Rocket.ttf}Thanks to you finishing my quest, I'm finally able to complete our connection.{/font}

    {font=Kenney Rocket.ttf}Which means right now, I {i}need{/i} your help. [preferredName], I have to know...{/font}

    {font=Kenney Rocket.ttf}{i}Do you trust me?{/i}{/font}
    """
    menu:
        "Yes":
            "[hacker] lets out a sigh of relief."
            "{font=Kenney Rocket.ttf}[hacker]{/font}" """
            {font=Kenney Rocket.ttf}Alright. This next part is gonna feel weird.{/font}

            {font=Kenney Rocket.ttf}Just promise to stay calm, alright?{/font}
            """
        "No":
            "[hacker] lets out a disappointed sigh."
            "{font=Kenney Rocket.ttf}[hacker]{/font}" """
            {font=Kenney Rocket.ttf}I'm sorry [preferredName], but there's no other way...{/font}

            {font=Kenney Rocket.ttf}{i}I have to do this{/i}.{/font}
            """
    show screen tear()
    $ renpy.pause(1.0)
    show screen tear(30)
    $ renpy.pause(2.0)
    show screen tear(40, 0.5)
    $ renpy.pause(2.0)
    show screen tear(50, 0.25)
    $ renpy.pause(0.5)
    scene black with pulse(12, "#777", 0.5, 1, 0.1, 0.1, 0.25, 1.0)
    hide screen tear
    if config.developer:
        "{cps=0}END SCENE 8{/cps}"

label scene9Start:
    # TODO: music 1.3.1
    scene Bedroom with None
    """
    {i}I'm...{w=0.5} home?{/i}

    Without thinking, you stand up.

    {i}Something's not right{/i}.

    {i}{font=Kenney Rocket.ttf}I have to go now.{/font}{/i}

    {i}But why?{/i}

    You walk toward the door.

    As you reach for the handle, you notice the <hacker item> on your wrist.

    {i}Is this real?{/i}
    """
    "You leave your room and step outside"
    scene City with fade
    """
    You begin walking down the street.

    {i}I've never been this way before, but it feels oddly familiar{/i}.

    {i}{font=Kenney Rocket.ttf}It must be this way.{/font}{/i}

    {i}What is?{/i}

    You move as if you've walked this route a thousand times.

    {i}{font=Kenney Rocket.ttf}I have to hurry.{/font}{/i}
    """
    # TODO: transition to corporation building scene
    "{i}Here?{/i}"
    # TODO: zoom into building
    scene Hallway with fade
    "{i}Won't somebody see me?{/i}"
    "{font=Kenney Rocket.ttf}[hacker]{/font}" "{font=Kenney Rocket.ttf}They only see what I want them to see.{/font}"
    # TODO: zoom
    "{i}Are you{w=0.5}... in my head?{/i}"
    "{font=Kenney Rocket.ttf}[hacker]{/font}" "{font=Kenney Rocket.ttf}Always have been.{/font}"
    # TODO: zoom again
    """
    {i}{font=Kenney Rocket.ttf}Almost there...{/font}{/i}

    {i}{font=Kenney Rocket.ttf}I can't believe it. This actually might work!{/font}{/i}

    As you open the door, you feel a growing sense of excitement. You cannot tell if it's your own.
    """
    stop music fadeout 1.0
    if config.developer:
        "{cps=0}END SCENE 9{/cps}"

label scene10Start:
    # TODO: music 3.11.1
    scene Prison
    """
    You appear to be in some kind of server room.

    {i}What is this place?{/i}

    Without hesitation, you walk purposefully through the maze of consoles.

    {i}This is it.{/i}

    Before you lies a massive control panel. You begin adjusting various devices...

    As you continue to work on the panel, you notice a faint sound...

    {i}The machine is... breathing{/i}.

    {i}Almost there{/i}...

    {i}Just this{/i}...

    {i}And this{/i}...

    {i}And - There!{/i}

    You press one more button and step away from the center console.
    """
    scene Prison Alert
    $ renpy.pause(5.0)
    scene black
    show Prison Open
    # TODO: show image of hacker behind door wedges
    $ distMult = 0.5
    show doorWedge1:
        pos (0.36, 0.282)
        ease_quint 5.0 pos (0.36, 0.282 + (0.39 - 0.282) * distMult)
    show doorWedge2:
        pos (0.371, 0.1725)
        ease_quint 5.0 pos (0.371 - (0.371 - 0.31) * distMult, 0.1725 + (0.2325 - 0.1725) * distMult)
    show doorWedge3:
        pos (0.4345, 0.156)
        ease_quint 5.0 pos (0.4345 - (0.4345 - 0.36) * distMult, 0.156)
    show doorWedge4:
        pos (0.4805, 0.1755)
        ease_quint 5.0 pos (0.4805 - (0.4805 - 0.425) * distMult, 0.1755 - (0.1755 - 0.1) * distMult)
    show doorWedge5:
        pos (0.4825, 0.2875)
        ease_quint 5.0 pos (0.4825, 0.2875 - (0.2875 - 0.1725) * distMult)
    show doorWedge6:
        pos (0.483, 0.369)
        ease_quint 5.0 pos (0.483 + (0.538 - 0.483) * distMult, 0.369 - (0.369 - 0.2935) * distMult)
    show doorWedge7:
        pos (0.432, 0.3665)
        ease_quint 5.0 pos (0.432 + (0.504 - 0.432) * distMult, 0.3665)
    show doorWedge8:
        pos (0.3685, 0.3675)
        ease_quint 5.0 pos (0.3685 + (0.424 - 0.3685) * distMult, 0.3675 + (0.435 - 0.3675) * distMult)
    $ renpy.pause(1.0)
    "Unknown Male Voice" "Hey! Stop right there!"
    stop music
    # TODO: gunshot sfx
    # TDDO: hide hacker filter if I add one
    if noFlashing:
        "The man shoots you"
    show black with pulse(1, "#fff", 0.0, 1.0, 0.0, 0.1, 0.5, 2.0)
    hide black
    """
    You wake up on the floor in front of the center console.

    {i}My head hurts{/i}...

    Lying on the floor next to you is your headset. There is a large hole in it.

    {i}Was I just...{w=0.5} shot?{/i}

    Standing across the room is a man. He looks familiar.

    He's aiming a gun right at you.
    """
    "Man" "Your 'game' ends here."
    "Unknown Female Voice" "No!"
    # TODO: explosion sfx
    # TODO: music 1.2.1
    """
    Before the man is able to fire another shot, the console nearest him explodes, knocking him to the ground.

    His gun skitters out of reach into the daarkness.

    {i}That voice{/i}...
    """
    "Man" "Ughhh..."
    "The man appears to be unconscious."
    $ distMult = 1.0
    show doorWedge1:
        ease_quint 5.0 pos (0.36, 0.282 + (0.39 - 0.282) * distMult)
    show doorWedge2:
        ease_quint 5.0 pos (0.371 - (0.371 - 0.31) * distMult, 0.1725 + (0.2325 - 0.1725) * distMult)
    show doorWedge3:
        ease_quint 5.0 pos (0.4345 - (0.4345 - 0.36) * distMult, 0.156)
    show doorWedge4:
        ease_quint 5.0 pos (0.4805 - (0.4805 - 0.425) * distMult, 0.1755 - (0.1755 - 0.1) * distMult)
    show doorWedge5:
        ease_quint 5.0 pos (0.4825, 0.2875 - (0.2875 - 0.1725) * distMult)
    show doorWedge6:
        ease_quint 5.0 pos (0.483 + (0.538 - 0.483) * distMult, 0.369 - (0.369 - 0.2935) * distMult)
    show doorWedge7:
        ease_quint 5.0 pos (0.432 + (0.504 - 0.432) * distMult, 0.3665)
    show doorWedge8:
        ease_quint 5.0 pos (0.3685 + (0.424 - 0.3685) * distMult, 0.3675 + (0.435 - 0.3675) * 1.0)
    $ renpy.pause(3.5)
    "{i}Is that...?{/i}"
    "Strange girl" "Hey [player]."
    menu:
        "What's going on here?":
            pass
        "Who are you?":
            hacker "It's me, [hacker]."
    hacker "This here is the truth behind [digitalWorld]."
    "{i}Her voice is strange, but it's undeniably [hacker]'s{/i}."
    hacker """
    I'm sorry for lying to you [player].
    
    As it turns out, we've actually had the 'world's strongest super computer' with us all along.

    Only in the mind can there exist truly endless possibilities.

    For years, researchers at [corporation] tried to replicate that power, creating countless super computers, AI after AI, even quantum processing.

    But in the end, no machine could ever do what the brain so effortlessly can:

    Dream.

    Thus, [corporation] had failed, and their research was canned.

    At least that's what should have happened.

    Because while the power of the human brain can't be replicated, it can be harnessed,{w=0.5} rewired,{w=0.5} {i}abused{/i}.

    Do you get it now [player]? All these fancy computers around us? They're not the [digitalWorld].

    {i}I am{/i}.
    """
    "Guy" "How - *cough* - How did you?"
    hacker """
    Try as you might, some parts of the mind just can't be altered.

    Like just now [player], even though I had taken control of your body, your thoughts were still all your own.

    I kept my consciousness hidden for a long time, and working under the radar, I was able to hide a key in the [digitalWorld].

    Something that, if found, could still connect a player to that hidden, unaltered part of myself, or the <hacker item>, as you know it, [player].
    """
    menu:
        "What happened to you?":
            pass # TODO: comment in script maybe (?)
        "Why is [corporation] doing this?":
            hacker "This is...{w=1.0} my punishment."
    hacker """
    A long time ago, right before the [digitalWorld] first launched, I was caught by [corporation].

    I messed up so bad in fact, that [corporation] actually managed to find a capture me.

    They wanted to kill me then and there. Which, looking back, may have been a better fate than what actually happened.

    You see, [corporation] know they had to get rid of me, but they also happened to need a human host for their newly-created [digitalWorld].

    And what better candidate than someone who already has no traceable identity?

    This, [corporation] was able to hit two birds with one stone:

    By imprisoning me as the [digitalWorld]'s host, [corporation] was able to both get away with the crime this is the [digitalWorld], {i}and{/i} eliminate the only person with any shot at exposing it.
    """
    "Guy" "We did what we had to. The [digitalWorld] was the greatest scientific breakthrough of the 21st century!"
    hacker "At what cost?! Is it worth trading in lives?!"
    "Guy" """
    {i}You{/i} are a world-class criminal! You're lucky to be alive at all.

    Besides, society needs the [digitalWorld].
    """
    python:
        if playerSubjectPronoun == "they":
            tmpChosen = "do"
        else:
            tmpChosen = "does"
    hacker "You don't get to decide that anymore, {i}[playerSubjectPronoun] [tmpChosen]{/i}."
    player "?"
    hacker "I can't control you anymore [player], it's up to you to save or destroy [digitalWorld]."
    """
    {i}It's up to me now{/i}...

    {i}What [corporation] is doing to [hacker] is evil{/i}.

    {i}But, what will happen to the world without the [digitalWorld]?{/i}

    {i}What should I do?{/i}
    """
    $ tmpFlag = True
    $ tmpFlag1 = True

label talkChoice:
    menu:
        "Talk to [corporation] official" if tmpFlag:
            $ tmpFlag = False
            "[corporation] Official" """
            Please, if you shut down the [digitalWorld], years of scientific progress will be lost. The world could fall into chaos!

            Think of all the people you've met through the [digitalWorld].

            Without it, you wouldn't be able to see them anymore.

            I don't know what she's told you, but this woman is a criminal. It's her own fault she's here!

            And you can't trust her.
            """
            if tmpFlag:
                """
                {i}Without the [digitalWorld], I'll never see [friendA] and [friendB] again{/i}...

                {i}But what's being done to [hacker] is terrible{/i}...
                """
            jump talkChoice
        "Talk to [hacker]" if tmpFlag1:
            $ tmpFlag1 = False
            hacker """
            Look [player], I'm not going to sit here and act like I'm perfect.

            If I was, I probably wouldn't be here.

            But can you really let [corporation] get away with this?

            I mean, if they're willing to use such cruel and unusual measures to achieve their goals, who knows what else they may be capable of?

            I need you help, [player]. Please...
            """
            if tmpFlag:
                """
                {i}What they're doing to [hacker] is terrible{/i}...
            
                {i}But without the [digitalWorld], I'll never see [friendA] and [friendB] again{/i}...
                """
            jump talkChoice
        "I think I've made up my mind...":
            menu:
                "Set [hacker] free":
                    pass # TODO: play end 1
                "Leave [hacker] here":
                    pass # TODO: play end 2
    if config.developer:
        "{cps=0}END SCENE 10{/cps}"
label kill:
    if config.developer:
        "{cps=0}GAME DIE{/cps}"
    stop music fadeout 1.0
    # TODO: music 3.12.1. peaceful ambient ending music
    call credits from _call_credits
    scene whitedrop with fade
    show Rice Bowl:
        xalign 0.5
        ypos 1.3
        rotate 180
        parallel:
            easeout 3.0 ypos -0.7
        parallel:
            linear 3.0 rotate 660
    $ renpy.pause(4.0)
    scene black with fade
    $ renpy.quit()