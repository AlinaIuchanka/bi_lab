class Bookstore(object):
    visitors_count = 0

    def __init__(self, visitor_name, discount):
        self.visitor_name = visitor_name
        self.discount = discount
        # self.sum_bill = 0
        self.book_dict = {}
        Bookstore.visitors_count += 1

    @staticmethod
    def get_visitors_count():
        return Bookstore.visitors_count

    @staticmethod
    def print_visitors_count():
        print("Count of visitors: %d" % Bookstore.visitors_count)

    @property
    def get_visitor_books_count(self):
        return len(self.book_dict)

    @property
    def get_visitor_book_list(self):
        return self.book_dict

    def print_visitor_book_list(self):
        for book, price in self.book_dict.items():
            print(book, price)

    def add_book(self, book_name, book_price):
        self.book_dict[book_name] = book_price

    @property
    def get_bill_without_discount(self):
        sum_bill = 0
        for book, price in self.book_dict.items():
            sum_bill += price
        return sum_bill

    @property
    def get_bill_with_discount(self):
        return self.get_bill_without_discount * (1 - self.discount / 100)

    def del_book(self, book_name):
        self.book_dict.pop(book_name)

    def print_full_info(self):
        print()
        print("Name: ", self.visitor_name)
        print("Discount: ", self.discount, "%")
        print("Sum without discount: ", self.get_bill_without_discount)
        print("Sum with discount: ", self.get_bill_with_discount)
        print("Books count: ", self.get_visitor_books_count)
        print("Books:")
        self.print_visitor_book_list()
        print()


visitor1 = Bookstore("Alice", 10)
visitor1.add_book("The Lord of The Rings", 25)
visitor1.add_book("Harry Potter and the Half-Blood Prince", 20)
visitor1.add_book("Alice in the Wonderland", 15)
visitor1.del_book("Alice in the Wonderland")

visitor1.print_full_info()

Bookstore.print_visitors_count()

visitor2 = Bookstore("Lola", 0)
visitor2.add_book("The Lord of The Rings", 25)
visitor2.del_book("The Lord of The Rings")

visitor2.print_full_info()

Bookstore.print_visitors_count()
