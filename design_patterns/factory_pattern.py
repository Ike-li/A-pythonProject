"""
工厂模式是一种创建对象的设计模式，通过定义一个接口来创建对象，而不是直接实例化对象。
工厂模式可以将对象的创建与使用分离，从而提高代码的可维护性和可扩展性。
实际例子：汽车工厂
假设你正在经营一家汽车制造公司。公司生产的汽车有两种类型：Sedan（轿车）和 Truck（卡车）。
客户可以根据自己的需求选择要购买的汽车类型，而你希望用一种灵活的方式来创建这两种类型的汽车，而不是在每次需要创建汽车时都写一堆重复的代码。
工厂类：负责根据输入条件（比如客户的订单类型）创建不同类型的产品对象。
产品接口：定义产品应该实现的通用方法。
具体产品类：实现产品接口的具体类，比如 Sedan 和 Truck。
"""


# 1. 定义产品接口
class Car:
    """
    定义一个通用的汽车接口，所有的汽车都应该实现 drive() 方法。
    """
    def drive(self):
        pass


# 2. 创建具体产品类
class Sedan(Car):
    """
    轿车类，继承自 Car 类，实现 drive() 方法。
    """
    def drive(self):
        return "Driving a sedan."


class Truck(Car):
    """
    卡车类，继承自 Car 类，实现 drive() 方法。
    """
    def drive(self):
        return "Driving a truck."


# 3. 创建工厂类
class CarFactory:
    """
    工厂类，根据输入条件创建不同类型的汽车对象。
    """
    @staticmethod
    def get_vehicle(car_type):
        if car_type == "sedan":
            return Sedan()
        elif car_type == "truck":
            return Truck()
        else:
            raise ValueError(f"Unknown car type: {car_type}")


# 4. 使用工厂模式
car1 = CarFactory.get_vehicle("sedan")
car1.drive()  # "Driving a sedan."

car2 = CarFactory.get_vehicle("truck")
car2.drive()  # "Driving a truck."

# CarFactory.create_car("suv")    # ValueError: Unknown car type: suv
"""
案例 1：发奖系统的商品发放
在某些系统中，需要根据用户的需求发放不同类型的商品，比如优惠券、实物商品、第三方兑换卡等。
每种商品的发放逻辑和接口可能不同，但可以通过工厂模式来统一管理。
场景描述
假设有一个发奖系统，支持发放以下三种类型的奖品：
优惠券：需要调用 sendCoupon 方法。
实物商品：需要调用 deliverGoods 方法。
第三方兑换卡：需要调用 grantToken 方法。
每种商品的发放逻辑不同，且可能会随着业务发展新增其他类型的商品。
"""


# 1.定义商品接口和具体实现类：
class Coupon:
    """优惠券"""
    def send(self, u_id, coupon_number, uuid):
        print(f"优惠券已发放给用户: {u_id}, 优惠券编号: {coupon_number}, UUID: {uuid}")


class PhysicalGoods:
    """
    实物商品
    """
    def deliver(self, req):
        print(f"实物商品已发货，发货地址：{req['address']}, 商品ID: {req['product_id']}")


class Token:
    """
    第三方兑换卡
    """
    def grant(self, mobile_number, card_id):
        print(f"兑换卡已发放，手机号：{mobile_number}, 卡ID: {card_id}")


# 2.创建工厂类
class AwardFactory:
    """
    奖品工厂类，根据输入条件创建不同类型的奖品对象。
    """
    @staticmethod
    def create_award(award_type):
        if award_type == "coupon":
            return Coupon()
        elif award_type == "physical_goods":
            return PhysicalGoods()
        elif award_type == "token":
            return Token()
        else:
            raise ValueError("未知的奖品类型")


# 客户端调用
factory = AwardFactory()

# 发放优惠券
coupon = factory.create_award("coupon")
coupon.send(u_id="123", coupon_number="ABC456", uuid="XYZ789")

# 发放实物商品
goods = factory.create_award("physical_goods")
goods.deliver(req={"address": "北京市朝阳区", "product_id": "P123"})

# 发放兑换卡
token = factory.create_award("token")
token.grant(mobile_number="13800138000", card_id="TK789")
