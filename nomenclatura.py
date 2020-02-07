'''
Programma di Nomenclatura dei Composti Binari
----------------------------------------------------------
Il programma interpreta una scritta tipo "HCl" e visualizza come risultato:
"Nomenclatura IUPAC: Cloruro di Idrogeno
 Nomenclatura Tradizionale: Acido Cloridrico"
'''

#File utile per i nomi degli elementi
with open("elementi.txt", "r") as nomi_el:
    #Dizionario che contiene I codici e i nomi degli elementi
    dic = {}
    #Popolo il dizionario
    while True:
        #Linea di testo estratta
        l = nomi_el.readline()

        #Se mi trovo alla fine esco dal ciclo
        if not l:
            break;

        #Splitto per "spazio" la stringa e inserisco la coppia in una lista
        coppia = l.split()

        #Inserisco la coppia elemento-nome nel dizionario
        dic[coppia[0]] = coppia[1]

#formula chimica nel formato "PCl3" (elemento-indice)
while True:
    ins_form = input("|Inserisci la formula chimica|: ")
    #se la stringa inserita ha una lunghezza uguale a zero ritorna un messaggio d'errore
    if len(ins_form) == 0:
        print("---!Il campo non può rimanere vuoto!---\n")
    #se la lunghezza è maggiore di zero, rompe il while True
    else:
        break

#Lista che contiene gli elementi scritti nella formula
elementi = []

#lista che contiene gli indici degli elementi
indici = []

#Leggo ogni lettera in formula
for i in range(len(ins_form)):
    if ins_form[i].isupper() == True: #Controllo se la lettera e' maiuscola o minuscola per memorizzare l'elemento
        if (len(ins_form) - 1) == i: #Se mi trovo a fine riga
            elementi.append(ins_form[i]) #Inserisco l'elemento nella lista per evitare che il programma vada a cercare nel carattere successivo della lista (che non esiste)
            indici.append(1) #L'indice e' necessariamente 1
        else: #Non mi trovo a fine riga
            if ins_form[i+1].isupper() == True: #Se anche quella dopo e' maiuscola la memorizzo nella lista
                elementi.append(ins_form[i])
                indici.append(1) #Aggiungo l'indice "1" alla lista
            elif ins_form[i+1].islower() == True:
                elementi.append(ins_form[i] + ins_form[i + 1]) #Se la lettera dopo e' minuscola inserisco entrambe le lettere nella lista
                #Controllo se dopo c'e' un indice
                if (i + 1) == (len(ins_form) - 1): #Se questo era l'ultimo carattere
                    indici.append(1) #L'indice e' necessariamente 1
                elif ins_form[i+2].isdigit() == True: #Controllo l'indice
                    indici.append(int(ins_form[i+2]))
                elif ins_form[i+2].isupper() == True: #Altrimenti la lettera dopo e' maiuscola e l'indice e' 1
                    indici.append(1)

            elif ins_form[i+1].isdigit() == True: #Se la lettera dopo e' una cifra (indice)
                elementi.append(ins_form[i]) #Aggiungo il primo elemento alla lista
                indici.append(int(ins_form[i+1])) #Aggiungo l'indice del primo elemento alla lista



#Funzionante. Hai correttamente salvato e interpretato la formula. Ora inizia l'elaborazione.
#Memorizza elettronegativita' o numeri di ossidazione o altro per fare Nomenclatura IUPAC.

'''Nomenclatura IUPAC'''

#Nome finale IUPAC
nomeIupac = ""

#Prefissi della IUPAC
prefissi = ["Mono", "Di", "Tri", "Tetra", "Penta", "Esa", "Epta", "Octo", "Enna", "Deca"]

'''Ossidi IUPAC'''
#Per essere un Ossido il composto deve avere al suo interno l'Ossigeno
for i in range(len(elementi)):
    if elementi[i] == "O":
        #Indice ossigeno
        ind_oss = indici[i]
        #Trovo l'indice dell'altro elemento.HHH
        for x in range(len(indici)):
            if x != i:
                #indice altro elemento
                ind_2 = indici[x]
        #Trovo il secondo elemento
        elem_2 = ""
        for z in range(len(elementi)):
            if elementi[z] != "O":
                elem_2 = elementi[z]
        #ìformula IUPAC dell'Ossido (la lista prefissi e' sfalsata di 1 rispetto agli indici degli elementi)
        nomeIupac = f"{prefissi[ind_oss - 1]}ossido di {prefissi[ind_2 - 1]}{dic[elem_2]}"

print(f"formula IUPAC: {nomeIupac}")
