import os

# Check if file exists
if not os.path.exists("items.txt"):
    # Create file if it doesn't exist
    open("items.txt", "w").close()

while True:
    # Prompt user to choose action
    action = input("Enter '1' to add new item, '2' to read all items, '3' to remove an item, '4' to view number of items and dollar total, or '-1' to exit: ")
    
    if action == "-1":
        # Exit program if action is -1
        break
        
    if action == "1":
        # Ask user for input
        item_name = input("Enter item name: ")
        dollars = input("Enter dollars: ")

        # Append to file
        with open("items.txt", "a") as f:
            f.write(f"{item_name}: {dollars}\n")

        print(f"{item_name}: {dollars} added to file")
    
    elif action == "2":
        # Read all items in file and display to user
        print("All items in file:")
        with open("items.txt", "r") as f:
            for line in f:
                print(line.strip())
    
    elif action == "3":
        # Ask user for item name to remove
        item_name = input("Enter item name to remove: ")

        # Read all lines, filtering out the one to remove
        with open("items.txt", "r") as f:
            lines = f.readlines()
        with open("items.txt", "w") as f:
            removed = False
            for line in lines:
                if line.startswith(item_name + ":"):
                    print(f"Removed item: {line.strip()}")
                    removed = True
                else:
                    f.write(line)
            if not removed:
                print("Item not found in file")
    
    elif action == "4":
        # Count items and compute total dollars
        count = 0
        total = 0
        with open("items.txt", "r") as f:
            for line in f:
                parts = line.split(": ")
                if len(parts) == 2:
                    try:
                        dollars = float(parts[1])
                        count += 1
                        total += dollars
                    except ValueError:
                        pass
        
        # Display results to user
        print(f"Number of items: {count}")
        print(f"Total dollars: {total:.2f}")
    
print("Exiting program")
