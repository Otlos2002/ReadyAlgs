def bubble_sort(elements):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            a = elements[j]
            b = elements[j+1]

            if a > b:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True

        if not swapped:
            break


def bubble_sort_descending(elements):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            a = elements[j]
            b = elements[j+1]

            if a < b:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True

        if not swapped:
            break


def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i-1
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j-1
        elements[j+1] = anchor

def insertion_sort_descending(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i-1
        while j >= 0 and anchor > elements[j]:
            elements[j+1] = elements[j]
            j = j-1
        elements[j+1] = anchor


def selection_sort(lista: list):
    size = len(lista)
    list1 = []
    for i in range(size-1):
        min_index = i
        for j in range(min_index+1, size):
            if lista[j] < lista[min_index]:
                min_index = j

        if i != min_index:
            lista[i], lista[min_index] = lista[min_index], lista[i]

def selection_sort_descending(lista: list):
    size = len(lista)
    list1 = []
    for i in range(size-1):
        min_index = i
        for j in range(min_index+1, size):
            if lista[j] > lista[min_index]:
                min_index = j

        if i != min_index:
            lista[i], lista[min_index] = lista[min_index], lista[i]