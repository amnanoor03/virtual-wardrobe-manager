# ClothingItem Class
class ClothingItem:
    def __init__(self, name, category, color, size, fabric, season):
        self.name = name
        self.category = category
        self.color = color
        self.size = size
        self.fabric = fabric
        self.season = season

    def display_item(self):
        return f"{self.name} ({self.category}): {self.color}, Size {self.size}, Fabric: {self.fabric}, Season: {self.season}"

    def modify_item(self, color=None, size=None):
        if color:
            self.color = color
        if size:
            self.size = size


# Wardrobe Class
class Wardrobe:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item.name} added to wardrobe.")

    def remove_item(self, item_name):
        self.items = [item for item in self.items if item.name != item_name]
        print(f"{item_name} removed from wardrobe.")

    def search_items(self, **kwargs):
        results = []
        for item in self.items:
            if all(getattr(item, key) == value for key, value in kwargs.items()):
                results.append(item)
        return results

    def display_wardrobe(self):
        for item in self.items:
            print(item.display_item())


# Outfit Class
class Outfit:
    def __init__(self):
        self.items = []

    def add_to_outfit(self, item):
        if item.category not in [i.category for i in self.items]:
            self.items.append(item)
            print(f"{item.name} added to outfit.")
        else:
            print(f"An item from category {item.category} already exists in this outfit.")

    def is_complete(self):
        required_categories = {'top', 'bottom', 'footwear'}
        present_categories = {item.category for item in self.items}
        return required_categories.issubset(present_categories)

    def display_outfit(self):
        for item in self.items:
            print(item.display_item())


# FashionCollection Class
class FashionCollection:
    def __init__(self):
        self.outfits = []

    def add_outfit(self, outfit):
        if outfit.is_complete():
            self.outfits.append(outfit)
            print("Outfit added to collection.")
        else:
            print("Outfit is incomplete and cannot be added to the collection.")

    def display_collection(self):
        for i, outfit in enumerate(self.outfits, 1):
            print(f"Outfit {i}:")
            outfit.display_outfit()
            print("---")


# Simple User Interface
def main():
    wardrobe = Wardrobe()
    collection = FashionCollection()

    while True:
        print("\nVirtual Wardrobe Manager")
        print("1. Add Clothing Item")
        print("2. Remove Clothing Item")
        print("3. View Wardrobe")
        print("4. Create Outfit")
        print("5. View Fashion Collection")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter item name: ")
            category = input("Enter category (top, bottom, footwear, etc.): ")
            color = input("Enter color: ")
            size = input("Enter size: ")
            fabric = input("Enter fabric: ")
            season = input("Enter season: ")
            item = ClothingItem(name, category, color, size, fabric, season)
            wardrobe.add_item(item)

        elif choice == '2':
            item_name = input("Enter the name of the item to remove: ")
            wardrobe.remove_item(item_name)

        elif choice == '3':
            print("\nYour Wardrobe:")
            wardrobe.display_wardrobe()

        elif choice == '4':
            outfit = Outfit()
            while True:
                item_name = input("Enter the name of the item to add to outfit (or 'done' to finish): ")
                if item_name == 'done':
                    break
                found_items = wardrobe.search_items(name=item_name)
                if found_items:
                    outfit.add_to_outfit(found_items[0])
                else:
                    print(f"No item found with the name {item_name}.")

            if outfit.is_complete():
                print("Outfit is complete!")
            else:
                print("Outfit is incomplete.")

            collection.add_outfit(outfit)

        elif choice == '5':
            print("\nYour Fashion Collection:")
            collection.display_collection()

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
