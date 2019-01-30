s = {'唐僧','悟空','八戒','沙僧'}

# for x in s:
#     print(x)
# else:
#     print('遍历结束')

# it = iter(s)
# while True:
#     try:
#         s = next(it)
#         print(s)
#     except StopIteration:
#         print('遍历结束')
#         break


i = iter(s)
while True:
    try:
        s = next(i)
        print(s)
    except StopIteration:
        print('遍历结束')
        break
