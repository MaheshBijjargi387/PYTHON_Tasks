class Inventory:
    def __init__(self):
        self.Dict = {}

    def add_item(self, Item, Quantity):
        if Item in self.Dict:
            self.Dict[Item] += Quantity
        else:
            self.Dict[Item] = Quantity

    def remove_item(self, Item, Quantity):
        if Item in self.Dict:
            if self.Dict[Item] > Quantity:
                self.Dict[Item] -= Quantity
            else:
                del self.Dict[Item]
        else:
            print("No item found.")

    def view_inventory(self):
        for key, value in self.Dict.items():
            print(f"{key}: {value}")

    def get_total_stock(self):
        print(sum(self.Dict.values()))


new = Inventory()

new.add_item("mobile", 3)
new.view_inventory()
new.remove_item("mobile", 1)
new.view_inventory()
new.get_total_stock()


while True:
    print("\n--- Inventory Management ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Inventory")
    print("4. Get Total Stock")
    print("5. Exit")

    num=int("choose the number")

    if num==1:
        item=input("Enter item")
        qutity=int(input("enter qutity"))

        new.add_item(item,qutity)

    elif num==2:
        item=input("Enter item :")
        qutity=int(input("Enter qutity :"))

        new.remove_item(item,qutity)

    elif num==3:
        new.view_inventory()

    elif num==4:
        new.get_total_stock()

    else:
        print("not correct choise")