########################################################################################################################
# 封装（Encapsulation）：封装就是把对象的属性和方法（功能）包装到一个独立的单元（类）中，
# 让外部只能通过特定的接口（方法）来访问内部数据，这样可以隐藏内部的实现细节，防止外部直接修改数据。
########################################################################################################################
class BankAccount:
    """
    重点：
    __owner 和 __balance 是私有属性，外部不能直接访问，只能通过方法（如 deposit 和 withdraw）来操作。
    这样可以保护数据，防止外部直接修改余额。
    """
    def __init__(self, owner, balance):
        self.__owner = owner  # 私有属性
        self.__balance = balance  # 私有属性

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"存入{amount}元，当前余额：{self.__balance}元")
        else:
            print("存入金额必须大于0")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"取出{amount}元，当前余额：{self.__balance}元")
        else:
            print("余额不足")

    def get_balance(self):
        return self.__balance


# 使用封装
account = BankAccount("小明", 1000)
account.deposit(500)  # 正常操作
account.withdraw(200)  # 正常操作
print(account.get_balance())  # 获取余额


########################################################################################################################
# 继承（Inheritance）：继承就是让一个类（子类）继承另一个类（父类）的属性和方法，
# 子类可以复用父类的代码，还可以添加新的属性和方法，或者修改父类的方法。
########################################################################################################################
class Animal:
    """父类"""
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name}正在吃东西")

    def sleep(self):
        print(f"{self.name}正在睡觉")


class Dog(Animal):  # 子类，继承Animal
    """
    Dog 类继承了 Animal 类的 eat 和 sleep 方法。
    子类可以添加自己的方法（如 bark）。
    子类还可以修改父类的方法（称为方法重写）。
    """
    def bark(self):  # 添加自己的方法
        print(f"{self.name}正在叫")


# 使用继承
dog = Dog("旺财")
dog.eat()  # 继承自Animal
dog.sleep()  # 继承自Animal
dog.bark()  # 自己的方法


########################################################################################################################
# 多态（Polymorphism）: 多态是指同一个方法在不同的对象上调用时，可以有不同的实现。简单来说，就是“一个接口，多种实现”。
########################################################################################################################
class Animal:
    """父类"""
    def make_sound(self):
        pass  # 父类定义接口，不实现具体功能


class Dog(Animal):
    """子类"""
    def make_sound(self):  # 实现具体功能
        print("汪汪")


class Cat(Animal):
    """子类"""
    def make_sound(self):  # 实现具体功能
        print("喵喵")


# 使用多态
def animal_sound(animal):
    animal.make_sound()


"""
Animal 类定义了一个 make_sound 方法，但没有具体实现。
Dog 和 Cat 类分别实现了 make_sound 方法。
调用 animal_sound 函数时，根据传入的对象类型（狗或猫），调用对应的方法。
"""

dog = Dog()
cat = Cat()

animal_sound(dog)  # 输出：汪汪
animal_sound(cat)  # 输出：喵喵
"""
总结
封装：隐藏内部细节，通过方法操作数据。
继承：子类继承父类的属性和方法，可以扩展或修改。
多态：同一个方法在不同对象上有不同的实现。
"""
