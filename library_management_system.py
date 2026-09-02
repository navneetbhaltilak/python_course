class library:
    def __init__(self):
        pass
    def add_book(self):
        name = input("Enter the name of the book : ").upper()
        Id = input("Enter the id of book : ")
        no_of_books=input("Enter the no. of books : ")
        with open('library_data.txt','a') as f:
            f.write(f"{Id} : {no_of_books} : {name}\n")
        print("Book added successfully")
    def access_book(self):
        find=input("Enter the name or Id of the book : ").upper()
        found = False
        with open('library_data.txt','r') as f:
       
            for line in f:
                if find in line:
                    print("Book Found:", line.strip())
                    found = True
                    break 
            if not found:
                print("Book not found!")
    def delete_book(self):
        find=input("Enter the name or Id of the book : ").upper()
        with open('library_data.txt','r') as f:
            lines= f.readlines()
        with open('library_data.txt','w') as f:
            for line in lines:
                if find not in line:
                    f.write(line)
        print("File is Successfully Deleted!")           
        return
    def start(self):
        while True:
            choice = int(input("1.Add Book\n2.Access Book\n3.Delete Book\n4.exit\nEnter(1,2,3,4) : "))
            match choice:
                case 1:
                    print("\nAdding Book to library")
                    self.add_book()
                    print("Added!..")
                case 2:
                    print("\nAccessing Book from library")
                    self.access_book()
                case 3:
                    print("\nDeleting Book from library")
                    self.delete_book()
                case 4:
                    print("..............Exiting..............")
                    return
                case _:
                    print("Invalid choice")



a=library()
a.start() 