parentChild = {
    'Luda': ['Igor', 'Inga'],
    'Viktor': ['Igor', 'Inga'],
    'Inga': ['Andrey', 'Lila'],
    'Maksim': ['Andrey', 'Lila'],
    'Gala': ['Luda'],
    'Roza': ['Viktor'],
    'Vladilen': ['Viktor']
}


def is_parent(parent, child):
    return parent in parentChild and child in parentChild[parent]


def is_child(child, parent):
    return parent in parentChild and child in parentChild[parent]


def is_grand_parent(parent, grand_child):
    return grand_child in get_grand_children(parent)


def is_grand_child(child, grand_parent):
    return child in get_grand_children(grand_parent)


def get_grand_children(person):
    grand_children = []

    if person in parentChild.keys():
        children = parentChild[person]
        for child in children:
            if child in parentChild.keys():
                grand_children += parentChild[child]

    return grand_children


print(is_child('Igor', 'Maksim'))
print(is_child('Andrey', 'Inga'))
print(is_parent('Viktor', 'Igor'))
print(is_grand_parent('Viktor', 'Igor'))
print(is_grand_parent('Viktor', 'Andrey'))
print(is_grand_parent('Gala', 'Igor'))
