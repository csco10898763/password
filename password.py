i = 3
while True:
    password = input('\n請輸入密碼：')
    if password == 'a123456':
        print('\n登入成功 !!!')
        break
    else:    
        i = i - 1
        if i == 0:
            print('\n輸入三次錯誤 !!!')
            break
        print('\n密碼錯誤!! 您還有', i, '次機會')
        