promt = ">   "
resp = " "
within_Loop = False
print_message = False
def for_Whit_Print_Emulated(message, ini, end):
    if ( len(message) != 0 ):
        for x in range(ini, end):
            print (message)

# Main Loop
while ( resp != "exit" ):

    resp = raw_input(promt)
    line = resp.split()

    # Change to "tokens"
    if ( line[0] == "for" ):
        within_Loop = True
        # Scan "For" parameters
        ini_Loop = int(line[1])
        end_Loop = int(line[2])

    if ( line[0] == "print" and within_Loop ):
        message = line[1]
        print_message = True

    if ( line[0] == "forend" ):
        within_Loop = False
        if ( print_message ):
            for_Whit_Print_Emulated(message, ini_Loop, end_Loop)
        else:
            print ("Error")

    # Rules for end main loop
    if (within_Loop):
        promt = ">..."
    else:
        promt = ">"

# End main loop
print("Off-Loop")