def quick_sort(arr):
    """
    快速排序函数
    参数:
    arr (list): 待排序的列表
    返回值:
    list: 排序后的列表
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # 选择中间元素作为基准值
    print("选择中间元素作为基准值：",pivot)
    left, middle, right = [], [], []
    for num in arr:
        if num < pivot:
            left.append(num)  # 小于基准值的元素放入左子列表
            print("小于基准值的元素放入左子列表:",num)
        elif num == pivot:
            middle.append(num)  # 等于基准值的元素放入中间子列表
            print("中间基准值的元素放入左子列表:",num)
        else:
            right.append(num)  # 大于基准值的元素放入右子列表
            print("大于基准值的元素放入左子列表:",num)
    print("左边",left, "中间",middle, "右边",right)
    return quick_sort(left) + middle + quick_sort(right)  # 递归排序左子列表和右子列表，并合并结果

# 示例用法：
if __name__ == "__main__":
    unsorted_list = [4, 6, 8, 10, 1, 2, 1]
    print("原始列表为",unsorted_list)
    sorted_list = quick_sort(unsorted_list)
    print("排序后的列表:", sorted_list)

