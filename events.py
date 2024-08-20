def setup_events(root, add_button, delete_button, task_entry, task_list):
    def add_task():
        task = task_entry.get()
        if task:
            task_list.insert('end', task)
            task_entry.delete(0, 'end')

    def delete_task():
        selected_tasks = task_list.curselection()
        for index in reversed(selected_tasks):
            task_list.delete(index)

    add_button.config(command=add_task)
    delete_button.config(command=delete_task)
