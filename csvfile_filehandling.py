import csv

# Initial employee entry
fp = open("Employee.csv", "w+", newline='')
writer1 = csv.writer(fp)
writer1.writerow(["Employee Id", "Name", "Designation", "Salary"])
n = int(input("Enter the number of employees:"))
for i in range(n):
    empid = input("Enter Employee Id: ")
    Name = input("Enter the Name of Employee: ")
    design = input("Enter the Designation: ")
    salary = input("Enter the Salary: ")
    list1 = [empid, Name, design, salary]
    writer1.writerow(list1)
fp.seek(0)
reader1 = csv.reader(fp)
for i in reader1:
    print(i[0] + "\t" + i[1] + "\t" + i[2] + "\t" + i[3] + "\n")
fp.close()


# insert()
def insert():
    fp = open("Employee.csv", "a+", newline='')
    writer1 = csv.writer(fp)
    t = int(input("Enter the number of data to be inserted: "))
    for i in range(t):
        empid = input("Enter Employee Id: ")
        Name = input("Enter the Name of Employee: ")
        design = input("Enter the Designation: ")
        salary = input("Enter the Salary: ")
        list1 = [empid, Name, design, salary]
        writer1.writerow(list1)
    fp.close()


# display()
def display():
    fp = open("Employee.csv", "r", newline='')
    reader1 = csv.reader(fp)
    
    print("\n{:<15} {:<20} {:<20} {:<10}".format("Employee Id", "Name", "Designation", "Salary"))
    print("-" * 70)
    
    for row in reader1:
        print("{:<15} {:<20} {:<20} {:<10}".format(row[0], row[1], row[2], row[3]))
    
    fp.close()


# search-display()
def search_display():
    fp = open("Employee.csv", "r", newline='')
    reader1 = csv.reader(fp)
    
    header = next(reader1)  # Skip header row
    flag = 0
    
    print("\nSearching for employees with salary > 40000...\n")
    print("{:<15} {:<20} {:<20} {:<10}".format("Employee Id", "Name", "Designation", "Salary"))
    print("-" * 70)

    for row in reader1:
        if int(row[3]) > 40000:
            print("{:<15} {:<20} {:<20} {:<10}".format(row[0], row[1], row[2], row[3]))
            flag = 1

    if flag == 0:
        print("No such record found.")
    
    fp.close()


# modify()
def modify():
    fp = open("Employee.csv", "r", newline='')
    reader1 = csv.reader(fp)
    data = list(reader1)
    fp.close()

    des = input("Enter the designation to be modified: ")
    flag = 0

    for i in range(1, len(data)):
        if data[i][2] == des:
            new_des = input("Enter the new designation: ")
            data[i][2] = new_des
            print("Updated designation is: " + data[i][2] + "\n")
            flag = 1
            break

    if flag == 0:
        print("No such record exists, please try again.")
    else:
        fp = open("Employee.csv", "w", newline='')
        writer1 = csv.writer(fp)
        writer1.writerows(data)
        fp.close()


# main
insert()
display()
search_display()
modify()
