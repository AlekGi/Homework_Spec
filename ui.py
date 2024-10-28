import Note


def create_note(number):
    title = check_len_text_input(
        input('Введите Заголовок заметки: '), number)
    body = check_len_text_input(
        input('Введите Текст заметки: '), number)
    return Note.Note(title=title, body=body)


def menu():
    print("=" * 36)
    print(" Пожалуйста, введите код операции с клавиатуры\n")
    print(" [1] -- Показать все заметки")
    print(" [2] -- Добавить новую заметку")
    print(" [3] -- Редактировать заметку")
    print(" [4] -- Найти заметки по \033[36mДате публикации\033[39m")
    print(" [5] -- Найти заметку по \033[31mID\033[39m")
    print(" [6] -- Удалить заметку")
    print("\n [0] -- Выход")
    print("=" * 36)


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите текст: ')
    else:
        return text


def goodbuy():
    print("\033[32mСпасибо, что пользуетесь нашими заметками. Ждём Вас снова \033[33m;)\033[39m")
