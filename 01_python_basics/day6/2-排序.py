# 作者: 余殷博
# cangj87@gmail.com
import copy
import random


class Sort(object):
    def __init__(self, count, nums_range):
        self.count = count
        self.arr = []
        self.nums_range = nums_range
        self.random_nums()

    def random_nums(self):
        for i in range(self.count):
            self.arr.append(random.randint(0, self.nums_range - 1))

    def partition(self, left, right):
        arr = self.arr
        k = left
        # 以最右侧为枢轴量
        # k是“小于等于pivot”的区域边界
        for i in range(left, right):
            # i用来遍历数组，只遍历到倒数第二个，因为最后一个是枢轴量
            if arr[i] < arr[right]:
                arr[i], arr[k] = arr[k], arr[i]
                k += 1
                # 发现了一个比枢轴量小的数，则该区域元素加一
        arr[k], arr[right] = arr[right], arr[k]
        return k

    def partition1(self, left, right):
        # 另有挖坑法，先将枢轴量取出暂存，形成一个坑
        arr = self.arr
        pivot = arr[left]
        while left < right:
            while (left < right) and (arr[right] >= pivot):
                right -= 1
                # 右指针不断向左，直到找到第一个比枢轴量小的元素
            arr[left] = arr[right]
            # 放在最左边
            while (left < right) and (arr[left] <= pivot):
                left += 1
                # 左指针不断向右，直到找到第一个比枢轴量大的元素
            arr[right] = arr[left]
            # 放在最右边
        arr[left] = pivot
        return left

    def quick_sort(self, left, right):
        if left < right:
            pivot = self.partition(left, right)
            self.quick_sort(left, pivot - 1)
            self.quick_sort(pivot + 1, right)

    def heapify(self, parent_pos, arr_len):
        """
        把某一子树调整为大根堆
        :param parent_pos:要调整的位置
        :param arr_len:列表的长度
        :return:
        """
        arr = self.arr
        dad = parent_pos
        son = 2 * dad + 1
        # 先看左孩子
        while son < arr_len:
            # 如果子节点存在
            if son + 1 < arr_len and arr[son] < arr[son + 1]:  # 如果有右孩子且左孩子小于右孩子
                son += 1  # 则son指向右孩子
            if arr[dad] < arr[son]:  # 如果父节点小于孩子中较大的一个
                arr[dad], arr[son] = arr[son], arr[dad]  # 交换父子
                dad = son  # 交换后的son成为新dad
                son = 2 * dad + 1
            else:
                # 假如父节点已经是最大的了
                break
                # 这棵子树已经调整好了

    def heap_sort(self):
        """
        大根堆实际上输出的是从小到大的排序
        """
        arr = self.arr
        # 先将数组建堆
        for parent_pos in range(self.count // 2 - 1, -1, -1):
            # 最后一个非叶节点的下标是n//2-1，倒着遍历到0
            self.heapify(parent_pos, len(arr))

        for end_pos in range(self.count - 1, 0, -1):
            # 将未排序区域逐步前移，下界为1，实际上end_pos=1时不会调用调整函数
            arr[0], arr[end_pos] = arr[end_pos], arr[0]
            # 将堆顶放到队列末尾
            self.heapify(0, end_pos)
            # 只有堆顶不符合大根堆的要求，所以只需要对堆顶做一次调整


if __name__ == '__main__':
    s = Sort(10, 100)
    t = copy.deepcopy(s)
    # 将t设置为s的副本
    print(s.arr)
    s.quick_sort(0, 9)
    print(s.arr)
    t.heap_sort()
    print(t.arr)
