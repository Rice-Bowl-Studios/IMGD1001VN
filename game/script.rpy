# The script of the game goes in this file.

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
define friendA = Character("Ognian", image="Friend01")
define friendB = Character("Hilda", image="Friend02")
define startBoss = Character("Ignis the Conqueror", image="Boss01")
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
image crash = "bg_GW_crash.png"
image logInScreen = "bg_GW_login.png"

# Char IMG
image Boss01 angry = "ch_GW_Boss01_angry.png"
image Boss01 attacking = "ch_GW_Boss01_attacking.png"
image Boss01 neutral = "ch_GW_Boss01_neutral.png"
image Boss01 possessed = "ch_GW_Boss01_POSSESSED.png"
image Boss02 angry = "ch_GW_Boss02_angry.png"
image Boss02 attacking = "ch_GW_Boss02_attacking.png"
image Boss02 neutral = "ch_GW_Boss02_neutral.png"
image Boss02 possessed = "ch_GW_Boss02_POSSESSED.png"
image Friend01 angry = im.Crop("ch_GW_Friend01_angry.png", (100, 0, 520, 720))
image Friend01 happy = im.Crop("ch_GW_Friend01_happy.png", (100, 0, 520, 720))
image Friend01 neutral = im.Crop("ch_GW_Friend01_neutral.png", (100, 0, 520, 720))
image Friend01 possessed = im.Crop("ch_GW_Friend01_POSSESSED.png", (100, 0, 520, 720))
image Friend01 sad = im.Crop("ch_GW_Friend01_sad.png", (100, 0, 520, 720))
image Friend02 angry = im.Crop("ch_GW_Friend02_angry.png", (100, 0, 520, 720))
image Friend02 happy = im.Crop("ch_GW_Friend02_happy.png", (100, 0, 520, 720))
image Friend02 neutral = im.Crop("ch_GW_Friend02_neutral.png", (100, 0, 520, 720))
image Friend02 possessed = im.Crop("ch_GW_Friend02_POSSESSED.png", (100, 0, 520, 720))
image Friend02 sad = im.Crop("ch_GW_Friend02_sad.png", (100, 0, 520, 720))
image GWHacker = "ch_GW_Hacker.png"
image RWHacker neutral = "ch_RW_Hacker_neutral.png"

# Item IMG
image hacker item = im.Scale("item_hackerItem.png", 360, 360)

# Other IMG
image HP 0 = im.Scale("boss_hp_0.png", 360, 90)
image HP 25 = im.Scale("boss_hp_25.png", 360, 90)
image HP 50 = im.Scale("boss_hp_50.png", 360, 90)
image HP 75 = im.Scale("boss_hp_75.png", 360, 90)
image HP 100 = im.Scale("boss_hp_100.png", 360, 90)

# Non game vars
image credit = Text(creditText, font="Montserrat-Medium.ttf", text_align=0.5)

# Other vars
define noFlashing = True

# The game starts here.

label splashscreen:
    $ renpy.pause (0)
    scene whitedrop with None
    if config.developer:
        "{cps=0}DEBUG MODE ENABLED{/cps}"
        "{cps=0}Splashscreen here{/cps}"
    return

label main_menu:
    play music "audio/Space Cadet.ogg"
    call screen volume

label start:
    if config.developer:
        "{cps=0}GAME START{/cps}"
    #"Please be careful playing if you are sensitive to flashing lights, this game does not have a filter for it implemented yet."
    menu: 
        "{cps=0}This game has flashing and strobing, which can cause seizures. Would you like to disable them?{/cps}"
        "{cps=0}Yes{/cps}":
            $ noFlashing = True
        "{cps=0}No{/cps}":
            $ noFlashing = False
    python:
        playerUsername = renpy.input("What is your username?")
        playerUsername = playerUsername.strip()
        if not playerUsername:
            playerUsername = "Pat Rick"
    menu:
        "{cps=0}What are your pronouns?{/cps}"
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
                playerCharacterDepPossesivePronoun = renpy.input("Dependent Possessive Pronoun (ex. his, her, their):")
                playerCharacterDepPossesivePronoun = playerCharacterDepPossesivePronoun.strip()
                if not playerCharacterDepPossesivePronoun:
                    playerCharacterDepPossesivePronoun = "their"
                playerCharacterIndepPossesivePronoun = renpy.input("Independent Possessive Pronoun (ex. his, hers, theirs):")
                playerCharacterIndepPossesivePronoun = playerCharacterIndepPossesivePronoun.strip()
                if not playerIndepPossesivePronoun:
                    playerCharacterIndepPossesivePronoun = "theirs"
        
label startBossFight:
    scene Game World Arena 01
    show Boss01 neutral at right
    show Friend01 angry at left
    show HP 100 at top with easeintop
    $ playerCharacterSubjectPronoun = playerCharacterSubjectPronoun.lower()
    friendA "Ugh! Why's this taking so long? Where the heck is [playerCharacterSubjectPronoun]?"
    startBoss "HAHAHAHA THERE IS NO HOPE FOR YOU PUNY MORTAL"
    play sound "audio/mirror_shattering.wav"
    show Boss01 neutral with vpunch
    friendA "Damn my weapon's almost broken! I can't stay here much longer."
    gameLog "{i}[playerCharacter] has entered the area{/i}"
    show Friend01 happy
    friendA "There you are, it's about time! Wasn't the plan to ambush this boss like 30 minutes ago?"
    menu:
        "Sorry I'm late, I fell asleep.":
            pass
        "I'm here now, let's do this.":
            pass
    friendA "Well come on! You know, if we don't beat this <insulting nickname for boss> tonight [friendB]'s never gonna let us forget it."
    "{i}You draw your weapon, [friendA] draws his weapon{/i}"
    startBoss "YOU PATHETIC CREATURES REALLY THINK YOU CAN DEFEAT ME?"
    show Friend01 angry
    friendA "I'm going in. Cover me!"
    menu:
        "Attack 1":
            pass
        "Attack 2":
            pass
    play sound "audio/swordMetal6.ogg"
    show HP 75
    "{i}[friendA]'s weapon shatters into a million pieces{/i}"
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
            gameLog "Critical Hit!"
            show HP 50
            friendA "Nice!"
        "Run Away" if not tmpFlag:
            $ tmpFlag = True
            startBoss @ angry "HAHAHA YOU FOOLS CAN'T ESCAPE ME"
            jump startBossAttackChoice
    $ tmpFlag = False

label startBossAttackChoice2:
    menu:
        "Attack":
            play sound "audio/swordMetal6.ogg"
            gameLog "Critical Hit!"
            show HP 25
            friendA "Wow!"
        "Run Away" if not tmpFlag:
            $ tmpFlag = True
            startBoss @ angry "YOU WON'T GET AWAY THAT EASY"
            jump startBossAttackChoice2
    $ tmpFlag = False

label startBossAttackChoice3:
    menu:
        "Attack":
            play sound "audio/swordMetal6.ogg"
            gameLog "Critical Hit!"
            show HP 0
            friendA "What the-"
        "Run Away" if not tmpFlag:
            $ tmpFlag = True
            startBoss @ angry "WHO SAYS YOU CAN RUN?"
            jump startBossAttackChoice3
    startBoss "AAAARRRGGGGHHHHH HOW COULD THIS HAPPEN???"
    hide Boss01 with zoomout
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
    friendA "Oh wait... never mind"
    friendA "Ooo maybe this is-"
    friendA "Nah, I got nothin. How about you? Anything good?"
    "{i}Only one item appears on your screen{/i}"
    show hacker item at right with zoomin
    $ tmpGlitchText = glitchText(16)
    gameLog "[tmpGlitchText] was added to your inventory"
    friendA "That's all you got? God, [friendB]'s gonna get a kick outta this one."
    friendA "Hey wait. What's up with it's name? I can't read it on my screen. Can you?"
    playerCharacter "No"
    friendA "Huh, weird. Well maybe [friendB] knows something about it-"
    play sound "audio/computer_error_alert.wav"
    scene crash with vpunch
    $ renpy.pause(1.5)

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
                playerDepPossesivePronoun = renpy.input("Dependent Possessive Pronoun (ex. his, her, their):")
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
    play sound "<to 5>audio/phone_ringing.wav"
    $ renpy.pause(3.0)
    "It's [friendB]"
    show Friend02 neutral with easeinbottom
    friendB "Hey [player] where are you two? I thought you and [friendA] were gonna come over after you took down that [startBoss]"
    menu:
        "About that…":
            friendB "Ha! You seriously fell asleep? Here I was thinking [friendA] was the stupid one."
        "I'll be there in a few minutes.":
            friendB "Alright. Are you still with [friendA]?"
    friendB "Oh, here he is now. I’ll see you in a bit. Bye."
    hide Friend02
    "I'd better try logging back in"
    "{i}You put your headset back on{/i}"
    scene logInScreen with None
    $ renpy.pause(2.0)
    scene black with None
    "..."
    "My headset is getting hot again."
    "{i}Tries to remove headset{/i}"
    scene reddrop with None
    stop music
    play music "audio/Mission Plausible.ogg"
    "I can't lift my arm."
    "My head feels like it's on fire."
    "It feels like something's grabbing my wrist."
    "I can't get the headset off with my arm stuck like this."
    "The heat is getting unbearable..."
    scene black with None
    $ renpy.pause(2.0)

label startHackerSpace:
    scene Hacker Space with fade
    "{i}Where am I?{/i}"
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
            hacker "Oh, if only it were that simple! What do I look like? Some kind of fortune teller?"
            hacker "Let's just say I made an extremely educated guess"
        "How did you know that?":
            $ tmpChosen = 2
            hacker "Um... I'm actually a psychic."
            hacker "No, a genie!"
            hacker "Or maybe I'm your conscience! Hehe, spooky, right?"
    menu:
        "Who are you?" if tmpChosen != 0:
            pass
        "Did you just read my mind?" if tmpChosen != 1:
            pass
        "How did you know that?" if tmpChosen != 2:
            pass
    hacker "Okay, I think that's enough questioning for today."
    "{i}You try to speak, but nothing comes out. It feels as though you are underwater.{/i}"
    hacker "Right, now where was I? Let's see, plant the <hacker item>, dramatic entrace, obligatory exposition..."
    hacker "Ah of course"
    hacker "{i}*ahem*{/i}"
    if playerName != playerUsername:
        hacker "Welcome to my world, [playerCharacter]! Or should I say [player]."
        hacker "Which would you prefer?"
        jump hackerSpaceNameChoice
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
        "How do you know my name?":
            play sound "audio/error2.ogg"
            hacker "Hey, what did I say about asking questions?"
            jump hackerSpaceNameChoice
    
label afterHackerSpaceNameChoice:
    if playerName != playerUsername:
        hacker "Ya know, I'm so glad you're here [preferredName]. I was really starting to think {i}nobody{/i} would show up to my little party."
    else:
        hacker "Ya know, I'm so glad you're here. I was really starting to think {i}nobody{/i} would show up to my little party."
    hacker "But then, right when I was about to call it off, you came along and found my invitation!"
    show hacker item at right with zoomin
    "{i}The mysterious figure gestures toward the <HackerItem>, which is now fastened to your wrist{/i}"
    "{i}How did that get there?{/i}"
    hacker "And guess what. The best part is...{w=3.0} it's yours to keep! Consider it a party favor from your new best friend."
    hacker "Oh, that reminds me,{w=1.0} I haven't introduced myself yet! {i}gosh, what kind of friend doesn't even know their friend's name?{/i} Sorry, it's been a while since I've actually talked to someone for real like this."
    hacker "Hmmm...{w=0.5} where do I begin?{w=1.0} I've gone by a LOT of names in the past, <name1>{w=0.5}, <name2>{w=0.5}, <name3>{w=1.0}, {i}<embarrassing name>... I don't know what I was thinking with that one{/i}..."
    hacker "Anything ring a bell? You've probably heard of me before, right? I mean - I'm {i}kind of{/i} a big deal."
    "..."
    hacker "..."
    hacker "?"
    hacker "Nothing?{w=1.0} Seriously?"
    $ hackerName = "Medusa"
    hacker "Well, whatever, since we're friends you can call me [hacker]"
    hacker "So.. I'm sure you're probably wondering why I invited you here today. Well you see, I actually noticed you and your friends are pretty into that game."
    hacker "What was it called again?{w=2.0} You know, the one you've been playing {i}literally{/i} non-stop. {i}like seriously don't you have a job or something?{/i}"
    hacker "Anyways, I've got a game of my own going on{w=0.5} -so to speak-, and it's {i}really{/i} important. But you see, the thing is, I kind of need some help getting to the end of it."
    hacker "And you know..."
    hacker "I just thought..."
    hacker "{i}Since we are friends{/i}"
    hacker "You could lend me a hand!"
    menu:
        "ok...?":
            pass
        "Hell no!":
            pass
    hacker "Awesome! I knew I could count on you [preferredName]!{w=1.0} I mean, what are friends for, right?"
    hacker "And don't worry! I promise that when we beat my little game, there's gonna be a special reward just for you.{w=1.0} Oh! And I can even help you with your game too!"
    hacker "Alright, [preferredName], it's been a pleasure chatting with you tonight, however, I now have a very important train to catch.{w=1.0} I'll be contacting you with more info on our deal pretty soon, so be on the lookout!"
    hacker "Anyways, [hacker] out!"
    scene black with pixellate
    "{i}What was that?{/i}"

label startFriendTwoTavern:
    scene Game Tavern with fade
    show Friend01 neutral at left with easeinleft
    show Friend02 angry at right with easeinright
    friendB "There you are. [friendA] was about to tell me about the big fight, {i}specifically the part where he somehow lost the weapon I gave him?{/i}"
    friendA "Right..."
    friendA "About that..."
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
    #"{i}You explain to [friendA] and [friendB] about what just happened{/i}"
    scene black with fade
    scene Game Tavern with fade
    show Friend01 neutral at left
    show Friend02 angry at right
    friendA "..."
    friendB "..."
    show Friend01 neutral
    show Friend02 neutral
    friendA "{i}Seriously?{/i}"
    friendB "Hold on, so you're telling me somebody just showed up and starting talking to you on the <digital world>? And you didn't know who it was or where you were?"
    friendA "That doesn't make any sense. Are you sure you weren't just on some weird night time TV channel? Sometimes I'll fall asleep on the <digital world>, and then I wake up with no idea how I got there? It's freaky."
    friendB "Um I doubt [playerCharacterSubjectPronoun]'s had that happen to [playerCharacterObjectPronoun]. Or anyone but you for that matter, like-{w=0.5} what the heck?"
    friendB "Hmm, maybe it was some kind of glitch in <game name>? That would explain the crash, and I've heard there might still be some bugs left behind from before the <digital world>."
    friendA "Or {i}maybe{/i} you you got hacked!"
    friendB "Wow, you really have been watching too much TV. You know the <digital world> runs on the most powerful supercomputer in the world. It can't be hacked."
    friendB "You said your headset overheated right? Maybe you passed out and it was all some weird dream."
    menu:
        "I think it has something to do with this bracelet.":
            pass
        "The person put this thing on my wrist":
            pass
    friendA "Oh yeah, I forgot about that; after [playerCharacter] killed [startBoss], [playerCharacterSubjectPronoun] picked up that weird item. [friendB], have you ever seen anything like it?"
    show hacker item at center with zoomin
    friendB "No. It looks just like any normal accessory, but it has no name and {w=0.5} wait, that's strange."
    friendB "It's identified as a quest item?"
    friendA "If it's a quest item, then it must be important! You really haven't seen it before [friendB]? I thought you knew everything there is to know about <game>."
    friendB "Well... not everything. I do have a life you know."
    hide hacker item
    friendA "I didn't mean it that way. I just figured... well you know, if there really is some crazy quest that involves whatever the heck just happened to [playerCharacter], you would have heard about it."
    friendB "Yeah, I'm pretty shocked myself."
    friendA "Well, I say we go see what this mystery quest is all about! I bet we'll find some rare loot along the way too. {i}maybe even some stuff [friendB] doesn't have{/i}"
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
    friendB "You know, [friendA], you may be the least qualified 'fearless leader' I know, but I'm actually pretty excited about this."
    friendA "I'll take that as a compliment"
    friendB "So, when are we starting our grand adventure?"
    friendA "How about same time tomorrow? But no falling asleep this time!"
    friendB "Fine by me."
    menu:
        "Ok.":
            pass
        "I'm not so sure about this.":
            friendA "Look, I know you're freaked out about what you saw, but the only way to figure it out is to go on this quest."
            friendA "{i}also we kinda need you since you've got the quest item and all.{/i}"
    "You nod your head affirmatively, agreeing to come along."
    friendA "Great. In that case, I think I'l be signing off for the night. We've got a big day ahead of us after all"
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
    Do you want the short answer, or the technical one?{w=1.0} Ah, screw it, I'll give you both. {i}I do love hearing the sound of my own voice after all{/i}

    [preferredName], I don't know what they taught you in school about <digital world>, but I'm assuming it was some kind of pretentious spiel about \"the world's most powerful supercomputer\" and \"a new era of digtal communication\", generously brought to you by <corporation>

    Which honestly isn't far off in some aspects

    {i}But my god, there is so much more to it than that.{/i}

    Don't get me wrong. I love our education system just as much as the next person, but let me tell you a secret. Your 8th grade history teacher has no idea what's actually going on under the hood of <corporation>'s little simmulation. In fact, nobody does.

    Hold on, did I say \"nobody\"?{w=0.5} Ha!{w=0.25} {i}They wish.{/i}

    You see, what <corporation> doesn't want you to know about their fancy \"supercomputer\" is that most of its design was actually {i}stolen.{/i}

    Don't believe me? Look no further than the first thought you had when I brought you here today.
    """
    "I thought I was in a dream..."
    hacker """
    Exactly! Let me explain...

    Believe it or not, the suits and ties at <corporation> are pretty clever. You see, their so-called \"supercomputer\" isn't much of a computer at all. It's actually emulating something much more akin to what goes on in our brains when we fall asleep. A dream, essentially.
    """
    menu:
        "Are we dreaming right now?":
            pass
        "Is everyone on <digital world> dreaming?":
            pass
    hacker """
    Well, not exactly. It's more like one person <the computer> is having some kind of comatose fever-dream, and everyone else, you and your weird friends, gets to show up and whisper in the dreamer's ear.

    With enough whispering, you can make an imprint on their subconscious, and then the dream can be whatever you want.

    In essence, they made an artificial dream machine.
    """
    if config.developer:
        "END SCENE 4"

label scene5Start:
    scene black with None
    """
    In this scene, MainC and friends begin their unusual quest.  The scene begins in a dense forest with an encounter with a very high level monster that they have no chance of defeating.

    [friendB] decides that stealth is their best option, but as they are sneaking around, [friendA] makes a mistake alerting the monster of their presence, and the group is separated.

    As MainC wanders the forest looking for [friendA] and [friendB], something strange begins to happen: The trees appear to be changing positions, but not only that, you can also hear [hacker]’s voice inside your head.

    Thoroughly confused and hopelessly lost, MainC walks almost unconsciously through the forest, unaware of where you're going or where you've been, listening only to the voice of [hacker].

    It sounds as if she’s trying to find her way around some kind of building, and suddenly -almost as if right on queue- MainC begins to see the faint outline of a hallway.
    
    As MainC walks in this dreamlike state, your vision shifts back and forth between the forest and the building.

    You can hear [hacker]’s frantic thoughts as she traverses the seemingly endless hallways, all while trying to stay undetected.

    Eventually, the forest fades away and they reach a door.  MainC can feel [hacker]’s excitement as she approaches it, however right when they are about to go inside, the door begins to open from the other end!

    Before MainC can see what lies behind the door, the surroundings are abruptly replaced by the forest again, and standing where the door once stood is the monster. Cornered and caught off guard, MainC has no choice but to fight.

    MainC attacks the monster with all your might, but it’s no use.  Each attack does barely any damage to the monster, and MainC is brought to critically low HP.
    
    However, right when it looks like there is no hope for MainC, there is a strange interaction between the beast and MainC’s quest item.

    Shockingly, the beast turns the other way, wandering off into the forest in a dazed state.  MainC quickly puts some distance between yourself and the monster, and reunites with [friendA] and [friendB].

    Once the group makes their way out of the forest, they stop for a moment to figure out where to go next.  To their surprise, MainC’s bracelet is now directing them toward a new quest marker that appears to be outside the boundaries of the game world.

    Confused but curious, they decide to head toward the edge of the map where the marker would theoretically be located.  To no one’s surprise, when they reach their destination they find a dead end.
    
    Not knowing where to go next, the group decides to take a break here and set up camp.

    They sit around and discuss their options, however as they are speaking, MainC suddenly is unable to hear them, your vision becomes blurry and dark…
    """
    if config.developer:
        "END SCENE 5"

label scene6Start:
    scene Hacker Space with fade
    hacker "Now {i}that{/i} was a close call."
    hacker "You're welcome by the way."
    """
    In this scene [hacker] triumphantly explains to MainC that she’s found exactly what she’s been looking for.

    What that is?

    She won’t say, but what she does tell MainC is that the building MainC saw is actually a secret research facility of the same company that created the <digital world>.

    It’s now time for MainC to uphold your end of their deal.  She warns MainC that from here on out this quest is not going to be just a game.  What [hacker] has found could put the digital world in danger, and she needs MainC’s help to stop it.

    At this point, [hacker] has proven to MainC that she’s not lying, and you agree to help.  [hacker] tells MainC to return to <game-world> and finish the quest.

    Once MainC reaches the end, they will have everything they need, and [hacker] will then contact you to explain what comes next.
    """
    if config.developer:
        "END SCENE 6"

label scene7Start:
    if config.developer:
        "END SCENE 7"

label scene8Start:
    if config.developer:
        "END SCENE 8"

label scene9Start:
    "\"Where am I?\""
    "\"I can't feel my body\""
    hacker """
    This is it [player]. Before we continue{w=1.0}, I have to apologize. I haven't been 100 percent honest with you.

    I'm sure you know by now, but the truth is the <serpent temple> was never supposed to be part of the game. In face, now that you've found it, I fear we're both in terrible danger.

    The core of the <temple> you just entered is barely part of the <digital world> at all in fact.

    It's part of {i}me{/i}.
    """
    "\"?\""
    hacker "Thanks to you finishing my quest, I'm finally able to complete our connection."
    "\"???\""
    hacker """
    Look, I don't have much time, but I promise everything will make sense soon.
    
    Right now I {i}need{/i} your help. [player], I have to know...

    {i}Do you trust me?{/i}
    """
    menu:
        "Yes":
            "[hacker] let's out a sigh of relief"
            hacker """
            Alright. This next part is gonna feel weird.

            Just promise to stay calm, alright?
            """
        "No":
            "[hacker] let's out a disappointed sigh.."
            hacker """
            I'm sorry [player], but there's no other way...

            I {i}have{/i} to do this.
            """
    scene black with fade
    $ renpy.pause(2.0)
    if config.developer:
        "END SCENE 9"

label scene10Start:
    scene Bedroom with None
    "\"I'm... home?\""
    "Without thinking, you stand up"
    "\"Something's not right.\""
    "You walk toward the door"
    "As you reach for the door handle, you notice the <quest item> on your wrist"
    "\"Is this real?\""
    scene black with fade
    "You leave your room and step outside"
    scene City with None
    "You begin walking down the street"
    if config.developer:
        "END SCENE 10"

label scene11Start:
    """
    You appear to be in some kind of server room

    Without hesitation, you walk purposefully through the maze of consoles

    You've never stepped foot in this place, yet if feels as if you've walked this route countless times

    You reach a large console in the center of the room. All of the room's wires lead to this machine
    
    \"This is it\"
    
    Before you lies a massive control panel. You begin adjusting various devices...

    As you continue to work on the panel, you notice a faint sound...

    \"The machine is... breathing.\"

    \"Almost there...\"

    \"Just this...\"

    \"And this...\"

    \"And - There!\"

    You press one more button and step away from the center console

    The front of the machine begins to open. Through he cracks you get a small glimpse of what's inside, but you are interrupted by a voice...
    """
    "Unknown Male Voice" "Hey! Stop right there!"
    play sound "audio/9_mm_gunshot.wav"
    """
    You wake up on the floor in front of the center console

    \"My head hurts...\"

    Lying on the floor next to you is your headset. There is a large hole in it

    \"Was I just... shot?\"
    
    Standing across the room is a man. He looks familiar

    He's aiming a gun right at you
    """
    "Unknown Man" "Your game ends here."
    "Unknown Female Voice" "No!"
    "Explosion sound"
    """
    Before the man is able to shoot again, the console nearest him explodes, knocking him to the ground. His gun skitters out of reach into the darkness

    \"That voice...\"
    """
    "Unknown Man" "Ughhh..."
    """
    The man appears to be unconscious

    The center console opens completely, revealing [hacker]'s true self. She is connected to the machine, suspended by cables

    \"Is that...?\"
    """
    "Strange Girl" "Hey [player]"
    menu:
        "What's going on here?":
            pass
        "WHo are you?":
            hacker "It's me, [hacker]"
    hacker "This here is the truth behind the <digital world>"
    "Her voice is strange, but it's undeniably [hacker]'s"
    hacker """
    I'm sorry [player]. To be honest I didn't lead you here to save it.{w=2.0} I brought you here to destroy the <digital world>

    As it turns out, we've actually had the world's strongest supercomputer with us all along.

    Only in the mind can there exist truly endless possibilities.

    For years, scientists tried to replicate that power, creating countless supercomputers, AI after AI, and even quantum processing.

    But in the end, no machine could compare to the brain, so humans did what they do best:{w=0.5} Adapt.

    While the power of the human brain can't be replicated, it can be harnessed, rewired, {i}abused{/i}

    Do you get it now [player]? All these fancy computers around us? They're not running the <digital world>.{w=0.5} {i}I am.{/i}
    """
    menu:
        "Set [hacker] free":
            pass
        "Leave [hacker] here":
            pass

label kill:
    if config.developer:
        "{cps=0}GAME DIE{/cps}"
    stop music
    call credits from _call_credits
    $ renpy.quit()