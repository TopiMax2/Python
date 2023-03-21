#TD1 Langage Python - Paul CUCHET (TD-D)
#%% Exercice 1

def Exo1():
    temps = 6.892
    distance = 19.7
    vitesse = distance/temps
    print(f'la vitesse est : {vitesse}')
    print(f'{vitesse:.2f}')
    
#%% Exercice 2

def Exo2Q1(value1,value2):
    if(value1 >= value2):
        print('max = ', value1, ' min = ', value2)
    else:
        print('max = ', value2, ' min = ', value1)

def Exo2Q2(value1,value2):
    if(value1 >= value2):
        print('max = ', value1, ' min = ', value2)
    if(value2 >= value1):
        print('max = ', value2, ' min = ', value1)
    
def Exo2Q3(value1, value2):
    max = value1 if value1 >= value2 else value2
    min = value1 if value1 <= value2 else value2
    print('max = ',max,' min = ',min)
#%% Exercice 3

def volBoite(x1=None, x2=None, x3=None):
    if x1 is None and x2 is None and x3 is None:
        return -1
    if x2 is None and x3 is None:
        # Si un seul argument est entrer
        return pow(x1,3)
    elif x3 is None:
        return pow(x1,2)*x2
    else:
        return x1*x2*x3
    
#%% Exercice 4

def eleMax(liste,debut=0,fin=None):
    if(fin == None):
        fin = len(liste)
    if(debut > fin):
        debut, fin = fin, debut
    maxele = 0
    for i in range(debut,fin):
        if liste[i] > maxele:
            maxele = liste[i]
    return maxele
    
#%% Exercice 5

def Exo5(t1,t2):
    length = len(t1)+len(t2)
    t3 = []
    index1 = 0
    index2 = 0
    for i in range(length):
        if(i%2 == 0):
            t3.append(t2[index1])
            index1 += 1
        else:
            t3.append(t1[index2])
            index2 += 1
            
    return t3
    
#%% Exercice 6

def Exo6(string):
    return string[::-1]

#%% Exercice 7

def mafonction(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#%% Exercice 8

def Exo8(start):
    while(start != 0):
        print(start)
        start -= 1
    print("Go!")

#%% Exercice 9

def Exo9(string):
    if(string == string[::-1]):
        print(string,"is palindrome")
    else:
        print(string, "is not palindrome")

#%% Exercice 10

def Exo10(list):
    
    list11 = list+list[::-1]
    print(list11)
    
    list12 = []
    for i in range(3):
        for j in range(4):
            list12.append(list[j])
    print(list12)
    
    length = len(list)
    list13 = []
    for i in range(length):
        if(i%3 == 0):
            list13.append(list[i])
    print(list13)
    
#%% Exercice 11

def Exo11(x):
    return "pair" if x%2 == 0 else "impair"

#%% Exercice 12

def Exo12(string):
    split_string = string.split(" ")
    result = ""
    for i in range(len(split_string)):
        result += split_string[i][0]
    return result

#%% Exercice 13

def Exo13(chaine,c):
    sum = 0
    for i in range(len(chaine)):
        if(chaine[i] == c):
            sum += 1
    print(f"{c} apparait ",sum,"fois dans ",chaine)
    
#%% Exercice 14

def vowel_count(chaine):
    vowels = ['a','e','i','o','u','y','A','E','I','O','U','Y']
    sum = 0
    for i in range(len(chaine)):
        if chaine[i] in vowels:
            sum += 1
    print(chaine,'contient',sum,'voyelles')
    
#%% Exercice 15, 16 et 17

def Exo15():
    my_dict = {"pi":3.14,"mot":"mot","nombre":42,"liste":[1,2,3]}
    # Le code ci-dessous rempli l'exercice 16
    print("Entrez une valeur : ")
    user = input()
    if user in my_dict:
        print(user,"vaut",my_dict[user],"dans my_dict")
    else:
        print(user,"n'est pas dans my_dict")
    # Le code ci-dessous rempli l'exercice 17
    my_dict["hello"] = "world"
    my_dict["nombre"] = 0
    del my_dict["pi"]
    
#%% Exercice 18

def Exo18():
    
    s1 = {1,2,3}
    print("s1 =",s1)
    string = "Hello World"
    s2 = set(string)
    print("s2 =",s2)
    values = [10,20,30,40,10,2,40]
    s3 = set(values)
    print("s3 =",s3)
    s4 = set(range(5,16))
    print("s4 =",s4)
    
#%% Main

def main():
    print('TD1')
    #Exo1()
    
    #Exo2Q1(5,10)
    #Exo2Q2(4,6)
    #Exo2Q3(9,7)
    
    #print(volBoite())
    #print(volBoite(5))
    #print(volBoite(5,4))
    #print(volBoite(3,4,6))
    
    #liste = [9,3,6,1,7,5,4,8,2]
    #print(eleMax(liste))
    #print(eleMax(liste,2,5))
    #print(eleMax(liste,2))
    #print(eleMax(liste,3,1))
    
    #t1 = [31,28,31,30,31,30,31,31,30,31,30,31]
    #t2 = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']
    
    #print(Exo5(t1,t2))
    
    #print(Exo6('bonjour'))
    
    #print(mafonction(liste)) # Cette fonction est un tri de liste
    
    #Exo8(10)
    
    #Exo9("kayak")
    #Exo9("bonjour")
    
    #my_list = [0,1,2,3,4]
    #Exo10(my_list)
    
    #print(Exo11(5))
    #print(Exo11(4))
    
    #print(Exo12("Scoiété Nationale Chemin Fer"))
    
    #Exo13("test",'t')
    
    #vowel_count('ceci est une chaine test')
    
    #Exo15()
    
    Exo18()
    
if __name__ == '__main__':
    main()