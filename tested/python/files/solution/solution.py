import sys

bronbestandslocatie = sys.argv[1]
doelbestandslocatie = sys.argv[2]

with open(bronbestandslocatie, 'r') as bronbestand:
    inhoud = bronbestand.readlines()

inhoud.sort()

with open(doelbestandslocatie, 'w') as doelbestand:
    doelbestand.writelines(inhoud)
