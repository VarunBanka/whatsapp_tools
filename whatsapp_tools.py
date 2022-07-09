def start():
    import pywhatkit
    print(
        "A)Send a message to a group \n"
        "B)Send a WhatsApp Message to a Contact at 12 AM \n"
        "C)Send a WhatsApp Message to a Group at 12:00 AM \n"
        "D)Ask anything \n"
    )
    to_do = input("Select a option ")

    if to_do == "A" or to_do == "a" or to_do == "1":
        try:
            grp_name = input("enter the name of group \n ")
            msg = input("enter your message \n")
            pywhatkit.sendwhatmsg_to_group_instantly(grp_name, msg)

        except:
            # code by Dev Varun
            print("An unknown error occurred")

    if to_do == "B" or to_do == "b" or to_do == "1":
        try:
            number = input("enter a number \n")
            msg = input("enter your message \n")
            pywhatkit.sendwhatmsg(number, msg, 00, 00)
        except:
            print("An unknown error occurred")

    if to_do == "C" or to_do == "c" or to_do == "3":
        try:
            grp_name = input("enter the name of group \n ")
            msg = input("enter your message \n")
            pywhatkit.sendwhatmsg_to_group(grp_name, msg, 0, 0)
        except:
            print("An unknown error occurred")

    if to_do == "D" or to_do == "d" or to_do == "3":
        try:
            to_search = input("enter your quary  \n")
            pywhatkit.search(to_search)
        except:
            print("An unknown error occurred")


start()


def restart_and_exit():
    print("do you want to restart ? \n")
    restart = input("y/n \n")
    if restart == "y":
        start()
    if restart == "n":
        print("okay, exiting.....")
        print("end of program")
        exit()


restart_and_exit()

xyz_pro_plus = 1

while (xyz_pro_plus < 2):
    restart_and_exit()
