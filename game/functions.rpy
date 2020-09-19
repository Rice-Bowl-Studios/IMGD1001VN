label playerPronounHelper:
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
    return

label playerCharacterPronounHelper:
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
    return