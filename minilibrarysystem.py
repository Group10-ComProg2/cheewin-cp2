def initialize_library():
    try:
        f = open("Mini Library.txt", "x")
        f.close()
        print("Library file created successfully!")


    except FileExistsError:
        print("Library file already exists!")


def write_initial_data():
    f = open("Mini Library.txt", "w")


    f.write("Welcome to the Mini Library System!\n")
    f.write("Book No. 001 | Title: Learn Computer Programing\n")
    f.write("Book No. 002 | Title: Behind the Blue Sky\n")

    f.close()


    print("Initial data written successfully!\n")

initialize_library()
write_initial_data()


def append_data():
    try:
        f = open("MLS.txt", "a")

        print("\n=== Add New Book Entries ===")
        
        while True:
            book_no = input("Enter Book No.: ")
            title = input("Enter Book Title: ")

            f.write(f"Book No. {book_no} | Title: {title}")
            
            another = input("Do you want to add another book? (y/n): ")
            if another.lower() != 'y':
                break
        f.close()
        print("New book entries added successfully!")
        
    except FileNotFoundError:
        print("Library file not found! Please initialize the library first.")
        
append_data()
