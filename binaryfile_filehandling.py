import pickle

def create_library():
    with open("Library.dat", "wb") as fp:
        n = int(input("Enter the number of books: "))
        for i in range(n):
            print(f"\nBook {i + 1}:")
            ac_no = input("  Accession number: ")
            bnm = input("  Book name: ")
            anm = input("  Author name: ")
            yrp = int(input("  Year of publishing: "))
            rec = [ac_no, bnm, anm, yrp]
            pickle.dump(rec, fp)
    print("\nLibrary records created successfully!\n")

## display function

def display_all():
    print("\n***** LIBRARY RECORDS *****\n")
    try:
        with open("Library.dat", "rb") as fp:
            while True:
                rec = pickle.load(fp)
                print(rec)
    except EOFError:
        pass

## search function 

def search():
    flag = 0
    try:
        with open("Library.dat", "rb") as fp:
            while True:
                rec = pickle.load(fp)
                if rec[3] < 2000:
                    print("\nRecord found (published before 2000):")
                    print(rec)
                    flag = 1
                    break
    except EOFError:
        if flag == 0:
            print("\nNo record found before the year 2000.")

## update function

def new_books():
    try:
        with open("Library.dat", "ab") as fp:
            n = int(input("How many new records to add? "))
            for i in range(n):
                print(f"\nNew Book {i + 1}:")
                a_c = input("  Accession number: ")
                b_m = input("  Book name: ")
                a_m = input("  Author name: ")
                y_p = int(input("  Year of publishing: "))
                rec = [a_c, b_m, a_m, y_p]
                pickle.dump(rec, fp)
        print("\nNew books added successfully!\n")
    except Exception as e:
        print("Error while adding new books:", e)

### main

create_library()
display_all()

ans = input("\nClick 'Y' to search for books before the year 2000: ")
if ans.lower() == 'y':
    search()

update = input("Click 'yes' to update the file with new books: ")
if update.lower() == "yes":
    new_books()
    display_all()
