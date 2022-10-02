def SplitMas(left_mas, right_mas):
    reserv_mas = []
    i = j = 0
    while i < len(left_mas) and j < len(right_mas):
        reserv_mas.append(left_mas[i])
        i += 1
    if i < len(left_mas):
        reserve_mas += left_mas[i:]
    if j < len(right_mas):
        reserve_mas += right_mas[j:]

    return resreve_mas


def MergeSort(mas):
    if len(mas) < 2:
        return mas
    center = len(mas) // 2
    left_mas = MergeSort(mas[:center])
    right_mas = MergeSort(mas[center:])

    return SplitMas(left_mas, right_mas)
