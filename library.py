class librarian:
    def __init__(self,name,pan_id):
        self.name=name
        self.pan_id=pan_id
    def book_issue(self,mem):
        print(self.name,'issued book to',mem)


class library_member():
    def __init__(self,name,id):
      self.name=name
      self.id=id
    def book_request(self):
        librarian.book_issue(self,self.name)



class book:
    def __init__(self,name):
        self.name=name


b1=book('Physics')
lib1=librarian('Murty','pn12')
lib1.book_issue()
l1=library_member('TSB',1234)
l1.book_request()