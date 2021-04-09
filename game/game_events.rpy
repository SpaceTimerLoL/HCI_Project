##--Game Intro--##
label intro:

    martin "Hello there, Tony!"
    martin "My name is Martin and I'm here to be your guide."
    martin "In this game, you will be playing as a teenager of Kristang descent, Tony."
    martin "You will start a house in the Portuguese Settlement of Melaka."
    martin "You can explore Melaka or perform the quests to create your own story."
    martin "The quest story is not just a simple drama. It is wholesome, humourous and meaningful."
    martin "Invest the characters, you will find a lot to love here."
    martin "Now, let's begin."
    return

##--Game Tutorial--##
label tutorial:
    return
##--Arrows--#
init:
    transform arrowsize:
        zoom 0.3

##--Player is in the living room--##
label livingroom:
    show screen map_icon
    show screen livingdoor
    hide screen gotoJonkerStreet
    hide screen gotoPrayaLane
    hide screen gotoNightMarket
    hide screen gotoPortugueseSettlement
    hide screen gotoHome
    scene livingroom
    "Living Room"
    $ renpy.pause(hard=True)

##--Player click the door at living room--##
label clickedLivingDoor:
    "You just opended the door."
##--Change this to Portuguese Settlement--##
    jump PrayaLaneChapel

    $ renpy.pause(hard=True)

##--Highlights door when hovered--##
screen livingdoor():
    imagebutton:
        xalign 0.7521
        yalign 0.5479
        idle "door.png"
        hover "door_hover.png"
        action Call("clickedLivingDoor")

##--Chapel location--#
label PrayaLaneChapel:
    scene plchapel
    hide screen gotoJonkerStreet
    hide screen gotoPrayaLane
    hide screen gotoNightMarket
    hide screen gotoPortugueseSettlement
    hide screen gotoHome
    hide screen livingdoor
    hide screen goleftHouse1
    hide screen gorightHouse1
    show screen gorightChapel
    "At the Assumption Chapel"

    $ renpy.pause(hard=True)

##--1st house location--#
label PrayaLaneHouse1:
    scene plhouse1

    hide screen gorightChapel
    hide screen goleftHouse2
    show screen goleftHouse1
    show screen gorightHouse1
    "Praya Lane at the back of the chapel."

    $ renpy.pause(hard=True)

##--2nd house location--#
label PrayaLaneHouse2:
    scene plhouse2
    hide screen goleftHouse1
    hide screen gorightHouse1
    show screen goleftHouse2
    "Arriving at the house."

    $ renpy.pause(hard=True)

##--Arrows for Chapel--#
screen gorightChapel():
    imagebutton:
        xalign 0.98
        yalign 0.54
        idle "arrowright.png"
        hover "arrowright_hover.png"
        action Jump("PrayaLaneHouse1")
        at arrowsize

##--Arrows for House 1--#
screen goleftHouse1():
    imagebutton:
        xalign 0.02
        yalign 0.54
        idle "arrowleft.png"
        hover "arrowleft_hover.png"
        action Jump("PrayaLaneChapel")
        at arrowsize

screen gorightHouse1():
    imagebutton:
        xalign 0.98
        yalign 0.54
        idle "arrowright.png"
        hover "arrowright_hover.png"
        action Jump("PrayaLaneHouse2")
        at arrowsize

##--Arrows for House 2--#
screen goleftHouse2():
    imagebutton:
        xalign 0.02
        yalign 0.54
        idle "arrowleft.png"
        hover "arrowleft_hover.png"
        action Jump("PrayaLaneHouse1")
        at arrowsize

screen gotoStalls():
    imagebutton:
        xalign 0.0
        yalign 0.5
        idle "arrowleft.png"
        hover "arrowleft_hover.png"
        action Jump("nextMarket")
        at arrowsize


screen gotoMarket():
    imagebutton:
        xalign 0.0
        yalign 0.5
        idle "arrowright.png"
        hover "arrowright_hover.png"
        action Jump("start")
        at arrowsize

label newMarket:
    hide screen gotoJonkerStreet
    hide screen gotoPrayaLane
    hide screen gotoNightMarket
    hide screen gotoPortugueseSettlement
    hide screen gotoHome
    scene market
    "Welcome to the night market!"
    show screen gotoStalls
    $ renpy.pause(hard=True)


label nextMarket:
    scene stalls
    hide screen gotoStalls
    show screen gotoMarket
    $ renpy.pause(hard=True)

label towns:
    scene town
    hide screen gotoJonkerStreet
    hide screen gotoPrayaLane
    hide screen gotoNightMarket
    hide screen gotoPortugueseSettlement
    hide screen gotoHome
    show screen gotoStreet
    $ renpy.pause(hard=True)

screen gotoStreet():
    imagebutton:
        xalign 0.0
        yalign 0.5
        idle "arrowright.png"
        hover "arrowright_hover.png"
        action Jump("streets")
        at arrowsize

label streets:
    scene street
    hide screen gotoStreet
    show screen gotoTown
    $ renpy.pause(hard=True)

screen gotoTown():
    imagebutton:
        xalign 0.0
        yalign 0.5
        idle "arrowright.png"
        hover "arrowright_hover.png"
        action Jump("towns")
        at arrowsize

