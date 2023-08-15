class Falcon:
    def __init__(self, name):
        self.name = name
        self.tricks = []
    
    def add_trick(self, trick):
        self.tricks.append(trick)
    
    def show_tricks(self):
        print(f"{self.name} can perform the following tricks:")
        for trick in self.tricks:
            print(trick)

# Create a falcon instance
falcon = Falcon("Arya")

# Add tricks
falcon.add_trick("Aerial loops")
falcon.add_trick("Landing on the glove")
falcon.add_trick("Fetching tiny Python snakes")

# Display the falcon's tricks
falcon.show_tricks()
