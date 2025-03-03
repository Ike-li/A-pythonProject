"""
抽象工厂模式（Abstract Factory Pattern）是一种常见的设计模式，用于创建一系列相关的对象，而无需指定具体的类。
通俗地说，它就像是一个“工厂的工厂”，能够根据不同的需求生产出一整套产品，而不是单个产品。

示例场景：汽车工厂
假设我们有两家汽车制造商：特斯拉（Tesla）和 宝马（BMW）。
每家制造商都生产两种类型的汽车：轿车（Sedan）和 SUV。这些汽车都需要一个 核心部件（如电池管理系统或发动机控制系统）。
目标
我们需要一个系统，可以根据用户的需求（特斯拉或宝马），生产出对应的轿车和 SUV，并包含对应的核心部件。
"""


class Sedan:
    """
    轿车类
    """

    def display_info(self):
        pass


class SUV:
    """
    SUV类
    """

    def display_info(self):
        pass


class CoreComponent:
    """
    核心部件类
    """

    def describe(self):
        pass


class TeslaModel3(Sedan):
    """
    特斯拉轿车类
    """

    def display_info(self):
        return "Tesla Model 3 - Sedan"


class TeslaModelY(SUV):
    """
    特斯拉SUV类
    """

    def display_info(self):
        return "Tesla Model Y - SUV"


class TeslaCoreBattery(CoreComponent):
    """
    特斯拉核心部件类:电池管理系统
    """

    def describe(self):
        return "Tesla Battery Management System"


class BMW3Series(Sedan):
    """
    宝马轿车类
    """

    def display_info(self):
        return "BMW 3 Series - Sedan"


class BMWX5(SUV):
    """
    宝马SUV类
    """

    def display_info(self):
        return "BMW X5 - SUV"


class BMWEngine(CoreComponent):
    """
    宝马核心部件类：发动机控制系统
    """

    def describe(self):
        return "BMW Engine System"


class AbstractFactory:
    """
    抽象工厂类
    """

    def create_sedan(self):
        pass

    def create_suv(self):
        pass

    def create_core_component(self):
        pass


class TeslaFactory(AbstractFactory):
    """
    特斯拉工厂类
    """

    def create_sedan(self):
        return TeslaModel3()

    def create_suv(self):
        return TeslaModelY()

    def create_core_component(self):
        return TeslaCoreBattery()


class BMWFactory(AbstractFactory):
    """
    宝马工厂类
    """

    def create_sedan(self):
        return BMW3Series()

    def create_suv(self):
        return BMWX5()

    def create_core_component(self):
        return BMWEngine()


def client_code(factory):
    """
    客户端代码
    """
    sedan = factory.create_sedan()
    suv = factory.create_suv()
    component = factory.create_core_component()

    print("Sedan:", sedan.display_info())
    print("SUV:", suv.display_info())
    print("Core Component:", component.describe())
    print("*****************")


# 使用特斯拉工厂
print("Using Tesla Factory:")
client_code(TeslaFactory())

# 使用宝马工厂
print("Using BMW Factory:")
client_code(BMWFactory())


"""
Using Tesla Factory:
Sedan: Tesla Model 3 - Sedan
SUV: Tesla Model Y - SUV
Core Component: Tesla Battery Management System
*****************
Using BMW Factory:
Sedan: BMW 3 Series - Sedan
SUV: BMW X5 - SUV
Core Component: BMW Engine System
*****************
"""
