"""
原型模式是一种设计模式，用于通过复制一个现有实例（原型）来创建新实例，而不是通过调用构造函数。
这种方法可以通过减少对象创建的开销（特别是当对象初始化很复杂时）来优化代码性能，并且可以轻松地修改新对象的某些属性。
下面是一个通俗易懂的示例，结合实际的例子来讲解 Python 中的原型模式。

假设我们正在开发一款游戏，需要创建很多不同类型的怪物。
每个怪物有类似的属性（如名称、生命值、攻击力），但可能有一些不同。我们可以使用原型模式来简化怪物的创建过程。

原型模式的优点
减少冗余代码：无需每次都手动创建复杂的对象。
提高性能：复制已有实例比调用构造函数更快。
增强灵活性：可以轻松地创建变体对象。

目标
创建一个怪物原型（MonsterPrototype），并生成其克隆体。
修改克隆体的某些属性（如名称），而不影响原始原型。
"""

import copy


# 原型类
class MonsterPrototype:
    """
    怪物原型类
    """

    def __init__(self, hp=100, attack=10):
        self.hp = hp
        self.attack = attack
        self.name = "Monster Prototype"

    def clone(self):
        """克隆对象"""
        return copy.copy(self)

    def display(self):
        """显示怪物信息"""
        print(f"Monster: {self.name}, HP: {self.hp}, Attack: {self.attack}")


# 使用原型模式克隆怪物
if __name__ == "__main__":
    # 创建一个原型怪物
    prototype_monster = MonsterPrototype()
    print("原型怪物：")
    prototype_monster.display()

    # 克隆原型怪物并修改属性
    cloned_monster = prototype_monster.clone()
    cloned_monster.name = "Goblin"
    cloned_monster.display()

    # 再克隆一个怪物
    another_cloned_monster = prototype_monster.clone()
    another_cloned_monster.name = "Orc"
    another_cloned_monster.display()
