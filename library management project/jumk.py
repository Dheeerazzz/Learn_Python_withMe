
#add_book,del_book,show_books,mark_as_read
books=[]
def create_file():
    with open ("storage.txt",'r') as file:
        pass

def add_book(book,author):
    with open("storage.txt",'a') as file:
        file.write(f'{book},{author},0\n')


def _save_all(books):
    with open("storage.txt",'w') as file:
        for book in books:
             file.write(f'{book[0]},{book[1]},{book[2]}\n')              
                
def show_books():
    with open("storage.txt",'r') as file:
        lines=[line.strip().split(',') for line in file.readlines()]
        return(lines)
def del_book(book):
         supple=list()
         books=show_books()
         for bookk in books:
            if bookk[0]!=book:
                supple.append(bookk)
         _save_all(supple)
def mark_as_read(booka):
    boks=show_books()
    for book in boks:
        if book[0]==booka:
            book[2]='1'
    _save_all(boks)


