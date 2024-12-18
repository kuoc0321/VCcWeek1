'''
Cho 2 mảng đã được sắp xếp. Tìm giao của hai mảng với độ phức tạp là o(mlog(n)) với m và n tương ứng là độ dài của 2 mảng

Kiến thức cần tìm hiểu:
- Độ phức tạp thuật toán
- Tìm kiếm nhị phân
'''

def binary_search(arr, high , low , target):
    if low > high:
        return False
    mid = low + (high - low) // 2
    if arr[mid] == target:
        return True
    if arr[mid] < target:
        return binary_search(arr,high, mid + 1, target )
    if arr[mid] > target:
        return  binary_search(arr,mid - 1 , low , target)

    return False

def intersection(arr1, arr2):
    arr2.sort()
    res = []
    for element in arr1:
        if binary_search(arr2, len(arr2) - 1, 0, element) :
            res.append(element)
    return res
arr1 = [12, 25, 37, 42, 18, 30]
arr2 = [37, 42, 12, 25, 55, 60, 72, 85, 18, 33, 49, 90, 27, 68]
print(intersection(arr1, arr2))