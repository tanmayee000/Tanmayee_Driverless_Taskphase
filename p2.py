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


n = int(input("Enter n: "))

strings = []
for i in range(n):
    strings.append(input(f"String {i+1}: "))

sorter = StringSorter(strings)
print("Sorted:", sorter.selection_sort())
