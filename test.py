# 1

# import calendar
# y1 = 1990
# print(calendar.isleap(y1))

# 2

# n = int(input())
# i = 1
# while i <= n:
#     print(i, end = '')
#     i = i + 1

# 3
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
#
# print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if sum([x, y, z]) != n])

#4

# inp = input().split()
# func = lambda x: int(x)
# a = list(map(func, inp))
# print(len(a))
# print(max(a))
# print(list(enumerate(a)))
# a = [9, 2, 10, 20, 9]
# # print(a)
# # a.sort()
# # print(a)
# # print(a[-2])
# print(a)
#
# a.sort()
# print(a[-2])


# lst = [1, 2, 5, 7, 12, 3320]
# func = lambda x: x
# print(list(map(func, lst)))
# a = list(enumerate(lst))
# print(len(a))


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(set(arr))[-2])
