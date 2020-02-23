#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

ans = input ('so you want to see how I want to start my day?')

if ans == 'yes':
    print ('first I get up and go walk my dog!')
    dogname = input('but first guess what is my dog name?')
    print('puppy', dogname, '!')
    print('lets start')
    print('give dog breakfast')
    ing = input ('what does he eat?')
    if ing == 'dog food':
        print('yes! my dog is very spoiled!')
        ing2 = input('do I eat anything for breakfast?')
        if ing2 =='yes':
            print('I make coffee and eggs')
     
            
            ing3 = input ('do I really want to go to work?')
            if ing3 == 'no':
                print('thats right! I want to be home and do my homework')
                print('but I like money')
                ans2 = input ('have I medidate yet?')
                if ans2 == 'yes':
                    print('then I more prepared for my day')
                    print('I eat my breakfast')
                    print('then go brush my teeth and wash my face')
                    print ('change my clothes get ready to leave for work')
                    print('get my car keys and drive for 45 min in traffic')
                    print('get to work and stayed there for 8 hours')
                else:
                    print('Im still tired')
            else:
                print('actually I really wanna go back to sleep')
    else:
            print('im hungry') 
                    
                
                
    

