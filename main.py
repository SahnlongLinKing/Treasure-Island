a = input(
    "Type every input all lowercase, with no punctuation. Type confirm to confirm you're ready."
)
if a == "confirm":
    print(
        """"*******************************************************************************
         ,,
        `""*$b..
             ""*$o.
                 "$$o.
                   "*$$o.
                      "$$$o.
                        "$$$$bo...       ..o:
                          "$$$$$$$$booocS$$$    ..    ,.
                       ".    "*$$$$SP     V$o..o$$. .$$$b
                        "$$o. .$$$$$o. ...A$$$$$$$$$$$$$$b
                  ""bo.   "*$$$$$$$$$$$$$$$$$$$$P*$$$$$$$$:
                     "$$.    V$$$$$$$$$P"**""*"'   VP  * "l
                       "$$$o.4$$$$$$$$X
                        "*$$$$$$$$$$$$$AoA$o..oooooo..           .b
                               .X$$$$$$$$$$$P""     ""*oo,,     ,$P
                              $$P""V$$$$$$$:    .        ""*****"
                            .*"    A$$$$$$$$o.4;      .
                                 .oP""   "$$$$$$b.  .$;
                                          A$$$$$$$$$$P
                                          "  "$$$$$P"
                                              $$P*"
            mls                              .$"
                                             "
        *******************************************************************************"""
    )
    print("Your mission is to find the treasure.")

    #https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

    #Write your code below this line 👇
    direction = input("Go left or right? ")
    if direction.lower() == "left":
        print("Yay! You survived.")
        swimwait = input("Would you like to walk, or drive? ")
        if swimwait == "walk":
            print("Yay! You survived.")
            door = input(
                "Which door would you like to go through? Red, Blue, or Yellow? "
            )
            if door.lower() == "yellow":
                victory = True
                input(
                    """8b           d8 88                                                       
`8b         d8' ""              ,d                                       
 `8b       d8'                  88                                       
  `8b     d8'   88  ,adPPYba, MM88MMM ,adPPYba,  8b,dPPYba, 8b       d8  
   `8b   d8'    88 a8"     ""   88   a8"     "8a 88P'   "Y8 `8b     d8'  
    `8b d8'     88 8b           88   8b       d8 88          `8b   d8'   
     `888'      88 "8a,   ,aa   88,  "8a,   ,a8" 88           `8b,d8'    
      `8'       88  `"Ybbd8"'   "Y888 `"YbbdP"'  88             Y88'     
                                                                d8'      
                                                               d8' """)
            elif door.lower() == "red":
                input("Burned by fire. Game over.")
            elif door.lower() == "blue":
                input("Eaten by beasts. Game over.")
            else:
                input("Game over.")
        else:
            input("Attacked by serpent. Game over.")
    else:
        input("You fell into a hole. Game over.")
