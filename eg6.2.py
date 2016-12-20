num = 23
running = True
while running:
    guess = input("please input num")
    if num == guess:
        running = False
        print ('yes,you guess it')
    elif guess < num:
        print ('you guess too small')
    else:
        print ("you guess too large")
else:
    print ('loop over')
