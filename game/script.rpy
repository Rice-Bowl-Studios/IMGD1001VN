# The script of the game goes in this file.

init python:
    _game_menu_screen = "preferences"

define e = Character("Eileen")
default no_flashing = False

# The game starts here.

label splashscreen:
    $ renpy.pause (0)
    scene whitedrop with None
    if config.developer:
        "DEBUG MODE ENABLED"
    menu:
        "This game has flashing and strobing, which can cause seizures. Would you like to disable them?"
        "Yes":
            $ no_flashing = True
        "No":
            pass
    
    return

label main_menu:
    return

label start:

    scene whitedrop with None

    "GAME START"

    "GAME DIE"

    $ renpy.quit()
