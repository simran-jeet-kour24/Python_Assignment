# 5 Unique Classes Program

# 1️ Fan Class
class Fan:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed  # speed in RPM

    def show_info(self):
        print("Fan Brand:", self.brand)
        print("Speed (RPM):", self.speed)
        print("----------------")

# 2️ Table Class
class Table:
    def __init__(self, material, length):
        self.material = material
        self.length = length  # length in cm

    def show_info(self):
        print("Table Material:", self.material)
        print("Length (cm):", self.length)
        print("----------------")

# 3️ TV Class
class TV:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size  # size in inches

    def show_info(self):
        print("TV Brand:", self.brand)
        print("Size (inches):", self.size)
        print("----------------")

# 4️ Laptop Class
class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram  # RAM in GB

    def show_info(self):
        print("Laptop Brand:", self.brand)
        print("RAM (GB):", self.ram)
        print("----------------")

# 5️ Pen Class
class Pen:
    def __init__(self, color, type):
        self.color = color
        self.type = type  # ballpoint/gel etc.

    def show_info(self):
        print("Pen Color:", self.color)
        print("Pen Type:", self.type)
        print("----------------")

# -------------------------
# Objects and Method Calls
# -------------------------

f1 = Fan("Orient", 1200)
f1.show_info()

t1 = Table("Wood", 150)
t1.show_info()

tv1 = TV("Samsung", 42)
tv1.show_info()

l1 = Laptop("HP", 16)
l1.show_info()

p1 = Pen("Blue", "Ballpoint")
p1.show_info()