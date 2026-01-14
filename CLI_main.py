from generator import generate_plate

print("=== Générateur de Matricules Algériens (Format Moderne) ===")

vehicle_type = int(input("Type du véhicule (0-9) : "))
year = int(input("Année (1985–2084) : "))
serial = int(input("Numéro de série : "))

plate = generate_plate(vehicle_type, year, serial)
print("Matricule généré :", plate)
