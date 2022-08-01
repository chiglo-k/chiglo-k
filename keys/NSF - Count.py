
def count (total_count, total_box):
    count_1 = total_count / total_box # на общий вес
    return count_1


def count_nsf (weight_on_all, count_2):
    nsf_total = count_2 / weight_on_all # NSF по весу
    return nsf_total


total_count = int(input('\nКоличество продукции : '))
total_box = int(input('\nКоличество ящиков : '))
weight_on_all = count(total_count, total_box)
print(f'\nОбщее {weight_on_all}')
number_of_grade = int(input('\nВведите сколько размеров продукции : '))
while number_of_grade != 0 :
    number_of_grade -= 1
    count_2 = int(input('\nВведите количество: '))
    nsf = count_nsf (weight_on_all, count_2)
    print(f'\nКоличество образцов: {nsf}')
else:
    print(f'\nEnd {nsf}')
