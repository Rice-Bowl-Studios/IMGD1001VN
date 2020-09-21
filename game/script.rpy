# The script of the game goes in this file.

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
define hacker = Character("Hacker")

# BG
image Game Tavern = "bg_GW_GameTavern.png"
image Game World Arena 01 = "bg_GW_GameWorldArena01.png"
image Game World Arena 02 = "bg_GW_GameWorldArena02.png"
image Generic Game Env = "bg_GW_GenericGameEnvironment.png"
image Hacker Space = "bg_GW_HackerSpace.png"
image Bedroom = "bg_RW_Bedroom.png"
image City = "bg_RW_City.png"
image Prison = "bg_RW_Prison.png"

# IMG
image Boss01 angry = "ch_GW_Boss01_angry.png"
image Boss01 attacking = "ch_GW_Boss01_attacking.png"
image Boss01 neutral = "ch_GW_Boss01_neutral.png"
image Boss01 possessed = "ch_GW_Boss01_POSSESSED.png"
image Boss02 angry = "ch_GW_Boss02_angry.png"
image Boss02 attacking = "ch_GW_Boss02_attacking.png"
image Boss02 neutral = "ch_GW_Boss02_neutral.png"
image Boss02 possessed = "ch_GW_Boss02_POSSESSED.png"
image Friend01 angry = "ch_GW_Friend01_angry.png"
image Friend01 happy = "ch_GW_Friend01_happy.png"
image Friend01 neutral = "ch_GW_Friend01_neutral.png"
image Friend01 possessed = "ch_GW_Friend01_POSSESSED.png"
image Friend01 sad = "ch_GW_Friend01_sad.png"
image Friend02 angry = "ch_GW_Friend02_angry.png"
image Friend02 happy = "ch_GW_Friend02_happy.png"
image Friend02 neutral = "ch_GW_Friend02_neutral.png"
image Friend02 possessed = "ch_GW_Friend02_POSSESSED.png"
image Friend02 sad = "ch_GW_Friend02_sad.png"
image GWHacker = "ch_GW_Hacker.png"
image RWHacker neutral = "ch_RW_Hacker_neutral.png"

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
            python:
                playerCharacterSubjectPronoun = renpy.input("Subject Pronoun (ex. he, she, they):")
                playerCharacterSubjectPronoun = playerCharacterSubjectPronoun.strip()
                if not playerCharacterSubjectPronoun:
                    playerCharacterSubjectPronoun = "they"
                playerCharacterObjectPronoun = renpy.input("Object Pronoun (ex. him, her, them):")
                playerCharacterObjectPronoun = playerCharacterObjectPronoun.strip()
                if not playerCharacterObjectPronoun:
                    playerCharacterObjectPronoun = "them"
                playerCharacterDepPossesivePronoun = renpy.input("Dpeendent Possessive Pronoun (ex. his, her, their):")
                playerCharacterDepPossesivePronoun = playerCharacterDepPossesivePronoun.strip()
                if not playerCharacterDepPossesivePronoun:
                    playerCharacterDepPossesivePronoun = "their"
                playerCharacterIndepPossesivePronoun = renpy.input("Independent Possessive Pronoun (ex. his, hers, theirs):")
                playerCharacterIndepPossesivePronoun = playerCharacterIndepPossesivePronoun.strip()
                if not playerIndepPossesivePronoun:
                    playerCharacterIndepPossesivePronoun = "theirs"
        
label startBossFight:
    scene Game World Arena 01 with None
    show Boss01 angry at right with easeinright
    show Friend01 angry at left with easeinleft
    $ playerCharacterSubjectPronoun = playerCharacterSubjectPronoun.lower()
    friendA "Ugh! Why's this taking so long? Where the heck is [playerCharacterSubjectPronoun]?"
    startBoss "HAHAHAHA THERE IS NO HOPE FOR YOU PUNY MORTAL"
    show Boss01 angry with vpunch
    "TODO: PLAY EXPLOSION/LOUD CRASH"
    friendA "Damn my <weapon>'s almost broken! I can't stay here much longer."
    gameLog "{i}[playerCharacter] has entered the area{/i}"
    show Friend01 happy
    friendA "There you are, it's about time! Wasn't the plan to ambush the [startBoss] like 30 minutes ago?"
    menu:
        "Sorry I'm late, I fell asleep.":
            pass
        "I'm here now, let's do this.":
            pass
    friendA "Well come on! You know, if we don't beat this <insulting nickname for boss> tonight [friendB]'s never gonna let us forget it."
    "{i}You draw your <weapon>, [friendA] draws his <weapon>{/i}"
    startBoss "YOU PATHETIC CREATURES REALLY THINK YOU CAN DEFEAT ME?"
    show Friend01 angry
    friendA "I'm going in. Cover me!"
    menu:
        "<Attack 1>":
            pass
        "<Attack 2>":
            pass
    "{i}[friendA]'s <weapon> shatters into a million pieces{/i}"
    friendA "Shit!"
    friendA "I don't get it, our level is way higher than his. Shouldn't this fight be easy?"
    menu:
        "Yeah, it's kind of weird.":
            pass
        "Maybe you're just bad.":
            friendA "Very funny coming from the one who almost missed the whole fight."
    friendA "I don't know if we can win this [playerCharacter]"
    $ tmpFlag = False

label startBossAttackChoice:
    menu:
        "<Attack>":
            gameLog "Critical Hit!"
            friendA "Nice!"
        "<Run Away>" if not tmpFlag:
            $ tmpFlag = True
            startBoss "HAHAHA YOU FOOLS CAN'T ESCAPE ME"
            jump startBossAttackChoice
    $ tmpFlag = False

label startBossAttackChoice2:
    menu:
        "<Attack>":
            gameLog "Critical Hit!"
            friendA "Wow!"
        "<Run Away>" if not tmpFlag:
            $ tmpFlag = True
            startBoss "[startBoss] blocks your path"
            jump startBossAttackChoice2
    $ tmpFlag = False

label startBossAttackChoice3:
    menu:
        "<Attack>":
            gameLog "Critical Hit!"
            friendA "What the-"
        "<Run Away>" if not tmpFlag:
            $ tmpFlag = True
            startBoss "[startBoss] blocks your path"
            jump startBossAttackChoice3
    startBoss "AAAARRRGGGGHHHHH HOW COULD THIS HAPPEN???"
    hide Boss01 with easeoutright
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
    friendA "Oh wait... nevermind"
    friendA "Ooo maybe this is-"
    friendA "Nah, I got nothin. How about you? Anything good?"
    "{i}Only one item appears on your screen{/i}"
    show item hacker item at right with zoomin
    $ tmpGlitchText = glitchText(16)
    gameLog "[tmpGlitchText] was added to your inventory"
    friendA "That's all you got? God, [friendB]'s gonna get a kick outta this one."
    friendA "Hey wait. What's up with it's name? I can't read it on my screen. Can you?"
    playerCharacter "No"
    friendA "Huh, weird. Well maybe [friendB] knows something about it-"
    scene crash with vpunch
    "TODO: crash effect"

label startRealWorld:
    scene Bedroom with None
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
            python:
                playerSubjectPronoun = renpy.input("Subject Pronoun (ex. he, she, they):")
                playerSubjectPronoun = playerSubjectPronoun.strip().capitalize()
                if not playerSubjectPronoun:
                    playerSubjectPronoun = "they"
                playerObjectPronoun = renpy.input("Object Pronoun (ex. him, her, them):")
                playerObjectPronoun = playerObjectPronoun.strip().capitalize()
                if not playerObjectPronoun:
                    playerObjectPronoun = "them"
                playerDepPossesivePronoun = renpy.input("Dpeendent Possessive Pronoun (ex. his, her, their):")
                playerDepPossesivePronoun = playerDepPossesivePronoun.strip().capitalize()
                if not playerDepPossesivePronoun:
                    playerDepPossesivePronoun = "their"
                playerIndepPossesivePronoun = renpy.input("Independent Possessive Pronoun (ex. his, hers, theirs):")
                playerIndepPossesivePronoun = playerIndepPossesivePronoun.strip().capitalize()
                if not playerIndepPossesivePronoun:
                    playerIndepPossesivePronoun = "theirs"
    "<game title> seems to have crashed"
    "My headset is burning hot"
    "What {i}was{/i} that weird bracelet item"
    "TODO: play phone ring sound"
    "It's [friendB]"
    show Friend02 neutral with None
    friendB "Hey [player] where are you two? I thought you and [friendA] were gonna come over after you took down that [startBoss]"
    menu:
        "About that…":
            friendB "Ha! You seriously fell asleep? Here I was thinking [friendA] was the stupid one."
        "I'll be there in a few minutes.":
            friendB "Alright. Are you still with [friendA]?"
    friendB "Oh, here he is now. I’ll see you in a bit. Bye."
    "I'd better try logging back in"
    "{i}You put your headset back on{/i}"
    scene logInScreen with None
    $ renpy.pause(2.0)
    scene black with None
    "..."
    "My headset is getting hot again."
    "{i}Tries to remove headset{/i}"
    scene red with None
    "I can't life my arm."
    "My head feels like it's on fire."
    "It feels like somehting's grabbing my wrist."
    "I can't get the headset off with my arm stuck like this."
    "The heat is getting unbearable..."
    scene black with None
    $ renpy.pause(2.0)

label startHackerSpace:
    scene Hacker Space with fade
    "{i}Where am I?{/i}"
    show GWHacker at center with easeinbottom
    hacker "God question. From what I can see, I'm pretty sure you're in a bedroom."
    $ tmpChosen = -1
    menu:
        "Who are you?":
            $ tmpChosen = 0
            hacker "That's kind of complicated. Could we start with the easy questions please?"
        "Did you just read my mind?":
            $ tmpChosen = 1
            hacker "Oh, if only it were that simple! What do I look like? Some kind of fortune teller?"
            hacker "Let's just say I made an extremely educated guess"
        "How did you know that?":
            $ tmpChosen = 2
            hacker "Um... I'm actually a psychic."
            hacker "No, a genie!"
            hacker "Or maybe I'm your consience! Hehe, spooky, right?"
    menu:
        "Who are you?" if tmpChosen != 0:
                pass
        "Did you just read my mind?" if tmpChosen != 1:
                pass
        "How did you know that?" if tmpChosen != 2:
                pass
    hacker "Okay, I think that's enough questioning for today."
    "{i}You try to speak, but nothing comes out. It feels as though you are underwater.{/i}"
    hacker "Right, now hwere was I? Let's see,{w=1.0}{nw}"
    show item hacker item at right with zoomin
    hacker "Ah of course"
    hacker "{i}ahem{/i}"
    if playerName != playerUsername:
        hacker "Welcome to my world [playerCharacter]! Or should I say [player]."
        hacker "Which would you prefer?"
        jump hackerSpaceNameChoice
    else:
        hacker "Welcome to my world [player]."
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
        "How do you know my name?":
            hacker "Hey, what did I say about asking questions?"
            jump hackerSpaceNameChoice
    
label afterHackerSpaceNameChoice:
    if playerName != playerUsername:
        hacker "Ya know, I'm so glad you're here [preferredName]. I was really starting to think {i}nobody{/i} would show up to my little party."
    else:
        hacker "Ya know, I'm so glad you're here. I was really starting to think {i}nobody{/i} would show up to my little party."
    hacker "But then, right when I was about to call it off, you came along and found my invitation!"
    "{i}The mysterious figure gestures toward the <HackerItem>, which is now fastened to your wrist{/i}"
    "{i}How did that get there?{/i}"
    hacker "And guess what. The best part is,{w=3.0} It's yours to keep! Consider it a party favor from your new best friend."
    hacker "Oh, that reminds me,{w=1.0} I haven't introduced myself yet! Sorry, it's been a while since I've actually talked to someone for real like this."

label kill:
    "GAME DIE"

    $ renpy.quit()