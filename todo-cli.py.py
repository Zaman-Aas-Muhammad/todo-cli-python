tasks = []

while True :

    print("\n===== SEO TASK MANAGER =====")
    print("1. Add new task : ") 
    print("2. View all tasks : ")
    print("3. Remove a task : ")
    print("4. Show SEO stats : ")
    print("5. Exit")

    choice = input("Enter you choice : ")

    if choice == "1" :
        task = input("Enter task : ")
        category = input("Enter category (SEO / Python / General) : ")
        tasks.append (f"{task}, [{category}]")
        print("Task added successfully !")

        if "seo" in task.lower() :
            print("SEO related task detected")

        if "python" in task.lower() :
            print("Python related task detected")
        if "blog" in task.lower() :
            print("Tip : Use keywords in your blog title for better SEO")

    elif choice == "2" :
        if len (tasks) == 0 :
            print("No tasks available")
        else :
            print("\nYour tasks : ")
            for i, task in enumerate(tasks, start=1) :
                print(f"{i}. {task}")

    elif choice == "3" :
        if len (tasks) == 0 :
            print("No tasks to remove")
        else :
            for i, task in enumerate(tasks, start=1) :
                print(f"{i}. {task}")

        index = int(input("Enter task number to remove : "))
        if 1 <= index <= len(tasks) :
            removed = tasks.pop(index - 1)
            print(f"Removed : {removed}")
        else :
            print("Invalid number")

    elif choice == "4" :
        seo_count = 0
        python_count = 0

        for task in tasks :
            if "[SEO]" in task :
                seo_count += 1
            if "[Python]" in task :
                python_count += 1

        print(f"Total SEO tasks : {seo_count}")
        print(f"Total Python tasks : {python_count}")
        print(f"Total tasks : {len(tasks)}")


    elif choice == "5" :
        print("Goodbye 👋")
        break   
    else :
        print("Invalid choice, please try again")