class StringSorter:
    def __init__(self, items):
        self.items = items

    def selection_sort(self):
        arr = self.items
        n = len(arr)
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j].lower() < arr[min_idx].lower():
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    def binary_search(self, key):
        arr = self.items
        key = key.lower()
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            current = arr[mid].lower()

            if current == key:
                return mid
            elif current < key:
                low = mid + 1
            else:
                high = mid - 1

        return -1


n = int(input("Enter n: "))

strings = []
for i in range(n):
    strings.append(input(f"String {i+1}: "))

obj = StringSorter(strings)
print("Sorted:", obj.selection_sort())

target = input("Enter string to search: ")
pos = obj.binary_search(target)

if pos != -1:
    print(f"'{target}' found at index {pos}")
else:
    print(f"'{target}' not found")
