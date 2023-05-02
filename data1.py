people = {
    'Igor': 'male',
    'Andrey': 'male',
    'Viktor': 'male',
    'Vladilen': 'male',
    'Maksim': 'male',

    'Luda': 'female',
    'Gala': 'female',
    'Roza': 'female',
    'Lila': 'female',
    'Inga': 'female'
}

parentChild = {
    'Luda': ['Igor', 'Inga'],
    'Viktor': ['Igor', 'Inga'],
    'Inga': ['Andrey', 'Lila'],
    'Maksim': ['Andrey', 'Lila'],
    'Gala': ['Luda'],
    'Roza': ['Viktor'],
    'Vladilen': ['Viktor']
}


def is_mother(x, y):
    return x in parentChild and y in parentChild[x] and people[x] == 'female'


def is_father(x, y):
    return x in parentChild and y in parentChild[x] and people[x] == 'male'


def is_son(x, y):
    return y in parentChild and x in parentChild[y] and people[x] == 'male'


def is_daughter(x, y):
    return y in parentChild and x in parentChild[y] and people[x] == 'female'


def is_grand_father(grand_father, child):
    return child in get_grand_children(grand_father) and people[grand_father] == 'male'


def is_grand_mother(grand_mother, child):
    return child in get_grand_children(grand_mother) and people[grand_mother] == 'female'


def is_grand_son(son, grand_parent):
    return son in get_grand_children(grand_parent) and people[son] == 'male'


def is_grand_daughter(daughter, grand_parent):
    return daughter in get_grand_children(grand_parent) and people[daughter] == 'female'


def get_grand_children(person):
    grand_children = []

    if person in parentChild.keys():
        children = parentChild[person]
        for child in children:
            if child in parentChild.keys():
                grand_children += parentChild[child]

    return grand_children


print(is_son('Igor', 'Maksim'))
print(is_son('Igor', 'Luda'))
print(is_son('Inga', 'Luda'))

print(is_grand_son('Igor', 'Luda'))
print(is_grand_son('Igor', 'Roza'))
print(is_grand_mother('Roza', 'Luda'))
print(is_grand_mother('Roza', 'Igor'))





