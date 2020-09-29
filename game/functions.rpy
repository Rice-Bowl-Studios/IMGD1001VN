init python:
    import random

    nonunicode = "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž"

    def glitchText(length):
        out = ""
        for x in range(length):
            out += random.choice(nonunicode)
        return out

    credits = ("Writing", "Samuel France"), ("Art", "Conor Dolan"), ("Audio", "Ryan Darcey"), ("Programming", "Dennis James Stelmach"), ("External Assets", ""), ("click1.ogg, Kenney Game Assets, Kenney, https://kenney.itch.io/kenney-game-assets-1", ""), ("swordMetal6.ogg, Kenney Game Assets, Kenney, https://kenney.itch.io/kenney-game-assets-1", ""), ("metalPot3.ogg, Kenney Game Assets, Kenney, https://kenney.itch.io/kenney-game-assets-1", ""), ("Space Cadet.ogg, Kenney Game Assets, Kenney, https://kenney.itch.io/kenney-game-assets-1", ""), ("Mission Plausible.ogg, Kenney Game Assets, Kenney, https://kenney.itch.io/kenney-game-assets-1", ""), ("phone_ringing.wav, http://soundbible.com/1518-Phone-Ringing.html", ""), ("9_mm_gunshot.wav, http://soundbible.com/994-Mirror-Shattering.html", ""), ("mirror_shattering.wav, http://soundbible.com/994-Mirror-Shattering.html", ""), ("computer_error_alert.wav, http://soundbible.com/1540-Computer-Error-Alert.html", "")
    creditText = "{size=76}Credits\n"
    for c in credits:
        if not c==c[0]:
            creditText += "\n{size=48}" + c[0] + "\n"
        creditText += "{size=64}" + c[1] + "\n"
    creditText += "\n{size=48}Engine\n{size=64}" + renpy.version()

screen volume:
    frame:
        xalign 0.5
        yalign 0.5
        has vbox

        text "Sound Volume"
        bar value Preference("sound volume")
        text "Music Volume"
        bar value Preference("music volume")
        textbutton "Confirm" action Jump("start")

label credits:
    $ credits_speed = 30
    scene black with dissolve
    show credit at Move((0.5, 7.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed + 2)
    return