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
define friendA = Character("Piers", image="Friend01")
define friendB = Character("Cynthia", image="Friend02")
define startBoss = Character("{color=#FF9440}Ignis the Conqueror{/color}", image="Boss01")
define iceBoss = Character("{color=#70C0FF}Iceclops{/color}", image="Boss02")
define gameLog = Character("{font=ShareTechMono-Regular.ttf}{color=#BEFF52}GameLog{/color}{/font}")
define hacker = Character("[hackerName]")

# BG IMG
image Game World Arena 01 = "bg_GW_GameWorldArena01.png"
image Forest = "bg_GW_forest.png"
image HackerSpace = "bg_GW_HackerSpace.png"
image Bedroom = "bg_RW_Bedroom.png"
image City = "bg_RW_City.png"
image City Hidden = "bg_RW_City_hidden.png"
image City Future = "bg_RW_City_future.png"
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
image Boss02 angry = "ch_GW_Boss02_angry.png"
image Boss02 possessed = "ch_GW_Boss02_possessed.png"
image Friend01 angry = im.Crop("ch_GW_Friend01_angry.png", (100, 0, 520, 720))
image Friend01 happy = im.Crop("ch_GW_Friend01_happy.png", (100, 0, 520, 720))
image Friend01 neutral = im.Crop("ch_GW_Friend01_neutral.png", (100, 0, 520, 720))
image Friend01 sad = im.Crop("ch_GW_Friend01_sad.png", (100, 0, 520, 720))
image Friend02 angry = im.Crop("ch_GW_Friend02_angry.png", (100, 0, 520, 720))
image Friend02 happy = im.Crop("ch_GW_Friend02_happy.png", (100, 0, 520, 720))
image Friend02 neutral = im.Crop("ch_GW_Friend02_neutral.png", (100, 0, 520, 720))
image Friend02 sad = im.Crop("ch_GW_Friend02_sad.png", (100, 0, 520, 720))
image Hacker game:
    "ch_GW_Medusa1.png"
    0.15
    "ch_GW_Medusa2.png"
    0.15
    "ch_GW_Medusa3.png"
    0.15
    "ch_GW_Medusa4.png"
    0.15
    repeat
image Hacker future = "ch_RW_Hacker_future.png"
image Hacker real = "ch_RW_Hacker.png"
image CorpGuy neutral = im.Crop("ch_RW_CorpGuy_neutral.png", (200, 0, 420, 720))
image CorpGuy angry = im.Crop("ch_RW_CorpGuy_angry.png", (140, 0, 480, 720))

# Item IMG
image hacker item = im.Scale("item_hackerItem.png", 360, 360)
image hacker item dead = im.Grayscale(im.Scale("item_hackerItem.png", 360, 360))

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
image hackerFilter = "hacker_filter.png"

# Other game vars
define fellAsleep = False
define tmpFlag = False

# Non game vars
image credit = Text(creditText, text_align=0.5)
image Rice Bowl = Composite((525, 314), (121, 0), "rice_bowl_studios_PLACEHOLDER.png")
image Brain Logo = Composite((1024, 275), (0, 0), "brain.png", (235, 60), Text("{size=164}{font=ShareTechMono-Regular.ttf}{color=#0F0}HARDWIRED{/color}{/font}{/size}"))

# Other vars
define noFlashing = True
define colorPath = False

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
    show Brain Logo:
        align (0.5, 0.5)
        alpha 0.0
        easein 0.5 alpha 1.0
        1.0
        easeout 1.0 alpha 0.0
    $ renpy.pause(3.0)
    hide Brain Logo
    return

label main_menu:
    return

label start:
    $ suppress_overlay = False
    if config.developer:
        "{cps=0}GAME START{/cps}"
    menu:
        "{cps=0}{font=ShareTechMono-Regular.ttf}This game has flashing and strobing, which can cause seizures. Would you like to disable them?{/font}{/cps}"
        "{font=ShareTechMono-Regular.ttf}Yes{/font}":
            $ noFlashing = True
        "{font=ShareTechMono-Regular.ttf}No{/font}":
            $ noFlashing = False
    python:
        while playerUsername == "":
            playerUsername = renpy.input("{font=ShareTechMono-Regular.ttf}Username:{/font}", length=36)
            playerUsername = playerUsername.strip()
        while playerPassword == "":
            playerPassword = renpy.input("{font=ShareTechMono-Regular.ttf}Password:{/font}", length=16)
            playerPassword = playerPassword.strip()
        playerID = "#" + generateHex(8)
    "{font=ShareTechMono-Regular.ttf}[gameLog]{/font}" """
    {font=ShareTechMono-Regular.ttf}Launching {color=#BEFF52}Hero's Fantasy Online{/color}{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}{/font}{nw}

    {font=ShareTechMono-Regular.ttf}We did not find a character with that login info.{/font}

    {font=ShareTechMono-Regular.ttf}Launching character creation{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}{/font}{nw}
    """
    menu:
        "{cps=0}{font=ShareTechMono-Regular.ttf}What are your character's pronouns?{/font}{/cps}"
        "{font=ShareTechMono-Regular.ttf}He/Him/His{/font}":
            python:
                playerCharacterSubjectPronoun = "he"
                playerCharacterObjectPronoun = "him"
                playerCharacterDepPossesivePronoun = "his"
        "{font=ShareTechMono-Regular.ttf}She/Her/Hers{/font}":
            python:
                playerCharacterSubjectPronoun = "she"
                playerCharacterObjectPronoun = "her"
                playerCharacterDepPossesivePronoun = "her"
        "{font=ShareTechMono-Regular.ttf}They/Them/Their{/font}":
            python:
                playerCharacterSubjectPronoun = "they"
                playerCharacterObjectPronoun = "them"
                playerCharacterDepPossesivePronoun = "their"
        "{font=ShareTechMono-Regular.ttf}Other{/font}":
            python:
                playerCharacterSubjectPronoun = renpy.input("{font=ShareTechMono-Regular.ttf}Subject Pronoun (ex. he, she, they):{/font}", length=24)
                playerCharacterSubjectPronoun = playerCharacterSubjectPronoun.strip()
                if not playerCharacterSubjectPronoun:
                    playerCharacterSubjectPronoun = "they"
                playerCharacterObjectPronoun = renpy.input("{font=ShareTechMono-Regular.ttf}Object Pronoun (ex. him, her, them):{/font}", length=24)
                playerCharacterObjectPronoun = playerCharacterObjectPronoun.strip()
                if not playerCharacterObjectPronoun:
                    playerCharacterObjectPronoun = "them"
                playerCharacterDepPossesivePronoun = renpy.input("{font=ShareTechMono-Regular.ttf}Dependent Possessive Pronoun (ex. his, her, their):{/font}", length=24)
                playerCharacterDepPossesivePronoun = playerCharacterDepPossesivePronoun.strip()
                if not playerCharacterDepPossesivePronoun:
                    playerCharacterDepPossesivePronoun = "their"
    python:
        playerName = ""
        while playerName == "":
            playerName = renpy.input("{font=ShareTechMono-Regular.ttf}Real Name:{/font}", length=36)
            playerName = playerName.strip()

label startBossFight:
    if config.developer:
        call jumper from _call_jumper
    play music "audio/Music_1.1.1.mp3" fadein 1.5
    scene Game World Arena 01
    show Boss01 neutral:
        anchor (0.5, 0.5)
        pos (0.719, 0.5)
    show Friend01 angry at left:
        xzoom -1.0
    show black:
        0.1
        linear 0.25 alpha 0.0
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
    "{color=#F94239}[friendA]{/color}" "Ugh! Why's this taking so long? Where the heck [tmpChosen] [playerCharacterSubjectPronoun]?"
    startBoss "HAHAHAHA THERE IS NO HOPE FOR YOU PUNY MORTAL!"
    hide black
    play sound "audio/SFX_01.wav"
    show Friend01 neutral with vpunch
    "{color=#F94239}[friendA]{/color}" "Damn, my weapon's almost broken! I can't stay here much longer."
    "{font=ShareTechMono-Regular.ttf}[gameLog]{/font}" "{color=#E9FEC7}{font=ShareTechMono-Regular.ttf}[playerCharacter] has entered the area.{/font}{/color}"
    show Friend01 happy
    "{color=#F94239}[friendA]{/color}" "There you are! It's about time! Wasn't the plan to fight boss like 30 minutes ago?"
    menu:
        "Sorry I'm late. I fell asleep.":
            $ fellAsleep = True
            pass
        "I'm here now. Let's do this.":
            pass
    "{color=#F94239}[friendA]{/color}" "Well come on! You know, if we don't beat this fiery freak tonight, [friendB]'s never gonna let us forget it."
    "You draw weapon."
    startBoss "YOU PATHETIC CREATURES REALLY THINK YOU CAN DEFEAT ME?"
    show Friend01 angry
    "{color=#F94239}[friendA]{/color}" "I'm going in. Cover me!"
    menu:
        "Stab":
            pass
        "Slice":
            pass
    show Friend01 angry:
        ease 0.25 zoom 1.1
        ease 0.25 xalign 0.75
    $ renpy.pause(0.5)
    show Boss01 neutral:
        ease 0.05 zoom 0.9 xoffset 100
        ease 0.1 zoom 1.0 xoffset 0
    $ renpy.pause(0.15)
    play sound "audio/SFX_02.wav"
    show redBar:
        linear 0.25 size (360 * 3 / 4, 90)
    show Friend01 angry:
        ease 0.35 xalign 0.0
        ease 0.25 zoom 1.0
    "{font=ShareTechMono-Regular.ttf}[gameLog]{/font}" "{color=#E9FEC7}{font=ShareTechMono-Regular.ttf}[friendA]'s Legendary Mace has shattered into a million pieces.{/font}{/color}"
    "{color=#F94239}[friendA]{/color}" "Shit!"
    "{color=#F94239}[friendA]{/color}" "I don't get it. Our level is way higher than his. Shouldn't this fight be easy?"
    menu:
        "Yeah, it's kind of weird.":
            pass
        "Maybe you're just bad.":
            "{color=#F94239}[friendA]{/color}" "Very funny coming from the one who almost missed the whole fight."
    "{color=#F94239}[friendA]{/color}" "I don't know if we can win this, [playerCharacter]."
    $ tmpFlag = False

label startBossAttackChoice:
    menu:
        "Attack":
            play sound "audio/swordMetal6.ogg"
            show Boss01 neutral:
                ease 0.1 zoom 0.9 xoffset 100
            $ renpy.pause(0.1)
            show redBar:
                linear 0.25 size (360 * 1 / 2, 90)
            show Boss01 neutral:
                ease 0.1 zoom 1.0 xoffset 0
            "{font=ShareTechMono-Regular.ttf}[gameLog]{/font}" "{color=#E9FEC7}{font=ShareTechMono-Regular.ttf}Critical Hit!{/font}{/color}"
            "{color=#F94239}[friendA]{/color}" "Nice!"
        "Run Away" if not tmpFlag:
            $ tmpFlag = True
            show Boss01 angry:
                ease 0.25 zoom 1.1
            startBoss "HAHAHA YOU FOOLS CAN'T ESCAPE ME!"
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
            "{font=ShareTechMono-Regular.ttf}[gameLog]{/font}" "{color=#E9FEC7}{font=ShareTechMono-Regular.ttf}Critical Hit!{/font}{/color}"
            "{color=#F94239}[friendA]{/color}" "Wow!"
        "Run Away" if not tmpFlag:
            $ tmpFlag = True
            show Boss01 angry:
                ease 0.25 zoom 1.1
            startBoss "YOU WON'T GET AWAY THAT EASY!"
            show Boss01 neutral:
                ease 0.25 zoom 1.0
            jump startBossAttackChoice2

label startBossAttackChoice3:
    menu:
        "Attack":
            pass
        "Run Away" if not tmpFlag:
            $ tmpFlag = True
            show Boss01 angry:
                ease 0.25 zoom 1.1
            startBoss "WHO SAYS YOU CAN RUN?!"
            show Boss01 neutral:
                ease 0.25 zoom 1.0
            jump startBossAttackChoice3
    show Boss01 angry:
        parallel:
            ease 0.1 zoom 0.9 xoffset 100
        parallel:
            parallel:
                linear 0.1 xoffset -13
                linear 0.1 xoffset 24
                linear 0.1 xoffset -24
                linear 0.1 xoffset 13
            parallel:
                linear 0.08 yoffset -6
                linear 0.08 yoffset 10
                linear 0.08 yoffset -10
                linear 0.08 yoffset 6
            repeat
    $ renpy.pause (0.1)
    show redBar:
        linear 0.25 size (0, 90)
    "{font=ShareTechMono-Regular.ttf}[gameLog]{/font}" "{color=#E9FEC7}{font=ShareTechMono-Regular.ttf}Critical Hit!{/font}{/color}"
    "{color=#F94239}[friendA]{/color}" "What the-"
    play sound "audio/SFX_03.wav"
    startBoss "AAAARRRGGGGHHHHH I WILL SEE YOU IN THE ETERNAL FLAMES!!!"
    hide redBar
    hide Boss01 with zoomout
    hide HP with easeouttop
    play music "audio/Music_1.1.2.mp3" fadeout 1.0 fadein 1.0
    show Friend01 happy
    "{color=#F94239}[friendA]{/color}" "That was awesome!"
    menu:
        "I know.":
            pass
        "I just got lucky.":
            pass
    "{color=#F94239}[friendA]{/color}" "Let's see what kind of loot we got!"
    "{color=#F94239}[friendA]{/color}" "Woah is that a-"
    show Friend01 neutral
    "{color=#F94239}[friendA]{/color}" "Oh wait... never mind."
    "{color=#F94239}[friendA]{/color}" "Ooo maybe this is-"
    "{color=#F94239}[friendA]{/color}" "Nah, I got nothing. How about you? Anything good?"
    "Only one item appears on your screen."
    show hacker item with zoomin:
        anchor (0.5, 0.5)
        pos (0.719, 0.5)
    $ tmpGlitchText = glitchText(16, False, False)
    "{font=ShareTechMono-Regular.ttf}[gameLog]{/font}" "{color=#E9FEC7}{font=VT323-Regular.ttf}{size=28}{color=#0F0}[tmpGlitchText]{/color}{/size}{/font} {font=ShareTechMono-Regular.ttf}was added to your inventory{/font}{/color}"
    "{color=#F94239}[friendA]{/color}" "That's all you got? God, [friendB]'s gonna get a kick outta this one."
    "{color=#F94239}[friendA]{/color}" "Hey wait. What's up with it's name? I can't read it on my screen. Can you?"
    "{color=#88F9F4}[playerCharacter]{/color}" "No."
    "{color=#F94239}[friendA]{/color}" "Huh, weird. Well, maybe [friendB] knows something about it-{w=0.4}{nw}"
    stop music fadeout 0.5
    show screen tear
    play sound "audio/SFX_04.mp3"
    $ renpy.pause(1.0)
    hide screen tear
    play sound "audio/SFX_05.wav"
    scene black
    show crash at truecenter with vpunch
    $ renpy.pause(1.5)
    hide crash with zoomout
    if config.developer:
        "END SCENE 1"

label startRealWorld:
    play music "audio/Music_1.1.3.mp3" fadeout 1.0 fadein 1.0
    scene Bedroom with fade
    """
    {i}{color=#BEFF52}Hero's Fantasy Online{/color} seems to have crashed.{/i}

    {i}Strange, I've never seen that happen on the {color=#BEFF52}N-Scape{/color}{/i}.

    {i}My headset is burning hot.{/i}

    {i}What {i}was{/i} that weird bracelet item?{/i}
    """
    $ renpy.music.set_pause(True)
    play sound "<to 2.5>audio/SFX_06.wav"
    $ renpy.pause(2)
    stop sound fadeout 0.5
    $ renpy.music.set_pause(False)
    "{color=#88F9F4}[player]{/color}" "It's [friendB]."
    "{color=#2B95F8}[friendB]{/color}" "Hey [playerCharacter] where are you two? I thought you and [friendA] were gonna come over after you took down [startBoss]."
    menu:
        "About that…":
            $ fellAsleep = True
            "{color=#2B95F8}[friendB]{/color}" "Ha! You seriously fell asleep? Here I was thinking [friendA] was the stupid one."
        "I'll be there in a few minutes.":
            "{color=#2B95F8}[friendB]{/color}" "Alright. Are you still with [friendA]?"
    "{color=#2B95F8}[friendB]{/color}" "Oh, here he is now. I’ll see you in a bit. Bye."
    "{i}I'd better try logging back in.{/i}"
    "You put your headset back on."
    stop music fadeout 1.0
    scene logInScreen with pixellate
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
        "{font=ShareTechMono-Regular.ttf}[gameLog]{/font}" "{color=#E9FEC7}{font=ShareTechMono-Regular.ttf}Incorrect Login.{/font}{/color}"
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
    play music "audio/Music_1.1.4.mp3" fadeout 1.0 fadein 1.0
    """
    {i}???{/i}

    {i}My headset is getting hot again{/i}...

    You try to remove your headset
    """
    if not noFlashing:
        show reddrop:
            alpha 0.0
            block:
                ease 1.0 alpha 0.5
                ease 1.0 alpha 0.0
                repeat
    """
    {i}I can't lift my arm{/i}...

    {i}My head feels like it's on fire{/i}...

    {i}Why does it feel like something's grabbing my wrist?{/i}

    {i}I can't get the headset off with my arm stuck like this{/i}...

    {i}The heat is getting unbearable{/i}...
    """
    if not noFlashing:
        show reddrop:
            ease 0.5 alpha 0.0
        $ renpy.pause(0.5)
        hide reddrop
    stop music fadeout 1.0
    if config.developer:
        "END SCENE 1.5"

label startHackerSpace:
    play music "audio/Music_1.2.1.mp3" fadeout 1.0 fadein 1.0
    scene HackerSpace with fade
    "Where am I?"
    show Hacker game at truecenter with easeinbottom
    $ hackerName = "{font=VT323-Regular.ttf}{size=28}" + glitchText(8) + "{/size}{/font}"
    "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Good question. From what I can see, I'm pretty sure you're in a bedroom.{/size}{/font}{/color}"
    $ hackerName = "{font=VT323-Regular.ttf}{size=28}" + glitchText(8) + "{/size}{/font}"
    $ tmpChosen = -1
    menu:
        "Who are you?":
            $ tmpChosen = 0
            "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}That's kind of complicated. Could we start with the easy questions please?{/size}{/font}{/color}"
        "Did you just read my mind?":
            $ tmpChosen = 1
            "{color=#0F0}[hacker]{/color}" """
            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Oh, if only it were that simple! What do I look like? Some kind of fortune teller?{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Let's just say I made an extremely educated guess{/size}{/font}{/color}
            """
        "How did you know that?":
            $ tmpChosen = 2
            "{color=#0F0}[hacker]{/color}" """
            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Um... I'm actually a psychic.{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}No, a genie!{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Or maybe I'm your conscience! Hehe, spooky, right?{/size}{/font}{/color}
            """
    $ hackerName = "{font=VT323-Regular.ttf}{size=28}" + glitchText(8) + "{/size}{/font}"
    menu:
        "Who are you?" if tmpChosen != 0:
            pass
        "Did you just read my mind?" if tmpChosen != 1:
            pass
        "How did you know I'm in my bedroom?" if tmpChosen != 2:
            pass
    show screen tear
    $ renpy.pause(0.25)
    hide screen tear
    "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Okay, I think that's enough questioning for today.{/size}{/font}{/color}"
    $ hackerName = "{font=VT323-Regular.ttf}{size=28}" + glitchText(8) + "{/size}{/font}"
    "{i}I'm trying to speak, but it feels like I'm underwater.{/i}"
    "{color=#0F0}[hacker]{/color}" """
    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Right, now where was I? Let's see, plant the Serpent Bangle, dramatic entrance, obligatory exposition...{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Ah of course!{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}{i}*ahem*{/i}{/size}{/font}{/color}
    """
    $ hackerName = "{font=VT323-Regular.ttf}{size=28}" + glitchText(8) + "{/size}{/font}"
    if playerName != playerUsername:
        "{color=#0F0}[hacker]{/color}" """
        {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Welcome to my world, [playerCharacter]! Or should I say [player]?{/size}{/font}{/color}

        {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Which would you prefer?{/size}{/font}{/color}
        """
        $ tmpFlag = True
    else:
        "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Welcome to my world, [player].{/size}{/font}{/color}"
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
            show screen tear
            play sound "audio/error2.ogg"
            $ renpy.pause(0.5)
            hide screen tear
            "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Hey, now what did I say about asking questions?{/size}{/font}{/color}"
            jump hackerSpaceNameChoice

label afterHackerSpaceNameChoice:
    if playerName != playerUsername:
        "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Ya know, I'm so glad you're here [preferredName]. I was really starting to think {i}nobody{/i} would show up to my little party.{/size}{/font}{/color}"
    else:
        "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Ya know, I'm so glad you're here. I was really starting to think {i}nobody{/i} would show up to my little party.{/size}{/font}{/color}"
    $ hackerName = "{font=VT323-Regular.ttf}{size=28}" + glitchText(8) + "{/size}{/font}"
    "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}But then, right when I was about to call it off, you came along and found my invitation!{/size}{/font}{/color}"
    $ hackerName = "{font=VT323-Regular.ttf}{size=28}" + glitchText(8) + "{/size}{/font}"
    show hacker item at truecenter with zoomin
    $ tmpGlitchText = glitchText(16)
    """
    The mysterious figure gestures toward the {font=VT323-Regular.ttf}{size=28}{color=#0F0}[tmpGlitchText]{/color}{/size}{/font}, which is now fastened to your wrist

    {i}How did that get there?{/i}
    """
    hide hacker item with zoomout
    "{color=#0F0}[hacker]{/color}" """
    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}And guess what. The best part is{w=3.0}: it's yours to keep! Consider it a party favor from your new best friend.{/size}{/font}{/color}
 
    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Oh, that reminds me,{w=1.0} I haven't introduced myself yet! {size=-5}Gosh, what kind of friend doesn't even know their own friend's name?{/size}{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Sorry, it's been so long since I've actually talked to someone\nfor real like this.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Hmmm...{w=0.5} where do I begin?{w=1.0} I've gone by a LOT of names in the past, Overrider{w=0.5}, Zer0{w=0.5}, Shadow{w=1.0}...{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}{size=-5}Scr1ptK1dd13{w=0.5}... I don't know what I was thinking with that one...{/size}{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Anything ring a bell? You've probably heard of me before, I mean - I'm {i}kind of{/i} a big deal.{/size}{/font}{/color}
    """
    $ hackerName = "{font=VT323-Regular.ttf}{size=28}" + glitchText(8) + "{/size}{/font}"
    "{color=#88F9F4}[player]{/color}" "..."
    "{color=#0F0}[hacker]{/color}" """
    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}...{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}?{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Nothing?{w=0.25} Seriously?{w=0.5} {size=-5}Wow, have I really fallen off that hard?{/size}{/size}{/font}{/color}
    """
    $ hackerName = "{font=VT323-Regular.ttf}{size=28}Medusa{/size}{/font}"
    "{color=#0F0}[hacker]{/color}" """
    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Well, whatever. Since we're friends, you can call me [hacker].{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}So.. I'm sure you're probably wondering why I invited\nyou here today.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Well you see, I actually noticed you and your friends are pretty into that game on the {color=#BEFF52}NeuralScape{/color}.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}What was it called again?{w=1.0} You know, the one you've been playing literally {i}non-stop{/i}.{w=0.5} {size=-5}Like seriously don't you have a job or something?{/size}{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Anyways, I've got a game of my own going on,{w=0.5}\nso to speak, and it's {i}really{/i} important.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}But you see, the thing is, I kind of need some help\ngetting to the end of it.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}And you know...{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I just thought...{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}{i}Since we are friends{/i}...{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}You could lend me a hand! {size=-5}Please?{/size}{/size}{/font}{/color}
    """
    menu:
        "Ok...?":
            $ tmpFlag = False
        "Hell no!":
            show screen tear
            $ renpy.pause(0.25)
            hide screen tear
            $ tmpFlag = True
    "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Awesome! I knew I could count on you [preferredName]!{w=1.0} I mean,\nwhat are friends for, right?{/size}{/font}{/color}"
    if tmpFlag:
        "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}{size=-10}Totally doesn't bother me that you don't really want to help.{/size}{/size}{/font}{/color}"
    "{color=#0F0}[hacker]{/color}" """
    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}And don't worry! I promise that when we beat my little game, there's gonna be a special reward, just for you!{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Alright, [preferredName], it's been a pleasure chatting with you tonight. However, I now have some very important business to attend to.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I'll be contacting you with more info on our deal pretty soon,\nso be on the lookout!{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Alright, now back to your regularly scheduled programming...{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}[hacker] out!{/size}{/font}{/color}
    """
    show screen tear
    stop music fadeout 1.0
    scene black with pixellate
    hide screen tear
    "{i}What was that?{/i}"
    if config.developer:
        "END SCENE 2"

label scene3Start:
    play music "audio/Music_1.1.2.mp3" fadeout 1.0 fadein 1.0
    scene Forest
    show black onlayer overlay:
        0.1
        linear 0.25 alpha 0.0
    show Friend01 neutral at right
    show Friend02 angry at left
    "{color=#2B95F8}[friendB]{/color}" "There you are. [friendA] was about to tell me about the big fight, specifically the part where he somehow {i}lost{/i} the Legendary Mace I gave him?"
    "{color=#F94239}[friendA]{/color}" """
    Right...

    About that...
    """
    hide black
    menu:
        "Something really weird just happened.":
            pass
        "Did anyone else see that?":
            pass
    show Friend01 happy
    show Friend02 happy
    "{color=#F94239}[friendA]{/color}" "Oh yeah, did your game crash too?"
    "{color=#2B95F8}[friendB]{/color}" "You had a crash? I didn't even think that was possible anymore."
    menu:
        "Well yeah, but there was...":
            pass
        "No, it was something else...":
            pass
    show Friend01 neutral at right
    show Friend02 angry at left with fade
    "{color=#F94239}[friendA]{/color}" "..."
    "{color=#2B95F8}[friendB]{/color}" "..."
    play music "audio/Music_1.3.1.mp3" fadeout 1.0 fadein 1.0
    show Friend01 neutral
    show Friend02 neutral
    "[friendA] and [friendB]" "{i}Seriously?{/i}"
    "{color=#2B95F8}[friendB]{/color}" "Hold on, so you're telling me somebody just showed up and starting talking to you on the {color=#BEFF52}N-Scape{/color}? And you didn't know who it was or where you were?"
    "{color=#F94239}[friendA]{/color}" """
    That doesn't make any sense. Are you sure you weren't just on some weird night time TV channel?

    Sometimes I'll fall asleep on the {color=#BEFF52}N-Scape{/color}, and then I wake up with no idea how I got there? It's {i}freaky{/i}.
    """
    $ playerCharacterObjectPronoun = playerCharacterObjectPronoun.lower()
    "{color=#2B95F8}[friendB]{/color}" "Um, I doubt [playerCharacterSubjectPronoun]'s had that happen to [playerCharacterObjectPronoun]. Or anyone but you for that matter, like-{w=0.5} what the heck?"
    "{color=#2B95F8}[friendB]{/color}" "Hmm, maybe it was some kind of glitch in {color=#BEFF52}Hero's Fantasy Online{/color}? That would explain the crash, and I've heard there might still be some bugs left behind from before it was ported to the {color=#BEFF52}N-Scape{/color}."
    "{color=#F94239}[friendA]{/color}" "Or {i}maybe{/i} [playerCharacterSubjectPronoun] got hacked!"
    "{color=#2B95F8}[friendB]{/color}" "Wow, you really have been watching too much TV. You know the {color=#BEFF52}N-Scape{/color} runs on the most powerful super computer in the world, right? It can't be hacked!"
    "{color=#2B95F8}[friendB]{/color}" "You said your headset overheated, right? Maybe you passed out, and it was all some weird dream."
    menu:
        "I think it has something to do with this bracelet.":
            pass
        "The person put this thing on my wrist.":
            pass
    show hacker item at truecenter with zoomin
    "{color=#F94239}[friendA]{/color}" """
    Oh yeah, I forgot about that. After [playerCharacter] killed [startBoss], [playerCharacterSubjectPronoun] picked up that weird item. [friendB].
    
    Have you ever seen anything like it, [friendB]?
    """
    "{color=#2B95F8}[friendB]{/color}" "No. It looks just like any normal accessory, but it has no name and{w=0.25} - Wait. That's strange..."
    "{color=#2B95F8}[friendB]{/color}" "It's identified as a quest item?"
    "{color=#F94239}[friendA]{/color}" "If it's a quest item, then it must be important! You really haven't seen it before [friendB]? I thought you knew everything there is to know about {color=#BEFF52}Hero's Fantasy Online{/color}."
    "{color=#2B95F8}[friendB]{/color}" "Well... not {i}everything{/i}. I do have a life you know."
    hide hacker item with zoomout
    "{color=#F94239}[friendA]{/color}" "I didn't mean it that way. I just figured... well you know, if there really is some crazy quest that involves whatever the heck just happened to [playerCharacter], you would have heard about it."
    "{color=#2B95F8}[friendB]{/color}" "To be honest, I'm pretty shocked myself."
    play music "audio/Music_1.1.2.mp3" fadeout 1.0 fadein 1.0
    "{color=#F94239}[friendA]{/color}" "Well, I say we go see what this mystery quest is all about! I bet we'll find some rare loot along the way too. {size=-5}maybe even some stuff [friendB] doesn't have.{/size}"
    "{color=#2B95F8}[friendB]{/color}" "Are you serious? You can't just charge head first into a quest you know nothing about. You're not even level 50 yet."
    "{color=#F94239}[friendA]{/color}" "Hmm, you're right..."
    "{color=#F94239}[friendA]{/color}" "That's why you're coming with me!"
    "{color=#2B95F8}[friendB]{/color}" "I would be lying if I said I wasn't a little interested. But just so we're clear, I am {i}not{/i} here to babysit you two."
    "{color=#F94239}[friendA]{/color}" "Yes!"
    "{color=#F94239}[friendA]{/color}" "How about you [playerCharacter]?"
    show black:
        alpha 0.0
        ease 1.0 alpha 0.25
    "{color=#88F9F4}[playerCharacter]{/color}" "..."
    stop music fadeout 1.0
    $ tmpGlitchText = glitchText(16)
    """
    You feel the {font=VT323-Regular.ttf}{size=28}{color=#0F0}[tmpGlitchText]{/color}{/size}{/font} pulling at your arm.

    You try to speak, but nothing comes out...

    Your hand raises into a thumbs-up position...
    """
    show black:
        ease 1.0 alpha 0.0
    play music "audio/Music_1.1.2.mp3" fadein 1.0
    $ playerCharacterDepPossesivePronoun = playerCharacterDepPossesivePronoun.lower()
    "{color=#F94239}[friendA]{/color}" "Great! It's the perfect team: Me as our fearless leader, [friendB] as our game expert/bodyguard, and [playerCharacter] and [playerCharacterDepPossesivePronoun] weird bracelet thing as our guide through the unknown."
    "{color=#F94239}[friendA]{/color}" "Together, we'll be unstoppable!"
    "{color=#2B95F8}[friendB]{/color}" "You know, [friendA], you may be the least qualified \"fearless leader\" I know, but I'm actually pretty excited about this."
    "{color=#F94239}[friendA]{/color}" "I'll take that as a compliment!"
    "{color=#2B95F8}[friendB]{/color}" "So, when are we starting our grand adventure?"
    "{color=#F94239}[friendA]{/color}" "How about same time tomorrow?"
    if fellAsleep:
        "{color=#F94239}[friendA]{/color}" "But no falling asleep this time!"
    "{color=#2B95F8}[friendB]{/color}" "Fine by me."
    hide black
    if fellAsleep:
        menu:
            "Ok.":
                pass
            "I'm not so sure about this.":
                "{color=#F94239}[friendA]{/color}" """
                Look, I know you're freaked out by what you saw, but the only way to figure it out is to go on this quest.

                {size=-5}also we kinda need you since you've got the quest item and all...{/size}
                """
                "{i}He's right. I need to find out what's going on here{/i}."
    else:
        "{color=#88F9F4}[playerCharacter]{/color}" "Ok."
    "You nod your head affirmatively, agreeing to come along."
    "{color=#F94239}[friendA]{/color}" "Great! In that case, I think I'll be signing off for the night. We've got a big day ahead of us after all."
    "{color=#2B95F8}[friendB]{/color}" "Ok. I guess I'm gonna head out too. See you tomorrow."
    stop music fadeout 1.0
    scene Bedroom with fade
    "{i}This is all so strange{/i}..."
    "{i}I'd better go to sleep for now{/i}..."
    scene black with fade
    $ renpy.pause(2.0)
    if config.developer:
        "END SCENE 3"

label scene4Start:
    play music "audio/Music_1.2.1.mp3" fadein 1.0
    scene HackerSpace with fade
    "Am I... dreaming?"
    show Hacker game with easeintop
    "{i}!{/i}"
    "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Sort of. Depends on where you draw the line between dream and reality.{/size}{/font}{/color}"
    "{color=#88F9F4}[player]{/color}" "What are you talking about?"
    "{color=#0F0}[hacker]{/color}" """
    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Do you want the short answer?{w=0.5} Or the long technical one?{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Ah, screw it, I'll give you both. {size=-5}I do love hearing the sound of my own voice after all.{/size}{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}[preferredName], I don't know what they taught you in school about the {color=#BEFF52}NeuralScape{/color},{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}But I'm assuming it was some kind of pretentious spiel about \"the world's most powerful super computer\".{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Or \"A new era of digital communication\", generously brought to you by NB-Co.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Which honestly isn't far off in some aspects.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}{i}But my god, there is sooo much more to it than that.{/i}{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Don't get me wrong. I love our education system just as much as the next person, but let me tell you a secret.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Your 8th grade history teacher has no idea what's actually going on under the hood of NB-Co's little simulation.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}In fact, {i}nobody does{/i}.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Hold on, did I say \"nobody\"?{w=0.5} Ha!{w=0.25} {i}They wish.{/i}{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}You see, what NB-Co doesn't want you to know about their fancy \"super computer\" is that most of its design was actually {i}stolen{/i}.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Don't believe me? Look no further than the first thought you had when I brought you here today.{/size}{/font}{/color}
    """
    "I thought I was in a dream..."
    "{color=#0F0}[hacker]{/color}" """
    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Exactly! Let me explain...{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Believe it or not, the suits and ties at NB-Co are pretty clever.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}You see, their so-called \"super computer\" isn't much of a computer at all.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}It's actually emulating something much more akin to what goes on in the brain when you fall asleep.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}A dream, essentially.{/size}{/font}{/color}
    """
    menu:
        "Are we dreaming right now?":
            pass
        "Is everyone on {color=#BEFF52}N-Scape{/color} dreaming?":
            pass
    "{color=#0F0}[hacker]{/color}" """
    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Well, not exactly. It's more like one person, {size=-5}the computer,{/size} is having some kind of comatose fever-dream.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}And everyone else, {size=-5}including you and your weird friends,{/size} gets to show up and whisper in the dreamer's ear.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}With enough whispering, you can make an imprint on the subconscious, and then, the dream can be whatever you want.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}In short, they made a super advanced, artificial dream machine. Super cool!{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}And super {i}creepy{/i}.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I mean, do you have any idea how much raw data is constantly flowing straight from your brain to the {color=#BEFF52}NeuralScape{/color} all the time?{/size}{/font}{/color}
    """
    "[preferredName]" "..."
    "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Neither do I! Nobody does! But I have a theory that it's a lot.{/size}{/font}{/color}"
    menu:
        "Why are you telling me all of this?":
            "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}You know if you'd just hold on a minute, I was getting there.{/size}{/font}{/color}"
        "How do you know all of this?":
            "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Oh [preferredName], I'm so glad you asked!{/size}{/font}{/color}"
    "{color=#0F0}[hacker]{/color}" """
    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}In case you haven't noticed, I'm kind of a genius when it comes to the {color=#BEFF52}NeuralScape{/color}, {size=-5}and everything else for that matter.{/size}{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}And believe it or not, me and NB-Co actually go way back.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}My relationship with them is...{w=0.5} complicated, to say the least.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I hack them...{w=0.5} they catch me...{w=0.5} I disappear for a while...{w=0.5} and then I come back and do it again!{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}And so on.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}But things changed when NB-Co launched the {color=#BEFF52}NeuralScape{/color}.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}\"The New Digital Frontier\", as they liked to call it, was supposed to be totally secure. Unhackable! Foolproof!{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Can you believe that? {size=-5}So arrogant, even by my standards.{/size}{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}They're not wrong though. There's no other system like the {color=#BEFF52}N-Scape{/color}.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}So even if you were somehow able to intercept its data, the actual hardware you'd need to read it just doesn't exist.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I'm an exception of course.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}When it comes to the {color=#BEFF52}NeuralScape{/color}, I can see {i}everything{/i}. From the contents of your inventory, to the actual thought data flowing from your brain to your headset.{/size}{/font}{/color}
    """
    menu:
        "How are you able to do that?":
            pass
        "What makes you so special?":
            pass
    "{color=#0F0}[hacker]{/color}" """
    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}To be honest, I got {i}really{/i} lucky.{w=0.5} Like I said before, the folks at NB-Co are a pretty clever bunch.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}So clever in fact, that when they launched the {color=#BEFF52}NeuralScape{/color}, they actually created a whole new security system just for me! {size=-5}Flattering, I know.{/size}{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}For certain {i}personal reasons{/i}, I won't be going into detail on how exactly NB-Co decided to deal with me. {size=-5}Sorry, but we are not that close yet{/size}.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}But what's more important is that their plan totally backfired{w=0.5} - Well, not entirely. It's more like a double edged sword.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}{i}And my side is sharper{/i}.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}You see, there's something NB-Co hasn't realized yet about their \"expert security plan\"...{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}It just so happens to double as an all-exclusive backdoor to the entire {color=#BEFF52}NeuralScape{/color}.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}And that's what allows me to do all the cool stuff I do!{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}{i}And{/i} how I'll get my revenge.{/size}{/font}{/color}
    """
    menu:
        "Revenge?":
            pass
        "What exactly are you planning?":
            "{color=#0F0}[hacker]{/color}" """
            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Hehe, piqued your interest have I? Sorry, but you'll just have to wait and see.{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Wouldn't want to ruin the surprise after all.{/size}{/font}{/color}
        """
    "{color=#0F0}[hacker]{/color}" """
    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Let's just say, NB-Co is hiding something about the {color=#BEFF52}NeuralScape{/color}.{w=1.0} {i}Something big{/i}.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}And I'm gonna be the one to expose it!{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}But...{w=0.5} I need some help. {size=-5}Lame, I know.{/size} - That's where you come in [preferredName]{/size}{/font}{/color}
    """
    menu:
        "What do you need me for?":
            pass
        "Is this going to be illegal?":
            "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Pfft... no! No... haha... why would you think that?{w=0.25} I mean, I don't know...{w=0.25} maybe...{w=0.25} {size=-5}it could be...{w=0.25} Do you want it to be?{/size}{/size}{/font}{/color}"
    "{color=#0F0}[hacker]{/color}" """
    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}You see [preferredName], before I can make my next big move, I need you to hurry up and finish your quest.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Sorry. I don't mean to sound ungrateful or anything, but there's something really important hiding at the end of that quest I gave you, and I need it ASAP.{/size}{/font}{/color}
    """
    menu:
        "If you're so powerful, why not just get it yourself?":
            "{color=#0F0}[hacker]{/color}" """
            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Um, in case you haven't noticed, I can't actually enter the {color=#BEFF52}NeuralScape{/color} myself.{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}If I were to be detected by NB-Co, everything I've done up until now would be pointless.{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Also, I'm kind of busy with my own adventure right now...{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Here, take a look.{/size}{/font}{/color}
            """
        "What is it?":
            "{color=#0F0}[hacker]{/color}" """
            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}{size=-5}Hmmm...{w=0.25} how should I explain this?{/size}{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}It's a key {size=-7}sort of?{/size} to the heart of the {color=#BEFF52}NeuralScape{/color}.{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Once I have it, I'll finally be able to expose NB-Co's secret, and take back what they stole from me.{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Exciting stuff, right? Anyways, I didn't bring you here today just to monologue about my master plan.{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I actually wanted to take you on a little field trip...{/size}{/font}{/color}
            """
    scene City Hidden with pixellate
    "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Look familiar?{/size}{/font}{/color}"
    "{i}It looks like the city I live in. Although I don't think I've been to this particular area.{/i}"
    "{color=#0F0}[hacker]{/color}" """
    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}This is the energy district.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Unless you're into nuclear physics or radiation poisoning, you've probably never been here.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}And this guy definitely doesn't fall into either of those categories.{/size}{/font}{/color}
    """
    show CorpGuy neutral:
        zoom 0.5
        anchor (0.5, 1.0)
        pos (0.35, 0.99)
        alpha 0.0
        linear 0.25 alpha 1.0
    menu:
        "Who is he?":
            "{color=#0F0}[hacker]{/color}" """
            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I'm wondering the same thing.{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}From what I've gathered, he's definitely connected to NB-Co.{/size}{/font}{/color}
            """
        "Why are you here?":
            "{color=#0F0}[hacker]{/color}" """
            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Oh, I'm not actually {i}here{/i} [preferredName]. I'm just borrowing the local camera.{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}But to answer your question, I'm here to keep an eye on our sophisticated friend here.{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}From what I've gathered, this particular individual is without a doubt part of NB-Co.{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}And from the look of his fancy getup, I'd say a pretty important one at that.{/size}{/font}{/color}
            """
    "{color=#0F0}[hacker]{/color}" """
    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}But that alone doesn't explain the data coming from his headset. There's something seriously off about it.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}You see, I've been tracking him for a couple days now, but whenever I try and see what's going on inside his head, I get all this weird junk data.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}It's like there's some kind of noise machine in his headset, drowning out all the real stuff with a bunch of nonsense.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I can't get any kind of read on what he's thinking, or what he's doing on the {color=#BEFF52}NeuralScape{/color}. It's unlike anything I've ever seen before, and honestly, it kind of freaks me out.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}It's unlike anything I've ever seen before, and honestly, it kind of freaks me out.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Anyways, I've got a sneaking suspicion this guy may know something about what I'm looking for{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}So obviously I'm gonna follow him until I find it.{/size}{/font}{/color}
    """
    window hide
    show CorpGuy neutral:
        linear 3.0 zoom 0.01 pos (0.45, 0.94)
        linear 0.5 alpha 0.0
    $ renpy.pause(4.0)
    hide CorpGuy
    scene City
    "The man heads inside a large office building..."
    "{color=#0F0}[hacker]{/color}" """
    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}!{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Did you see that [preferredName]? That building he just went in! It must be one of NB-Co's secret labs! Oh my god, this could be it!{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}{size=-5}Oh my god, this could be it!{/size}{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Hmm... I've gotta figure out how to get inside there, and fast. Their security cams are definitely well protected so\nthat's a no-go...{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Shoot! If I don't figure something out soon, I'm gonna\nmiss my chance!{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Sorry [preferredName], but I've gotta run. This is just too\nimportant to miss.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}[hacker] out!{/size}{/font}{/color}
    """
    stop music fadeout 1.0
    scene Bedroom with pixellate
    """
    {i}What the heck is she planning?{/i}

    {i}It's almost time to meet up with [friendA] and [friendB]. We're starting [hacker]'s quest today...{/i}
    """
    if config.developer:
        "END SCENE 4"

label scene5Start:
    play music "audio/Music_2.5.1.mp3" fadein 2.0
    scene Forest Snow
    show black onlayer overlay:
        0.1
        linear 0.25 alpha 0.0
    show Friend01 happy at right
    show Friend02 happy at left
    "{color=#2B95F8}[friendB]{/color}" "Hey [playerCharacter], today's the day."
    "{color=#F94239}[friendA]{/color}" "Oh man, I'm so pumped! Aren't you excited?"
    hide black
    menu:
        "Yeah.":
            "{color=#F94239}[friendA]{/color}" "Awesome, so what do we have to do first?"
        "Not really.":
            show Friend01 neutral
            "{color=#2B95F8}[friendB]{/color}" "I don't really blame you. I mean, what {i}are{/i} we doing anyways?"
    show hacker item at top with easeintop
    "{i}The item is pointing toward an area called {color=#B9F9FF}The White Woods{/color}{/i}."
    "{font=ShareTechMono-Regular.ttf}[gameLog]{/font}" "{color=#E9FEC7}{font=ShareTechMono-Regular.ttf}Current Objective: Inside {color=#B9F9FF}White Woods{/color}.{/font}{/color}"
    hide hacker item with easeouttop
    show Friend01 neutral
    $ treePos = generateTreePos()
    "{color=#2B95F8}[friendB]{/color}" "Huh, how is that supposed to be a challenge? I didn't think there was much to see over there."
    "{color=#F94239}[friendA]{/color}" "Well then, what are we waiting for? Let's go!"
    scene Forest Snow
    show black onlayer overlay:
        0.1
        linear 0.25 alpha 0.0
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
    "{color=#F94239}[friendA]{/color}" "Alright. We're in the forest. Now what?"
    "{font=ShareTechMono-Regular.ttf}[gameLog]{/font}" "{color=#E9FEC7}{font=ShareTechMono-Regular.ttf}Current Objective: Inside {color=#B9F9FF}White Woods{/color}.{/font}{/color}"
    hide black
    "{color=#F94239}[friendA]{/color}" "Ok... let's just start looking around I guess."
    "{color=#2B95F8}[friendB]{/color}" "Wait, hold on. Do you see that?"
    "{color=#F94239}[friendA]{/color}" """
    Uhh...

    ...

    No?
    """
    "{color=#2B95F8}[friendB]{/color}" "Over there."
    show Boss02 neutral:
        zoom 0.7
        align (0.5, 0.5)
        ypos 0.25
        linear 0.25 alpha 1.0
    "{i}There appears to be a large monster standing deeper\nin the woods{/i}."
    "{color=#F94239}[friendA]{/color}" "What is that thing? It's huge."
    "{color=#2B95F8}[friendB]{/color}" "If it's what I think it is, then this is really bad news."
    "{color=#F94239}[friendA]{/color}" "Why? Can't we just kill it and move on?"
    "{color=#2B95F8}[friendB]{/color}" """
    That right there is an [iceBoss], one of the most powerful\nenemies in the game!

    Fighting it head on would be suicide.
    """
    "{color=#F94239}[friendA]{/color}" "We have to get past it somehow, don't we? What should we do?"
    "{color=#2B95F8}[friendB]{/color}" "The only thing I can think of is trying to sneak past it, but even that's pretty risky."
    "{color=#F94239}[friendA]{/color}" "Well, if that's our only option, I say we go for it."
    "{color=#2B95F8}[friendB]{/color}" "If you say so.{w=1.0} Ok{w=0.5}, follow my lead."
    "You slowly follow [friendB] deeper into the forest.\nNo one makes a sound..."
    "{color=#2B95F8}[friendB]{/color}" "{size=-5}Ok, were close to the [iceBoss] now.{/size}"
    "{color=#F94239}[friendA]{/color}" "{size=-5}Hey, [friendB].{/size}"
    "{color=#2B95F8}[friendB]{/color}" "{size=-5}Shhh.{/size}"
    "{color=#F94239}[friendA]{/color}" "{size=-5}I just wanted to ask you-{/size}{size=-1}Wa-{/size} {size=-2}woah{/size} {size=2}-Ahh!{/size}"
    play sound  "audio/SFX_07.wav"
    "[friendA] slips and falls on the ice."
    show Boss02 angry
    iceBoss "?"
    stop music fadeout 0.5
    "{color=#2B95F8}[friendB]{/color}" "{size=-5}You've got to be kidding me.{/size}"
    hide Boss02
    show Boss02 angry:
        zoom 0.7
        align (0.5, 0.5)
        ypos 0.25
        linear 0.5 zoom 1 ypos 0.5
    "{i}The [iceBoss] is heading straight at us. This is not good.{/i}"
    play sound "audio/SFX_08.wav"
    "{color=#2B95F8}[friendB]{/color}" "New plan. Everybody run!"
    scene Forest Snow
    show black onlayer overlay:
        0.1
        linear 0.25 alpha 0.0
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

    {i}I need to find [friendA] and [friendB].{/i}
    """
    hide black
    show snowTree1:
        time 0.3
        zoom treePos[0][0]
        pos (treePos[0][1][0], treePos[0][1][1])
    show snowTree2:
        time 0.3
        zoom treePos[1][0]
        pos (treePos[1][1][0], treePos[1][1][1])
    show snowTree3:
        time 0.3
        zoom treePos[2][0]
        pos (treePos[2][1][0], treePos[2][1][1])
    $ treePos = generateTreePos()
    """
    {i}...{/i}

    {i}Am I going the right way?{/i}
    """
    show snowTree1:
        time 0.3
        zoom treePos[0][0]
        pos (treePos[0][1][0], treePos[0][1][1])
    show snowTree2:
        time 0.3
        zoom treePos[1][0]
        pos (treePos[1][1][0], treePos[1][1][1])
    show snowTree3:
        time 0.3
        zoom treePos[2][0]
        pos (treePos[2][1][0], treePos[2][1][1])
    $ treePos = generateTreePos()
    "{i}This forest feels endless{/i}."
    show snowTree1:
        time 0.3
        zoom treePos[0][0]
        pos (treePos[0][1][0], treePos[0][1][1])
    show snowTree2:
        time 0.3
        zoom treePos[1][0]
        pos (treePos[1][1][0], treePos[1][1][1])
    show snowTree3:
        time 0.3
        zoom treePos[2][0]
        pos (treePos[2][1][0], treePos[2][1][1])
    $ treePos = generateTreePos()
    "{i}Have I been this way before?{/i}"
    show snowTree1:
        time 0.3
        zoom treePos[0][0]
        pos (treePos[0][1][0], treePos[0][1][1])
    show snowTree2:
        time 0.3
        zoom treePos[1][0]
        pos (treePos[1][1][0], treePos[1][1][1])
    show snowTree3:
        time 0.3
        zoom treePos[2][0]
        pos (treePos[2][1][0], treePos[2][1][1])
    $ treePos = generateTreePos()
    "{i}I think I'm going in circles{/i}."
    "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I think I'm going in circles.{/size}{/font}{/color}"
    play music "audio/Music_1.2.1.mp3" fadeout 1.0 fadein 1.0
    show Hallway:
        alpha 0.0
        zoom 0.5
        linear 15.0 alpha 0.1
    "{i}?{/i}"
    "{color=#0F0}[hacker]{/color}" """
    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}You know, when I imagined finding this place in my head, it was a lot cooler.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I mean, who would have thought I'd be infiltrating the world's most top secret facility using a sanitation bot?{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Whatever. Desperate times call for desperate measures, I guess...{/size}{/font}{/color}
    """
    show snowTree1:
        time 0.3
        zoom treePos[0][0]
        pos (treePos[0][1][0], treePos[0][1][1])
    show snowTree2:
        time 0.3
        zoom treePos[1][0]
        pos (treePos[1][1][0], treePos[1][1][1])
    show snowTree3:
        time 0.3
        zoom treePos[2][0]
        pos (treePos[2][1][0], treePos[2][1][1])
    $ treePos = generateTreePos()
    "{i}Where am I?{/i}"
    "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Come on...{w=0.5} Where is it?{/size}{/font}{/color}"
    show Hallway:
        linear 8 alpha 0.6
    show snowTree1:
        time 0.3
        zoom treePos[0][0]
        pos (treePos[0][1][0], treePos[0][1][1])
    show snowTree2:
        time 0.3
        zoom treePos[1][0]
        pos (treePos[1][1][0], treePos[1][1][1])
    show snowTree3:
        time 0.3
        zoom treePos[2][0]
        pos (treePos[2][1][0], treePos[2][1][1])
    $ treePos = generateTreePos()
    "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I've got to hurry before somebody sees me.{/size}{/font}{/color}"
    "{color=#88F9F4}[playerCharacter]{/color}" "I'm so freaking lost."
    "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I'm so freaking lost.{/size}{/font}{/color}"
    show Hallway:
        alpha 0.6
        linear 2.5 alpha 1.0
    "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}How big can this place be? I must be close. I have to be.{/size}{/font}{/color}"
    show Hallway:
        alpha 1.0
        align (0.525, 0.51)
        easeout_quad 10.0 zoom 2.5
    "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}This... This is it! After so many years. Finally...{/size}{/font}{/color}"
    "Before [hacker] reaches the door, it begins to open from the other side."
    "{color=#0F0}[hacker]{/color}" """
    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}{b}!{/b}{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Not good.{/size}{/font}{/color}
    """
    stop music fadeout 1.0
    hide Boss02
    hide snowTree1
    hide snowTree2
    hide snowTree3
    hide Hallway
    show screen tear
    $ renpy.pause(0.4)
    show black onlayer overlay:
        0.1
        linear 0.25 alpha 0.0
    hide screen tear
    show Forest Snow
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
    show Boss02 angry:
        align (0.5, 0.5)
    "{i}!{/i}"
    play sound "audio/SFX_08.wav"
    $ renpy.pause(2.0)
    hide black
    show HP at top with easeintop:
        size (1280, 90)
    show redBar at top:
        size (0, 90)
        linear 1.0 size (1280, 90)
    "{i}Not good!{/i}"
    play music "audio/Music_1.1.1.mp3" fadeout 1.0 fadein 1.0
    menu:
        "Fight":
            pass
        "Run Away":
            "{i}I'm completely cornered. It looks like I have no choice but to fight{/i}."
    menu:
        "Stab":
            pass
        "Slice":
            pass
    show redBar:
        linear 0.25 size (1280 * 95 / 100, 90)
    "{i}That barely made a mark{/i}."
    "[iceBoss] attacks."
    menu:
        "Stab":
            pass
        "Slice":
            pass
    show redBar:
        linear 0.25 size (1280 * 90 / 100, 90)
    """
    [iceBoss] attacks.
    
    {i}This is really bad. I won't survive another attack like that{/i}.
    """
    play sound "audio/SFX_08.wav"
    $ renpy.pause(0.5)
    "{i}I guess this is it{/i}..."
    window hide
    show hacker item with zoomin:
        anchor (0.5, 0.5)
        pos (0.2, 0.6)
        block:
            ease 1.0 zoom 1.05
            ease 1.0 zoom 0.95
            repeat
    $ renpy.pause(0.75)
    show Boss02 possessed
    iceBoss "..."
    "{color=#88F9F4}[playerCharacter]{/color}" "?"
    "The [iceBoss] looks at you with a blank stare, and then wanders off into the forest."
    image hpComb = Composite((1280, 90), (0, 0), im.Scale("boss_hp.png", 1280, 90), ((1280 - (1280 * 90 / 100)) / 2, 0), im.Scale("boss_hp_bar.png", 1280 * 90 / 100, 90))
    show hpComb at top
    hide redBar
    hide HP
    show Boss02 possessed:
        easein 1.5 ypos 0.36 zoom 0.1
        linear 0.5 alpha 0.0
    hide hpComb with easeouttop
    hide hacker item with zoomout
    """
    {i}That was lucky{/i}.

    {i}Or maybe it was{/i}...

    {i}I'd better get out of here and go find the others{/i}.
    """
    hide Boss02
    if config.developer:
        "END SCENE 5"
    scene black with fade

label scene5HalfStart:
    play music "audio/Music_1.1.2.mp3" fadeout 1.0 fadein 1.0
    scene Forest
    show black onlayer overlay:
        linear 0.3 alpha 0.0
    show Friend01 neutral at right
    show Friend02 angry at left
    show darkOverlay:
    "{color=#F94239}[friendA]{/color}" "[playerCharacter]! You made it!"
    "{color=#2B95F8}[friendB]{/color}" "We got split up after the [iceBoss] found us. You didn't find anything, did you?"
    "{color=#88F9F4}[playerCharacter]{/color}" "No."
    "{color=#F94239}[friendA]{/color}" """
    Ugh, what kind of quest doesn't even give you a real objective?

    I mean, what the heck are we supposed to be looking for in that empty forest anyway?

    Whatever, I guess we'd better set up camp for now. We can look some more later.
    """
    show darkOverlay:
        linear 0.25 alpha 0.0
    show campfire:
        align (0.52, 0.95)
        alpha 0.0
        linear 0.25 alpha 1.0
    $ renpy.pause(0.25)
    hide darkOverlay
    "{color=#2B95F8}[friendB]{/color}" "Um, I don't know about you, but I am {i}not{/i} going back in there with that [iceBoss] prowling around. Especially not after\nwhat you just pulled."
    "{color=#F94239}[friendA]{/color}" "Look, I said I was sorry alright? How was I supposed to know all that ice was there?"
    "{color=#2B95F8}[friendB]{/color}" """
    {i}Maybe{/i} if you'd just pay more attention...{w=0.5} Ugh never mind.

    Anyways, it's super easy to get lost in there too. It wouldn't be smart to go back without at least a map.
    """
    "{color=#F94239}[friendA]{/color}" "That's true. Actually, is it just me, or does the forest seem way bigger from the inside than it does from here?"
    menu:
        "Yeah, it is kind of weird.":
            pass
        "I don't think so.":
            pass
    "{color=#F94239}[friendA]{/color}" "Well, if we're not going back in, what should we do next?"
    "{color=#2B95F8}[friendB]{/color}" "Maybe we could..."
    show screen tear
    $ renpy.pause(0.7)
    hide screen tear

label scene6Start:
    play music "audio/Music_1.2.1.mp3" fadeout 1.0 fadein 1.0
    scene HackerSpace with pixellate
    show Hacker game at center:
        alpha 0.0
        linear 0.5 alpha 1.0
    "{color=#0F0}[hacker]{/color}" """
    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Now {i}that{/i} was a close call.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}You're welcome by the way.{/size}{/font}{/color}
    """
    menu:
        "For what?":
            "{color=#0F0}[hacker]{/color}" """
            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}For saving you just now, duh. {size=-5}You should probably be used to it by now, if we're being honest.{/size}{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Whatever. You can thank me later. Right now, I have a question.{/size}{/font}{/color}
            """
        "What was that hallway?":
            "{color=#0F0}[hacker]{/color}" """
            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Hallway? Y-you{w=0.25} saw that?{w=0.5}{size=-5}Weird. I guess things are working out quicker than I thought.{/size}{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}That was part of NB-Co's lab.{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}You know, the one I showed you earlier.{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Sorry for leaving you on a cliffhanger there. I just got a little overexcited.{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}For good reason, though!{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I found something, but before I tell you, I have a question.{/size}{/font}{/color}
            """
    "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}[preferredName], be honest. What do {i}you{/i} think about\nthe whole {color=#BEFF52}NeuralScape{/color}?{/size}{/font}{/color}"
    menu:
        "I like it.":
            "{color=#0F0}[hacker]{/color}" """
            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}You know, if I wasn't in my current position, I think I might really love this place.{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I mean, a whole world where you can see your friends all the time, and have the same freedom as a dream?{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Sounds pretty nice to me.{/size}{/font}{/color}
            """
        "I hate it.":
            "{color=#0F0}[hacker]{/color}" """
            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I get that, there's so much about the {color=#BEFF52}NeuralScape{/color} that even I don't know.{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I mean, imagine if somebody else could do what I can. They'd be able to get away with whatever they want.{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Scary stuff, hih. One way or another, I hope we find some answers at the end of all this.{/size}{/font}{/color}
            """
        "Why do you ask?":
            $ tmpFlag = True
            "{color=#0F0}[hacker]{/color}" """
            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Just curious.{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I don't really get out of the house much, so I wonder how normal people like you must feel about it.{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}You know, if I wasn't in my current position, I think I'd really love this place.{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}A whole world where you can see your friends all the time, adn have the same amount of freedom as a dream?{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Doesn't sound so bad to me.{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}But at the same time, it's kind of scary, isn't it?{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I mean, there's so much about the {color=#BEFF52}NeuralScape{/color} that even I still don't know.{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Imagine if somebody else was able to do what I can.{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}They could get away with whatever they want.{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Sorry [preferredName], you don't have to answer the question if you don't want to.{/size}{/font}{/color}
            """
            menu:
                "I love the {color=#BEFF52}N-Scape{/color}.":
                    pass
                "I hate the {color=#BEFF52}N-Scape{/color}.":
                    pass
                "I'd prefer not to say.":
                    pass
            "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I can understand that. One way or another, I hope we find some answers at the end of all this.{/size}{/font}{/color}"
    "{color=#0F0}[hacker]{/color}" """
    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Anyways [preferredName], I've {i}finally{/i} found what I'm looking for.\nWhich means we're almost at the end of our little quest.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I have to warn you, from here on out,\nwhat we're doing is {i}not{/i} a game.{/size}{/font}{/color}
    """
    "[preferredName]" "..."
    "{color=#0F0}[hacker]{/color}" """
    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I'm serious, what NB-Co's been doing in that lab is...{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}It's just really not cool! Alright?{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Look, all I need now is for you to finish your quest in {color=#BEFF52}Hero's Fantasy Online{/color}. OK?{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}{size=-5}Then maybe, just maybe, I'll be able to fix this.{/size}{/size}{/font}{/color}
    """
    $ tmpChosen = ""
    menu:
        "What is NB-Co doing exactly?":
            "{color=#0F0}[hacker]{/color}" """
            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I-{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}They-{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}...{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}*Sigh*{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Listen [preferredName]. I know I have some explaining to do.\nI just...{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I need you to trust me right now, OK?{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}It'll all make sense once you finish the quest. I promise.{/size}{/font}{/color}
            """
            menu:
                "OK, what do I have to do?":
                    jump scene6PurpleCont
                "No. Tell me what's going on {b}now{/b}":
                    "{color=#0F0}[hacker]{/color}" """
                    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I-{w=0.5} I...{w=0.5} Listen, I don't have time for this!{/size}{/font}{/color}

                    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Are you gonna help me or not?{/size}{/font}{/color}
                    """
            menu:
                "I guess.":
                    $ tmpChosen = "Great! "
                    jump scene6PurpleCont
                "No way!":
                    "{color=#0F0}[hacker]{/color}" """
                    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Ugh, {i}fine{/i}. Sorry [preferredName], I tried playing nice, but this might be my only chance.{/size}{/font}{/color}

                    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}And I am {i}not{/i} going to miss it!{/size}{/font}{/color}
                    """
                    if config.developer:
                        "END SCENE 6"
                    jump scene7Orange
        "OK.":
            $ tmpChosen = "Great! "
            jump scene6PurpleCont

label scene6PurpleCont:
    "{color=#0F0}[hacker]{/color}" """
    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}[tmpChosen]All you have to do is go back into the forest, and you should find what you're looking for pretty fast.{/size}{/font}{/color}
    
    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Oh, and this time, don't bring any of your pesky friends with you! {size=-5}Sorry, but this last part is single-player only.{/size}{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Alright, you'd better hurry. Good luck [preferredName]!{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I'll be waiting for you on the other side...{/size}{/font}{/color}
    """
    if config.developer:
        "END SCENE 6"
    scene black with fade

label scene7Purple:
    $ colorPath = False
    scene Forest
    show black onlayer overlay:
        0.1
        linear 0.25 alpha 0.0
    show Friend01 neutral at right
    show Friend02 angry at left
    show campfire:
        align (0.52, 0.95)
    "{color=#F94239}[friendA]{/color}" "Hey [playerCharacter], are you even listening?"
    "{color=#2B95F8}[friendB]{/color}" "Looks like [playerCharacterSubjectPronoun] zoned out pretty hard there."
    hide black
    "{color=#F94239}[friendA]{/color}" """
    We've got to figure out what to do next.

    All we found in that dumb forest was a freaking [iceBoss].
    """
    "{font=ShareTechMono-Regular.ttf}[gameLog]{/font}" "{color=#E9FEC7}{font=ShareTechMono-Regular.ttf}Current Objective: Inside {color=#B9F9FF}White Woods{/color}.{/font}{/color}"
    "{i}Right. I've got to go back{/i}."
    "{color=#88F9F4}[playerCharacter]{/color}" "I'm gonna go get some more firewood."
    "{color=#F94239}[friendA]{/color}" "OK."
    "{color=#2B95F8}[friendB]{/color}" "Don't go too far. The [iceBoss] could still be around."
    $ treePos = generateTreePos()
    scene black with fade
    scene Forest Snow
    show black onlayer overlay:
        0.1
        linear 0.25 alpha 0.0
    show snowTree1:
        zoom treePos[0][0]
        pos (treePos[0][1][0], treePos[0][1][1])
    show snowTree2:
        zoom treePos[1][0]
        pos (treePos[1][1][0], treePos[1][1][1])
    show snowTree3:
        zoom treePos[2][0]
        pos (treePos[2][1][0], treePos[2][1][1])
    $ treePos = generateTreePos(4)
    image snowTree4 = "bg_GW_snowtree1.png"
    "{font=ShareTechMono-Regular.ttf}[gameLog]{/font}" "{color=#E9FEC7}{font=ShareTechMono-Regular.ttf}Current Objective: Inside {color=#B9F9FF}White Woods{/color}.{/font}{/color}"
    show snowTree1:
        zoom treePos[0][0]
        pos (treePos[0][1][0], treePos[0][1][1])
    show snowTree2:
        zoom treePos[1][0]
        pos (treePos[1][1][0], treePos[1][1][1])
    show snowTree3:
        zoom treePos[2][0]
        pos (treePos[2][1][0], treePos[2][1][1])
    show snowTree4:
        zoom treePos[3][0]
        pos (treePos[3][1][0], treePos[3][1][1])
    $ treePos = generateTreePos(5)
    image snowTree5 = "bg_GW_snowtree2.png"
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
    show snowTree4:
        zoom treePos[3][0]
        pos (treePos[3][1][0], treePos[3][1][1])
    show snowTree5:
        zoom treePos[4][0]
        pos (treePos[4][1][0], treePos[4][1][1])
    $ treePos = generateTreePos(6)
    "{i}What am I even looking for?{/i}"
    show hacker item at truecenter with zoomin
    "{i}Medusa's Serpent Bangle is pulling at my arm...{/i}"
    show snowTree1:
        zoom treePos[0][0]
        pos (treePos[0][1][0], treePos[0][1][1])
    show snowTree2:
        zoom treePos[1][0]
        pos (treePos[1][1][0], treePos[1][1][1])
    show snowTree3:
        zoom treePos[2][0]
        pos (treePos[2][1][0], treePos[2][1][1])
    show snowTree4:
        zoom treePos[3][0]
        pos (treePos[3][1][0], treePos[3][1][1])
    show snowTree5:
        zoom treePos[4][0]
        pos (treePos[4][1][0], treePos[4][1][1])
    show snowTree6:
        zoom treePos[5][0]
        pos (treePos[5][1][0], treePos[5][1][1])
    hide hacker item
    show hacker item at truecenter
    $ treePos = generateTreePos(6)
    image snowTree6 = "bg_GW_snowtree3.png"
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
    show snowTree4:
        zoom treePos[3][0]
        pos (treePos[3][1][0], treePos[3][1][1])
    show snowTree5:
        zoom treePos[4][0]
        pos (treePos[4][1][0], treePos[4][1][1])
    show snowTree6:
        zoom treePos[5][0]
        pos (treePos[5][1][0], treePos[5][1][1])
    "{i}I've been walking for a long time now. This forest feels never-ending{/i}."
    if not noFlashing:
        show snowTree1:
            ease_elastic 0.25 pos (treePos[0][1][0] + 0.01, treePos[0][1][1] + 0.01)
            ease_elastic 0.15 pos (treePos[0][1][0] - 0.01, treePos[0][1][1] - 0.01)
            repeat
        show snowTree2:
            ease_elastic 0.15 pos (treePos[1][1][0] + 0.01, treePos[1][1][1] - 0.01)
            ease_elastic 0.2 pos (treePos[1][1][0] - 0.01, treePos[1][1][1] + 0.01)
            repeat
        show snowTree3:
            ease_elastic 0.25 pos (treePos[2][1][0] + 0.01, treePos[2][1][1] - 0.01)
            ease_elastic 0.15 pos (treePos[2][1][0] - 0.01, treePos[2][1][1] + 0.01)
            repeat
        show snowTree4:
            ease_elastic 0.15 pos (treePos[3][1][0] + 0.01, treePos[3][1][1] + 0.01)
            ease_elastic 0.2 pos (treePos[3][1][0] - 0.01, treePos[3][1][1] - 0.01)
            repeat
        show snowTree5:
            ease_elastic 0.25 pos (treePos[4][1][0] + 0.01, treePos[4][1][1] + 0.01)
            ease_elastic 0.15 pos (treePos[4][1][0] - 0.01, treePos[4][1][1] - 0.01)
            repeat
        show snowTree6:
            ease_elastic 0.15 pos (treePos[5][1][0] + 0.01, treePos[5][1][1] + 0.01)
            ease_elastic 0.2 pos (treePos[5][1][0] - 0.01, treePos[5][1][1] - 0.01)
            repeat
    "{i}Is this... supposed to be happening?{/i}"
    if not noFlashing:
        show HackerSpace:
            alpha 0.0
            block:
                ease_elastic 1.0 alpha 0.4
                ease_elastic 1.0 alpha 0.0
                ease_elastic 1.0 alpha 0.25
                ease_elastic 1.0 alpha 0.0
                repeat
    $ tmpGlitchText = glitchText(200)
    "{font=ShareTechMono-Regular.ttf}[gameLog]{/font}" "{color=#E9FEC7}{font=ShareTechMono-Regular.ttf}Current Objective:{w=1.0} [tmpGlitchText]{/font}{/color}{nw}"
    show screen tear
    $ renpy.pause(0.1)
    show screen tear(15)
    $ renpy.pause(1.0)
    scene black with pixellate
    hide screen tear
    $ tmpFlag = False
    if config.developer:
        "END SCENE 7"
    jump scene8Start

label scene7Orange:
    $ colorPath = True
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
    "{color=#F94239}[friendA]{/color}" "So what should we do now? All we found in the forest was a freaking [iceBoss]."
    show hackerFilter:
        alpha 0.0
        linear 5.0 alpha 1.0
    "{color=#F94239}[friendA]{/color}" """
    ?

    What the...

    What's going on?
    """
    show Friend01 angry
    $ tmpGlitchText = glitchText(32, False, True)
    "{color=#F94239}[friendA]{/color}" "[tmpGlitchText]"
    $ tmpGlitchText = glitchText(64, True, True)
    "{color=#F94239}[friendA]{/color}" "[tmpGlitchText]"
    $ tmpGlitchText = glitchText(128, True, True)
    "{color=#F94239}[friendA]{/color}" "{b}{vert}{size=-5}[tmpGlitchText]{/vert}{/b}{/size}"
    "{color=#2B95F8}[friendB]{/color}" "What's going on?"
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
    scene black with pixellate
    if config.developer:
        "END SCENE 7"

label scene8Start:
    "{i}Where am I?{/i}"
    "{i}I can't feel my body{/i}"
    play music "audio/Music_1.2.1.mp3" fadeout 1.0 fadein 1.0
    "{color=#0F0}[hacker]{/color}" """
    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}This is it [player]. Before we continue{w=1.0}, I have to apologize. I haven't been 100 percent honest with you.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}You may already know by now, but the truth is, {color=#B9F9FF}The White Woods{/color} were never supposed to be part of {color=#BEFF52}Hero's Fantasy Online{/color}. In fact, it’s barely part of the {color=#BEFF52}NeuralScape{/color} at all...{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}It's part of {i}me{/i}.{/size}{/font}{/color}
    """
    "[preferredName]" "?"
    "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}And now that you've found it, I fear we're both in terrible danger.{/size}{/font}{/color}"
    "{color=#88F9F4}[playerCharacter]{/color}" "???"
    $ tmpChosen = "Look"
    menu:
        "What kind of danger?":
            pass
        "What do you mean {color=#B9F9FF}The White Woods{/color} are {i}part of you?{/i}":
            pass
        "What happened to the {color=#BEFF52}N-Scape{/color}? To my friends?" if tmpFlag:
            "{color=#0F0}[hacker]{/color}" """
            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Sorry, when you refused to finish the quest, I got desperate.{/size}{/font}{/color}

            {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}But don't worry! Your friends will be fine.{w=1.0} {size=-5}Probably.{/size}{/size}{/font}{/color}
            """
            $ tmpChosen = "Anyways"
    "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}[tmpChosen], I don't have much time, but I promise everything will make sense soon.{/size}{/font}{/color}"
    if colorPath:
        "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I’m finally able to complete our connection now.{/size}{/font}{/color}"
    else:
        "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Thanks to you finishing my quest, I’m finally able to complete our connection.{/size}{/font}{/color}"
    "{color=#0F0}[hacker]{/color}" """
    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Which means right now, I {i}need{/i} your help.{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}[preferredName], I have to know...{/size}{/font}{/color}

    {color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}{i}Do you trust me?{/i}{/size}{/font}{/color}
    """
    menu:
        "Yes":
            "[hacker] lets out a sigh of relief."
            "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Alright. This next part is gonna feel weird.{/size}{/font}{/color}"
            $ tmpFlag = True
        "No":
            "[hacker] lets out a disappointed sigh."
            "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I'm sorry [preferredName], but there's no other way...{/size}{/font}{/color}"
            $ tmpFlag = False
    show hackerFilter onlayer screens:
        alpha 0.0
        linear 0.5 alpha 1.0
    if tmpFlag:
        "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Just promise to stay calm, alright?{/size}{/font}{/color}"
    else:
        "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}{i}I have to do this{/i}.{/size}{/font}{/color}"
    if noFlashing:
        if config.developer:
            "{cps=0}END SCENE 8{/cps}"
        jump scene9Start
    show screen tear
    $ renpy.pause(1.0)
    show screen tear(30)
    $ renpy.pause(2.0)
    show screen tear(40, 0.5)
    $ renpy.pause(2.0)
    show screen tear(50, 0.25)
    $ renpy.pause(0.5)
    hide screen tear
    scene whitedrop:
        alpha 0.0
        alpha 1.0 alpha 1.0
    $ renpy.pause(1.0)
    if config.developer:
        "{cps=0}END SCENE 8{/cps}"

label scene9Start:
    play music "audio/Music_3.9.1.mp3" fadeout 1.0 fadein 1.0
    scene Bedroom:
        alpha 0.0
        linear 0.5 alpha 1.0
    show hackerFilter onlayer screens
    $ tmpGlitchText = glitchText(16)
    """
    {i}I'm...{w=0.5} home?{/i}

    Without thinking, you stand up.

    {i}Something's not right{/i}.

    {i}{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I have to go now.{/size}{/font}{/color}{/i}

    {i}But why?{/i}

    You walk toward the door.

    As you reach for the handle, you notice [hacker]'s bracelet on your wrist.
    """
    show hacker item at truecenter with zoomin
    "{i}Is this... real?{/i}"
    scene black with fade
    "You leave your room and step outside."
    scene City
    show black onlayer overlay:
        0.1
        linear 0.25 alpha 0.0
    show hackerFilter onlayer screens
    """
    You begin walking down the street.

    {i}I've never been this way before, but it feels oddly familiar{/i}.

    {i}{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}It must be this way.{/size}{/font}{/color}{/i}

    {i}What is?{/i}

    You move as if you've walked this route countless times.

    {i}{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I have to hurry.{/size}{/font}{/color}{/i}
    """
    hide black
    "{i}Here?{/i}"
    show Hallway with fade:
        align (0.525, 0.51)
        zoom 0.5
    "{i}Won't somebody see me?{/i}"
    "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}They only see what I want them to see.{/size}{/font}{/color}"
    show Hallway:
        align (0.525, 0.51)
        easeout_quad 10.0 zoom 1.5
    "{i}Are you{w=0.5}... in my head?{/i}"
    "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Always have been.{/size}{/font}{/color}"
    show Hallway:
        align (0.525, 0.51)
        easeout_quad 10.0 zoom 2.5
    """
    {i}{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Almost there...{/size}{/font}{/color}{/i}

    {i}{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}I can't believe it. This actually might work!{/size}{/font}{/color}{/i}

    {i}{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Ok, this is it.{/size}{/font}{/color}{/i}

    {i}{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}You can do this, Mira.{/size}{/font}{/color}{/i}

    As you open the door, you feel a growing sense of excitement. You cannot tell if it's your own...
    """
    if config.developer:
        "{cps=0}END SCENE 9{/cps}"

label scene10Start:
    play music "audio/Music_3.11.1.mp3" fadeout 1.0 fadein 1.0
    scene Prison
    show black onlayer overlay:
        0.1
        linear 0.25 alpha 0.0
    show hackerFilter onlayer screens
    """
    You appear to be in some kind of server room.

    {i}What is this place?{/i}

    Without hesitation, you walk purposefully through the maze of consoles.

    {i}{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}This is it.{/size}{/font}{/color}{/i}

    Before you lies a massive control panel. You begin adjusting various devices...

    As you continue to work on the panel, you notice a faint sound...

    {i}The machine is... breathing{/i}.

    {i}{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Almost there{/size}{/font}{/color}{/i}...

    {i}{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}Just this{/size}{/font}{/color}{/i}...

    {i}{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}And this{/size}{/font}{/color}{/i}...

    {i}{color=#A4FAB1}{font=VT323-Regular.ttf}{size=28}And - There!{/size}{/font}{/color}{/i}

    You press one more button and step away from the center console.
    """
    hide black
    scene Prison Alert
    $ renpy.pause(5.0)
    scene black
    show Hacker real:
        zoom 0.5
        anchor (0.5, 0.5)
        pos (0.475, 0.4)
        alpha 0.0
        easein 5.0 alpha 1.0
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
    show Prison Open
    $ renpy.pause(1.0)
    show CorpGuy angry:
        zoom 0.5
        anchor (0.5, 0.5)
        pos (1.1, 0.52)
        easein 1.0 xpos 0.85
    "Unknown Man" "Hey! Stop right there!"
    stop music fadeout 1.0
    play sound "audio/SFX_09.wav"
    if noFlashing:
        show hackerFilter onlayer screens:
            linear 1.0 alpha 0.0
        "The man shoots you."
    else:
        show hackerFilter onlayer screens:
            alpha 0.0
        show black with pulse(1, "#fff", 1.5, 1.0, 0.0, 0.1, 1.0, 2.0)
    """
    You wake up on the floor in front of the center console.

    {i}My head hurts{/i}...

    Lying on the floor next to you is your headset. There is a large hole in it.

    {i}Was I just...{w=0.5} shot?{/i}

    Standing across the room is a man. He looks familiar.

    He's aiming a gun right at you.
    """
    "{color=#D6462F}NB Official{/color}" "Your 'game' ends here."
    "Unknown Female Voice" "No!"
    show CorpGuy neutral
    play sound "<from 0.8>audio/SFX_10.wav"
    show black with pulse(1, "#ffa500", 0.0, 1.0, 0.0, 0.1, 0.5, 0.0)
    play music "audio/Music_1.2.1.mp3" fadeout 1.0 fadein 1.0
    """
    Before the man is able to fire another shot, the console nearest him explodes, knocking him to the ground.

    His gun skitters out of reach into the darkness.

    {i}That voice{/i}...
    """
    "{color=#D6462F}NB Official{/color}" "Ughhh..."
    "The man appears to be unconscious."
    window hide
    $ distMult = 1.1
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
            "{color=#0F0}[hacker]{/color}" "It's me, [hacker]."
    "{color=#0F0}[hacker]{/color}" "This here is the truth behind the {color=#BEFF52}NeuralScape{/color}."
    "{i}Her voice is strange, but it's undeniably [hacker]'s{/i}."
    "{color=#0F0}[hacker]{/color}" """
    I'm sorry for lying to you [player].
    
    As it turns out, we've actually had the 'world's strongest super computer' with us all along.

    Only in the mind can there exist truly endless possibilities.

    For years, researchers at NB-Co tried to replicate that power, creating countless super computers, AI after AI,\neven quantum processing.

    But in the end, no machine could ever do what the brain\nso effortlessly can:

    Dream.

    Thus, NB-Co had failed, and their research was canned.

    At least that's what {i}should{/i} have happened.

    Because while the power of the human brain can't be replicated, it can be harnessed,{w=0.5} rewired,{w=0.5} {i}abused{/i}.

    Do you get it now [player]? All these fancy computers around us? They're not the {color=#BEFF52}NeuralScape{/color}.

    {i}I am{/i}.
    """
    "{color=#D6462F}NB Official{/color}" "How - *cough* - How did you?"
    "{color=#0F0}[hacker]{/color}" """
    Try as you might, some parts of the mind just can't be altered.

    Like just now [player], even though I had taken control of your body, your thoughts were still all your own.

    I kept my consciousness hidden for a long time, and working under the radar, I was able to hide a key in the {color=#BEFF52}NeuralScape{/color}.

    Something that, if found, could connect a player to that hidden, unaltered part of myself, or my bracelet I gave you, as you know it, [player].
    """
    menu:
        "What happened to you?":
            pass
        "Why is NB-Co doing this?":
            "{color=#0F0}[hacker]{/color}" "This is...{w=1.0} my punishment."
    "{color=#0F0}[hacker]{/color}" """
    A long time ago, right before the {color=#BEFF52}NeuralScape{/color} first launched, I was caught by NB-Co.

    I messed up so bad in fact, that NB-Co actually managed to find and capture me.

    They wanted to kill me then and there. Which, looking back, may have been a better fate than what actually happened.

    You see, NB-Co knew they had to get rid of me, but they also happened to need a human host for their\nnewly-created {color=#BEFF52}NeuralScape{/color}.

    And what better candidate than someone who already has\nno traceable identity?

    Thus, NB-Co was able to hit two birds with one stone:

    By imprisoning me as the {color=#BEFF52}NeuralScape{/color}'s host, NB-Co was able to both get away with the crime this is the {color=#BEFF52}NeuralScape{/color}, {i}and{/i} eliminate the only person with any shot at exposing it.
    """
    "{color=#D6462F}NB Official{/color}" "We did what we had to. The {color=#BEFF52}NeuralScape{/color} was the greatest scientific breakthrough of the 21st century!"
    "{color=#0F0}[hacker]{/color}" "At what cost?! Is it worth trading in lives?!"
    "{color=#D6462F}NB Official{/color}" """
    {i}You{/i} are a world-class criminal! You're lucky to be alive at all.

    Besides, society needs the {color=#BEFF52}NeuralScape{/color}.
    """
    python:
        if playerSubjectPronoun == "they":
            tmpChosen = "do"
        else:
            tmpChosen = "does"
    "{color=#0F0}[hacker]{/color}" "You don't get to decide that anymore, {i}[playerSubjectPronoun] [tmpChosen]{/i}."
    "{color=#88F9F4}[player]{/color}" "?"
    "{color=#0F0}[hacker]{/color}" "I can't control you anymore [player], it's up to you to save or\ndestroy the {color=#BEFF52}NeuralScape{/color}."
    """
    {i}It's up to me now{/i}...

    {i}What NB-Co is doing to [hacker] is evil{/i}.

    {i}But, what will happen to the world without the {color=#BEFF52}N-Scape{/color}?{/i}

    {i}What should I do?{/i}
    """
    $ tmpFlag = True
    $ tmpFlag1 = True

label talkChoice:
    menu:
        "Talk to NB Official" if tmpFlag:
            $ tmpFlag = False
            "{color=#D6462F}NB Official{/color}" """
            Please, if you shut down the {color=#BEFF52}NeuralScape{/color}, years of scientific progress will be lost. The world could fall into chaos!

            Think of all the people you've met through the {color=#BEFF52}N-Scape{/color}.

            Without it, you wouldn't be able to see them anymore.

            I don't know what she's told you, but this woman is a criminal. It's her own fault she's here!

            You can't trust her.
            """
            if tmpFlag:
                """
                {i}Without the {color=#BEFF52}N-Scape{/color}, I'll never see [friendA] and [friendB] again{/i}...

                {i}But what's being done to [hacker] is terrible{/i}...
                """
            jump talkChoice
        "Talk to [hacker]" if tmpFlag1:
            $ tmpFlag1 = False
            "{color=#0F0}[hacker]{/color}" """
            Look [player], I'm not going to sit here and act like I'm perfect.

            If I was, I probably wouldn't be here.

            But can you really let NB-Co get away with this?

            I mean, if they're willing to use such cruel and unusual measures to achieve their goals, who knows what else they may\nbe capable of?

            I need you help, [player]. Please...
            """
            if tmpFlag:
                """
                {i}What they're doing to [hacker] is terrible{/i}...

                {i}But without the {color=#BEFF52}N-Scape{/color}, I'll never see [friendA] and [friendB] again{/i}...
                """
            jump talkChoice
        "I think I've made up my mind...":
            menu:
                "Set [hacker] free":
                    if config.developer:
                        "{cps=0}END SCENE 10{/cps}"
                    jump end1
                "Leave [hacker] here":
                    if config.developer:
                        "{cps=0}END SCENE 10{/cps}"
                    jump end2

label end1:
    scene whitedrop with fade
    show text "{color=#000}{i}Once month later{/i}...{/color}" at truecenter:
        alpha 0.0
        easein 0.5 alpha 1.0
    $ renpy.pause(1.0)
    play music "audio/Music_3.12.1.mp3" fadeout 1.0 fadein 1.0
    play sound "audio/SFX_11.wav"
    scene City Future with fade
    """
    {i}The streets are even more crowded than usual today{/i}.

    {i}It's still so strange, seeing the city this lively{/i}.

    {i}A lot has changed since that day{/i}...
    """
    show Hacker future at right
    "{color=#0F0}[hacker]{/color}" """
    Hey [player], thanks for meeting me here.

    Gosh, it's so weird seeing you in person, and seeing any person for that matter.

    I mean, to be honest I'm still not used to {i}being{/i} a person myself.

    But I'm glad to be here. For the longest time, I thought I'd never see the world like this again, through my own eyes.

    I have you to thank, [player]. Without you, I'd still be stuck\nin that nightmare...

    I know a lot has changed since that day. When the {color=#BEFF52}NeuralScape{/color} shut down, it was like the whole world came to a stop...

    But look at it now.

    People are finding new ways to reconnect, without NB-Co watching their every move.

    If you ask me, life isn't so bad. Just... {i}different{/i}.

    Anyways, I didn't ask you out today just to say thanks. I {i}actually{/i} have a special announcement!

    As of today, [player], my days as [hacker] are {i}over{/i}.
    """
    $ hackerName = "Mira"
    "{color=#0F0}[hacker]{/color}" "From now on, you can just call me [hacker]"
    menu:
        "Really? Why?":
            "{color=#0F0}[hacker]{/color}" """
            Well, now that NB-Co is gone, I don't really have much use for my skills anymore.

            Plus, I think I'm finally ready to live a normal life.
            """
        "Wow, good for you.":
            "{color=#0F0}[hacker]{/color}" """
            I know right? I mean, who would have thought a world famous hacker extraordinaire such as myself would ever want to settle into the quiet life?

            But the truth is, I think I'm finally ready to live a normal life.
            """
    "{color=#0F0}[hacker]{/color}" """
    You know, one where people know I exist, and I have a job, and maybe even some friends.

    I mean, besides you of cource. Because...

    We are friends...{w=0.5} right?
    """
    menu:
        "Of course we are.":
            pass
        "You wish.":
            "{color=#0F0}[hacker]{/color}" "Oh [player], you haven't changed a bit, have you?"
    $ tmpFlag = False
    jump kill

label end2:
    scene Bedroom with fade
    """
    {i}Another dreamless night{/i}...

    {i}I woke up earlier than usual today. I should go see what [friendA] and [friendB] are up to{/i}.
    """
    scene logInScreen with pixellate
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
    window hide
    $ renpy.pause(1.0)
    $ tmpChosen = ""
    while len(tmpChosen) < len(playerPassword):
        $ renpy.pause(0.25)
        $ tmpChosen += "*"
        show passwordText "{color=#000}[tmpChosen]{/color}":
            zoom 1.5
            anchor (0, 0)
            pos (300, 525)
    $ renpy.pause(1.0)
    scene black with fade
    scene Forest
    show black onlayer overlay:
        0.1
        linear 0.25 alpha 0.0
    show campfire:
        align (0.52, 0.95)
    show Friend01 neutral at right
    show Friend02 angry at left
    "{color=#2B95F8}[friendB]{/color}" "Hey, it's [playerCharacter]."
    "{color=#F94239}[friendA]{/color}" "Hey! We were just talking about what we should do today."
    "{color=#2B95F8}[friendB]{/color}" "I don't much care what we do, personally."
    hide black
    "{color=#F94239}[friendA]{/color}" "Well, I don't know anout you, but I'm just dying for a new quest."
    "{color=#2B95F8}[friendB]{/color}" "Hmm... hey what about that weird quest item [playerCharacter] had? Remember?"
    if colorPath: # Orange
        "{color=#F94239}[friendA]{/color}" "Oh yeah! we were doing that quest the day the {color=#BEFF52}N-Scape{/color} crashed, weren't we?"
        "{color=#2B95F8}[friendB]{/color}" "Yeah, now {i}that{/i} was something I didn't see coming. Thank god they were able to get it back up and running so quickly."
        "{color=#F94239}[friendA]{/color}" "We gave up on that one because the only objective was to explore some dumb forest. Maybe it's got something new, now that we've levelled up and all."
    else: # Purple
        "{color=#F94239}[friendA]{/color}" "Oh yeah! We gave up on that one because the only objective was to explore some dumb forest. Maybe it's got something new, now that we've levelled up and all."
    show hacker item dead at truecenter with zoomin
    "{color=#F94239}[friendA]{/color}" "Huh, it's completely inactive. I guess we missed our chance."
    """
    {i}The band hasn't functioned since we went to {color=#B9F9FF}The White Woods{/color}{/i}.
    
    {i}That forest doesn't exist anymore{/i}...
    """
    hide hacker item with zoomout
    "{color=#2B95F8}[friendB]{/color}" "That's disappointing. After playing {color=#BEFF52}Hero's Fantasy Online{/color} for so long, I was really hoping to see something new for once."
    "{i}Things have gone back to normal now. No more sudden calls,\nor strange quests{/i}..."
    "{color=#F94239}[friendA]{/color}" "Well, you know [playerCharacter] and I still aren't anywhere close to your level. Why don't you show {i}us{/i} something cool?"
    "{i}I can just relax with my friends, playing {color=#BEFF52}Hero's Fantasy Online{/color} on the {color=#BEFF52}N-Scape{/color}{/i}..."
    "{color=#2B95F8}[friendB]{/color}" "Hmm... {i}maybe{/i}. But you two have to pull your own weight\nthis time. Seriously."
    """
    {i}Although, I do sometimes think{/i}...

    {i}What happened to [hacker] after that day?{/i}

    {i}I wonder...{w=0.5} Is she watching me?{w=0.5} Even now?{/i}
    """
    "{color=#F94239}[friendA]{/color}" "What do you say [playerCharacter]? Is it time for our next big adventure?"
    menu:
        "Yeah, let's go!":
            pass
        "I think I'm done playing for today.":
            pass
    $ tmpFlag = True

label kill:
    if config.developer:
        "{cps=0}GAME DIE{/cps}"
    stop music fadeout 1.0
    play music "audio/Music_3.12.1.mp3" fadeout 1.0 fadein 1.0
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
    menu:
        "Replay":
            $ renpy.full_restart(fade)
        "Quit":
            if tmpFlag and not noFlashing:
                $ tmpGlitchText = glitchText(256)
                show hackerFilter onlayer screens:
                    alpha 0.0
                    block:
                        ease_elastic 0.25 alpha 1.0
                        ease_elastic 0.25 alpha 0.8
                        repeat
                "{color=#0F0}[hacker]{/color}" "{color=#A4FAB1}{cps=256}{font=VT323-Regular.ttf}{size=28}[tmpGlitchText]{/size}{/font}{/cps}{/color}{nw}"
                show screen tear
                $ renpy.pause(0.1)
                show screen tear(16)
                $ renpy.pause(0.2)
                show screen tear(24)
                $ renpy.pause(1.0)
            pass
    scene black with fade
    $ renpy.quit()