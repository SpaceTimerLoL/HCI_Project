image market = "market.jpg"
image stalls = "stalls.jfif"
image stalls2 = "stalls2.jpg"
image market_4 = "market4.jpg"






label start:

    

    scene market

    "Welcome to the night market!"

    show screen gotoStalls

    $ renpy.pause(hard=True)

        
label nextMarket:

    scene stalls

    hide screen gotoStalls

    show screen gotoMarket
    $ renpy.pause(hard=True)