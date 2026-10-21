def average_value1_by_type(rows):
    sums = {}
    counts = {}
    
    for point_type, val1, val2 in rows:
        if point_type not in sums:
            sums[point_type] = 0
            counts[point_type] = 0
        sums[point_type] += val1
        counts[point_type] += 1
        
    averages = []
    for pt in sorted(sums.keys()):
        avg = sums[pt] / counts[pt]
        averages.append((pt, round(avg, 2)))
        
    return averages