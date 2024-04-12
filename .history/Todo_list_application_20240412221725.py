# %%
import os

def load_todos():
    """ ToDo���X�g����������ŏ��������� """
    return []

def save_todos(todos):
    """ ToDo���X�g��ۑ�����K�v������ꍇ�ɔ����ċ�̊֐���p�� """
    pass  # ��������̃��X�g�ŊǗ����邽�߁A�ۑ������͕s�v

def add_todo(todos, item):
    """ Todo�A�C�e�������X�g�ɒǉ����� """
    todos.append(item)

def delete_todo(todos, index):
    """ �w�肳�ꂽ�C���f�b�N�X��Todo�A�C�e�����폜���� """
    if 0 <= index < len(todos):
        del todos[index]

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
