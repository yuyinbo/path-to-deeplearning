# 作者: 余殷博
# cangj87@gmail.com


class Gun:
    def __init__(self, model):
        # 枪的型号
        self.model = model
        # 子弹数量
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        # 判断是否还有子弹
        if self.bullet_count <= 0:
            print("没有子弹了")
            return
        # 发射一颗子弹
        self.bullet_count -= 1
        print("%s 发射子弹[%d]" % (self.model, self.bullet_count))


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
        self.gun.add_bullet(50)
        while self.gun.bullet_count:
            # 射到子弹耗尽
            # 假如此循环中再加入一个自减，每轮循环会减两次
            self.gun.shoot()


if __name__ == '__main__':
    gun1 = Gun('AK47')
    gun1.add_bullet(50)
    gun1.shoot()
    soldier1 = Soldier("Mark", None)
    soldier2 = Soldier("Tom", gun1)
    soldier1.fire()
    soldier2.fire()
