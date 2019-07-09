class Backpack:
    Items = []
    def __init__(self,weight,value,maxW):
        self.weight = weight
        self.value = value 
        self.maxW = maxW
    def canadd(self,item):
        return  self.weight + item.weight <= self.maxW
    def canswap(self,item):
        return self.value < item.value and item.weight < self.maxW
    def swap(self,item):
          if self.canswap(item):
            if len(self.Items) == 1:
                self.Items[0] = item
            else:
                self.Items.append(item)
            self.value = item.value
            self.weight = item.weight
    def additem(self,item):
        check = self.canadd(item)
        #if you can't add it check to see if you need to swap it
        if check:
            self.Items.append(item)
            self.value = self.value + item.value
            self.weight = self.weight + item.weight
        return check
        
            
class Item:
    def __init__(self,value,weight):
        self.weight = weight
        self.value = value
def knapsackLight(value1, weight1, value2, weight2, maxW):
    backpack = Backpack(0,0,maxW)
    item1 = Item(value1,weight1)
    item2 = Item(value2,weight2)
    check = backpack.additem(item1)
    check = backpack.additem(item2)
    #if it is unable to add it can we swap it? 
    if not check:
        check =backpack.swap(item2)
    return backpack.value
