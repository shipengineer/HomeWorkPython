import operand as op
import view as vw
file = 'phonebase.txt'


def button_click():
    command = vw.init_book(file)[0]
    book = vw.init_book(file)[1]
    if command == 1:
        vw.view_contacts
    if command == 2:
        op.find_contact(book, input("Кого ищем?"))
    if command == 3:
        op.create_contact(book, vw.create_contact_input())
    if command == 4:
        op.delete_contact_ID(book, vw.delete_contact_print())
    if command == 5:
        op.export_file(book, vw.export_question())
    if command == 6:
        op.import_file()


button_click()
