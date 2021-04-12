init:
    transform xbuttonSize:
        zoom 0.3
    transform taskbookSize:
        zoom 2.2

##--Tasks--##
screen tasklist():
    imagemap:
        ground "tasks.png"
        xalign 0.5
        yalign 0.6
        at taskbookSize
    text "Tasks":
        color "#000000"
        xalign 0.5
        yalign 0.2
        size 100
        bold True
    viewport:
        xmaximum 750
        ymaximum 500
        xalign 0.67
        yalign 0.6
        vbox:
                    textbutton "List of Ingredients to Buy.\n " action [Hide("tasklist"),Show("taskDetailBuy")]:
                        text_color "#000000"
                        text_hover_color "#A9A9A9"
                        text_size 30
                    textbutton "How to Cook." action [Hide("tasklist"),Show("taskDetailCook")]:
                        text_color "#000000"
                        text_hover_color "#A9A9A9"
                        text_size 30
    imagebutton:
        xalign 0.66
        yalign 0.185
        idle "xbutton.png"
        action [Hide("tasklist"),Hide("taskDetailBuy"),Hide("taskDetailCook")]
        at xbuttonSize

##----Ingredients List----##
screen taskDetailBuy():
    imagemap:
        ground "tasks.png"
        xalign 0.5
        yalign 0.6
        at taskbookSize
    text "Tasks":
        color "#000000"
        xalign 0.5
        yalign 0.2
        size 100
        bold True
    viewport:
        xmaximum 750
        ymaximum 500
        xalign 0.67
        yalign 0.6
        vbox:
            text "Ingredients: \n\n1. Chicken \n2. Potatoes \n3. Onion \n4. Garlic \n5. Sliced Chillies \n6. Shallots \n7. Galangal \n8. Ginger \n9. Lemon Grass \n10. Mustard Seeds \n11. Cloves \n12. Black Peppercorns":
                color "#000000"
                xpos 0.0
                size 30
    imagebutton:
        xalign 0.66
        yalign 0.185
        idle "xbutton.png"
        action [Show("tasklist"),Hide("taskDetailBuy")]
        at xbuttonSize

##-------Cooking Steps-----###
screen taskDetailCook():
    imagemap:
        ground "tasks.png"
        xalign 0.5
        yalign 0.6
        at taskbookSize
    text "Tasks":
        color "#000000"
        xalign 0.5
        yalign 0.2
        size 100
        bold True
    viewport:
        xmaximum 750
        ymaximum 500
        xalign 0.67
        yalign 0.6
        vbox:
            text "Instructions: \n\nStep 1: Heat \nStep 2: Saute \nStep 3: Fry \nStep 4: Mix \nStep 5: Cook":
                color "#000000"
                xpos 0.0
                size 30
    imagebutton:
        xalign 0.66
        yalign 0.185
        idle "xbutton.png"
        action [Show("tasklist"),Hide("taskDetailCook")]
        at xbuttonSize
