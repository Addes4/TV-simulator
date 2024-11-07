from TV import TV, read_file, write_file 
#importerar från modulen tv o write_file för att skriva en lista till en fil
#read file för o skapa en lista med dessa objekt
def change_channel(tv):  # funk för att ändra kanal på tv
    while True:
        try:
            ny_kanal = int(input(f"Ange ny kanal (1-{tv.max_kanaler}): "))  # användaren får välja ny kanal
            if 1 <= ny_kanal <= tv.max_kanaler:  # kontrollera om kanalen är inom giltigt intervall
                tv.change_channel(ny_kanal)  # anropar funktionen för att byta kanal
                print(f"\n{tv.namn} \nKanal: {tv.aktuell_kanal} \nLjudnivå: {tv.aktuell_volym}")
                break  # lämnar loopen när en giltig kanal är vald
            else:
                print(f"Kanal {ny_kanal} är ogiltig. Välj en kanal mellan 1 och {tv.max_kanaler}.")
        except ValueError:
            print("Ogiltig inmatning. Ange en siffra.")  # hanterar valueerror om användaren ej matar in siffra


def increase_volume(tv): #öka volym på tv
    if tv.aktuell_volym < tv.max_volym: #kontrollera så den inte är på max
        tv.increase_volume() #öka den med 1 med funk vi importerade
        print(f"\n{tv.namn} \nKanal: {tv.aktuell_kanal} \nLjudnivå: {tv.aktuell_volym}")
    else:
        print(f"Volymen är redan på max ({tv.max_volym}).") #om volymen är på max

def decrease_volume(tv): #minska volymen
    if tv.aktuell_volym > 0: #om volymen inte är lägsta
        tv.decrease_volume() #minska med 1 med importerad funk
        print(f"\n{tv.namn} \nKanal: {tv.aktuell_kanal} \nLjudnivå: {tv.aktuell_volym}")
    else:
        print("Volymen är redan på min (0).")

def adjust_TV_menu(): #funk för o visa en meny där användaren kan välja justera tvn
    print("\n1. Byt kanal")
    print("2. Sänk ljudnivå")   
    print("3. Höj ljudnivå")  
    print("4. Gå till huvudmenyn")  
    try: #låter användaren välja
        val = int(input("Välj ett alternativ: "))
        if val in [1, 2, 3, 4]: #om de är 1-4 så går de
            return val
        else:
            print("Fel val, försök igen.") #hantera fel
            return adjust_TV_menu()
    except ValueError: #fångar fel om användaren inte matar in ett giltilgt tal
        print("Ogiltig inmatning. Ange ett nummer.")
        return adjust_TV_menu()

def select_TV_menu(tv_list): #funk för o välja en tv från listan med tv apparater
    print("\n")
    for i, tv in enumerate(tv_list): #loopar igenom alla tv objekt o visar deras index,namn ak och volym
        print(f"{i + 1}. {tv.namn}")
    print(f"{len(tv_list) + 1}. Avsluta simulatorn") #lägger vi till ett alternativ för att avsluta simulatorn
    
    try: #låter användaren välja en tv från listan
        val = int(input("Gör ett val: "))
        if val == len(tv_list) + 1:
            return None  # Användaren vill avsluta
        elif 1 <= val <= len(tv_list):
            return tv_list[val - 1]  # Returnera vald TV om de är giltigt index
        else:
            print("Ogiltigt val. Försök igen.") #felhantering
            return select_TV_menu(tv_list)
    except ValueError:
        print("Ogiltig inmatning. Ange ett nummer.") #hanterar valueerror inte giltigt tal
        return select_TV_menu(tv_list)

def huvudprogram(): #huvudprogram som kör hela simulatorn
    print("***Välkommen till TV-simulatorn****")
    filnamn = "/Users/adriansohrabi/Desktop/Laboration 5/tv_data.txt"
    tv_obj_list = read_file(filnamn)  # Hämta TV-objekten från fil

    while True: #loop som låter anävnadren välja en tv och göra justeringar
        selected_tv = select_TV_menu(tv_obj_list)  # Välj en TV
        if selected_tv is None:  # Avsluta programmet
            print("Simuleringen Avslutas")
            break #avbryter huvudloopen o går ut

        print(f"\n{selected_tv.namn} \nKanal: {selected_tv.aktuell_kanal} \nLjudnivå: {selected_tv.aktuell_volym}")  
        
        while True: #loop som visar menyn för att justera den valda tvn
            val = adjust_TV_menu()  
            if val == 1:  # Byt kanal
                change_channel(selected_tv)
            elif val == 2:  # Höj volym
                decrease_volume(selected_tv)
            elif val == 3:  # Sänk volym
                increase_volume(selected_tv)
            elif val == 4:  # Återgå till huvudmenyn
                break

    write_file(tv_obj_list, filnamn)  # Spara uppdaterad information till fil


huvudprogram()