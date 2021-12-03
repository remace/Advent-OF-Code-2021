from Submarine import elvesSubmarine
from controlSubmarine import controlSubmarine
from BinaryDiagnostic import BinaryDiagnostic

# day 1 elvesSubmarine
print('\nday 1: elves submarine radar')
print(f"la profondeur augmente {elvesSubmarine.main()} fois sur l'échantillon.")
print(f"la profondeur augmente {elvesSubmarine.main2()} fois sur l'échantillon avec une fenêtre de 3 mesures")

# day 2 controlSubmarine
print('\nday 2: submarine drive')
print(f"la multiplication de la profondeur finale par l'avance finale est de {controlSubmarine.main()}")
print(f"la multiplication de la profondeur finale par l'avance finale est de {controlSubmarine.main2()}")

# day 3 binaryDiagnostic
print('\nday 3: Binary Biagnostic')
print(f'consommation d"énergie du sous-marin: {BinaryDiagnostic.main()}')
print(f'indice de vivabilité: {BinaryDiagnostic.main2()}')