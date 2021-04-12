init:
    transform arrowsize:
        zoom 0.3

##--Game Intro--##
label intro:

    martin "Hello there, Tony!"
    martin "My name is Martin and I'm here to be your guide."
    martin "In this game, you will be playing as a teenager of Kristang descent, Tony."
    martin "You will start a house in Praya Lane of Melaka."
    martin "You can explore Melaka or perform the quests to create your own story."
    martin "The quest story is not just a simple drama. It is wholesome, humourous and meaningful."
    martin "Invest the characters, you will find a lot to love here."
    martin "Now, let's begin."
    return

##--Game Tutorial--##
label tutorial:
    return

##--Cooking Tutorial--##
label cooking_tutorial:
    return

##--Player is in the living room--##
label livingroom:
    hide screen gotoJonkerStreet
    hide screen gotoPrayaLane
    hide screen gotoNightMarket
    hide screen gotoPortugueseSettlement
    hide screen gotoHome
    scene livingroom
    show screen map_icon
    "Living Room"
    if encounter == 0:
        call item_request
    if encounter == 1:
        jump cook
    show screen livingdoor
    $ renpy.pause(hard=True)

##--Player click the door at living room--##
label clickedLivingDoor:
    "You have just opened the door."
    jump PrayaLaneChapel
    $ renpy.pause(hard=True)

##--Highlights door when hovered--##
screen livingdoor():
    imagebutton:
        xalign 0.7521
        yalign 0.5479
        idle im.Scale("door.png", 302.36, 601.5)
        hover im.Scale("door_hover.png", 302.36, 601.5)
        action Call("clickedLivingDoor")

##--Chapel location--#
label PrayaLaneChapel:
    hide screen gotoJonkerStreet
    hide screen gotoPrayaLane
    hide screen gotoNightMarket
    hide screen gotoPortugueseSettlement
    hide screen gotoHome
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

##--Go to market from map--#
label newMarket:
    hide screen gotoJonkerStreet
    hide screen gotoPrayaLane
    hide screen gotoNightMarket
    hide screen gotoPortugueseSettlement
    hide screen gotoHome
    scene market
    "Welcome to the night market!"
    call buy_items
    $ renpy.pause(hard=True)


##--Portuguese Settlement--#
label towns:
    scene town
    hide screen gotoJonkerStreet
    hide screen gotoPrayaLane
    hide screen gotoNightMarket
    hide screen gotoPortugueseSettlement
    hide screen gotoHome
    hide screen gotoTown
    show screen gotoStreet
    $ renpy.pause(hard=True)

screen gotoStreet():
    imagebutton:
        xalign 0.95
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
        xalign 0.05
        yalign 0.5
        idle "arrowleft.png"
        hover "arrowleft_hover.png"
        action Jump("towns")
        at arrowsize


##--Jonker Walk--#
label Jonker88Cendol:
    hide screen gotoJonker88CendolArrow
    hide screen gotoJonkerWalk2Arrow
    scene jonker88cendol
    "This is Jonker Walk's famous cendol (shaved ice)!"
    "It only can be found in Melaka."
    show screen gotoJonkerWalk1Arrow
    $ renpy.pause(hard=True)

screen gotoJonkerWalk1Arrow():
    imagebutton:
        xalign 0.95
        yalign 0.5
        idle "arrowright.png"
        hover "arrowright_hover.png"
        action Jump("JonkerWalk1")
        at arrowsize

label JonkerWalk1:
    hide screen gotoJonkerStreet
    hide screen gotoPrayaLane
    hide screen gotoNightMarket
    hide screen gotoPortugueseSettlement
    hide screen gotoHome
    hide screen gotoJonkerWalk1Arrow
    hide screen gotoJonkerWalk1Arrow1
    hide screen gotoJonkerWalk3Arrow
    scene jonkerwalk1
    "There are so many things to buy here!"
    show screen gotoJonker88CendolArrow
    show screen gotoJonkerWalk2Arrow
    $ renpy.pause(hard=True)

screen gotoJonker88CendolArrow():
    imagebutton:
        xalign 0.05
        yalign 0.5
        idle "arrowleft.png"
        hover "arrowleft_hover.png"
        action Jump("Jonker88Cendol")
        at arrowsize

screen gotoJonkerWalk2Arrow():
    imagebutton:
        xalign 0.95
        yalign 0.5
        idle "arrowright.png"
        hover "arrowright_hover.png"
        action Jump("JonkerWalk2")
        at arrowsize

label JonkerWalk2:
    hide screen gotoJonkerWalk2Arrow
    hide screen gotoJonker88CendolArrow
    hide screen gotoJonkerWalk2Arrow1
    hide screen gotoJonkerWalkTempleArrow
    scene jonkerwalk2
    "This is the Statue of Datuk Wira Dr. Gan Boon Leong, the father of bodybuilding in Malaysia and a former Mr. Universe"
    "It is such a cultural heritage."
    show screen gotoJonkerWalk1Arrow1
    show screen gotoJonkerWalk3Arrow
    $ renpy.pause(hard=True)

screen gotoJonkerWalk1Arrow1():
    imagebutton:
        xalign 0.05
        yalign 0.5
        idle "arrowleft.png"
        hover "arrowleft_hover.png"
        action Jump("JonkerWalk1")
        at arrowsize

screen gotoJonkerWalk3Arrow():
    imagebutton:
        xalign 0.95
        yalign 0.5
        idle "arrowright.png"
        hover "arrowright_hover.png"
        action Jump("JonkerWalk3")
        at arrowsize

label JonkerWalk3:
    scene jonkerwalk3
    hide screen gotoJonkerWalk1Arrow1
    hide screen gotoJonkerWalk3Arrow
    hide screen gotoJonkerWalk3Arrow1
    hide screen gotoInsideTheTempleArrow
    "Let's continue walking and enjoy all the delicious Melaka street food."
    show screen gotoJonkerWalk2Arrow1
    show screen gotoJonkerWalkTempleArrow
    $ renpy.pause(hard=True)

screen gotoJonkerWalk2Arrow1():
    imagebutton:
        xalign 0.05
        yalign 0.5
        idle "arrowleft.png"
        hover "arrowleft_hover.png"
        action Jump("JonkerWalk2")
        at arrowsize

screen gotoJonkerWalkTempleArrow():
    imagebutton:
        xalign 0.95
        yalign 0.5
        idle "arrowright.png"
        hover "arrowright_hover.png"
        action Jump("JonkerWalkTemple")
        at arrowsize

label JonkerWalkTemple:
    scene jonkerwalktemple
    hide screen gotoJonkerWalk2Arrow1
    hide screen gotoJonkerWalkTempleArrow
    hide screen gotoJonkerWalkTempleArrow1
    "Here we have the famous Cheng Hoon Teng Temple located in the streets of Jonker Walk"
    "Melaka is known for temples and always treat the temples with utter respect."
    show screen gotoJonkerWalk3Arrow1
    show screen gotoInsideTheTempleArrow
    $ renpy.pause(hard=True)

screen gotoJonkerWalk3Arrow1():
    imagebutton:
        xalign 0.05
        yalign 0.5
        idle "arrowleft.png"
        hover "arrowleft_hover.png"
        action Jump("JonkerWalk3")
        at arrowsize

screen gotoInsideTheTempleArrow():
    imagebutton:
        xalign 0.95
        yalign 0.5
        idle "arrowright.png"
        hover "arrowright_hover.png"
        action Jump("InsideTheTemple")
        at arrowsize

label InsideTheTemple:
    scene insidethetemple
    hide screen gotoJonkerWalk3Arrow1
    hide screen gotoInsideTheTempleArrow
    "This temple is the oldest Buddhist place of worship in the country. Built in 1646, it is also known as the ‘Merciful Cloud Temple’."
    "Cheng Hoon Teng Temple was constructed by Chan Lak Koa, son-in-law to Captain Li, Malacca’s second Chinese kapitan."
    show screen gotoJonkerWalkTempleArrow1
    $ renpy.pause(hard=True)

screen gotoJonkerWalkTempleArrow1():
    imagebutton:
        xalign 0.05
        yalign 0.5
        idle "arrowleft.png"
        hover "arrowleft_hover.png"
        action Jump("JonkerWalkTemple")
        at arrowsize


