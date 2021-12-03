""" day 3: Binary Diagnostic """
from Mixins.mixins import read_file


def most_then_least_common_bits(dataset):
     # initialiser cumul. ce tableau va compter pour chaque colonne le nombre de 1
    cumul = []
    for index in range(dataset[0].__len__()):
        cumul.append(0)

    for line in dataset:
        for index in range(dataset[0].__len__()):
            index2 = index
            cumul[index] += int(line[index2])

    # créer le tableau des bits majoritaires
    most_common_bits = []
    for index in range(dataset[0].__len__()):
        most_common_bits.append('0')
    for index in range(dataset[0].__len__()):
        most_common_bits[index] = '0' if cumul[index] < dataset.__len__()/2 else '1'
    least_common_bits = []
    for bit in most_common_bits:
        least_common_bits.append('0' if bit == '1' else '1')
    
    return most_common_bits, least_common_bits

def main():
    gamma_rate_binary = ''
    epsilon_rate_binary = ''

    dataset = read_file("./BinaryDiagnostic/dataset_final.csv")
    
    most_common_bits, least_common_bits = most_then_least_common_bits(dataset)
    with open("./BinaryDiagnostic/answer1.csv","w") as f:
        # reconstruire chaque valeur de taux: epsilon et gamma
        f.write(f"most common bits: {most_common_bits}\nleast common bits:{least_common_bits}\n")
        most_common_bits.reverse()
        least_common_bits.reverse()
        gamma_rate = 0
        for index, bit in enumerate(most_common_bits):
            gamma_rate += int(bit)*2**index
        epsilon_rate=0
        for index, bit in enumerate(least_common_bits):
            epsilon_rate += int(bit)*2**index
        f.write(f'gamma rate: {gamma_rate}\tepsilon rate: {epsilon_rate}\tenergy_consumption_rate: {gamma_rate*epsilon_rate}')
    return gamma_rate*epsilon_rate


def main2():
    
    dataset = read_file("./BinaryDiagnostic/dataset_final.csv")
    most_common_bits, least_common_bits = most_then_least_common_bits(dataset)

    with open("./BinaryDiagnostic/answer2.csv","w") as f:

        # calculate oxygen generator rating
        i=0
        while dataset.__len__() > 1:
            most_common = most_common_bits[i]
            
            new_dataset = []
            for line in dataset:
                if line[i] == most_common:
                    new_dataset.append(line)
            i+=1
            dataset = new_dataset
            most_common_bits, _= most_then_least_common_bits(dataset)  
        
        dataset_reversed = dataset[0][::-1]
        oxygen_generator_rating = 0
        for index, bit in enumerate(dataset_reversed):
            oxygen_generator_rating += int(bit)*2**index

        f.write(f"O2 generator filtered value: {dataset[0]} -> oxygen generator rating: {oxygen_generator_rating}\n")

        # CO2 rating
        dataset = read_file("./BinaryDiagnostic/dataset_final.csv")
        _,least_common_bits = most_then_least_common_bits(dataset)

        # calcul de l'oxygen generatir rating
        i=0
        while dataset.__len__() > 1:
            least_common = least_common_bits[i]
            
            new_dataset = []
            for line in dataset:
                if line[i] == least_common:
                    new_dataset.append(line)
            i+=1
            dataset = new_dataset
            _, least_common_bits= most_then_least_common_bits(dataset)  
        
        dataset_reversed = dataset[0][::-1]
        CO2_scrubber_rating = 0
        for index, bit in enumerate(dataset_reversed):
            CO2_scrubber_rating += int(bit)*2**index

        f.write(f"CO2 scrubber filtered value: {dataset[0]} -> CO2 scrubber rating: {CO2_scrubber_rating}\n")

        f.write(f'life support rating: {oxygen_generator_rating * CO2_scrubber_rating}')
    return oxygen_generator_rating * CO2_scrubber_rating