# __init__()
# __str__()
# __len__()
#__del__()

class Book():
    def __init__(self, title, author, pages):
        print("Book is created")
        self.title = title
        self.author = author
        self.pages = pages

    #String Method
    def __str__(self):
        A = f"title:{self.title}, author:{self.author}, pages:{self.pages}"
        return A
    
    #Length Method
    def __len__(self):
        return self.pages

    #Delete Method
    def __del__(self):
        pass
        # print(f"{self.title} has benn deletd")


b1 = Book('Coding the Brains', 'Hamza', 100)
b2 = Book('Example Book', 'Ahmad', 200)

del b2

# print(len(b1))
print(b1)
# print(b2)
