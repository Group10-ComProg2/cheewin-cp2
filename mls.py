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
    f = open("MLS.txt", "a")

    f.write("ID: 004 | Book: Database Systems\n")
    f.write("ID: 005 | Book: Web Development\n")
    f.write("ID: 006 | Book: Artificial Intelligence\n")

    f.close()

    print("Data appended successfully.")
