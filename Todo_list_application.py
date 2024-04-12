# %%
import os

# Todo���X�g��ۑ�����t�@�C����
filename = 'todo_list.txt'

def load_todos():
    """ Todo���X�g���t�@�C������ǂݍ��� """
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            todos = file.readlines()
            todos = [todo.strip() for todo in todos]
    else:
        todos = []
    return todos

def save_todos(todos):
    """ Todo���X�g���t�@�C���ɕۑ����� """
    with open(filename, 'w') as file:
        for todo in todos:
            file.write(todo + '\n')

def add_todo(todos, item):
    """ Todo�A�C�e�������X�g�ɒǉ����� """
    todos.append(item)
    save_todos(todos)

def delete_todo(todos, index):
    """ �w�肳�ꂽ�C���f�b�N�X��Todo�A�C�e�����폜���� """
    if 0 <= index < len(todos):
        del todos[index]
        save_todos(todos)

def display_todos(todos):
    """ Todo���X�g�̓��e��\������ """
    for index, todo in enumerate(todos):
        print(f"{index + 1}: {todo}")

def main():
    todos = load_todos()
    
    while True:
        print("\nTodo���X�g�Ǘ��A�v��")
        print("1: Todo��ǉ�")
        print("2: Todo��\��")
        print("3: Todo���폜")
        print("4: �A�v�����I��")
        
        choice = input("�I�����Ă������� (1-4): ")
        
        if choice == '1':
            item = input("�ǉ�����Todo����͂��Ă�������: ")
            add_todo(todos, item)
        elif choice == '2':
            display_todos(todos)
        elif choice == '3':
            index = int(input("�폜����Todo�̔ԍ�����͂��Ă�������: ")) - 1
            delete_todo(todos, index)
        elif choice == '4':
            print("�A�v�����I�����܂��B")
            break
        else:
            print("�����ȑI���ł��B1-4�̐�������͂��Ă��������B")

if __name__ == "__main__":
    main()


# %%
