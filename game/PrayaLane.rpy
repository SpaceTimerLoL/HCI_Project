image plchapel = "prayalanechapel.png"
image plhouse1 = "prayalanehouse1.png"
image plhouse2 = "prayalanehouse2.png"

##--Chapel location--#
label PrayaLaneChapel:
    scene plchapel
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

##--Arrows--#
init:
    transform arrowsize:
        zoom 0.3

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
