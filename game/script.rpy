define martin = Character("Martin")

init -1 python:
    showitems = True
    showmoney = True
    global minn
    minn = 0

    def pass_time(mins=1):
        store.minn += mins
        store.fwd_time = True

default encounter = 0
default inventory = []
default money = 0
default Chicken = True
default Chicken_Price = 15
default Mutton = True
default Mutton_Price = 15
default Fish = True
default Fish_Price = 20
default Potatoes = True
default Potatoes_Price = 3
default Onion =  True
default Onion_Price = 3
default Garlic = True
default Garlic_Price = 5
default Ginger = True
default Ginger_Price = 5
default Tomatoes = True
default Tomatoes_Price = 5
default Scallops = True
default Scallops_Price = 10
default Sliced_Chillies = True
default Sliced_Chillies_Price = 15
default Shallots = True
default Shallots_Price = 5
default Salmon = True
default Salmon_Price = 40
default Black_Peppercorns = True
default Black_Peppercorns_Price = 3
default Gallanga = True
default Gallanga_Price = 3
default Olive_Oil = True
default Olive_Oil_Price = 10
default Lemon_Grass = True
default Lemon_Grass_Price = 5
default Mustard_Seeds = True
default Mustard_Seeds_Price = 5
default Cloves = True
default Cloves_Price = 3
default heat_oil_finished = False
default saute_finished = False
default combine_finished = False
default cook_finished = False
default fry_finished = False
default progress = 0
default order = 0

label start:
    scene room
    with fade
    $pass_time(60)
    show martin_introduction
    $mainname = renpy.input("My friend, what's your name?", "Tony")
    $mainname = mainname.strip()
    call livingroom
return




