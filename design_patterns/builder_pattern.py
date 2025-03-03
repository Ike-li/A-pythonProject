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
