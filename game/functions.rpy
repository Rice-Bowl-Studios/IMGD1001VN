init python:
    import random

    def generateTreePos(nTree=3, minScale=0.5, maxScale=0.7):
        out = []
        partChoices = range(3)
        random.shuffle(partChoices)
        for x in range(nTree):
            # TODO: maybe make scale dependent on y if I have time
            scale = random.random() * (maxScale - minScale) + minScale
            partChoice = partChoices.pop()
            x = min(880.0/1280.0, random.random() * (1.0 / nTree - 0.2) + (float(partChoice) / nTree))
            y = random.random() * 0.2 + 0.1
            out.append([scale, (x, y)])
        return out

    def generateHex(length):
        hexChars = "0123456789ABCDEF"
        out = random.choice(hexChars[1:])
        for x in range(length):
            out += random.choice(hexChars)
        return out

    def glitchText(length, japanese=False, full=False):
        nonunicode_full = "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž"
        nonunicode_kenney_rocket = "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ"
        hiragana = "あいうおえかきくけこなにぬねのはひふへほまみむめもたちつてとさしすせそがぎぐげごばびぶべぼぱぴぷぺぽだぢづでどざじずぜぞわをん"
        katakana = "アイウエオカキクケコナニヌネノハヒフヘホマミムメモタチツテトサシスセソガギグゲゴバビブベボパピプペポダヂヅデドザジズゼゾワヲン"
        kanji = "死火亡煩"
        out = ""
        for x in range(length):
            if japanese:
                tmp = random.randint(0, 4)
                if tmp == 0:
                    out += "{font=bananaslipplus.otf}" + random.choice(hiragana) + "{/font}"
                elif tmp == 1:
                    out += "{font=bananaslipplus.otf}" + random.choice(katakana) + "{/font}"
                elif tmp == 2:
                    out += "{font=bananaslipplus.otf}" + random.choice(kanji) + "{/font}"
                else:
                    if full:
                        out += random.choice(nonunicode_full)
                    else:
                        out += random.choice(nonunicode_kenney_rocket)
            else:
                if full:
                    out += random.choice(nonunicode_full)
                else:
                    out += random.choice(nonunicode_kenney_rocket)
        return out

    def pulse(pulses, color, t0, xt, dt, in_t, out_t, pause_t=0.0):
        print noFlashing
        if noFlashing:
            return None
        out = [False]
        t = t0
        for i in range(pulses):
            out += [Fade(in_t, t, out_t, color=color), False]
            t = t/xt-dt
            if t < 0:
                t = 0
        if pause_t > 0:
            out += [Pause(pause_t), False]
        return MultipleTransition(out)
    
    # Lines 41-94 and 104-108 are taken and modified from a decompiled version of Doki Doki Literature Club
    def screenshot_srf():
        srf = renpy.display.draw.screenshot(None, False)
        return srf

    def hide_windows_enabled(enabled=True):
        global _windows_hidden
        _windows_hidden = not enabled

    class TearPiece:
        def __init__(self, startY, endY, offtimeMult, ontimeMult, offsetMin, offsetMax):
            self.startY = startY
            self.endY = endY
            self.offTime = (random.random() * 0.2 + 0.2) * offtimeMult
            self.onTime = (random.random() * 0.2 + 0.2) * ontimeMult
            self.offset = 0
            self.offsetMin = offsetMin
            self.offsetMax = offsetMax
        
        def update(self, st):
            st = st % (self.offTime + self.onTime)
            if st > self.offTime and self.offset == 0:
                self.offset = random.randint(self.offsetMin, self.offsetMax)
            elif st <= self.offTime and self.offset != 0:
                self.offset = 0

    class Tear(renpy.Displayable):
        def __init__(self, number, offtimeMult, ontimeMult, offsetMin, offsetMax, srf=None):
            super(Tear, self).__init__()
            self.width, self.height = renpy.get_physical_size()
            if float(self.width) / float(self.height) > 16.0/9.0:
                self.width = self.height * 16 / 9
            else:
                self.height = self.width * 9 / 16
            self.number = number
            if not srf: self.srf = screenshot_srf()
            else: self.srf = srf
            self.pieces = []
            tearpoints = [0, self.height]
            for i in range(number):
                tearpoints.append(random.randint(10, self.height - 10))
            tearpoints.sort()
            for i in range(number+1):
                self.pieces.append(TearPiece(tearpoints[i], tearpoints[i+1], offtimeMult, ontimeMult, offsetMin, offsetMax))
        
        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)
            render.blit(self.srf, (0,0))
            for piece in self.pieces:
                piece.update(st)
                subsrf = self.srf.subsurface((0, max(0, piece.startY - 1), self.width, max(0, piece.endY - piece.startY)))
                render.blit(subsrf, (piece.offset, piece.startY))
            renpy.redraw(self, 0)
            return render
        
    credits = ("Writing", "Samuel France"), ("Art", "Conor Dolan"), ("Audio", "Ryan Darcey"), ("Programming", "Dennis James Stelmach"), ("External Assets", ""), ("click1.ogg, Kenney Game Assets, Kenney, https://kenney.itch.io/kenney-game-assets-1", ""), ("swordMetal6.ogg, Kenney Game Assets, Kenney, https://kenney.itch.io/kenney-game-assets-1", ""), ("metalPot3.ogg, Kenney Game Assets, Kenney, https://kenney.itch.io/kenney-game-assets-1", ""), ("Space Cadet.ogg, Kenney Game Assets, Kenney, https://kenney.itch.io/kenney-game-assets-1", ""), ("Mission Plausible.ogg, Kenney Game Assets, Kenney, https://kenney.itch.io/kenney-game-assets-1", ""), ("phone_ringing.wav, http://soundbible.com/1518-Phone-Ringing.html", ""), ("9_mm_gunshot.wav, http://soundbible.com/994-Mirror-Shattering.html", ""), ("mirror_shattering.wav, http://soundbible.com/994-Mirror-Shattering.html", ""), ("computer_error_alert.wav, http://soundbible.com/1540-Computer-Error-Alert.html", "")
    creditText = "{size=76}Credits\n"
    for c in credits:
        if c != "":
            creditText += "\n{size=48}" + c[0] + "\n"
        creditText += "{size=64}" + c[1] + "\n"
    creditText += "\n{size=48}Engine\n{size=64}" + renpy.version()

screen tear(number=10, offtimeMult=1, ontimeMult=1, offsetMin=0, offsetMax=50, srf=None):
    zorder 150
    add Tear(number, offtimeMult, ontimeMult, offsetMin, offsetMax, srf) size (1280,720)
    on "show" action Function(hide_windows_enabled, enabled=False)
    on "hide" action Function(hide_windows_enabled, enabled=True)

label credits:
    $ credits_speed = 30
    scene black with dissolve
    show credit at Move((0.5, 7.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed + 2)
    return