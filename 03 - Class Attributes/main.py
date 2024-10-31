class Item:
    pay_rate = 0.8 # The pay rate after 20% discount... Hint: This is class attributes
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!" # If price is greaternor equal to zero, It will output the string comment.
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

# Creating Instances
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)



# Hint: You can access the class attributes directly by calling it on the class 
priint(Item().pay_rate)

# __dict__ is a built-in magic attribute that helps us to find all the attributes belonging to a specific object 
print(Item.__dict__) # All the attributes for Class level
print(item1.__dict__) # All the attributes for the Instance level 


# Using forloop to print all the name in the `all` list

for instance in Item.all:
    print(instance.name)