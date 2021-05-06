# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import speech_recognition as sr
import os
import pyttsx3

engine = pyttsx3.init()

EMF = "emf"
Freezing = "freezing"
Box = "box"
Book = "book"
Orbs = "orbs"
Prints = "fingerprints"

Clues = [EMF, Freezing, Box, Book, Orbs, Prints]

Phantom = {"name": "phantom", "clues": [EMF, Freezing, Orbs]}
Banshee = {"name": "banshee", "clues": [EMF, Freezing, Prints]}
Jinn = {"name": "jinn", "clues": [EMF, Box, Prints]}
Revenant = {"name": "revenant", "clues":[EMF, Book, Prints]}
Shade = {"name":"shade", "clues":[EMF, Book, Orbs]}
Oni = {"name":"oni", "clues":[EMF, Box, Book]}
Wraith = {"name":"wraith", "clues":[Freezing, Box, Prints]}
Mare = {"name":"mare", "clues":[Freezing, Box, Orbs]}
Demon = {"name":"demon", "clues":[Freezing, Box, Book]}
Yurei = {"name":"yurei", "clues":[Freezing, Book, Orbs]}
Poltergeist = {"name":"poltergeist", "clues":[Box, Orbs, Prints]}
Spirit = {"name": "spirit", "clues":[Box, Book, Prints]}

def recognize_speech_from_mic(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response

def reset_ghost():
    ghost = {}
    ghost["Phantom"] = {"name": "phantom", "clues": [EMF, Freezing, Orbs]}
    ghost["Banshee"] = {"name": "banshee", "clues": [EMF, Freezing, Prints]}
    ghost["Jinn"] = {"name": "jinn", "clues": [EMF, Box, Prints]}
    ghost["Revenant"] = {"name": "revenant", "clues": [EMF, Book, Prints]}
    ghost["Shade"] = {"name": "shade", "clues": [EMF, Book, Orbs]}
    ghost["Oni"] = {"name": "oni", "clues": [EMF, Box, Book]}
    ghost["Wraith"] = {"name": "wraith", "clues": [Freezing, Box, Prints]}
    ghost["Mare"] = {"name": "mare", "clues": [Freezing, Box, Orbs]}
    ghost["Demon"] = {"name": "demon", "clues": [Freezing, Box, Book]}
    ghost["Yurei"] = {"name": "yurei", "clues": [Freezing, Book, Orbs]}
    ghost["Poltergeist"] = {"name": "poltergeist", "clues": [Box, Orbs, Prints]}
    ghost["Spirit"] = {"name": "spirit", "clues": [Box, Book, Prints]}
    return ghost

def unique(list_in):
    list_set = set(list_in)
    return list(list_set)

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def main():
    r = sr.Recognizer()
    mic = sr.Microphone()
    ghosts = reset_ghost()
    clues = []
    while True:
        line = recognize_speech_from_mic(r, mic)
        if line["transcription"]:
            text = line["transcription"]
            print("heard:", text)
            if text.startswith("ghost command"):
                print("received a ghost command")
                if text == "ghost command reset":
                    print("resetting ghost data")
                    clues = []
                elif text.startswith("ghost command I got"):
                    words = text.split()
                    clue = words[-1].lower()
                    print("received clue", clue)
                    if clue in Clues:
                        print("valid command")
                        clues.append(clue)
                        clues = unique(clues)
                        print(clues)
                        if len(clues) == 3:
                            ghostOut = []
                            for ghostKey in ghosts:
                                ghost = ghosts[ghostKey]
                                if all(clue in ghost["clues"] for clue in clues):
                                    print("it's a", ghost["name"], "!")
                                    ghostOut.append(ghost)
                            print("ghostOut:", str(ghostOut))
                            if len(ghostOut) == 1:
                                speak("it looks like it's a " + ghostOut[0]["name"])
                                clues = []
                            else:
                                speak("error try again")
                                clues = []
                        if len(clues) == 2:
                            speakGhosts = []
                            speakClues = []
                            for ghostKey in ghosts:
                                ghost = ghosts[ghostKey]
                                if all(clue in ghost["clues"] for clue in clues):
                                    speakGhosts.append(ghost["name"])
                                    for clueKey in ghost["clues"]:
                                        if clueKey not in clues:
                                            speakClues.append(clueKey)
                            ghostsLine = " or ".join(speakGhosts)
                            cluesLine = " or ".join(speakClues)
                            speak("it could be " +  ghostsLine + " look for " + cluesLine)


        else:
            print(line["error"])





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
