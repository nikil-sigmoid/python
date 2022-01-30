class Shirt:
    def make_shirt(self, size, text):
        print(f"Size of the shirt is: {size}")
        print(text)
        print()


obj = Shirt()
obj.make_shirt(40, "All is Well")
obj.make_shirt(text = "All is Well", size = 40)


