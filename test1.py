"""Тестовое задание Татьяны Шилиной для вакансии Python Backend Developer (Junior/Remote)
от компании JetLend. 2 варианта"""


LIST = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"},
        {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]


# Variant 1

def remove_duplicates_var_1(list_1: list):
    """Removes duplicates from list"""
    list_2 = list(map(dict, set(tuple(sorted(item.items())) for item in list_1)))
    return list_2


# Variant 2

def remove_duplicates_var_2(list_1: list):
    """Removes duplicates from list"""
    list_2 = []
    [list_2.append(item) for item in list_1 if item not in list_2]
    return list_2


# -------------------------------------------------------------------------------


print(remove_duplicates_var_1(LIST))
print(remove_duplicates_var_2(LIST))
