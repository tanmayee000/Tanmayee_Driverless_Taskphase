n=int(input("Enter n"))
hash_table =[[] for i in range(10)]

for i in range(n):
    num=int(input("Enter Number:"))
    hash_table[num%10].append(num)
    print(hash_table)
