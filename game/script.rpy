﻿# The script of the game goes in this file.

# Player vars
define player = Character("[playerName]")
default playerSubjectPronoun = "they"
default playerObjectPronoun = "them"
default playerDepPossesivePronoun = "their"
default playerIndepPossesivePronoun = "theirs"

# Player character vars
define playerCharacter = Character("[playerUsername]")
default playerCharacterSubjectPronoun = "they"
default playerCharacterObjectPronoun = "them"
default playerCharacterDepPossesivePronoun = "their"
default playerCharacterIndepPossesivePronoun = "theirs"

# Characters
define friendA = Character("Brogan", image="Friend01")
define friendB = Character("Cynthia", image="Friend02")
define startBoss = Character("Ignis the Conqueror", image="Boss01")
define iceBoss = Character("Ice Crab", image="Boss02")
define gameLog = Character("GameLog")
define hacker = Character("[hackerName]")

# BG IMG
image Game Tavern = "bg_GW_GameTavern.png"
image Game World Arena 01 = "bg_GW_GameWorldArena01.png"
image Game World Arena 02 = "bg_GW_GameWorldArena02.png"
image Generic Game Env = "bg_GW_GenericGameEnvironment.png"
image Hacker Space = "bg_GW_HackerSpace.png"
image Bedroom = "bg_RW_Bedroom.png"
image City = "bg_RW_City.png"
image Prison = "bg_RW_Prison.png"
image Hallway = "bg_RW_Hallway.png"
image crash = "bg_GW_crash.png"
image logInScreen = "bg_GW_login.png"

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
image CorpGuy neutral = "ch_RW_CorpGuy_neutral.png"
image CorpGuy angry = "ch_RW_CorpGuy_angry.png"

# Item IMG
image hacker item = im.Scale("item_hackerItem.png", 360, 360)

# Other IMG
image HP 0 = im.Scale("boss_hp_0.png", 360, 90)
image HP 25 = im.Scale("boss_hp_25.png", 360, 90)
image HP 50 = im.Scale("boss_hp_50.png", 360, 90)
image HP 75 = im.Scale("boss_hp_75.png", 360, 90)
image HP 100 = im.Scale("boss_hp_100.png", 360, 90)

# Non game vars
image credit = Text(creditText, text_align=0.5)
image Rice Bowl = Composite((525, 314), (121, 0), "rice_bowl_studios_PLACEHOLDER.png")


# Other vars
define noFlashing = True
define playerUsername = ""
define playerPassword = ""

# The game starts here.

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
    $ renpy.pause(4)
    scene black with fade
    return

label main_menu:
    return

label start:
    play music "audio/Space Cadet.ogg"
    if config.developer:
        "{cps=0}GAME START{/cps}"
    menu: 
        "{cps=0}This game has flashing and strobing, which can cause seizures. Would you like to disable them?{/cps}"
        "Yes":
            $ noFlashing = True
        "No":
            $ noFlashing = False
    python:
        while playerUsername == "":
            playerUsername = renpy.input("{font=Kenney Rocket.ttf}Username:{/font}")
            playerUsername = playerUsername.strip()
        while playerPassword == "":
            playerPassword = renpy.input("{font=Kenney Rocket.ttf}Password:{/font}")
            playerPassword = playerPassword.strip()
        if len(playerPassword) > 16:
            playerPassword = playerPassword[0:16]
    gameLog "{font=Kenney Rocket.ttf}Launching <game world>{w=0.5}.{w=0.5}.{w=0.5}.{/font}{w=0.5}{nw}"
    gameLog "{font=Kenney Rocket.ttf}We did not find a character with that login info.{/font}"
    gameLog "{font=Kenney Rocket.ttf}Launching character creation{w=0.5}.{w=0.5}.{w=0.5}.{/font}{w=0.5}{nw}"
    menu:
        "{cps=0}{font=Kenney Rocket.ttf}What are your character's pronouns?{/font}{/cps}"
        "{font=Kenney Rocket.ttf}He/Him/His{/font}":
            python:
                playerCharacterSubjectPronoun = "he"
                playerCharacterObjectPronoun = "him"
                playerCharacterDepPossesivePronoun = "his"
                playerCharacterIndepPossesivePronoun = "his"
        "{font=Kenney Rocket.ttf}She/Her/Hers{/font}":
            python:
                playerCharacterSubjectPronoun = "she"
                playerCharacterObjectPronoun = "her"
                playerCharacterDepPossesivePronoun = "her"
                playerCharacterIndepPossesivePronoun = "hers"
        "{font=Kenney Rocket.ttf}They/Them/Their{/font}":
            python:
                playerCharacterSubjectPronoun = "they"
                playerCharacterObjectPronoun = "them"
                playerCharacterDepPossesivePronoun = "their"
                playerCharacterIndepPossesivePronoun = "theirs"
        "{font=Kenney Rocket.ttf}Other{/font}":
            python:
                playerCharacterSubjectPronoun = renpy.input("{font=Kenney Rocket.ttf}Subject Pronoun (ex. he, she, they):{/font}")
                playerCharacterSubjectPronoun = playerCharacterSubjectPronoun.strip()
                if not playerCharacterSubjectPronoun:
                    playerCharacterSubjectPronoun = "they"
                playerCharacterObjectPronoun = renpy.input("{font=Kenney Rocket.ttf}Object Pronoun (ex. him, her, them):{/font}")
                playerCharacterObjectPronoun = playerCharacterObjectPronoun.strip()
                if not playerCharacterObjectPronoun:
                    playerCharacterObjectPronoun = "them"
                playerCharacterDepPossesivePronoun = renpy.input("{font=Kenney Rocket.ttf}Dependent Possessive Pronoun (ex. his, her, their):{/font}")
                playerCharacterDepPossesivePronoun = playerCharacterDepPossesivePronoun.strip()
                if not playerCharacterDepPossesivePronoun:
                    playerCharacterDepPossesivePronoun = "their"
                playerCharacterIndepPossesivePronoun = renpy.input("{font=Kenney Rocket.ttf}Independent Possessive Pronoun (ex. his, hers, theirs):{/font}")
                playerCharacterIndepPossesivePronoun = playerCharacterIndepPossesivePronoun.strip()
                if not playerIndepPossesivePronoun:
                    playerCharacterIndepPossesivePronoun = "theirs"
    python:
        playerName = ""
        while playerName == "":
            playerName = renpy.input("{font=Kenney Rocket.ttf}Real Name:{/font}")
            playerName = playerName.strip()
    menu:
        "{cps=0}{font=Kenney Rocket.ttf}What are your pronouns?{/font}{/cps}"
        "{font=Kenney Rocket.ttf}He/Him/His{/font}":
            python:
                playerSubjectPronoun = "he"
                playerObjectPronoun = "him"
                playerDepPossesivePronoun = "his"
                playerIndepPossesivePronoun = "his"
        "{font=Kenney Rocket.ttf}She/Her/Hers{/font}":
            python:
                playerSubjectPronoun = "she"
                playerObjectPronoun = "her"
                playerDepPossesivePronoun = "her"
                playerIndepPossesivePronoun = "hers"
        "{font=Kenney Rocket.ttf}They/Them/Their{/font}":
            python:
                playerSubjectPronoun = "they"
                playerObjectPronoun = "them"
                playerDepPossesivePronoun = "their"
                playerIndepPossesivePronoun = "theirs"
        "{font=Kenney Rocket.ttf}Other{/font}":
            python:
                playerSubjectPronoun = renpy.input("{font=Kenney Rocket.ttf}Subject Pronoun (ex. he, she, they):{/font}")
                playerSubjectPronoun = playerSubjectPronoun.strip().capitalize()
                if not playerSubjectPronoun:
                    playerSubjectPronoun = "they"
                playerObjectPronoun = renpy.input("{font=Kenney Rocket.ttf}Object Pronoun (ex. him, her, them):{/font}")
                playerObjectPronoun = playerObjectPronoun.strip().capitalize()
                if not playerObjectPronoun:
                    playerObjectPronoun = "them"
                playerDepPossesivePronoun = renpy.input("{font=Kenney Rocket.ttf}Dependent Possessive Pronoun (ex. his, her, their):{/font}")
                playerDepPossesivePronoun = playerDepPossesivePronoun.strip().capitalize()
                if not playerDepPossesivePronoun:
                    playerDepPossesivePronoun = "their"
                playerIndepPossesivePronoun = renpy.input("{font=Kenney Rocket.ttf}Independent Possessive Pronoun (ex. his, hers, theirs):{/font}")
                playerIndepPossesivePronoun = playerIndepPossesivePronoun.strip().capitalize()
                if not playerIndepPossesivePronoun:
                    playerIndepPossesivePronoun = "theirs"
    jump startRealWorld
        
label startBossFight:
    $ suppress_overlay = False
    scene Game World Arena 01
    show Boss01 neutral at right
    show Friend01 angry at left:
        xzoom -1.0
    show HP 100 at top with easeintop
    $ playerCharacterSubjectPronoun = playerCharacterSubjectPronoun.lower()
    friendA "Ugh! Why's this taking so long? Where the heck is [playerCharacterSubjectPronoun]?"
    startBoss "HAHAHAHA THERE IS NO HOPE FOR YOU PUNY MORTAL!"
    play sound "audio/mirror_shattering.wav"
    show Boss01 neutral with vpunch
    friendA "Damn, my weapon's almost broken! I can't stay here much longer."
    gameLog "{font=Kenney Rocket.ttf}[playerCharacter] has entered the area.{/font}"
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
    show HP 75
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
    friendA "I don't know if we can win this, [playerCharacter]"
    $ tmpFlag = False

label startBossAttackChoice:
    menu:
        "Attack":
            play sound "audio/swordMetal6.ogg"
            show Boss01 neutral:
                ease 0.1 zoom 0.9 xoffset 100
            $ renpy.pause(0.1)
            show Boss01 neutral:
                ease 0.1 zoom 1.0 xoffset 0
            gameLog "{font=Kenney Rocket.ttf}Critical Hit!{/font}"
            show HP 50
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
            show Boss01 neutral:
                ease 0.1 zoom 1.0 xoffset 0
            gameLog "{font=Kenney Rocket.ttf}Critical Hit!{/font}"
            show HP 25
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
            gameLog "{font=Kenney Rocket.ttf}Critical Hit!{/font}"
            show HP 0
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
    hide HP 0 with easeouttop
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
    gameLog "{font=Kenney Rocket.ttf}[tmpGlitchText] was added to your inventory{/font}"
    friendA "That's all you got? God, [friendB]'s gonna get a kick outta this one."
    friendA "Hey wait. What's up with it's name? I can't read it on my screen. Can you?"
    playerCharacter "No"
    friendA "Huh, weird. Well, maybe [friendB] knows something about it-"
    play sound "audio/computer_error_alert.wav"
    scene crash with vpunch
    $ renpy.pause(1.5)

label startRealWorld:
    scene Bedroom with None
    player """
    <game title> seems to have crashed
    
    My headset is burning hot
    
    What {i}was{/i} that weird bracelet item
    """
    play sound "<to 2.5>audio/phone_ringing.wav"
    $ renpy.pause(2)
    player "It's [friendB]"
    friendB "Hey [player] where are you two? I thought you and [friendA] were gonna come over after you took down [startBoss]"
    menu:
        "About that…":
            friendB "Ha! You seriously fell asleep? Here I was thinking [friendA] was the stupid one."
        "I'll be there in a few minutes.":
            friendB "Alright. Are you still with [friendA]?"
    friendB "Oh, here he is now. I’ll see you in a bit. Bye."
    player "I'd better try logging back in."
    "You put your headset back on."
    #scene black with None
    if config.developer:
        "The password is [playerPassword]"
    show text "Password\n" + playerPassword at truecenter
    python:
        tmpPassword = renpy.input("Username: [playerUsername]\nPassword:")
        tmpPassword = tmpPassword.strip()
    while tmpPassword != playerPassword:
        play sound "audio/error2.ogg"
        gameLog "Incorrect Login."
        python:
            tmpPassword = renpy.input("Username: [playerUsername]\nPassword:")
            tmpPassword = tmpPassword.strip()
    player """
    ...

    My headset is getting hot again.
    """
    "You try to remove your headset."
    stop music
    play music "audio/Mission Plausible.ogg"
    player """
    I can't lift my arm.
    
    My head feels like it's on fire.
    
    It feels like something's grabbing my wrist.
    
    I can't get the headset off with my arm stuck like this.
    
    The heat is getting unbearable...
    """
    scene black with pulse(12, "#f00", 0.7, 1.2, 0.1, 0.1, 0.25, 2.0)

label startHackerSpace:
    scene Hacker Space with fade
    "Where am I?"
    show GWHacker at center with easeinbottom
    $ hackerName = "{b}redacted{/b}"
    hacker "Good question. From what I can see, I'm pretty sure you're in a bedroom."
    $ tmpChosen = -1
    menu:
        "Who are you?":
            $ tmpChosen = 0
            hacker "That's kind of complicated. Could we start with the easy questions please?"
        "Did you just read my mind?":
            $ tmpChosen = 1
            hacker """
            Oh, if only it were that simple! What do I look like? Some kind of fortune teller?
            
            Let's just say I made an extremely educated guess
            """
        "How did you know that?":
            $ tmpChosen = 2
            hacker """
            Um... I'm actually a psychic.
            
            No, a genie!
            
            Or maybe I'm your conscience! Hehe, spooky, right?
            """
    menu:
        "Who are you?" if tmpChosen != 0:
            pass
        "Did you just read my mind?" if tmpChosen != 1:
            pass
        "How did you know that?" if tmpChosen != 2:
            pass
    hacker "Okay, I think that's enough questioning for today."
    "You try to speak, but nothing comes out. It feels as though you are underwater."
    hacker """
    Right, now where was I? Let's see, plant the <hacker item>, dramatic entrance, obligatory exposition...
    
    Ah of course
    
    {i}*ahem*{/i}
    """
    if playerName != playerUsername:
        hacker "Welcome to my world, [playerCharacter]! Or should I say [player]."
        hacker "Which would you prefer?"
        $ tmpFlag = True
    else:
        hacker "Welcome to my world, [player]."
        python:
            preferredName = playerName
            preferredSubjectPronoun = playerSubjectPronoun
            preferredObjectPronoun = playerObjectPronoun
            preferredDepPossesivePronoun = playerDepPossesivePronoun
            preferredIndepPossesivePronoun = playerIndepPossesivePronoun
        jump afterHackerSpaceNameChoice

label hackerSpaceNameChoice:
    menu:
        "Call me [playerCharacter]":
            python:
                preferredName = playerUsername
                preferredSubjectPronoun = playerCharacterSubjectPronoun
                preferredObjectPronoun = playerCharacterObjectPronoun
                preferredDepPossesivePronoun = playerCharacterDepPossesivePronoun
                preferredIndepPossesivePronoun = playerCharacterIndepPossesivePronoun
        "Call me [player]":
            python:
                preferredName = playerName
                preferredSubjectPronoun = playerSubjectPronoun
                preferredObjectPronoun = playerObjectPronoun
                preferredDepPossesivePronoun = playerDepPossesivePronoun
                preferredIndepPossesivePronoun = playerIndepPossesivePronoun
        "How do you know my name?" if tmpFlag:
            $ tmpFlag = False
            play sound "audio/error2.ogg"
            hacker "Hey, what did I say about asking questions?"
            jump hackerSpaceNameChoice
    
label afterHackerSpaceNameChoice:
    if playerName != playerUsername:
        hacker "Ya know, I'm so glad you're here [preferredName]. I was really starting to think {i}nobody{/i} would show up to my little party."
    else:
        hacker "Ya know, I'm so glad you're here. I was really starting to think {i}nobody{/i} would show up to my little party."
    hacker "But then, right when I was about to call it off, you came along and found my invitation!"
    show hacker item at truecenter with zoomin
    "The mysterious figure gestures toward the <HackerItem>, which is now fastened to your wrist"
    "How did that get there?"
    hide hacker item with zoomout
    hacker """
    And guess what. The best part is{w=3.0}: it's yours to keep! Consider it a party favor from your new best friend.
    
    Oh, that reminds me,{w=1.0} I haven't introduced myself yet! {size=-5}Gosh, what kind of friend doesn't even know their friend's name?{/size} Sorry, it's been a while since I've actually talked to someone for real like this.
    
    Hmmm...{w=0.5} where do I begin?{w=1.0} I've gone by a LOT of names in the past, <name1>{w=0.5}, <name2>{w=0.5}, <name3>{w=1.0}, {size=-5}<embarrassing name>{w=0.5}... I don't know what I was thinking with that one{/size}...
    
    Anything ring a bell? You've probably heard of me before, right? I mean - I'm {i}kind of{/i} a big deal.
    """
    "..."
    hacker """
    ...
    
    ?
    
    Nothing?{w=1.0} Seriously? {size=-5}Wow, have I really fallen off that hard?{/size}
    """
    $ hackerName = "Medusa"
    hacker """
    Well, whatever, since we're friends you can call me [hacker]
    
    So.. I'm sure you're probably wondering why I invited you here today. Well you see, I actually noticed you and your friends are pretty into that game.
    
    What was it called again?{w=2.0} You know, the one you've been playing {i}literally{/i} non-stop. {size=-5}Like seriously don't you have a job or something?{/size}
    
    Anyways, I've got a game of my own going on{w=0.5} -so to speak-, and it's {i}really{/i} important. But you see, the thing is, I kind of need some help getting to the end of it.
    
    And you know...
    
    I just thought...
    
    {i}Since we are friends,{/i}
    
    You could lend me a hand!
    """
    menu:
        "ok...?":
            pass
        "Hell no!":
            pass
    hacker """
    Awesome! I knew I could count on you [preferredName]!{w=1.0} I mean, what are friends for, right?
    
    And don't worry! I promise that when we beat my little game, there's gonna be a special reward just for you.{w=1.0} Oh! And I can even help you with your game too!
    
    Alright, [preferredName], it's been a pleasure chatting with you tonight. However, I now have a very important train to catch.{w=1.0} I'll be contacting you with more info on our deal pretty soon, so be on the lookout!
    
    Alright, now back to your regularly scheduled programming.

    Anyways, [hacker] out!
    """
    scene black with pixellate
    "{i}What was that?{/i}"

label scene3:
    scene Game World Arena 01 with fade
    show Friend01 neutral at right with easeinright
    show Friend02 angry at left with easeinleft
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
    show Friend01 neutral
    show Friend02 neutral
    friendA "{i}Seriously?{/i}"
    friendB "Hold on, so you're telling me somebody just showed up and starting talking to you on the <digital world>? And you didn't know who it was or where you were?"
    friendA "That doesn't make any sense. Are you sure you weren't just on some weird night time TV channel? Sometimes I'll fall asleep on the <digital world>, and then I wake up with no idea how I got there? It's {i}freaky{/i}."
    friendB "Um I doubt [playerCharacterSubjectPronoun]'s had that happen to [playerCharacterObjectPronoun]. Or anyone but you for that matter, like-{w=0.5} what the heck?"
    friendB "Hmm, maybe it was some kind of glitch in <game name>? That would explain the crash, and I've heard there might still be some bugs left behind from before <game name> was ported to <digital world>."
    friendA "Or {i}maybe{/i} [playerCharacterSubjectPronoun] got hacked!"
    friendB "Wow, you really have been watching too much TV. You know the <digital world> runs on the most powerful supercomputer in the world. It can't be hacked."
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
    friendA "If it's a quest item, then it must be important! You really haven't seen it before [friendB]? I thought you knew everything there is to know about <game>."
    friendB "Well... not everything. I do have a life you know."
    hide hacker item with zoomout
    friendA "I didn't mean it that way. I just figured... well you know, if there really is some crazy quest that involves whatever the heck just happened to [playerCharacter], you would have heard about it."
    friendB "Yeah, I'm pretty shocked myself."
    friendA "Well, I say we go see what this mystery quest is all about! I bet we'll find some rare loot along the way too. {size=-5}maybe even some stuff [friendB] doesn't have{/size}"
    friendB "Are you serious? You can't just charge headfirst into a quest you know nothing about. You're not even level 50 yet."
    friendA "You're right..."
    friendA "That's why you're coming with me!"
    friendB "I would be lying if I said I wasn't a little interested. But just so we're clear, I am not here to babysit you two."
    friendA "Yes!"
    friendA "How about you [playerCharacter]?"
    stop music
    "..."
    "You feel the <hacker item> pulling at your arm."
    "You try to speak, but nothing comes out."
    "Your hand raises into a thumbs-up position."
    play music "audio/Mission Plausible.ogg"
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
            friendA "Look, I know you're freaked out about what you saw, but the only way to figure it out is to go on this quest."
            friendA "{size=-5}also we kinda need you since you've got the quest item and all.{/size}"
    "You nod your head affirmatively, agreeing to come along."
    friendA "Great. In that case, I think I'll be signing off for the night. We've got a big day ahead of us after all"
    friendB "Ok. I'm gonna head out too. See you tomorrow."
    hide Friend01
    hide Friend02
    scene Bedroom
    "This is all so strange."
    "I'd better go to sleep for now"
    scene black with fade
    $ renpy.pause(2.0)

label scene4Start:
    scene Hacker Space with fade
    "Am I... dreaming?"
    show GWHacker at right with easeinright
    hacker "Sort of. Depends on where you draw the line between dream and reality."
    "What are you talking about?"
    hacker """
    Do you want the short answer, or the technical one?{w=1.0} Ah, screw it, I'll give you both. {size=-5}I do love hearing the sound of my own voice after all{/size}

    [preferredName], I don't know what they taught you in school about <digital world>,
    
    but I'm assuming it was some kind of pretentious spiel about \"the world's most powerful supercomputer\" and \"a new era of digital communication\", generously brought to you by <corporation>

    Which honestly isn't far off in some aspects

    {i}But my god, there is so much more to it than that.{/i}

    Don't get me wrong. I love our education system just as much as the next person, but let me tell you a secret. Your 8th grade history teacher has no idea what's actually going on under the hood of <corporation>'s little simulation. In fact, {i}nobody does{/i}.

    Hold on, did I say \"nobody\"?{w=0.5} Ha!{w=0.25} {i}They wish.{/i}

    You see, what <corporation> doesn't want you to know about their fancy \"supercomputer\" is that most of its design was actually {i}stolen{/i}.

    Don't believe me? Look no further than the first thought you had when I brought you here today.
    """
    "I thought I was in a dream..."
    hacker """
    Exactly! Let me explain...

    Believe it or not, the suits and ties at <corporation> are pretty clever. You see, their so-called \"supercomputer\" isn't much of a computer at all. It's actually emulating something much more akin to what goes on in our brains when we fall asleep.
    
    A dream, essentially.
    """
    menu:
        "Are we dreaming right now?":
            pass
        "Is everyone on <digital world> dreaming?":
            pass
    hacker """
    Well, not exactly. It's more like one person {size=-5}the computer{/size} is having some kind of comatose fever-dream, and everyone else{size=-5}, including you and your weird friends,{/size} gets to show up and whisper in the dreamer's ear.

    With enough whispering, you can make an imprint on their subconscious, and then the dream can be whatever you want.

    In short, they made a super advanced dream machine. Super cool!

    And super {i}creepy{/i}.

    I mean, do you have any idea how much raw data is constantly flowing straight from you brain to the <digital world> all the time?
    """
    "..."
    hacker "Neither do I! Nobody does! But I have a theory that it's a lot."
    menu:
        "Why are you telling me all of this":
            hacker "You know if you'd just hold on a minute, I was getting there."
        "How do you know all of this?":
            hacker "Oh [preferredName], I'm so glad you asked!"
    hacker """
    In case you haven't noticed, I'm kind of a genius when it comes to the <digital world>, {size=-5}and everything else for that matter{/size}. And believe it or not, me and <corporation> actually go way back.

    My relationship with them is...{w=0.5} complicated, to say the lease. I hack them...{w=0.5} they catch me...{w=0.5} I disappear for a while...{w=0.5} and then I come back and do it again!

    And so on.

    But things changed when <corporation> launched the <digital world>. {i}The New Digital Frontier{/i}, as they like to call it, was supposed to be totally secure. Unhackable! Foolproof!

    Can you believe that? {size=-5}So arrogant, even by my standards{/size}.

    They're not wrong though. There's no other system like <super computer>, so even if you were somehow able to intercept its data, the actual hardware you'd need to read it doesn't exist.

    I'm an exception of course. When it comes to the <digital world>, I can see {i}everything{/i}. From the contents of your inventory, to the actual thought data flowing through your headset.
    """
    menu:
        "How are you able to do that?":
            pass
        "What makes you so special?":
            pass
    hacker """
    To be honest, I got {i}really{/i} lucky.{w=0.5} Like I said before, the folks at <corporation> are a pretty clever bunch.

    So clever in fact, that when they launched the <digital world>, they actually created a whole new security system just for me! {size=-5}Flattering, I know.{/size}

    For certain {i}personal reasons{/i}, I won't be going into detail on how exactly <corporation> decided to deal with me. {size=-5}Sorry, we are not that close yet{/size}.

    But what's more important is that their plan backfired{w=0.5} - Well, not entirely. It's more like a double edged sword.

    {i}And my side is sharper{/i}.

    You see, what <corporation> hasn't realized yet about their \"expert security plan\" is that it just so happens to double as an all-exclusive backdoor to the <digital world>.

    And that's what allows me to do all the cool stuff I do!

    {i}And{/i} how I'll get my revenge
    """
    menu:
        "Revenge?":
            pass
        "What exactly are you planning?":
            hacker """
            Hehe piqued your interest have I? Sorry but you'll just have to wait and see.
            
            Wouldn't want to ruin the surprise after all.
        """
    hacker """
    Let's just say, <corporation> is hiding something about the <digital world>.{w=1.0} {i}Something big{/i}.

    And I'm gonna be the one to expose it!

    But...{w=0.5} I need some help. {size=-5}Lame, I know.{/size} That's where you come in [preferredName]
    """
    menu:
        "What do you need me for?":
            pass
        "Is this going to be illegal?":
            hacker "Pfft... no! No... haha... why would you thing that?{w=0.25} I mean, I don't know...{w=0.25} maybe...{w=0.25} {size=-5}it could be.{w=0.25} Do you want it to be?{/size}"
    hacker """
    You see [preferredName], before I can make my next big move, I need you to hurry up and finish your quest.

    Sorry. I don't mean to sound ungrateful or anything, but there's something really important hiding at the end of that quest I gave you, and I need it ASAP.
    """
    menu:
        "Why don't you just get it yourself?":
            hacker """
            In case you haven't noticed, I can't actually enter the <digital world> myself.

            If I were to be detected by <corporation>, everything I've done up until now would be pointless.

            Also, I'm kind of busy with my own adventure right now.

            Here, take a look.
            """
        "What is it?":
            hacker """
            {size=-5}Hmmm...{w=0.25} how should I explain this{/size}?

            It's a key (sort of?) to the heart of the <digital world>.

            Once I have it, I'll finally be able to expose <corporation>'s secret, and take back what they stole from me.

            Exciting stuff, right? Anyways, I didn't just bring you here today just to monologue about me master plan.

            I actually wanted to take you on a little field trip...
            """
    scene City with pixellate
    hacker "Look familiar?"
    "It looks like the city I live in. Although I don't thing I've been to this particular area."
    hacker """
    This is the energy district. Unless you're into nuclear physics or radiation poisoning, you've probably never been here.

    And this guy definitely doesn't fall into either of those categories.
    """
    show CorpGuy neutral at left with easeinleft
    menu:
        "Who is he?":
            hacker """
            I'm wondering the same thing.

            From what I've gathered, he's definitely connected to <corporation>.

            But that alone doesn't explain the data coming from his headset.

            There's something off about it. It's unlike any I've seen before.
            """
        "Why are you here?":
            hacker """
            Oh, I'm not actually {i}here{/i} [preferredName]. I'm just borrowing the local cameras.
            
            But to answer your question, I'm here to keep an eye on our sophisticated friend here.

            From what I've gathered, this particular individual is without a doubt part of <corporation>. And from the looks of his fancy getup, I'd say he's a pretty important one at that.
            """
    hacker """
    But that alone doesn't explain the data coming from his headset. There's something seriously off about it.

    You see, I've been tracking him for a couple days now, but whenever I try and see what's going on inside his head, I get all this weird junk data.

    It's like there's some kind of noise machine in his headset, drowning out all the real stuff with a bunch of nonsense.

    I can't get any kind of read on what he's thinking, or doing in <digital world>. It's unlike anything I've ever seen before, and honestly, it kind of freaks me out.

    Anyways, I've got a sneaking suspicion this guy may know something about what I'm looking for, so I'm gonna follow him until I find it.
    """
    "The man heads inside a large office building."
    hacker """
    !

    Did you see that [preferredName]? The building he just went in must be one of <corporation>'s secret labs! Oh my god, this could be it!

    Hmm... I've gotta figure out how to get inside there, and fast. Their security cams are definitely well protected so that's a no-go.

    Shoot! If I don't figure out something soon, I'm gonna miss my chance! Sorry [preferredName], but I've gotta run. This is just too important to miss.

    [hacker] out!
    """
    scene Bedroom with fade
    """
    {i}What the heck is she planning?{/i}
    
    {i}It's almost time to meet up with [friendA] and [friendB]. We're starting [hacker]'s quest today...{/i}
    """

# TODO: visuals
label scene5Start:
    scene black with None
    friendB "Hey [playerCharacter], today's the day."
    friendA "Oh man, I'm so pumped! Aren't you excited."
    menu:
        "Yeah.":
            friendA "Awesome. So what do we have to do first?"
        "Not really.":
            friendB "I don't really blame you. I mean, what {i}are{/i} we doing anyways?"
    "{i}The <hacker item> is pointing toward the forest region{/i}."
    gameLog "{font=Kenney Rocket.ttf}Current Objective: Inside <forest>.{/font}"
    friendB """
    Huh? How is that supposed to be a challenge?
    
    I didn't think there was much to see over there.
    """
    friendA "Well then, what are we waiting for? Let's go!"
    # TODO change to winter scene
    friendA "Alright. We're in the forest. Now what?"
    gameLog "{font=Kenney Rocket.ttf}Current Objective: Inside <forest>.{/font}"
    friendA "Ok... let's just start looking around I guess."
    friendB "Wait, hold on. Do you see that?"
    friendA """
    ...

    No?
    """
    friendB "Over there."
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
    friendA "{size=-5}I just wanted to ask you-{/size}{size=-1}Wa-{/size} {size=-2.5}woah{/size} {size=2}-Ahh!{/size}"
    "[friendA] slips and falls."
    iceBoss "?"
    friendB "{size=-5}You've got to be kidding me.{/size}"
    "{i}The [iceBoss] is heading right towards us. This is not good.{/i}"
    # I hate myself for doing this, but it's kind of funny
    iceBoss "rawr uwu" # TODO: make this a sound instead
    friendB "New plan. Everybody run!"
    # TODO animation / scene change
    """
    {i}I think I'm safe here, but now I'm totally lost.{/i}

    {i}I need to find [friendA] and [friendB]{/i}
    """
    # TODO: tree change position
    """
    {i}...{/i}
    
    {i}Am I going the right way?{/i}
    """
    # TODO: tree change position
    "{i}This forest feels endless{/i}."
    # TODO: tree change position
    "{i}Have I been this way before?{/i}"
    # TODO: tree change position
    "{i}I think I'm going in circles{/i}."
    hacker "I think I'm going in circles."
    # fade hallway
    "{i}?{/i}"
    hacker """
    You know, when I imagined finding this place in my head, it was a lot cooler.

    I mean, who would hae thought I'd be infiltrating the world;s most top secret facility using a sanitation bot?

    Whatever. Desperate times call for desperate measures, I guess.
    """
    # TODO: tree change position
    "{i}Where am I?{/i}"
    hacker "Come on...{w=0.5} Where is it?"
    # TODO: hallway 60% opacity
    # TODO: tree change position
    hacker "I've got to hurry before somebody sees me."
    "[preferredName]" "I'm so freaking lost."
    hacker "I'm so freaking lost."
    # TODO: hallway 100% opacity
    hacker "How big can this place be? I must be close. I have to be."
    # TODO: hacker move s to end of hallway
    hacker "Yes! This is it! After so many years. Finally..."
    "Before [hacker] reaches the door, it begins to open from the other side."
    # TODO: maybe play the solid snake alert sound?
    hacker """
    {b}!{/b}
    
    Not good.
    """
    # TODO: hard cut to forest. replace hacker with boss2
    "{i}!{/i}"
    iceBoss "rawr xD" # TODO: replace with sound
    "{i}Not good!{/i}"
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
    "[iceBoss] attacks."
    menu:
        "Attack 1":
            pass
        "Attack 2":
            pass
    "[iceBoss] attacks."
    """
    {i}This is really bad. I won't survive another attack like that{/i}.

    {i}I guess this is it{/i}...
    """
    # TODO: show hacker item
    iceBoss "..."
    playerCharacter "?"
    "The [iceBoss] looks at you with a blank stare, and then wanders off into the forest."
    # TODO: hide boss2 and hacker item
    """
    {i}What just happened?{/i}
    
    {i}I'd better get out of here and go find the others{/i}.
    """
    if config.developer:
        "END SCENE 5"

label scene5HalfStart:
    pass

# TODO: visuals
label scene6Start:
    scene Hacker Space with fade
    hacker "Now {i}that{/i} was a close call."
    hacker "You're welcome by the way."
    menu:
        "For what?":
            hacker """
            For saving you just new, dug. {size=-5}You should probably be used to it by now, if we're being honest.{/size}

            Whatever. You can thank me later. Right now, I have a question.
            """
        "What was that door?":
            hacker """
            Door? You{w=0.5} saw that?{w=0.5}{size=-5}Weird. I guess things are working out quicker than I thought.{/size}

            That was part of <corporation>'s lab.

            You know, the one I showed you earlier.

            Sorry for leaving you on a cliffhanger there. I just got a little overexcited.

            For good reason, though!

            I found something, but before I tell you, I have a question.
            """
    hacker """
    [preferredName], be honest
    
    What do {i}you{/i} think about hte whole <digital world>?
    """
    $ tmpFlag = False
    menu:
        "I like it.":
            hacker """
            You know, if I wasn't in my current position, I think I might really love this place.

            I mean, a whole world where you can see your friends all the time, and have the same freedom as a dream?

            Sounds pretty nice to me.
            """
        "I hate it.":
            hacker """
            I get that, there's so much about the <digital world> that even I don't know.

            I mean, imagine if somebody else could do what I can. They'd be able to get away with whatever they want.
            """
        "Why do you ask?":
            $ tmpFlag = True
            hacker """
            Just curious.

            I don't really get out of the house much, so I wonder how normal people like you must feel about it.

            You know, if I wasn't in my current position, I think I'd really love this place.

            A whole world where you can see your friends all the time, adn have the same amount of freedom as a dream?

            Doesn't sound so bad to me.

            But at the same time, it's kind of scary, isn't it?

            I mean, there's so much about the <digital world> that even I still don't know.

            Imagine if somebody else was able to do what I can.

            They could get away with whatever they want.

            Sorry [preferredName], you don't have to answer the question if you don't want to.
            """
    if tmpFlag:
        menu:
            "I love the <digital world>.":
                pass
            "I hate the <digital world>.":
                pass
            "I'd prefer not to say.":
                pass
        hacker "I can understand that. One way or another, I hope we find some answers at the end of this."
    hacker """
    Anyways [preferredName], I've {i}finally{/i} found what I'm looking for. Which means we're almost at the end of our little quest.

    I have to warn you, from here on out, what we're doing is {i}not{/i} a game.
    """
    "[preferredName]" "..."
    hacker """
    I'm serious, what <corporation>'s been doing in that lab is...

    It's just really not cool! Alright?

    Look, all I need now is for you to finish your quest in <game world>. OK?

    {size=-0.5}Then maybe, just maybe, I'll be able to fix this.{/size}
    """
    menu:
        "What is <corporation> doing exactly?":
            hacker """
            I-

            They-

            ...

            *Sigh*

            Listen [preferredName]. I know I have some explaining to do. I just...

            I need you to trust me right now, OK?

            It'll all make sense once you finish the quest. I promise.
            """
            menu:
                "OK, what do I have to do?":
                    jump scene6PurpleCont
                "No. Tell me what's going on {i}{b}now{/b}{/i}":
                    hacker """
                    I-{w=0.5} I...{w=0.5} Listen, I don't have time for this!
                    
                    Are you gonna help me or not?
                    """
            menu:
                "I guess.":
                    jump scene6PurpleCont
                "No way!":
                    hacker """
                    Ugh, {i}fine{/i}. Sorry [preferredName], I tried playing nice, but this might be my only change.

                    And I am {i}not{/i} going to miss it!
                    """
                    if config.developer:
                        "END SCENE 6"
                    jump scene7Orange
        "OK.":
            jump scene6PurpleCont

label scene6PurpleCont:
    hacker """
    Great! All you have to do is go back into the forest, and you should find what you're looking for pretty fast.
    
    Oh, and this time, don't bring any of your pesky friends with you! {size=-0.5}Sorry, but this last part is single-player only.{/size}

    ALright? You'd better hurry. Good Lick [preferredName]!

    I'll be waiting for you on the other side.
    """
    if config.developer:
        "END SCENE 6"

# TODO: visuals
label scene7Purple:
    friendA "Hey [playerCharacter], are you even listening?"
    friendB "Looks like [playerCharacterSubjectPronoun] zoned out pretty hard there."
    friendA """
    We've got to figure out what to do next.
    
    All we found in that dumb forest was a freaking [iceBoss].
    """
    gameLog "{font=Kenney Rocket.ttf}Current Objective: Inside <forest>.{/font}"
    "{i}Right. I've got to go back{/i}."
    playerCharacter "I'm gonna go get some more firewood."
    friendA "OK."
    friendB "Don't go too far. The [iceBoss] could still be around."
    gameLog "{font=Kenney Rocket.ttf}Current Objective: Inside <forest>.{/font}"
    "{i}This place makes no sense{/i}."
    "{i}What am I even looking for?{/i}"
    show hacker item at truecenter
    "{i}I guess I should follow it{/i}."
    """
    {i}I've been walking for a long time now{/i}.
    
    {i}This forest feels never-ending{/i}.
    """
    "{i}Is that...?{/i}"
    gameLog "{font=Kenney Rocket.ttf}Current Objective: <redacted>.{/font}"
    $ tmpFlag = False
    if config.developer:
        "END SCENE 7"
    jump scene8Start

label scene7Orange:
    friendA """
    So what should we do now?

    All we found in the forest was a freaking [iceBoss]
    """
    friendA """
    ?

    What the...
    """
    $ tmpGlitchText = glitchText(32)
    friendA "[tmpGlitchText]"
    $ tmpGlitchText = glitchText(64, True)
    friendA "[tmpGlitchText]"
    $ tmpGlitchText = glitchText(128, True)
    friendA "{b}{vert}[tmpGlitchText]{/vert}{/b}"
    friendB "What's going on?"
    python:
        if random.randint(0,2) == 0:
            tmpGlitchText = glitchText(32)
            tmpGlitchText1 = glitchText(32, True)
        else:
            tmpGlitchText = glitchText(32, True)
            tmpGlitchText1 = glitchText(32)
    menu:
        "[tmpGlitchText]":
            pass
        "[tmpGlitchText1]":
            pass
    scene black with fade
    $ tmpFlag = True
    if config.developer:
        "END SCENE 7"

label scene8Start:
    if config.developer:
        "END SCENE 8"

label scene9Start:
    "{i}Where am I?{/i}"
    "{i}I can't feel my body{/i}"
    hacker """
    This is it [player]. Before we continue{w=1.0}, I have to apologize. I haven't been 100 percent honest with you.

    You may already know by now, but the truth is, <forest> was never supposed to be part of the game.
    
    In fact, it’s barely part of the <digital world> at all.

    It's part of {i}me{/i}.
    """
    playerCharacter "?"
    hacker "And now that you've found it, I fear we're both in terrible danger."
    playerCharacter "???"
    $ tmpChosen = "Look"
    menu:
        "What kind of danger?":
            pass
        "What do you mean the <forest> is {i}part of you?{/i}":
            pass
        "What happened to the <digital world>? To my friends?" if tmpFlag:
            hacker """
            Sorry, when you refused to finish the quest, I got desperate.

            But don't worry! Your friends will be fine.{w=1.0} {size=-0.5}Probably.{/size}
            """
            $ tmpChosen = "Anyways"
    hacker """
    [tmpChosen], I don't have much time, but I promise everything will make sense soon.
    
    Thanks to you finishing my quest, I'm finally able to complete our connection.

    Which means right now, I {i}need{/i} your help. [preferredName], I have to know...

    {i}Do you trust me?{/i}
    """
    menu:
        "Yes":
            "[hacker] lets out a sigh of relief."
            hacker """
            Alright. This next part is gonna feel weird.

            Just promise to stay calm, alright?
            """
        "No":
            "[hacker] lets out a disappointed sigh."
            hacker """
            I'm sorry [preferredName], but there's no other way...

            {i}I have to do this{/i}.
            """
    # TODO: play a glitched out image with the below pulse transition
    scene black with pulse(12, "#fff", 0.5, 1.2, 0.1, 0.1, 0.25, 2.0)
    $ renpy.pause(2.0)
    if config.developer:
        "END SCENE 9"

label scene10Start:
    scene Bedroom with None
    """
    {i}I'm...{w=0.5} home?{/i}

    Without thinking, you stand up.

    {i}Something's not right{/i}.

    {i}{#TODO: hacker font}I have to go now.{/i}

    {i}But why?{/i}

    You walk toward the door.

    As you reach for the handle, you notice the <quest item> on your wrist.

    {i}Is this real?{/i}
    """
    scene black with fade
    "You leave your room and step outside"
    scene City with fade
    """
    You begin walking down the street.

    {i}I've never been this way before, but it feels oddly familiar{/i}.

    {i}{#TODO: hacker font}It must be this way.{/i}

    {i}What is?{/i}

    You move as if you've walked this route a thousand times.

    {i}{#TODO: hacker font}I have to hurry.{/i}
    """
    # TODO: transition to corporation building scene
    "{i}Here?{/i}"
    # TODO: zoom into building
    scene Hallway with fade
    "{i}Won't somebody see me?{/i}"
    hacker "They only see what I want them to see."
    # TODO: zoom
    "{i}Are you{w=0.5}... in my head?{/i}"
    hacker "Always have been."
    # TODO: zoom again
    """
    {i}{#TODO: hacker font}Almost there...{/i}

    {i}{#TODO: hacker font}I can't believe it. This actually might work!{/i}

    As you open the door, you feel a growing sense of excitement. You cannot tell if it's your own.
    """
    if config.developer:
        "END SCENE 10"

label scene11Start:
    """
    You appear to be in some kind of server room.

    Without hesitation, you walk purposefully through the maze of consoles.

    You've never stepped foot in this place, yet if feels as if you've walked this route countless times.

    You reach a large console in the center of the room. All of the room's wires lead to this machine.
    
    {i}This is it{/i}.
    
    Before you lies a massive control panel. You begin adjusting various devices...

    As you continue to work on the panel, you notice a faint sound...

    {i}The machine is... breathing{/i}.

    {i}Almost there...{/i}

    {i}Just this...{/i}

    {i}And this...{/i}

    {i}And - There!{/i}

    You press one more button and step away from the center console.

    The front of the machine begins to open. Through the cracks you get a small glimpse of what's inside, but you are interrupted by a voice...
    """
    "Unknown Male Voice" "Hey! Stop right there!"
    play sound "audio/9_mm_gunshot.wav"
    """
    You wake up on the floor in front of the center console.

    {i}My head hurts...{/i}

    Lying on the floor next to you is your headset. There is a large hole in it.

    {i}Was I just... shot?{/i}
    
    Standing across the room is a man. He looks familiar.

    He's aiming a gun right at you.
    """
    "Unknown Man" "Your game ends here."
    "Unknown Female Voice" "No!"
    play sound "audio/mirror_shattering.wav"
    """
    Before the man is able to shoot again, the console nearest him explodes, knocking him to the ground. His gun skitters out of reach into the darkness.

    {i}That voice...{/i}
    """
    "Unknown Man" "Ughhh..."
    """
    The man appears to be unconscious.

    The center console opens completely. The girl is connected to the machine, suspended by cables.

    {i}Is that...?{/i}
    """
    "Strange Girl" "Hey [player]."
    menu:
        "What's going on here?":
            pass
        "Who are you?":
            hacker "It's me, [hacker]."
    hacker "This here is the truth behind the <digital world>."
    "{i}Her voice is strange, but it's undeniably [hacker]'s{/i}."
    hacker """
    I'm sorry [player]. To be honest I didn't lead you here to save it.{w=2.0} I brought you here to destroy the <digital world>.

    As it turns out, we've actually had the world's strongest supercomputer with us all along.

    Only in the mind can there exist truly endless possibilities.

    For years, scientists tried to replicate that power, creating countless supercomputers, AI after AI, and even quantum processing.

    But in the end, no machine could compare to the brain, so humans did what they do best:{w=0.5} Adapt.

    While the power of the human brain can't be replicated, it can be harnessed, rewired, {i}abused{/i}.

    Do you get it now [player]? All these fancy computers around us? They're not running the <digital world>.{w=0.5} {i}I am{/i}.
    """
    menu:
        "Set [hacker] free":
            scene black with Pixellate(5, 24)
        "Leave [hacker] here":
            scene black

label kill:
    if config.developer:
        "{cps=0}GAME DIE{/cps}"
    stop music
    call credits from _call_credits
    $ renpy.quit()