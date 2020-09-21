init python:
    import random

    nonunicode = "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž"

    def glitchText(length):
        out = ""
        for x in range(length):
            out += random.choice(nonunicode)
        return out

    credits = ("Writing", "Samuel France"), ("Art", "Conor Dolan"), ("Audio", "Ryan Darcey"), ("Programming", "Dennis James Stelmach"), ("External Assets", ""), ("click1.ogg, Kenney Game Assets, Kenney, https://kenney.itch.io/kenney-game-assets-1", ""), ("swordMetal6.ogg, Kenney Game Assets, Kenney, https://kenney.itch.io/kenney-game-assets-1", ""), ("metalPot3.ogg, Kenney Game Assets, Kenney, https://kenney.itch.io/kenney-game-assets-1", ""), ("Space Cadet.ogg, Kenney Game Assets, Kenney, https://kenney.itch.io/kenney-game-assets-1", ""), ("Mission Plausible.ogg, Kenney Game Assets, Kenney, https://kenney.itch.io/kenney-game-assets-1", ""), ("See documentation file for sources", "")
    creditText = "{size=76}Credits\n\n"
    for c in credits:
        if not c==c[0]:
            creditText += "\n{size=48}" + c[0] + "\n"
        creditText += "{size=64}" + c[1] + "\n"
    creditText += "\n{size=48}Engine\n{size=64}" + renpy.version()

label credits:
    $ credits_speed = 25
    scene black with dissolve
    show theEnd:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide theEnd
    show credit at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks
    return