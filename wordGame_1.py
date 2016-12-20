# coding:utf-8
import random
temp = input("开始猜")
guess = temp
count = 0
think = random.randint(1, 10)
while guess != think and count <= 3:
    temp = input("猜错了")
    guess = temp
    if guess == think:
        print ("你居然猜中了")
        print ("猜中没奖励")
    else:
        if guess < think:
            print ('小了')
            count += 1
        else:
            print ('大了')
            count += 1
print ("游戏结束")
