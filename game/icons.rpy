init:
    transform iconSize:
        zoom 0.3
    transform jonkerSize:
        zoom 0.1

screen map_icon():
    imagebutton:
        xalign 0.95
        yalign 0.05
        idle "map_icon_idle.png"
        hover "map_icon_hover.png"
        action Call("world_map")

label world_map:
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
        xalign 0.5
        yalign 0.6
        idle "home_icon.png"
        action Jump("livingroom")
        at iconSize

screen gotoJonkerStreet():
    imagebutton:
        xalign 0.1
        yalign 0.2
        idle "jonker_icon.jpg"
        action Jump("jonker")
        at jonkerSize

screen gotoPrayaLane():
    imagebutton:
        xalign 0.2
        yalign 0.3
        idle "praya_icon.png"
        action Jump("PrayaLaneChapel")
        at iconSize

screen gotoNightMarket():
    imagebutton:
        xalign 0.3
        yalign 0.4
        idle "market_icon.png"
        action Jump("newMarket")
        at iconSize

screen gotoPortugueseSettlement():
    imagebutton:
        xalign 0.4
        yalign 0.5
        idle "town_icon.png"
        action Jump("towns")
        at iconSize