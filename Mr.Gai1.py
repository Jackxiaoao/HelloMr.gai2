phone = input("请输入一个手机号:")
list = [123,134,135,136,137,138]
try:
    int(phone)
    if(len(phone) == 11):
        a = phone[0:3]
        bool = False
        for i in list:
            if (int(a) == i):
                bool = True
                break
        if(bool):
            print("有效手机号")
        else:
            print("无效手机号")
    else:
        print("不正确手机号")
except ValueError:
    print("输入的不是有效手机号")