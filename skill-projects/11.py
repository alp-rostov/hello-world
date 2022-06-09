array = [i for i in range(1000000)]
for i in range(len(array)): # проходим по всему массиву

        idx_min = i # сохраняем индекс предположительно минимального элемента
        for j in range(i+1, len(array)):
            if array[j] > array[idx_min]:
                idx_min = j

                array[i], array[idx_min] = array[idx_min], array[i]

print(array)
print(count)