image livingroom = "livingroom.png"

##--Player is in the living room--##
label livingroom:

    scene livingroom

    "Living Room"

    show screen livingdoor

    $ renpy.pause(hard=True)

##--Player click the door at living room--##
label clickedLivingDoor:
    "You just opended the door."
##--Change this to Portuguese Steelement--##
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
