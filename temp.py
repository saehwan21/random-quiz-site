# def big_func():
#     for i in range(10):
#         print(i)
    

# def big_gen():
#     for i in range(10):
#         yield i

# print("big_func\n")
# print(big_func())
# print("\n")


# print("big_gen\n")
# g=big_gen()
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))

# gen_ex=(n*n for n in range(100))
# print(type(gen_ex))


# def asterisk_test(a,*args):
#     print(a, args)
#     print(type(args))
# test=(2,3,4,5,6)
# asterisk_test(1,*test)



# def asterisk_test(a,b,c,d,e=0):
#     print(a,b,c,d,e)
# data={"d":1, "c":2, "b":3}
# asterisk_test(10,**data)




# ex=([1,2],[3,4], [5,6])
# a,b,c=ex
# for value in zip(a,b,c):
#     print(value)


# for data in zip(*ex):
#     print(data)

# a=[1,2,3]
# b=['a','b','c']

# zip2=list(zip(a,b))

# print(list(zip2))
# print(dict(zip2))


# def swap_offset(offset_x, offset_y):
#     temp=a[offset_x]
#     a[offset_x]=a[offset_y]
#     a[offset_y]=temp


# def swap_reference(list_ex, offset_x, offset_y):
#     temp  =  list_ex[offset_x]
#     list_ex[offset_x]=list_ex[offset_y]
#     list_ex[offset_y]=temp

# a=[1,2,3,4,5]
# swap_reference(a,1,2)
# swap_offset(1,2)


class SoccerPlayer(object):
    pass

SoccerPlayer()



