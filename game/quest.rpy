init:
    transform arrowsize:
        zoom 0.3
    transform barsize:
        zoom 3
    transform restartsize:
        zoom 0.5

define god = Character("Master Mirror")

##--Market--##
label buy_items:
    show mm
    with fade
    god "Best stall in Melaka. How can I help you?"
    call seller
    return


label seller:
    menu:
        "Let me so what you got.":
            call items
        "'Wave awkwardly'":
            hide mm with fade
            jump world_map
        "Thank you. Bye.":
            god "Thank you and come again."
            hide mm
            jump world_map
            return
    $ renpy.pause(hard=True)


label items:
    $ money = 300
    menu:
        "Chicken | RM15":
            if Chicken_Price > money  :
                "Sorry, you don't have enough money."
                jump items
            elif not Chicken:
                "Sold out my friend."
                jump items
            else:
                $ money -= Chicken_Price
                $ Chicken = False
                "That's a good choice."
                $ inventory.append("Chicken")
                jump items
        "Mutton | RM15":
            if Mutton_Price > money:
                "Sorry, you don't have enough money."
                jump items
            elif not Mutton:
                "Sold out my friend."
                jump items
            else:
                $ money -= Mutton_Price
                $ Mutton = False
                "That's a good choice."
                $ inventory.append("Mutton")
                jump items
        "Fish | RM20":
            if Fish_Price > money:
                "Sorry, you don't have enough money."
                jump items
            elif not Fish:
                "Sold out my friend."
                jump items
            else:
                $ money -= Fish_Price
                $ Fish = False
                "That's a good choice."
                $ inventory.append("Fish")
                jump items
        "Potatoes | RM3":
            if Potatoes_Price > money:
                "Sorry, you don't have enough money."
                jump items
            elif not Potatoes:
                "Sold out my friend."
                jump items
            else:
                $ money -= Potatoes_Price
                $ Potatoes = False
                "That's a good choice."
                $ inventory.append("Potatoes")
                jump items
        "More":
            jump more
        "Return":
            jump seller
    $ renpy.pause(hard=True)

label more:
    menu:
        "Onion | RM3":
            if Onion_Price > money:
                "Sorry, you don't have enough money."
                jump more
            elif not Onion:
                "Sold out my friend."
                jump more
            else:
                $ money -= Onion_Price
                $ Onion = False
                "That's a good choice."
                $ inventory.append("Onion")
                jump more
        "Garlic | RM5":
            if Garlic_Price > money:
                "Sorry, you don't have enough money."
                jump more
            elif not Garlic:
                "Sold out my friend."
                jump more
            else:
                $ money -= Garlic_Price
                $ Garlic = False
                "That's a good choice."
                $ inventory.append("Garlic")
                jump more
        "Ginger | RM5":
            if Ginger_Price > money:
                "Sorry, you don't have enough money."
                jump more
            elif not Ginger:
                "Sold out my friend."
                jump more
            else:
                $ money -= Ginger_Price
                $ Ginger = False
                "That's a good choice."
                $ inventory.append("Ginger")
                jump more
        "Tomatoes | RM5":
            if Tomatoes_Price > money:
                "Sorry, you don't have enough money."
                jump more
            elif not Tomatoes:
                "Sold out my friend."
                jump more
            else:
                $ money -= Tomatoes_Price
                $ Tomatoes = False
                "That's a good choice."
                $ inventory.append("Tomatoes")
                jump more
        "Scallops | RM10":
            if Scallops_Price > money:
                "Sorry, you don't have enough money."
                jump more
            elif not Scallops:
                "Sold out my friend."
                jump more
            else:
                $ money -= Scallops_Price
                $ Scallops = False
                "That's a good choice."
                $ inventory.append("Scallops")
                jump more
        "Back":
            jump items
        "More":
            jump more1
        "Return":
            jump seller
    $ renpy.pause(hard=True)

label more1:
    menu:
        "Sliced Chillies | RM15":
            if Sliced_Chillies_Price > money:
                "Sorry, you don't have enough money."
                jump more1
            elif not Sliced_Chillies:
                "Sold out my friend."
                jump more1
            else:
                $ money -= Sliced_Chillies_Price
                $ Sliced_Chillies = False
                "That's a good choice."
                $ inventory.append("Sliced_Chillies")
                jump more1
        "Shallots | RM5":
            if Shallots_Price > money:
                "Sorry, you don't have enough money."
                jump more1
            elif not Shallots:
                "Sold out my friend."
                jump more1
            else:
                $ money -= Shallots_Price
                $ Shallots = False
                "That's a good choice."
                $ inventory.append("Shallots")
                jump more1
        "Gallanga | RM3":
            if Gallanga_Price > money:
                "Sorry, you don't have enough money."
                jump more1
            elif not Gallanga:
                "Sold out my friend."
                jump more1
            else:
                $ money -= Gallanga_Price
                $ Gallanga = False
                "That's a good choice."
                $ inventory.append("Gallanga")
                jump more1
        "Lemon Grass | RM5":
            if Lemon_Grass_Price > money:
                "Sorry, you don't have enough money."
                jump more1
            elif not Lemon_Grass:
                "Sold out my friend."
                jump more1
            else:
                $ money -= Lemon_Grass_Price
                $ Lemon_Grass = False
                "That's a good choice."
                $ inventory.append("Lemon_Grass")
                jump more1
        "Salmon | RM40":
            if Salmon_Price > money:
                "Sorry, you don't have enough money."
                jump more1
            elif not Salmon:
                "Sold out my friend."
                jump more1
            else:
                $ money -= Salmon_Price
                $ Salmon = False
                "That's a good choice."
                $ inventory.append("Salmon")
                jump more1
        "Back":
            jump more
        "More":
            jump more2
        "Return":
            jump seller
    $ renpy.pause(hard=True)

label more2:
    menu:
        "Black Peppercorns | RM3":
            if Black_Peppercorns_Price > money:
                "Sorry, you don't have enough money."
                jump more2
            elif not Black_Peppercorns:
                "Sold out my friend."
                jump more2
            else:
                $ money -= Black_Peppercorns_Price
                $ Black_Peppercorns = False
                "That's a good choice."
                $ inventory.append("Black_Peppercorns")
                jump more2
        "Olive Oil | RM10":
            if Olive_Oil_Price > money:
                "Sorry, you don't have enough money."
                jump more2
            elif not Olive_Oil:
                "Sold out my friend."
                jump more2
            else:
                $ money -= Olive_Oil_Price
                $ Olive_Oil = False
                "That's a good choice."
                $ inventory.append("Olive_Oil")
                jump more2
        "Mustard Seeds | RM5":
            if Mustard_Seeds_Price > money:
                "Sorry, you don't have enough money."
                jump more2
            elif not Mustard_Seeds:
                "Sold out my friend."
                jump more2
            else:
                $ money -= Mustard_Seeds_Price
                $ Mustard_Seeds = False
                "That's a good choice."
                $ inventory.append("Mustard_Seeds")
                jump more2
        "Cloves | RM3":
            if Cloves_Price > money:
                "Sorry, you don't have enough money."
                jump more2
            elif not Cloves:
                "Sold out my friend."
                jump more2
            else:
                $ money -= Cloves_Price
                $ Cloves = False
                "That's a good choice."
                $ inventory.append("Cloves")
                jump more2
        "Back":
            jump more1
        "Return":
            jump seller
    $ renpy.pause(hard=True)

##--Demo Quest Starts-##
label item_request:
    scene livingroom
    show martin with fade
    martin "Tonight we are preparing a special dinner for a secret guest."
    martin "I want you to go to the market to pick up some ingredients."
    martin "Take the RM300 and shopping list on the table."
    "Your money: RM300"
    hide martin with fade
    $ encounter += 1
    jump world_map
    return

label cook:
    scene livingroom
    show martin with fade
    if "Cloves" in inventory and "Mustard_Seeds" in inventory and "Black_Peppercorns" in inventory and "Lemon_Grass" in inventory and "Chicken" in inventory and "Gallanga" in inventory and "Shallots" in inventory and "Sliced_Chillies" in inventory and "Potatoes" in inventory and "Ginger" in inventory and "Garlic" in inventory and "Onion" in inventory:
        martin "Time to cook, boy!"
        martin "You will cook Kari Debal today."
        hide martin with fade
        jump cooking_game
    else:
        martin "Go back to the market, boy!"
        jump world_map

label cooking_game:
    scene cooking_bg
    show screen heat_oil
    show screen saute
    show screen fry
    show screen combine
    show screen cook
    show screen progress_bar
    $ renpy.pause(hard=True)

screen heat_oil():
    if not heat_oil_finished:
        imagebutton:
            xalign 0.1
            yalign 0.1
            idle im.Scale("heat.png", 200, 200)
            action Call("heat_finished")

label heat_finished:
    if not heat_oil_finished:
        if order != 0:
            martin "Cooking properly, boy!"
            jump restarting
        $ heat_oil_finished = True
        $ progress += 20
        if progress < 100:
            hide progress_bar
            show progress_bar
            $ order += 1
            jump cooking_game
        elif progress == 100:
            jump cooked_dish

screen saute():
    if not saute_finished:
        imagebutton:
            xalign 0.3
            yalign 0.1
            idle im.Scale("saute_icon.png", 200, 200)
            action Call("sautes_finished")

label sautes_finished:
    if not saute_finished:
        if order != 1:
            martin "Cooking properly, boy!"
            jump restarting
        $ saute_finished = True
        $ progress += 20
        if progress < 100:
            hide progress_bar
            show progress_bar
            $ order += 1
            jump cooking_game
        elif progress == 100:
            jump cooked_dish

screen fry():
    if not fry_finished:
        imagebutton:
            xalign 0.5
            yalign 0.1
            idle im.Scale("fry_icon.jpg", 200, 200)
            action Call("fryer_finished")

label fryer_finished:
    if not fry_finished:
        if order != 2:
            martin "Cooking properly, boy!"
            jump restarting
        $ fry_finished = True
        $ progress += 20
        if progress < 100:
            hide progress_bar
            show progress_bar
            $ order += 1
            jump cooking_game
        elif progress == 100:
            jump cooked_dish

screen combine():
    if not combine_finished:
        imagebutton:
            xalign 0.1
            yalign 0.5
            idle im.Scale("combine_icon.jpg", 200, 200)
            action Call("combines_finished")

label combines_finished:
    if not combine_finished:
        if order != 3:
            martin "Cooking properly, boy!"
            jump restarting
        $ combine_finished = True
        $ progress += 20
        if progress < 100:
            hide progress_bar
            show progress_bar
            $ order += 1
            jump cooking_game
        elif progress == 100:
            jump cooked_dish
    elif :
        "You have already perform this action"
        jump restarting

screen cook():
    if not cook_finished:
        imagebutton:
            xalign 0.1
            yalign 0.8
            idle im.Scale("cook_icon.png", 200, 200)
            action Call("cooks_finished")

label cooks_finished:
    if not cook_finished:
        if order != 4:
            martin "Cooking properly, boy!"
            jump restarting
        $ cook_finished = True
        $ progress += 20
        if progress < 100:
            hide progress_bar
            show progress_bar
            jump cooking_game
        elif progress == 100:
            jump cooked_dish


label restarting:
    $ order = 0
    $ progress = 0
    scene cooking_bg
    $ heat_oil_finished = False
    $ saute_finished = False
    $ combine_finished = False
    $ cook_finished = False
    $ fry_finished = False
    jump cooking_game

screen progress_bar():
    if progress == 0:
        imagebutton:
            idle "progress_0.png"
            xalign 0.5
            yalign 0.9
            at barsize
    elif progress == 20:
        imagebutton:
            idle "progress_20.png"
            xalign 0.5
            yalign 0.9
    elif progress == 40:
        imagebutton:
            idle "progress_40.png"
            xalign 0.5
            yalign 0.9
    elif progress == 60:
        imagebutton:
            idle "progress_60.png"
            xalign 0.5
            yalign 0.9
    elif progress == 80:
        imagebutton:
            idle "progress_80.png"
            xalign 0.5
            yalign 0.9

label cooked_dish:
    if progress == 100:
        hide screen restart
        scene kari_debal
        martin "Well done."
        "Demo ends here. Stay tuned for future updates."
        jump start
    else:
        jump retry

label retry:
    "You failed. Try again!"
    jump cooking_game
