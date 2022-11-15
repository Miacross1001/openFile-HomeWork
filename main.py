cook_book = {}

with open('recipes.txt', encoding='utf-8') as f:
    for line in f:
        key = line.strip()
        len_ingr = int(f.readline())
        list_ingr = []
        for _ in range(len_ingr):
            ingr = {}
            ingr['ingredient_name'], ingr['quantity'], ingr['measure'] = f.readline().split('|')
            ingr['quantity'] = int(ingr['quantity'])
            ingr['measure'] = ingr['measure'].strip()
            list_ingr.append(ingr)
        f.readline()
        cook_book[key] = list_ingr

print(cook_book)
print('\n###################################\n')
def get_shop_list_by_dishes(dishes, person_count):
    res = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredients in cook_book[dish]:
                value_for_ingr = {}
                value_for_ingr['measure'] = ingredients['measure']
                value_for_ingr['quantity'] = ingredients['quantity'] * person_count
                res[ingredients['ingredient_name']] = value_for_ingr
    return res

def sorted_files(file1 = None, file2 = None, file3 = None):
    len_file1 = len(file1.readlines())
    len_file2 = len(file2.readlines())
    len_file3 = len(file3.readlines())

    file_dict = {'1.txt': len_file1, '2.txt': len_file2, '3.txt': len_file3}
    sorted_dict = dict(sorted(file_dict.items(), key=lambda x: x[1]))

    res_file = open('file/res.txt', 'w')

    for key, value in sorted_dict.items():
        step_file = open('file/' + str(key), 'r')
        res_file.writelines(key)
        res_file.writelines('\n')
        res_file.write(step_file.read())
        res_file.writelines('\n\n')
        step_file.close()

    res_file.close()

    return sorted_dict


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

f1 = open('file/1.txt', 'r')
f2 = open('file/2.txt', 'r')
f3 = open('file/3.txt', 'r')

print(sorted_files(f1, f2, f3))

f1.close()
f2.close()
f3.close()