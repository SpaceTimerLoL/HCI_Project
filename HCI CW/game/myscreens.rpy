init: 
    transform arrowSize:
        zoom 0.4


screen gotoStalls():
    imagebutton:
        xalign 0.0
        yalign 0.5
        idle "arrow_left.png"
        action Jump("nextMarket")
        at arrowSize


screen gotoMarket():
    imagebutton:
        xalign 0.0
        yalign 0.5
        idle "arrow_right.png"
        action Jump("start")
        at arrowSize