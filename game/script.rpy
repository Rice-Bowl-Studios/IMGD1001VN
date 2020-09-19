﻿# The script of the game goes in this file.

# Player vars
define player = Character("[playerName]")
default playerSubjectPronoun = "they"
default playerObjectPronoun = "them"
default playerDepPossesivePronoun = "their"
default playerIndepPossesivePronoun = "theirs"

# Player Character vars
define playerCharacter = Character("[playerUsername]")
default playerCharacterSubjectPronoun = "they"
default playerCharacterObjectPronoun = "them"
default playerCharacterDepPossesivePronoun = "their"
default playerCharacterIndepPossesivePronoun = "theirs"

# Characters
define friendA = Character("Friend A")
define friendB = Character("Friend B")
define startBoss = Character("Start Boss")
define gameLog = Character("GameLog")


# Other vars
define noFlashing = True

# The game starts here.

label splashscreen:
    $ renpy.pause (0)
    scene whitedrop with None
    if config.developer:
        "DEBUG MODE ENABLED"
    "Splashscreen here"
    return



label main_menu:
    return

label start:

    "GAME START"

    menu:
        "This game has flashing and strobing, which can cause seizures. Would you like to disable them?"
        "Yes":
            $ noFlashing = True
        "No":
            pass
    python:
        playerUsername = renpy.input("What is your username?")
        playerUsername = playerUsername.strip()
        if not playerUsername:
            playerUsername = "Pat Rick"
    menu:
        "What are your pronouns?"
        "He/Him/His":
            python:
                playerCharacterSubjectPronoun = "he"
                playerCharacterObjectPronoun = "him"
                playerCharacterDepPossesivePronoun = "his"
                playerCharacterIndepPossesivePronoun = "his"
        "She/Her/Hers":
            python:
                playerCharacterSubjectPronoun = "she"
                playerCharacterObjectPronoun = "her"
                playerCharacterDepPossesivePronoun = "her"
                playerCharacterIndepPossesivePronoun = "hers"
        "They/Them/Their":
            python:
                playerCharacterSubjectPronoun = "they"
                playerCharacterObjectPronoun = "them"
                playerCharacterDepPossesivePronoun = "their"
                playerCharacterIndepPossesivePronoun = "theirs"
        "Other":
            call playerCharacterPronounHelper from _call_playerCharacterPronounHelper
    jump startBossFight
        
label startBossFight:
    scene bossLevel with None
    show start boss at right with easeinright
    show friend a at left with easeinleft
    $ playerCharacterSubjectPronoun = playerCharacterSubjectPronoun.lower()
    friendA "Ugh! Why's this taking so long? Where the heck is [playerCharacterSubjectPronoun]?"
    startBoss "HAHAHAHA THERE IS NO HOPE FOR YOU PUNY MORTAL"
    "TODO: PLAY EXPLOSION/LOUD CRASH"
    friendA "Damn my <weapon>'s almost broken! I can't stay here much longer."
    gameLog "{i}[playerCharacter] has entered the area{/i}"
    friendA "There you are, it's about time! Wasn't the plan to ambush the [startBoss] like 30 minutes ago?"
    menu:
        "Sorry I'm late, I fell asleep.":
            pass
        "I'm here now, let's do this.":
            pass
    friendA "Well come on! You know, if we don't beat this <insulting nickname for boss> tonight [friendB]'s never gonna let us forget it."
    "You draw your <weapon>, [friendA] draws his <weapon>"
    startBoss "YOU PATHETIC CREATURES REALLY THINK YOU CAN DEFEAT ME?"
    friendA "I'm going in. Cover me!"
    menu:
        "<Attack 1>":
            pass
        "<Attack 2>":
            pass
    "[friendA]'s <weapon> shatters into a million pieces"
    friendA "Shit!"
    friendA "I don't get it, our level is way higher than his. Shouldn't this fight be easy?"
    menu:
        "Yeah, it's kind of weird.":
            pass
        "Maybe you're just bad.":
            friendA "Very funny coming from the one who almost missed the whole fight."
    friendA "I don't know if we can win this [playerCharacter]"
    jump startBossAttackChoice

label startBossAttackChoice:
    menu:
        "<Attack>":
            gameLog "Critical Hit!"
            friendA "Nice!"
        "<Run Away>":
            startBoss "HAHAHA YOU FOOLS CAN'T ESCAPE ME"
            jump startBossAttackChoice
    jump startBossAttackChoice2

label startBossAttackChoice2:
    menu:
        "<Attack>":
            gameLog "Critical Hit!"
            friendA "Wow!"
        "<Run Away>":
            startBoss "[startBoss] blocks your path"
            jump startBossAttackChoice2
    jump startBossAttackChoice3

label startBossAttackChoice3:
    menu:
        "<Attack>":
            gameLog "Critical Hit!"
            friendA "What the-"
        "<Run Away>":
            startBoss "[startBoss] blocks your path"
            jump startBossAttackChoice3
    startBoss "AAAARRRGGGGHHHHH HOW COULD THIS HAPPEN???"
    hide start boss with easeoutright
    friendA "That was awesome!"
    menu:
        "I know":
            pass
        "I just got lucky":
            pass
    friendA "Let's see what kind of loot we got!"
    friendA "Woah is that a-"
    friendA "Oh wait... nevermind"
    friendA "Ooo maybe this is-"
    friendA "Nah, I got nothin. How about you? Anything good?"
    "Only one item appears on your screen"
    show hacker item at right with zoomin
    gameLog "<Unknown> was added to your inventory" # replace <Unknown> with glitch text
    friendA "That's all you got? God, [friendB]'s gonna get a kick outta this one."
    friendA "Hey wait. What's up with it's name? I can't read it on my screen. Can you?"
    playerCharacter "No"
    friendA "Huh, weird. Well maybe [friendB] knows something about it-"
    show hacker item with vpunch
    hide friendA
    "TODO: crash effect"
    jump startRealWorld

label startRealWorld:
    scene playerBedroom with None
    python:
        playerName = renpy.input("What is your name?")
        playerName = playerName.strip()
        if not playerName:
            playerName = "Pat Rick"
    menu:
        "What are your pronouns?"
        "He/Him/His":
            python:
                playerSubjectPronoun = "he"
                playerObjectPronoun = "him"
                playerDepPossesivePronoun = "his"
                playerIndepPossesivePronoun = "his"
        "She/Her/Hers":
            python:
                playerSubjectPronoun = "she"
                playerObjectPronoun = "her"
                playerDepPossesivePronoun = "her"
                playerIndepPossesivePronoun = "hers"
        "They/Them/Their":
            python:
                playerSubjectPronoun = "they"
                playerObjectPronoun = "them"
                playerDepPossesivePronoun = "their"
                playerIndepPossesivePronoun = "theirs"
        "Other":
            call playerPronounHelper from _call_playerPronounHelper
    "<game title> seems to have crashed"
    "My headset is burning hot"
    "What {i}was{/i} that weird bracelet item"
    "TODO: play phone ring sound"
    "It's [friendB]"
    friendB "Hey [player] where are you two? I thought you and [friendA] were gonna come over after you took down that [startBoss]"
    menu:
        "About that…":
            friendB "Ha! You seriously fell asleep? Here I was thinking [friendA] was the stupid one."
        "I'll be there in a few minutes.":
            friendB "Alright. Are you still with [friendA]?"
    friendB "Oh, here he is now. I’ll see you in a bit. Bye."
    "I'd better try logging back in"
    "You put your headset back on"
    scene logInScreen with None
    ""
    scene black with None
    "..."
    "My headset is getting hot again."
    "Tries to remove headset"
    scene red with None
    "I can't life my arm."
    "My head feels like it's on fire."
    "It feels like somehting's grabbing my wrist."
    "I can't get the headset off with my arm stuck like this."
    "The heat is getting unbearable..."
    scene black with None
    $ renpy.pause(2.0)
    jump startHackerSpace

label startHackerSpace:
    scene hackerSpace with fade
    jump kill

label kill:
    "GAME DIE"

    $ renpy.quit()