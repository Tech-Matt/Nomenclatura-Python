'''
Programma di Nomenclatura dei Composti Binari
----------------------------------------------------------
Il programma interpreta una scritta tipo "HCl" e visualizza come risultato:
"Nomenclatura IUPAC: Cloruro di Idrogeno
 Nomenclatura Tradizionale: Acido Cloridrico"
'''
#File utile per i nomi degli elementi
nomi_el = open("elementi.txt", "r")

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


#Formula chimica nel formato "PCl3" (elemento-indice)
formula = input("Inserisci la formula chimica: ")

#Lista che contiene gli elementi scritti nella formula
elementi = []

#lista che contiene gli indici degli elementi
indici = []

#Leggo ogni lettera in formula
for i in range(len(formula)):
    if formula[i].isupper() == True: #Controllo se la lettera e' maiuscola o minuscola per memorizzare l'elemento
        if (len(formula) - 1) == i: #Se mi trovo a fine riga
            elementi.append(formula[i]) #Inserisco l'elemento nella lista per evitare che il programma vada a cercare nel carattere successivo della lista (che non esiste)
            indici.append(1) #L'indice e' necessariamente 1
        else: #Non mi trovo a fine riga
            if formula[i+1].isupper() == True: #Se anche quella dopo e' maiuscola la memorizzo nella lista
                elementi.append(formula[i])
                indici.append(1) #Aggiungo l'indice "1" alla lista
            elif formula[i+1].islower() == True:
                elementi.append(formula[i] + formula[i + 1]) #Se la lettera dopo e' minuscola inserisco entrambe le lettere nella lista
                #Controllo se dopo c'e' un indice
                if (i + 1) == (len(formula) - 1): #Se questo era l'ultimo carattere
                    indici.append(1) #L'indice e' necessariamente 1
                elif formula[i+2].isdigit() == True: #Controllo l'indice
                    indici.append(int(formula[i+2]))
                else: #Altrimenti la lettera dopo e' maiuscola e l'indice e' 1
                    indici.append(1)

            elif formula[i+1].isdigit() == True: #Se la lettera dopo e' una cifra (indice)
                elementi.append(formula[i]) #Aggiungo il primo elemento alla lista
                indici.append(int(formula[i+1])) #Aggiungo l'indice del primo elemento alla lista


#Funzionante. Hai correttamente salvato e interpretato la formula. Ora inizia l'elaborazione.
#Memorizza elettronegativita' o numeri di ossidazione o altro per fare Nomenclatura IUPAC.

'''Nomenclatura IUPAC'''

#Nome finale IUPAC
nomeIupac = ""

#Prefissi della IUPAC
prefissi = ["Mono", "Di", "Tri", "Tetra", "Penta", "Esa", "Epta", "Octo", "Enna", "Deca"]

'''Ossidi'''
#Per essere un Ossido il composto deve avere al suo interno l'Ossigeno
for i in range(len(elementi)):
    if elementi[i] == "O":
        #Indice ossigeno
        ind_oss = indici[i]
        #Trovo l'indice dell'altro elemento. Per farlo creo un ciclo dove cerco l'indice dell'ossigeno e se il valore e' diseguale lo salvo
        for x in range(len(indici)):
            if indici[x] != ind_oss:
                #indice altro elemento
                ind_2 = indici[x]
        #Trovo il secondo elemento
        elem_2 = ""
        for z in range(len(elementi)):
            if elementi[z] != "O":
                elem_2 = elementi[z]
        #Formula IUPAC dell'Ossido (la lista prefissi e' sfalsata di 1 rispetto agli indici degli elementi)
        nomeIupac = prefissi[ind_oss - 1] + "ossido di " + prefissi[ind_2 - 1] + dic[elem_2]

print("Formula IUPAC: " + nomeIupac)
