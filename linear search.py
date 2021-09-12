
def reverse(li):
    l=len(li)
    for i in range(l//2):
        li[i],li[l-i-1]=li[l-i-1],li[i]

li=[int(x) for x in input().split()]
print(li)
reverse(li)
print(li)