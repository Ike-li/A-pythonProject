"""
想象一下，你去餐厅点一份汉堡，菜单上有经典汉堡、鸡肉汉堡、素食汉堡等。
每种汉堡的制作过程可能都有不同的步骤，比如加面包、加肉饼、加蔬菜、加酱料等。
但无论制作哪种汉堡，厨师的制作步骤都是固定的：先加面包，然后是肉饼（或素饼），接着是蔬菜、酱料，最后再盖上另一片面包。
此时，如果你是餐厅的厨师长，你会希望有一个流程规范来指导不同汉堡的制作吗？
是的，这样你就能控制每种汉堡的制作质量，并且可以根据顾客的要求（比如无肉、无蔬菜等）灵活调整制作步骤。
在编程中，建造者模式就扮演了这个“厨师长”的角色，它定义了一个清晰的构建流程，同时允许不同的“厨师”（建造者）根据需要，按照同样的流程创建不同的对象。
实际例子：动态构建产品
假设我们要创建一种汉堡类，但想要根据不同的需求（比如经典汉堡、素食汉堡）动态地添加不同的配料。这时就可以用建造者模式。
"""


class Hamburger:
    """
    产品类
    """

    def __init__(self):
        self.bun = None
        self.patty = None
        self.vegetables = None
        self.sauce = None

    def show_hamburger(self):
        print(
            f"汉堡完成：\n面包：{self.bun}\n肉饼/素饼: {self.patty}\n蔬菜: {self.vegetables}\n酱料: {self.sauce}"
        )


class Builder:
    """
    抽象建造者
    """

    def add_bun(self):  # 添加面包
        pass

    def add_patty(self):  # 添加肉饼或素饼
        pass

    def add_vegetables(self):  # 添加蔬菜
        pass

    def add_sauce(self):  # 添加酱料
        pass


class ClassicHamburgerBuilder(Builder):
    """
    具体建造者：经典汉堡建造者
    """

    def __init__(self):
        self.hamburger = Hamburger()

    def add_bun(self):
        self.hamburger.bun = "经典面包"

    def add_patty(self):
        self.hamburger.patty = "牛肉饼"

    def add_vegetables(self):
        self.hamburger.vegetables = "生菜，番茄"

    def add_sauce(self):
        self.hamburger.sauce = "经典酱料"

    def get_hamburger(self):
        return self.hamburger


class VegetarianHamburgerBuilder(Builder):
    """
    具体建造者：素食汉堡建造者
    """

    def __init__(self):
        self.hamburger = Hamburger()

    def add_bun(self):
        self.hamburger.bun = "全麦面包"

    def add_patty(self):
        self.hamburger.patty = "素肉饼"

    def add_vegetables(self):
        self.hamburger.vegetables = "西兰花、胡萝卜"

    def add_sauce(self):
        self.hamburger.sauce = "素食酱料"

    def get_hamburger(self):
        return self.hamburger


class Director:
    """
    指导者类
    """

    def __init__(self, builder):
        self.builder = builder

    def construct_hamburger(self):
        self.builder.add_bun()
        self.builder.add_patty()
        self.builder.add_vegetables()
        self.builder.add_sauce()
        return self.builder.get_hamburger()


# 使用建造者模式
if __name__ == "__main__":
    # 创建经典汉堡
    classic_builder = ClassicHamburgerBuilder()
    director = Director(classic_builder)
    classic_hamburger = director.construct_hamburger()
    classic_hamburger.show_hamburger()

    # 创建素食汉堡
    vegetarian_builder = VegetarianHamburgerBuilder()
    director = Director(vegetarian_builder)
    vegetarian_hamburger = director.construct_hamburger()
    vegetarian_hamburger.show_hamburger()


"""
代码解析
Hamburger 类：这是我们要创建的复杂对象，拥有多个属性（面包、肉饼、蔬菜、酱料）。
Builder 类：定义了所有建造者必须实现的接口（方法）。
ClassicHamburgerBuilder 和 VegetarianHamburgerBuilder：具体实现建造者接口，分别构建不同类型的汉堡。
Director 类：负责调用建造者的各个方法，完成对象的构建过程。如果需要改变构建流程，只需要改 Director 类即可，无需改动每个建造者。
"""
