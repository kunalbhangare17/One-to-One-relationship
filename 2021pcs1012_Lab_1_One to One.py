file = open("test1OOM.txt", "r")
total_number_of_elements = int(input())

lst = []
total = []
r = []
s = []
k = []

for i in range(1, total_number_of_elements + 1):
    input_1 = int(input())
    input_total = (i, input_1)
    if i == input_1:
        r.append(input_total)
    lst.append(input_total)

k = [t[::-1] for t in lst]

s = [i for i, j in zip(lst, k) if i != j]

b = [t[::-1] for t in s]

j = [i for i in s for j in b if i == j]
j = j + r

a = [b for a, b in j]
a = set(a)
print(a)