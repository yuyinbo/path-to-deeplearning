# 作者: 余殷博
# cangj87@gmail.com
# 对于对象的深copy和浅copy
import copy


class Gun:
    def __init__(self, model):
        # 枪的型号
        self.model = model
        # 子弹数量
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self, user_name = '无人'):
        # 判断是否还有子弹
        if self.bullet_count <= 0:
            print("没有子弹了")
            return
        # 发射一颗子弹
        self.bullet_count -= 1
        print("%s用%s射击, 剩余子弹%d" % (user_name, self.model, self.bullet_count))


class Soldier:
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun

    def fire(self):
        if self.gun is None:
            print("请给%s一把枪" % self.name)
            return
        # 如果士兵没枪
        print("%s开火了" % self.name)
        self.gun.shoot(self.name)


if __name__ == '__main__':
    gun1 = Gun('AK47')
    gun1.add_bullet(50)
    gun1.shoot()
    soldier1 = Soldier("Mark", None)
    soldier2 = Soldier("Tom", gun1)
    soldier1.fire()
    soldier2.fire()
    print('-'*50)

    gun2 = Gun('M4A1')
    soldier2 = Soldier("Tom", gun2)
    gun2.add_bullet(50)
    soldier3 = copy.copy(soldier2)
    print(f'id(soldier2)={id(soldier2)}, id(soldier3)={id(soldier3)}')
    print(f'id(soldier2.gun)={id(soldier2.gun)}, id(soldier3.gun)={id(soldier3.gun)}')
    # 浅copy，soldier3和soldier2实际上共用一把枪
    soldier3.name = "Jerry"
    soldier3.fire()
    soldier2.fire()
    # 两人只能用同一把枪交替射击
    print()

    gun3 = Gun('QBZ-95')
    soldier2 = Soldier("Tom", gun3)
    soldier4 = copy.deepcopy(soldier2)
    print(f'id(soldier2)={id(soldier2)}, id(soldier4)={id(soldier4)}')
    print(f'id(soldier2.gun)={id(soldier2.gun)}, id(soldier4.gun)={id(soldier4.gun)}')
    soldier4.name = "Mary"
    gun3.add_bullet(50)
    soldier4.gun.add_bullet(50)
    # 必须分别添加子弹
    soldier4.fire()
    soldier2.fire()
    # 两人有不同的枪