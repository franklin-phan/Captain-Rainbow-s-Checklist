#Create
checklist = list()
def create(item):
    checklist.append(item)
#Read
def read(index):
        mark_completed(int(index))
        return checklist[int(index)]

# Update
def update(index, item):
    checklist[index] = item

# Destroy
def destroy(index):
    checklist.pop(int(index))

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
        checklist[int(index)] = "√" + checklist[int(index)]

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)
        return True #new addition

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?")

        # Remember that item_index must actually exist or our program will crash.
        print(read(item_index)) #new addition
        return True #New Addition
    #Update item
    elif function_code == "U":
        item_index = user_input("Index to change: ")
        replace_item = user_input("Item to replace with: ")
        update(int(item_index), replace_item)
   
    elif function_code == "D":
        item_index = user_input("Index Number?: ")
        destroy(int(item_index))

    elif function_code == "P":
            list_all_items()
            return True #new addition
        # Print all items here

    elif function_code == "Q":
        # This is where we want to stop our loop
        return False
    else:
        #Catch all
        print("Unknown Option")
    return True

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    destroy(1)

    print(read(0))

    list_all_items()


test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, U to Update item in list, D to destroy item in list, P to display list, and Q to quit: ")
    running = select(selection)
