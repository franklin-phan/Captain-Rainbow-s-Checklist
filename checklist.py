#Create
checklist = list()
def create(item):
    checklist.append(item)
#Read
def read(index):
    return checklist[index]

# Update
def update(index, item):
    checklist[index] = item

# Destroy
def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def test():
        create("purple sox")
        create("red cloak")

        print(read(0))
        print(read(1))

        update(0, "purple socks")
        destroy(1)

        print(read(0))
        print(read(1))
test()
