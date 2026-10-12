"""二分查找：在有序数组中查找目标元素，返回其索引；不存在返回 -1"""


def binary_search(arr: list, target) -> int:
    """在升序列表 arr 中查找 target，找到返回索引，否则返回 -1"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11]
    print(f"在 {data} 中查找 7，索引: {binary_search(data, 7)}")
    print(f"在 {data} 中查找 4，索引: {binary_search(data, 4)}")
