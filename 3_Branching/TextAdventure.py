
# coding: utf-8

# # Text Adventure Game

# In[ ]:


class Item():
    def __init__(self, name, desc, next_room):
        self.name = name
        self.desc = desc
        self.next_room = next_room

class Location():    
    def __init__(self, name):
        self.name = name
        self.obj = {}
        
    def __repr__(self):
        s = "You are in the {}.\n".format(self.name)
        s = s + "Looking around you see:\n"
        for key, value in self.obj.items():
            s = s + "\tA {}.\n".format(key.capitalize())
        return s
    
    def prompt_user(self):
        choice = input("You look closer at the").lower()
        if choice in self.obj:
            item = self.obj[choice]
            print(item.desc)
            if item.next_room != None:
                move(item.next_room)
            else:
                self.prompt_user()
        elif choice == 'exit':
            return
        else:
            self.prompt_user()
            
    def _add_item(self, item):
        self.obj[item.name] = item
        
    def add_items(self, items):
        for elem in items:
            self._add_item(elem)

def move(location):
    print(location)
    location.prompt_user()

room = Location("Room")
forest = Location("Forest")
table = Location("Table")

book = Item("book", "You read the book:\nHello", None)
table_item = Item("table", "The table has some items on it!", table)
door = Item("door", "Moving into the Forest", forest)
tree = Item("tree", "The tree is very old", None)
path = Item("path", "Walking down the path.", room)
room_i = Item("room", "Leaving the table.", room)

room.add_items([book, table_item, door])
forest.add_items([tree, path])
table.add_items([room_i])

move(room)

