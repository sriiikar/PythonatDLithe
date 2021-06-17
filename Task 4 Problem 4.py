# Array of hill

n= int(input())

arr = list(map(int, input().split()))

if len(arr) == 1:
    print("Yes")
else:
    prev_val = arr[0]
    surface = False
    for index in range (1,len(arr)):
        if prev_val == arr[index]:
            surface = True
        elif prev_val > arr[index] and not surface:
            print("No")
            break
        elif prev_val < arr[index] and surface:
            print("No")
            break
        prev_val = arr[index]
    else:
        print("Yes")