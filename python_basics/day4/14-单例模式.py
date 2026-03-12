# 作者: 余殷博
# cangj87@gmail.com


class MusicPlayer(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        # __new__会在创建对象时自动调用（用来分配空间）
        if cls.instance is None:
            # 如果此前没分配过该类的空间
            # 按照父类的__new__就会多次分配空间
            print("创建对象，分配空间")
            # 为对象分配空间
            cls.instance = super().__new__(cls)
            # 返回对象的引用
        return cls.instance

    def __init__(self, music_name):
        print(f"播放器初始化{music_name}")
        self.music_name = music_name


if __name__ == '__main__':
    player1 = MusicPlayer('Faded')
    player2 = MusicPlayer('500 Miles Away')
    print(id(player1))
    print(id(player2))
    # 实际上就是同一个对象
