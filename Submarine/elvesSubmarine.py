""" day 1: Submarine sonar """

from Mixins.mixins import read_file


def main():
    dataset = read_file("./Submarine/dataset.csv")
    count = 0
    with open("./Submarine/answer1.csv","w") as f:
        for i in range(1,len(dataset)):
            if int(dataset[i]) > int(dataset[i-1]):
                count+=1
            f.write(f"i: {i}, data: {dataset[i]}, previous:{dataset[i-1]}, count: {count}, line:{'increased' if dataset[i]> dataset[i-1] else 'decreased'}\n")
    
        f.write(f"\n\n réponse: la profondeur augmente {count} fois sur l'échantillon.")
    return count

def main2():
    dataset = read_file("./Submarine/dataset.csv")
    count = 0
    with open("./Submarine/answer2.csv","w") as f:
        for i in range(3,len(dataset)):
            if int(dataset[i]) > int(dataset[i-3]):
                count+=1
            f.write(f"cas {i-2}: série 1:{dataset[i-3]} {dataset[i-2]} {dataset[i-1]} somme: {int(dataset[i-1])+int(dataset[i-2])+int(dataset[i-3])} \t série 2: {dataset[i-2]} {dataset[i-1]} {dataset[i]} somme:{int(dataset[i-2])+int(dataset[i-1])+int(dataset[i])} \t résultat:{'increased' if int(dataset[i-2])+int(dataset[i-1])+int(dataset[i]) > int(dataset[i-3])+int(dataset[i-2])+int(dataset[i-1]) else 'decreased'}, count: {count}")
        f.write(f"\n\n réponse: la profondeur augmente {count} fois sur l'échantillon.")
    return count
