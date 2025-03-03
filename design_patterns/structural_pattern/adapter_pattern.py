"""
适配器模式（Adapter Pattern）是一种结构型设计模式，
其目的是通过将一个类的接口转换成客户端所期望的另一个接口，让原本因接口不兼容而不能一起工作的类能够一起工作。

通俗解释：
就像你买了一个国外的电器，但是它的插头和国内的插座形状不匹配。
适配器模式就像一个多国电源适配器，把不匹配的插头改成能插入国内插座的形状，让这个电器能正常工作。

例子：电源适配器
假设我们有一个电热水壶，它使用的是中国标准的插头（摁插头），但你想把它带到美国使用，而美国的插孔是叉形的。这时，适配器模式就有了用武之地。
"""


class CoffeeMachine:
    """被适配者：使用美标插头的咖啡机"""

    def __init__(self):
        self.plug_type = "叉插头"

    def us_plug_insert(self):
        print("咖啡机插入了美标插座，开始工作！")


class ElectricKettle:
    """目标接口：可以插入中标插座的电热水壶"""

    def __init__(self):
        self.plug_type = "摁插头"

    def cn_plug_insert(self):
        print("电热水壶插入了中标插座，开始工作！")


class PowerAdapter:
    """适配器，将美标的咖啡机转换为符合中标标准"""

    def __init__(self, coffee_machine):
        self.coffee_machine = coffee_machine  # 被适配者

    def cn_plug_insert(self):
        # 调用被适配者的方法，但转换插头类型
        print("适配器将美标插头转换为摁插头")
        self.coffee_machine.us_plug_insert()


if __name__ == "__main__":
    # 客户端代码
    coffee_machine = CoffeeMachine()  # 美标的咖啡机
    adapter = PowerAdapter(coffee_machine)  # 创建适配器

    # 测试电热水壶（正常工作）
    kettle = ElectricKettle()
    kettle.cn_plug_insert()  # 输出：电热水壶插入了中标插座，开始工作！

    # 测试适配后的咖啡机
    adapter.cn_plug_insert()
    # 输出：
    # 适配器将美标插头转换为摁插头
    # 咖啡机插入了美标插座，开始工作！
