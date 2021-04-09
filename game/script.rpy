define martin = Character("Martin")

init -1 python:
    global minn
    minn = 0

    def pass_time(mins=1):
        store.minn += mins
        store.fwd_time = True


label start:
    scene room
    with fade
    $pass_time(60)
    show martin_introduction
    $mainname = renpy.input("My friend, what's your name?", "Tony")
    $mainname = mainname.strip()
    menu:
        "Do you want to skip the tutorial?"
        "Yes":
            call intro
        "No":
            call tutorial
    call livingroom
return




