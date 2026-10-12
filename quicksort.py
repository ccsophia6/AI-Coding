"""快速排序：返回升序排序的新列表（不修改原列表）"""


def quicksort(arr: list) -> list:
    """对列表进行快速排序，返回新的升序列表"""
    # 递归终止条件：空数组或单元素数组本身就是有序的
    if len(arr) <= 1:
        return arr[:]
    pivot = arr[len(arr) // 2]
    # 分区：按与基准比较分成三部分，equal 天然处理重复元素
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return quicksort(less) + equal + quicksort(greater)


if __name__ == "__main__":
    data = [9, 3, 7, 1, 8, 2, 5]
    print(f"{data} 排序后: {quicksort(data)}")
