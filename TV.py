class TV: #definerar klassen tv med egenskaperna namn, antal kanaler och volym
    def __init__(self, namn, max_kanaler, aktuell_kanal, max_volym, aktuell_volym):
        #init är en konstruktor som anropas när ett objekt av klassen tv skapas, sätter tvs attribut
        self.namn = namn 
        self.max_kanaler = int(max_kanaler) #self.märke hänvisar till objektets attribud marke
        self.aktuell_kanal = int(aktuell_kanal)
        self.max_volym = int(max_volym)
        self.aktuell_volym = int(aktuell_volym)

    def change_channel(self, ny_kanal): #för kanalbyte
        if 1 <= ny_kanal <= self.max_kanaler: #kontrollera om kanalen är inom giltigt intervall
            self.aktuell_kanal = ny_kanal #om kanalen finns så byts den
            #print(f"Kanal ändrad till: {self.aktuell_kanal}") #skriver ut de
        else:
            print(f"Kanal {ny_kanal} är ogiltig. Välj en kanal mellan 1 och {self.max_kanaler}.") #om kanalen inte finns 

    def increase_volume(self):
        if self.aktuell_volym < self.max_volym:  # Korrigerat till self.aktuell_volym
            self.aktuell_volym += 1  # Ökar aktuell_volym
            #print(f"Volymen höjd till: {self.aktuell_volym}")  # Skriver ut förändringen
        else:
            print(f"Volymen är redan på max ({self.max_volym}).")

    def decrease_volume(self):
        if self.aktuell_volym > 0:  # Korrigerat till self.aktuell_volym
            self.aktuell_volym -= 1  # Minskar aktuell_volym
            #print(f"Volymen sänkt till: {self.aktuell_volym}")  # Skriver ut förändringen
        else:
            print("Volymen är redan på min (0).")  # Meddelande om volymen är på min
       
    def __str__(self):
        return f"TV:{self.namn}, Kanal: {self.aktuell_kanal}, Volym: {self.aktuell_volym}"


    def str_for_file(self): #funk används för o definiera hur en instans av tv ska representeras som en sträng
        return f"{self.namn},{self.max_kanaler},{self.aktuell_kanal},{self.max_volym},{self.aktuell_volym}"
#här får vi tillbaka den kommaseparerad tvn med dess egenskaper

def read_file(filename): #funk för o läsa fil o skapa tv objekt baserat på filens innehåll
    tv_list = [] #tom lista för att lagra tv objekt
    try:
        with open(filename, 'r',encoding='utf-8') as file:
            for line in file: #delar upp varje rad i en litamed hjälp av kommatecken som separerar
                data = line.strip().split(',')
                if len(data) == 5: #kontrollera att raden har 5 värden alltså namn, maxk, ak, mv o av
                    tv = TV(data[0], data[1], data[2], data[3], data[4]) #skapar tv objekt med datan som hätats från filen
                    tv_list.append(tv) #lägger till de i den tomma listan.
    except FileNotFoundError:
        print(f"Fil {filename} hittades inte. Inga TV-apparater laddades.") #om fil ej hittas
    return tv_list #returnerar listan med tv objekt


def write_file(tv_list, filename): #funk för att skriva en lita med tv objekt till en fil
    with open(filename, 'w',encoding='utf-8') as file: #skriver över de som finns med w
        for tv in tv_list:
            file.write(str(tv.str_for_file() + '\n')) #skriver reprensationenen av tvn som en sträng till filen