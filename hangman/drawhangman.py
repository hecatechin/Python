def drawhangman(lefttime):
    """
    :param lefttime: the number of gesses left in the hangman game
    :return: a string that shows the picture of the game prosess
    """

    hangstr=["    _________\n　　｜　　　　｜\n　　", \
             "　",
             "　　　　｜\n　", \
             "　", \
             "　", \
             "　", \
             "　　　｜\n　　", \
             "　", \
             "　　　　｜\n　　　　　　　｜\n      　￣￣￣￣\n"]
    failchars = ["〇","〨","乀","丿","ㄏ","𠘨","囧","丿","亅"]
    result = ""

    if lefttime <= 6:
        hangstr[1]=failchars[0]
        if lefttime <=5:
            hangstr[4] = failchars[1]
            if lefttime <= 4:
                hangstr[3] = failchars[2]
                if lefttime <=3 :
                    hangstr[5] = failchars[3]
                    if lefttime <=2:
                        hangstr[7] = failchars[4]
                        if lefttime <= 1:
                            hangstr[7] = failchars[5]
                            if lefttime == 0:
                                hangstr[1] = failchars[6]
                                hangstr[3] = failchars[7]
                                hangstr[5] = failchars[8]

    if lefttime < 8:
        for strs in hangstr:
            result += strs
        return result
    else:
        return "The hanging is on the way! Guesses countdown: "+str(lefttime-8)

print(drawhangman(0),end="")
