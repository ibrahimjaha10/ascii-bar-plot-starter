import csv

def load_rows(csv_path):
    """Liest die CSV-Datei ein und gibt eine Liste von Tupeln zurück."""
    rows = []
    with open(csv_path, newline="", encoding="utf-8") as file:
        # DictReader nutzt die erste Zeile (type, value1, value2) automatisch als Schlüssel
        reader = csv.DictReader(file)
        
        for row in reader:
            point_type = row["type"]
            # Die Werte aus der CSV sind noch Text (Strings), wir machen Kommazahlen (floats) daraus
            val1 = float(row["value1"])
            val2 = float(row["value2"])
            
            # Als Tupel an die Liste anhängen
            rows.append((point_type, val1, val2))
            
    return rows