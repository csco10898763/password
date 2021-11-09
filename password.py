password = 'a123456'
i = 3
while i > 0:
    i = i - 1
    pwd = input('\n請輸入密碼：')
    if pwd == password:
        print('\n登入成功 !!!')
        break
    else:    
        # i = i - 1
        # if i == 0:
            # print('\n輸入三次錯誤 !!!')
            # break
        
        if i > 0:
            print('\n密碼錯誤!!! 您還有', i, '次輸入機會 !!!')
        else:
            print('\n您已錯誤三次,系統已鎖定 !!!')