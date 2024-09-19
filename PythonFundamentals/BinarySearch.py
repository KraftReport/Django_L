import pandas as pd

datas = pd.Series([1, 4, 5, 8, 12, 15, 19, 23, 28, 33, 37])

def binary_search(list,value):
    start = 0
    end = len(datas) - 1

    while start <= end:
        mid = (start + end) // 2
        mid_value = list[mid]

        if mid_value == value:
            print(f"data is found at index {mid}")
            return

        elif mid_value > value:
            end = mid - 1

        elif mid_value < value:
            start = mid + 1

    print("data is not found in given list")


binary_search(datas, 15)