from numpy import sqrt

# Fonction pour calculer la distance euclidienne entre deux points dans l'espace des caractéristiques
def distance(test_data, comp_point):
    dist = sqrt((float(comp_point[0])-float(test_data[0]))**2 + (float(comp_point[1])-float(test_data[1]))**2 +
                (float(comp_point[2])-float(test_data[2]))**2 + (float(comp_point[3])-float(test_data[3]))**2)
    return dist

def Print_List(plist,i):
    print(f"{i} point distance is : {plist[0]} and the category is {plist[1]}")


def Find_Cat(distances,k):
    countA = 0
    countB = 0
    countC = 0
    for i in range(k):
        if distances[i][1] == 'Iris-setosa':
            countA = countA + 1
        elif distances[i][1] == 'Iris-versicolor':
            countB = countB + 1
        elif distances[i][1] == 'Iris-virginica':
            countC = countC + 1;
    if (countA >= countB) and (countA >= countC):
       largest = 'Iris-setosa'
    elif (countB >= countA) and (countB >= countC):
       largest = 'Iris-versicolor'
    else:
       largest = 'Iris-virginica'
    return largest


def Knn(file,k,test_data):
    with open(file) as f:
        lines = f.readlines()
    
    cleanlist = []
    for i in range(len(lines)):
        cleanlist.append(lines[i].strip('\n'))
    
    training_data = []
    for i in range(len(cleanlist)):
        training_data.append(cleanlist[i].split(','))
    training_data.pop()
    print('[!] training_data imported !')
    distances = []
    for i in range(len(training_data)):
        ret_list = []
        ret_list.append(distance(test_data,training_data[i]))
        ret_list.append(training_data[i][4])
        distances.append(ret_list)
    distances.sort()
    print("[!] Distances computed")
    print("[!] Printing k best distances...")
    
    for i in range(k):
        Print_List(distances[i], i)
    
    print("[!] Calculating most propable category...")
    largest = Find_Cat(distances,k)
    print(f"[!] most probable category is : {largest}")
    
    
def main():
    file = 'C:/Users/paulc/Desktop/python/IA3-ml_data_iris.txt'
    k = 5
    test_data = [5.0,1.5,2.4,1.2]
    Knn(file,k,test_data)
    
if __name__ == '__main__':
    main()