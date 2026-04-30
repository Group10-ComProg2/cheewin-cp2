# STUDENT A -- "x" and "w"

def initialize_library():
    try:
        f = open("MLS.txt", "x")
        f.close()
        print("Library file created successfully!\n")

    except FileExistsError:
        print("Library file already exists!\n")


def write_initial_data():
    f = open("MLS.txt", "w")

    f.write("===== Welcome to the Mini Library System of Group 10 =====\n")
    f.write("Book No. 1 | Title: Learn Computer Programing\n")
    f.write("Book No. 2 | Title: Behind the Blue Sky\n")
    f.write("Book No. 3 | Title: Data Structure and Algorithms\n")
    f.write("Book No. 4 | Title: The Art of Computer Programming\n")

    f.close()

    print("Initial data written successfully!\n")


initialize_library()
write_initial_data()


# STUDENT B -- "a"

def append_data():
    try:
        f = open("MLS.txt", "a")

        print("\n=== Add New Book Entries ===")

        while True:

            book_no = input("\nEnter Book No.: ")
            title = input("Enter Book Title: ")

            f.write(f"Book No. {book_no} | Title: {title}\n")

            another = input("\nDo you want to add another book? (y/n): ")

            if another.lower() != 'y':
                break

        f.close()

        print("\nNew book entries added successfully!")

    except FileNotFoundError:
        print("Library file not found!")


# STUDENT C -- "r"

def read_library():
    try:
        f = open("MLS.txt", "r")

        print("\n===== LIBRARY RECORDS =====\n")

        lines = f.readlines()

        for line in lines:
            print(line.strip())

        print("\nTotal number of lines:", len(lines))

        f.close()

    except FileNotFoundError:
        print("Library file not found!")


# STUDENT D -- UPDATE

def update_book():
    try:
        f = open("MLS.txt", "r")

        lines = f.readlines()

        f.close()

        search_book = input("\nEnter Book No. to update: ")
        new_title = input("\nEnter new Book Title: ")

        updated = False

        for i in range(len(lines)):

            if f"Book No. {search_book}" in lines[i]:

                lines[i] = f"Book No. {search_book} | Title: {new_title}\n"

                updated = True

        if updated:

            f = open("MLS.txt", "w")

            f.writelines(lines)

            f.close()

            print("\nBook updated successfully!")

        else:
            print("Book number not found!")

    except FileNotFoundError:
        print("Library file not found!")


# SEARCH FUNCTIONALITY

def search_book():
    try:
        f = open("MLS.txt", "r")

        keyword = input("\nEnter Book No. or Title to search: ")

        found = False

        print("\n===== SEARCH RESULT =====\n")

        for line in f:

            if keyword.lower() in line.lower():

                print(line.strip())

                found = True

        if not found:
            print("Book not found!")

        f.close()

    except FileNotFoundError:
        print("Library file not found!")


# DELETE FUNCTIONALITY

def delete_book():
    try:
        f = open("MLS.txt", "r")

        lines = f.readlines()

        f.close()

        delete_book_no = input("\nEnter Book No. to delete: ")

        updated_lines = []

        deleted = False

        for line in lines:

            if f"Book No. {delete_book_no}" not in line:

                updated_lines.append(line)

            else:
                deleted = True

        if deleted:

            f = open("MLS.txt", "w")

            f.writelines(updated_lines)

            f.close()

            print("Book deleted successfully!")

        else:
            print("Book number not found!")

    except FileNotFoundError:
        print("Library file not found!")


# MENU OPTIONS BASED ON INSTRUCTIONS

while True:

    print("\n===== MINI LIBRARY SYSTEM =====\n")
    print("1 - Add New Book")
    print("2 - Read and Count Lines")
    print("3 - Update Book")
    print("4 - Search Book")
    print("5 - Delete Book")
    print("6 - Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        append_data()

    elif choice == "2":
        read_library()

    elif choice == "3":
        update_book()

    elif choice == "4":
        search_book()

    elif choice == "5":
        delete_book()

    elif choice == "6":
        print("Exiting Mini Library System...")
        break

    else:
        print("Invalid choice! Please try again.")