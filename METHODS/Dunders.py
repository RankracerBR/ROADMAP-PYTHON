#Class
class Softwares:
    names = []
    versions = {}
    def __init__(self, names): #Initiate the values
        if names: 
            self.names = names.copy()
            for name in names:
                self.versions[name] = 1
        else:
            raise Exception("Please Enter the names") 
        
    def __str__(self): #Returns the values
        s = "The current softwares and their versions are listed below: \n"
        for key, value in self.versions.items():
            s += f"{key} : v{value} \n"
        return s
    
    def __setitem__(self,name,version): #set a item
        if name in self.versions:
            self.versions[name] = version
        else:
            raise Exception("Software Name doesn't exist")

    def __getitem__(self,name): #Get a item
        if name in self.versions:
            return self.versions[name]
        else:
            raise Exception("Software Name doesn't exist")
 
    def __delitem__(self,name): #delete a item
        if name in self.versions:
            del self.versions[name]
            self.names.remove(name)
        else:
            raise Exception("Software Name doesn't exist")
        
    def __len__(self):
        return len(self.names)        
    
    def __contains (self, name):
        if name in self.versions:
            return True
        else:
            return False
    

class Point:
    x = None
    y = None
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        s = f"({self.x},{self.y})"
        return s  
    
    def __add__(self,p2): #invoked when using '+'
        x = self.x + p2.x
        y = self.y + p2.y
        return Point(x,y)
        
    def __iadd__(self, p2): #invoked when using '+='
        self.x += p2.x
        self.y += p2.y
        return self
    
    def __isub__(self,p2): #invoked when using '-='
        self.x -= p2.x
        self.y -= p2.y
        return self
    
    def __imul__(self,p2): #invoked when using '*='
        self.x *= p2.x
        self.y *= p2.y
        return self
    
    def __itruediv__(self,p2): #invoked when using '/='
        self.x /= p2.x
        self.y /= p2.y
        return self
    
    def __ifloordiv__(self,p2): #invoked when using '//='
        self.x //= p2.x
        self.y //= p2.y
        return self
    
    def __call__(self):
        print(f"Called Point {self.x},{self.y}")
    
#Variables
p = Softwares(['S1','S2','S3'])
#p1 = Softwares([])
print(p)

p['S1'] = 2
print(p)
#p['2'] = 2

print(p['S1'])
#print(p['1'])

del p['S1']

print(len(p))

#if 'S2' in p:
#    print("Software Exists")
#else:
#    print("Software DOESN'T exist")
    

p1 = Point(5,4)
p2 = Point(2,3)
print(p1)
print(p2)

p3 = p1 + p2
print(p3)

p1 += p2
print(p1)