# %%
def add_item(item_list):
    s = input("ใส่ชื่อสินค้า: ")
    if not item_list:
        item_list.append(s)
        print("Item has been added")
    elif s in item_list:
        print("Item is already in the list")
    else:
        print("Item has been added")
        item_list.append(s)


# %%
def change_item(item_list):
    s = input("เปลี่ยนชื่อสินค้า: ")
    if s not in item_list:
        print("Item is not in the list")
    elif s in item_list:
        n = input("เปลี่ยนชื่อสินค้าใหม่: ")
        for i in range(len(item_list)):
            if s == item_list[i]:
                item_list[i] = n
                print("Item has been changed")


# %%
def insert_item(item_list):
    s = input("แทรกชื่อสินค้า: ")
    i = int(input("ตำแหน่ง: "))
    item_list.insert(i, s)
    print("Item has been inserted")


# %%
def remove_item(item_list):
    s = input("ลบชื่อสินค้า: ")
    if s not in item_list:
        print("This item is not the list")
    elif s in item_list:
        item_list.remove(s)
        # for i in range(len(item_list)):
        #      if s in item_list[i]:
        #         del item_list[i]
        print("Item has been removed")


# %%
def show_item(item_list):
    if not item_list:
        print("The list is currently empty")
    else:
        print(item_list)


# %%
print("What would you like to do?")
print("1: add item")
print("2: change item")
print("3: insert item")
print("4: remove item")
print("5: show item")
print("6: exit")

# %%
x = []
choose = input("Enter a number : ")
while choose != "6":
    if choose == "1":
        add_item(x)
    elif choose == "2":
        change_item(x)
    elif choose == "3":
        insert_item(x)
    elif choose == "4":
        remove_item(x)
    elif choose == "5":
        show_item(x)
    choose = input("Enter a number : ")
