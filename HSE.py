n = int(input())
dic = {"север": 0, "запад": 0, "юг": 0, "восток": 0}
for i in range(n):
    s = input().split()
    dic[s[0]] += int(s[1])
x = dic["восток"]
x -= dic["запад"]
y = dic["север"]
y -= dic["юг"]
print(x, y)
