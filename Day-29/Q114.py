arr = list(map(int, input("Enter array elements: ").split()))

print("1. Display Array")
print("2. Find Maximum")
print("3. Find Minimum")
print("4. Sort Array")

choice = int(input("Enter choice: "))

if choice == 1:
    print(arr)

elif choice == 2:
    print("Maximum:", max(arr))

elif choice == 3:
    print("Minimum:", min(arr))

elif choice == 4:
    arr.sort()
    print("Sorted Array:", arr)

else:
    print("Invalid choice")
