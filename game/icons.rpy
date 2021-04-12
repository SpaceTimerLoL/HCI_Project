init:
    transform iconSize:
        zoom 0.1
    transform taskiconSize:
        zoom 0.8
    transform homeSize:
        zoom 1.5
    transform jonkerSize:
        zoom 0.15
    transform prayaSize:
        zoom 0.25

screen gotoTask():
    imagebutton:
        xalign 0.015
        yalign 0.015
        idle "task_icon.png"
        action Show("tasklist")
        at taskiconSize


screen map_icon():
    imagebutton:
        xalign 0.95
        yalign 0.05
        idle "map_icon_idle.png"
        hover "map_icon_hover.png"
        action Call("world_map")

label world_map:
    show screen gotoTask
    show screen map_icon
    hide screen gorightChapel
    hide screen goleftHouse2
    hide screen livingdoor
    hide screen goleftHouse1
    hide screen gotoJonker88CendolArrow
    hide screen gotoJonkerWalk1Arrow
    hide screen gotoJonkerWalk1Arrow1
    hide screen gotoJonkerWalk2Arrow
    hide screen gotoJonkerWalk2Arrow1
    hide screen gotoJonkerWalk3Arrow
    hide screen gotoJonkerWalk3Arrow1
    hide screen gotoJonkerWalkTempleArrow
    hide screen gotoJonkerWalkTempleArrow1
    hide screen gotoInsideTheTempleArrow
    hide screen gotoTown
    hide screen gotoStreet
    hide screen heat_oil
    hide screen saute
    hide screen fry
    hide screen combine
    hide screen cook
    hide screen progress_bar
    scene melaka_map
    show screen gotoJonkerStreet
    show screen gotoPrayaLane
    show screen gotoNightMarket
    show screen gotoPortugueseSettlement
    show screen gotoHome
    hide screen livingdoor
    $ renpy.pause(hard=True)

screen gotoHome():
    imagebutton:
        xalign 0.88
        yalign 0.045
        idle "home_icon.png"
        hover "home_icon_hover.png"
        action Jump("livingroom")
        at homeSize

screen gotoJonkerStreet():
    imagebutton:
        xalign 0.27
        yalign 0.05
        idle "jonker_icon.jpg"
        action Jump("JonkerWalk1")
        at jonkerSize


screen gotoPrayaLane():
    imagebutton:
        xalign 0.67
        yalign 0.57
        idle "praya_icon.png"
        action Jump("PrayaLaneChapel")
        at prayaSize

screen gotoNightMarket():
    imagebutton:
        xalign 0.3
        yalign 0.4
        idle "market_icon.png"
        action Jump("newMarket")
        at iconSize

screen gotoPortugueseSettlement():
    imagebutton:
        xalign 0.93
        yalign 0.82
        idle "town_icon.png"
        action Jump("towns")
        at iconSize
