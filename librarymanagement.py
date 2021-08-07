class lib():
    #construction of the object
    def __init__(self,lib_name,lib_list):
        self.lib_lend= {}
        self.lib_name = lib_name
        self.lib_list = lib_list
    #Intializing the value to each books as none to show thay are not lended
        for i in self.lib_list:
            self.lib_lend[i]= None
    #Function to store the lended book information
    def lend_book(self,book,reader):
        if book in self.lib_list:                   #Checking if the book is listed in the system or not.
            if self.lib_lend[book] is None:         #Checking if the book is already lended or not.
                self.lib_lend[book] = reader
                print("Book Lended!Please returned")
            else:
                print(f"Book is already lended to {self.lib_lend[book]}")
        else:
            print("Wrong name input!")
    #Displaying the books listed in the system
    def display(self):
        print("Here are the list you wanted")
        for index,books in enumerate(self.lib_list):
            print(f"{index}:{books}")
    #Adding new books to the list
    def add(self,book):
        self.lib_list.append(book)
        self.lib_lend[book] = None
        print("The book has been added to the system.")
    #
    def ret(self,book):
        if book in self.lib_list:
            if self.lib_lend[book] is not None:
                self.lib_lend[book] = None
            else:
                print("The book is not lended so cannot be retunrned")
        else:
            print("Wrong title entered. Please enter the correct title")
    def dele(self,book):
        self.lib_list.remove(book)
        self.lib_lend.pop(book)

    

def main():
        list_book = ['Sherlock Holmes', 'I Too Had love story', 'Alchemist', 'Harry Potter', 'Half-Girlfriend']
        name = "Central"
        passcode = "12345"
        central = lib(name,list_book)
        print(f"Welcome to the {central.lib_name} library choose: \nd to display book \nl to lend book \na to add the book \nx to "
              f"delete the book  \nq to exit")
        E = True
        while E:
            print("Enter your choices")
            k = input()
            if k=="q":
                print("Thank you for using the system,hope we meet again!")
                E = False
            elif k == "d":
                central.display()
            elif k == "l":
                print("Enter your name")
                n = input()
                print("Enter the name of the book")
                b = input()
                central.lend_book(b,n)
            elif k == "a":
                print("Please enter the passcode to confirm your are the admin")
                p = input()
                if p==passcode:
                    print("Enter the title you want to add:")
                    bk = input()
                    central.add(bk)
                else:
                    print("Sorry wrong passcode entered! You can't add books.")
            elif k == "x":
                print("Please enter the passcode to confirm your are the admin")
                p = input()
                if p==passcode:
                    print("Enter the title you want to delete:")
                    bk = input()
                    central.dele(bk)
                else:
                    print("Sorry wrong passcode entered! You can't add books.")
            elif k == "r":
                print("Please enter name of the book to be returned")
                bk = input()
                central.ret(bk)

if __name__ == "__main__":
    main()

