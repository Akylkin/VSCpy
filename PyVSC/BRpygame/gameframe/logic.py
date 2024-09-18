class Player():
    def __init__(self, hp, items: list) -> None:
        self.hp = hp
        self.items = items   

    def add_hp(self, hp=1):
        self.hp += hp
        return self.hp
    
    def sub_hp(self, hp=1):
        self.hp -= hp
        return self.hp
    
    def items_list_use(self, item, turn):
        if item == 'knife' and item in self.items:
            self.items.pop(item)
            return self.items
       
        elif item == 'beer' and item in self.items:
            self.items.pop(item)
            return self.items
        
        elif item == 'magnifier' and item in self.items:
            self.items.pop(item)
            return self.items
        
        elif item == 'cigarettes' and item in self.items:
            self.items.pop(item)
            return self.items
        
        elif item == 'handcuffs' and item in self.items:
            self.items.pop(item)
            return self.items
        
        else:
            print('что ты пытаешься этим сказать?')
            return None
        
    def items_list_add(self, item):
        if item == 'knife':
            self.items.append(item)
            return self.items
        
        if item == 'beer':
            self.items.append(item)
            return self.items
        
        if item == 'magnifier':
            self.items.append(item)
            return self.items
        
        if item == 'cigarettes':
            self.items.append(item)
            return self.items
        
        if item == 'handcuffs':
            self.items.append(item)
            return self.items 
    