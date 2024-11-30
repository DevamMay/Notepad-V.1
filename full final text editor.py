def password_manager():
    a = "devam"  # Preloaded password (you can change as per your will)
    p = 5  # Number of attempts
    print(f"You can only enter the password {p} times. After that, access is denied.")
    while p > 0:
        password = input("Enter the preloaded password: ")
        if password == a:
            print("You can now use the text editor! Fuyoh!!")
            return True 
        else:
            p -= 1
            print(f"Incorrect password. You have {p} attempts left.")  
    print("Oops! It seems like you forgot the password. Try again next time.")
    print("Press Enter to exit the terminal.")
    input() 
    return False 
if password_manager():
    while True:
        u = input("Press 1 to open the editor, 2 to open saved text, or 'q' to quit: ")
        if u == '1':
            t = input("Text heading: ")
            with open(t, 'w') as file:
                content = input("Enter text for the text editor (body): ")
                file.write(content)
            print(f"File '{t}' saved.")    
        elif u == '2':
            filename = input("Enter the filename to open: ")
            try:
                with open(filename, 'r') as file:
                    content = file.read()
                    print("\nFile content:\n")
                    print(content)
            except FileNotFoundError:
                print(f"Error: '{filename}' not found.")
        elif u.lower() == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please try again.")