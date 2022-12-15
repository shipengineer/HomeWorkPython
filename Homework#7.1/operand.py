from view import print_finded
from export_xml import create_export


def find_contact(data, item):
    for elem in data:
        if item in elem:
            print_finded(elem)


def delete_contact_ID(data, ID):
    for elem in data:
        if ID in elem:
            data.remove(elem)


def create_contact(data, item):
    mutable = list(map(dicrionary, [x.split(' ') for x in item]))
    data.append(mutable)


def dicrionary(elem):
    a1 = []
    a2 = []
    for i in range(0, len(elem)-1):
        if i % 2 == 0:
            a1.append(elem[i])
            a2.append(elem[i+1])
        else:
            continue
    return dict(zip(a1, a2))


def export_file(data, IDs):
    IDs = IDs.split(" ")
    new_data = []
    for contact in IDs:
        for elem in data:
            if contact in elem:
                new_data.append(elem)
    create_export(new_data)


def import_file():
    pass
