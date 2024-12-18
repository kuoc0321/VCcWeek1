'''
Tìm vị trí đầu tiên và cuối cùng của một thành phần trong mảng đã sắp xếp
input: một mảng đã được sắp xếp tăng dần và một số
output: vị trí đầu tiên và cuối cùng của số đã cho
nếu không tồn tại thì trả về -1
'''

def binary_search(arr, high , low , target):
    if low > high:
        return -1
    mid = low + (high - low) // 2
    if arr[mid] == target:
        first_ele = mid
        while first_ele - 1 >= 0 and arr[first_ele - 1] == target:
            first_ele -= 1
        last_ele = mid
        while last_ele + 1 <= len(arr) -1 and arr[last_ele + 1] == target:
            last_ele += 1
        return [first_ele, last_ele]
    if arr[mid] < target:
        return binary_search(arr,high, mid + 1, target )
    if arr[mid] > target:
        return  binary_search(arr,mid - 1 , low , target)
    return -1

nums = [5,6,7,8,8,15]
target = 8

print(binary_search(nums, len(nums) - 1 , 0 , target))
