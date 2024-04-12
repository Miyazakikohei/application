# %%
import os

# Todoリストを保存するファイル名
filename = 'todo_list.txt'

def load_todos():
    """ Todoリストをファイルから読み込む """
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            todos = file.readlines()
            todos = [todo.strip() for todo in todos]
    else:
        todos = []
    return todos

def save_todos(todos):
    """ Todoリストをファイルに保存する """
    with open(filename, 'w') as file:
        for todo in todos:
            file.write(todo + '\n')

def add_todo(todos, item):
    """ Todoアイテムをリストに追加する """
    todos.append(item)
    save_todos(todos)

def delete_todo(todos, index):
    """ 指定されたインデックスのTodoアイテムを削除する """
    if 0 <= index < len(todos):
        del todos[index]
        save_todos(todos)

def display_todos(todos):
    """ Todoリストの内容を表示する """
    for index, todo in enumerate(todos):
        print(f"{index + 1}: {todo}")

def main():
    todos = load_todos()
    
    while True:
        print("\nTodoリスト管理アプリ")
        print("1: Todoを追加")
        print("2: Todoを表示")
        print("3: Todoを削除")
        print("4: アプリを終了")
        
        choice = input("選択してください (1-4): ")
        
        if choice == '1':
            item = input("追加するTodoを入力してください: ")
            add_todo(todos, item)
        elif choice == '2':
            display_todos(todos)
        elif choice == '3':
            index = int(input("削除するTodoの番号を入力してください: ")) - 1
            delete_todo(todos, index)
        elif choice == '4':
            print("アプリを終了します。")
            break
        else:
            print("無効な選択です。1-4の数字を入力してください。")

if __name__ == "__main__":
    main()


# %%
