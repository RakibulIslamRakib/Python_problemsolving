def unlimied_item(*args, **keyword_args):
    for key , items in keyword_args.items():
        print('{} : {}'.format(key,items))
    for i in args:
        print(i)

unlimied_item(1,3,4,4,name='rakib',age=22)#1 to 5
unlimied_item(*[1,2,3,4])#1 to 5
print("THE elements are {} ,{} ,{}".format(*[1,2,3]))
