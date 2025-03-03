"""
假设我们正在开发一款游戏，需要创建很多不同类型的怪物。
每个怪物有类似的属性（如名称、生命值、攻击力），但可能有一些不同。我们可以使用原型模式来简化怪物的创建过程。

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
