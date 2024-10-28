import operation
import Note
import ui

number = 3  # минимальное количество знаков в заметке


def add():
    note = ui.create_note(number)
    array = operation.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    operation.write_file(array, 'a')
    print('\033[32mЗаметка успешно добавлена!\033[39m')


def show(text):
    logic = True
    array = operation.read_file()
    if text == 'date':
        date = input('Введите дату в формате ДД.ММ.ГГГГ (например, 25.10.2020): ')
    for notes in array:
        if text == 'all':
            logic = False
            print(Note.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + Note.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in Note.Note.get_date(notes):
                print(Note.Note.map_note(notes))
    if logic == True:
        print('На эту дату нет заметок')


def id_edit_del_show(text):
    id = input('Введите ID необходимой заметки: ')
    array = operation.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = ui.create_note(number)
                Note.Note.set_title(notes, note.get_title())
                Note.Note.set_body(notes, note.get_body())
                Note.Note.set_date(notes)
                print('\033[32mЗаметка успешно изменена!\033[39m')
            if text == 'del':
                array.remove(notes)
                print('\033[31mЗаметка удалена\033[39m')
            if text == 'show':
                print(Note.Note.map_note(notes))
    if logic == True:
        print('С таким ID заметок нет, возможно ввели неверный ID')
    operation.write_file(array, 'a')
