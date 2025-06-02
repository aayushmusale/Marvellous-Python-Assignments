class Book:
    def __init__(self, price):
       self.__price = price     #get price

    def setPrice(self, price):
        self.__price = price    #set price
    
    def DisplayPrice(self):
        print("Price of the Book is ", self.__price)
    

def main():
    obj = Book(500)
    obj.DisplayPrice()
    obj.setPrice(280)
    obj.DisplayPrice()
    
    obj.__price = 1000                 # you can try to modify the private data member but it does not change
    obj.DisplayPrice()
    

if __name__ == "__main__":
    main()