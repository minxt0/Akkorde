tonleiter = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

note = ""
gr_terz = 4
quinte = 7
list_len = len(tonleiter)

note = input("Note hier eingeben: ").upper()

if note not in tonleiter:
    print("Ungültige Eingabe")
else:
    #searching for position of note in list
    for i,j in enumerate(tonleiter):
        if j == note:
            notenpos = i 
            break    
    #setting position of qr_terz and quinte based of notenpos
    gr_terz_pos = notenpos+gr_terz
    quinte_pos = notenpos+quinte
    #checking if position of gr_terz and quinte is bigger then len of list
    if gr_terz_pos >= list_len:
        gr_terz_pos = gr_terz_pos-list_len
        quinte_pos = quinte_pos-list_len
    elif quinte_pos >= list_len:
        quinte_pos = quinte_pos-list_len
    #output of Akkord
    print(tonleiter[notenpos],tonleiter[gr_terz_pos],tonleiter[quinte_pos])

