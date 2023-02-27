#input tesko (a,d,s,r)
import jumk
def menu():
   case=input("enter a or d or s or r::::")
   while case!="q":
        if case=="a":
           book,author=input("enter names of book and author::::").split()
           jumk.add_book(book,author)
        elif case=='d':
              book=input("please enter the name of the book")
              jumk.del_book(book)

        elif(case=='s'):
               x=jumk.show_books()
               print(x)

        elif(case=='r'):
                book=input("what book have ypu completed reading??")
                jumk.mark_as_read(book)
        case=input("enter a or d or s or r::::")
menu()