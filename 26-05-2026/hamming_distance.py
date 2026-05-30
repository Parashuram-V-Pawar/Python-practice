def hamming_distance(a: int, b: int):
    distance = (a ^ b).bit_count()
    print(distance)

hamming_distance(1, 4)
