
print('--------------------------------')
print('         UIC CS Track')
print('--------------------------------\n')

credits = 0

cs111_class = 'NA'
cs112_class = 'NA'
cs113_class = 'NA'
cs141_class = 'NA'
cs151_class = 'NA'
cs211_class = 'NA'
cs251_class = 'NA'
cs277_class = 'NA'
cs401_class = 'NA'
cs377_class = 'NA'
cs261_class = 'NA'
cs301_class = 'NA'
cs341_class = 'NA'
cs342_class = 'NA'
cs361_class = 'NA'
cs362_class = 'NA'
cs499_class = 'NA'

# Here we grab the user's answers to 'Have you taken ...' questions and add up credits for each class.
print('QUESTION 1')
cs_major = input('Are you a CS major? (Yes or No): ')
if cs_major.upper() == 'YES':
    engr = input('\nQUESTION 2\n' + 'Have you taken ENGR100? (Yes or No): ')
    # Level 1 classes
    if engr.upper() == 'YES' or 'NO':
        cs111_class = input('\nQUESTION 3\n' + 'Have you taken CS111? (Yes or No): ')
        if cs111_class.upper() == 'NO':
            cs112_class = input('Have you taken CS112? (Yes or No): ')
            if cs112_class.upper() == 'NO':
                cs113_class = input('Have you taken CS113? (Yes or No): ')
        # Level 2 and 3 classes        
        if cs111_class.upper() == 'YES' or cs112_class.upper() == 'YES' or cs113_class.upper() == 'YES':
            credits = credits + 3
            cs141_class = input('\nQUESTION 4\n' + 'Have you taken CS141? (Yes or No): ')
            if cs141_class.upper() == 'YES':
                credits = credits + 3
                cs151_class = input('\nQUESTION 5\n' + 'Have you taken CS151? (Yes or No): ')
                if cs151_class.upper() == 'YES':
                    credits = credits + 3
                    cs211_class = input('\nQUESTION 6\n' + 'Have you taken CS211? (Yes or No): ')
                    if cs211_class.upper() == 'YES' or cs211_class.upper() == 'NO':
                        cs251_class = input('\nQUESTION 7\n' + 'Have you taken CS251? (Yes or No): ')
                        if cs211_class.upper() == 'YES':
                            credits = credits + 3
                        if cs251_class.upper() == 'YES':
                            credits = credits + 4
                            cs277_class = input('Have you taken CS277? (Yes or No): ')
                            if cs277_class.upper() == 'YES':
                                credits = credits + 3
                                cs377_class = input('Have you taken CS377? (Yes or No): ')
                                if cs377_class.upper() == 'YES':
                                   credits = credits + 3 
                            cs401_class = input('Have you taken CS401? (Yes or No): ')
                            if cs401_class.upper() == 'YES':
                                credits = credits + 3
                        cs261_class = input('\nQUESTION 8\n' + 'Have you taken CS261? (Yes or No): ')
                        if cs261_class.upper() == 'YES':
                            credits = credits + 4
                            # Level 4 classes
                            if cs211_class.upper() == 'YES' and cs251_class.upper() == 'YES' and cs261_class.upper() == 'YES' and cs277_class.upper() == 'YES' and cs377_class.upper() == 'YES' and cs401_class.upper() == 'YES':
                                cs301_class = input('\nQUESTION 9\n' + 'Have you taken CS301? (Yes or No): ')
                                if cs301_class.upper() == 'YES':
                                    credits = credits + 3
                            cs341_class = input('\nQUESTION 10\n' + 'Have you taken CS341? (Yes or No): ')
                            if cs341_class.upper() == 'YES':
                                credits = credits + 3
                            cs342_class = input('\nQUESTION 11\n' + 'Have you taken CS342? (Yes or No): ')
                            if cs342_class.upper() == 'YES':
                                credits = credits + 3
                            cs361_class = input('\nQUESTION 12\n' + 'Have you taken CS361? (Yes or No): ')
                            if cs361_class.upper() == 'YES':
                                credits = credits + 4
                            cs362_class = input('\nQUESTION 13\n' + 'Have you taken CS362? (Yes or No): ')
                            if cs362_class.upper() == 'YES':
                                credits = credits + 4
                            if cs301_class.upper() == 'YES' and cs341_class.upper() == 'YES' and cs342_class.upper() == 'YES' and cs361_class.upper() == 'YES' and cs362_class.upper() == 'YES':
                                cs499_class = input('\nQUESTION 14\n' + 'Have you taken CS499? (Yes or No): ')
                                credits = credits + 0

print('\n--------------------------------')
print('           Summary')
print('--------------------------------\n')

# Here we give the user thier summary based on thier input.
if cs_major.upper() == 'NO':
    print('Sadly, you are not a CS major.')  
else:
    print('You are a CS major!')
    if credits == 46 and cs401_class == 'YES':
        print('Congratulations on your upcoming graduation!')
    if engr.upper() == 'NO':
        print('Do not forget to take ENGR100!')
if cs_major.upper() == 'YES':
    print('\nRequired CS credits earned: ' + str(credits) + '.')
    print('Required CS credits left: ' + str(46 - credits) + '.')

print('\nThank you for using App!')
print('Closing app...')