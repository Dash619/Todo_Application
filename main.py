while True:
    user_action = input("Type add, show, edit, complete or exit : ")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:] + '\n'
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
            todos.append(todo)
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    elif 'show' in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item.capitalize()}"
            print(row)
    elif 'edit' in user_action:
        # number = int(input("Number of the todo to edit : "))
        # number = number - 1
        number = int(user_action[4:])
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        new_todo = input("Enter a new todo : ")
        todos[number - 1] = new_todo + '\n'
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    elif 'complete' in user_action:
        number = int(user_action[8:])
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        # number = int(input("Number of the todo to complete : "))
        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
        message = f"Todo {todo_to_remove} was removed from the list"
        print(message)
    elif 'exit' in user_action:
        break

print("bye")

