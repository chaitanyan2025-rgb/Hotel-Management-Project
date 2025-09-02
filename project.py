import mysql.connector as ms

# Connect to MySQL
mycon = ms.connect(
    host='localhost',
    user="root",
    password="Password@123",
    database="store"
)
mycursor = mycon.cursor()
mycon.commit()


def addbooks():
    global mycon, mycursor
    print("All information prompted are mandatory to be filled")

    book = input("Enter Book Name: ")
    genre = input("Genre: ")
    quantity = int(input("Enter quantity: "))
    author = input("Enter author name: ")
    publication = input("Enter publication house: ")
    price = int(input("Enter the price: "))

    mycursor.execute("select * from Available_Books where bookname='" + book + "'")
    row = mycursor.fetchone()

    if row is not None:
        mycursor.execute(
            "update Available_Books set quantity=quantity+" + str(quantity) + " where bookname='" + book + "'"
        )
        mycon.commit()
        print("""++++++++++++++++++++++
++SUCCESSFULLY ADDED++
++++++++++++++++++++++""")
    else:
        mycursor.execute(
            "insert into Available_Books(bookname,genre,quantity,author,publication,price) "
            "values('" + book + "','" + genre + "','" + str(quantity) + "','" + author + "','" + publication + "','" + str(price) + "')"
        )
        mycon.commit()
        print("""++++++++++++++++++++++
++SUCCESSFULLY ADDED++
++++++++++++++++++++++""")


def searchbook():
    global mycon, mycursor
    print("""1: Search by name
2: Search by genre
3: Search by author""")

    l = int(input("Search by?: "))

    # BY BOOKNAME
    if l == 1:
        o = input("Enter Book to search: ")
        mycursor.execute("select bookname from available_books where bookname='" + o + "'")
        tree = mycursor.fetchone()
        if tree is not None:
            print("""++++++++++++++++++++
++BOOK IS IN STOCK++
++++++++++++++++++++""")
        else:
            print("BOOK IS NOT IN STOCK!!!!!!!")

    # BY GENRE
    elif l == 2:
        g = input("Enter genre to search: ")
        mycursor.execute("select genre from available_books where genre='" + g + "'")
        poll = mycursor.fetchall()
        if poll:
            print("""++++++++++++++++++++
++BOOK IS IN STOCK++
++++++++++++++++++++""")
            mycursor.execute("select * from available_books where genre='" + g + "'")
            for y in mycursor:
                print(y)
        else:
            print("BOOKS OF SUCH GENRE ARE NOT AVAILABLE!!!!!!!!!")

    # BY AUTHOR NAME
    elif l == 3:
        au = input("Enter author to search: ")
        mycursor.execute("select author from available_books where author='" + au + "'")
        home = mycursor.fetchall()
        if home:
            print("""++++++++++++++++++++
++BOOK IS IN STOCK++
++++++++++++++++++++""")
            mycursor.execute("select * from available_books where author='" + au + "'")
            for z in mycursor:
                print(z)
        else:
            print("BOOKS OF THIS AUTHOR ARE NOT AVAILABLE!!!!!!!")

    mycon.commit()


def addstaff():
    global mycon, mycursor
    fname = input("Enter Fullname: ")
    gender = input("Gender(M/F/O): ")
    age = int(input("Age: "))
    phno = input("Staff phone no.: ")
    add = input("Address: ")

    mycursor.execute(
        "insert into Staff_details(name,gender,age,phonenumber,address) "
        "values('" + fname + "','" + gender + "','" + str(age) + "','" + str(phno) + "','" + add + "')"
    )
    print("""+++++++++++++++++++++++++++++
+STAFF IS SUCCESSFULLY ADDED+
+++++++++++++++++++++++++++++""")
    mycon.commit()


def removestaff():
    global mycon, mycursor
    nm = input("Enter staff name to remove: ")
    mycursor.execute("select name from staff_details where name='" + nm + "'")
    toy = mycursor.fetchone()
    if toy is not None:
        mycursor.execute("delete from staff_details where name='" + nm + "'")
        print("""+++++++++++++++++++++++++++++++++
++STAFF IS SUCCESSFULLY REMOVED++
+++++++++++++++++++++++++++++++++""")
        mycon.commit()
    else:
        print("STAFF DOES NOT EXIST!!!!!!")


def displaystaff():
    global mycon, mycursor
    mycursor.execute("select * from Staff_details")
    staff = mycursor.fetchall()
    if staff:
        print("EXISTING STAFF DETAILS...")
        for t in staff:
            print(t)
    else:
        print("NO STAFF EXISTS!!!!!!!")
    mycon.commit()


def available_books():
    global mycon, mycursor
    mycursor.execute("select * from available_books order by bookname")
    for v in mycursor:
        print(v)


# Main Menu Loop
while True:
    print("\n******************* BOOK STORE MANAGEMENT SYSTEM **************************")
    print("1. ADD NEW BOOK ")
    print("2. SEARCH BOOK")
    print("3. NEW STAFF ENTRY ")
    print("4. REMOVE STAFF FROM THE STORE ")
    print("5. DISPLAY STAFF DETAILS ")
    print("6. DISPLAY AVAILABLE BOOKS")
    print("7. EXIT")
    print("***************************************************************************")

    ans = int(input("Enter your choice: "))

    if ans == 1:
        addbooks()
    elif ans == 2:
        searchbook()
    elif ans == 3:
        addstaff()
    elif ans == 4:
        removestaff()
    elif ans == 5:
        displaystaff()
    elif ans == 6:
        available_books()
    elif ans == 7:
        mycon.close()
        break
    else:
        print("\nInvalid Choice!!")
