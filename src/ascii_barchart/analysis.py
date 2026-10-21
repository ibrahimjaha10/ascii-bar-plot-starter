def average_value1_by_type(rows):
    """Berechnet den Durchschnitt von value1 für jeden Typ (A, B, C, D)."""
    sums = {}
    counts = {}
    
    # Werte aufsummieren und zählen
    for point_type, val1, val2 in rows:
        if point_type not in sums:
            sums[point_type] = 0
            counts[point_type] = 0
            
        sums[point_type] += val1
        counts[point_type] += 1
        
    # Durchschnitte berechnen und runden
    averages = []
    # sorted() sorgt dafür, dass die Reihenfolge immer A, B, C, D ist
    for pt in sorted(sums.keys()):
        avg = sums[pt] / counts[pt]
        averages.append((pt, round(avg, 2)))
        
    return averages