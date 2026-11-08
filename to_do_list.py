from termcolor import colored
import os

tasks = []


while True:
    os.system('cls')
    print(colored('\n===== TO-DO LIST =====' , 'blue' , attrs=['bold']))
    
    choice = input(' 1) add a task \n 2)show your task \n 3)Delete task \n 4)task completed \n 5)exit \n --->' )
   
    if choice == '1':
        print(colored('To go back wirt ..' ,'red' , attrs=['bold'] ))
        task = input('wirt a task: ') 
        if choice == '..':
              continue
        else:
            tasks.append(task)
        
              
              
        
     

    elif choice == '2':
            for x in tasks:
                print('-', x)
            input('press Enter to continue...')

    elif choice == '3':
        for x in tasks:

            print('-', x)
            print('To go back wirt  ..')
        deL = input('what do you want to Delete: ')
        if deL == '..':
              
              continue
        else:
            try:
                tasks.remove(deL)
                print('Deleted successfully!')
            except ValueError:
                    print('task not found')
            input('press Enter to continue...')
       
             
    
    elif choice == '4':
        for x in tasks:
              print('-' , x)
              print('To go back wirt ..')
        completed_task = input('what do you completed:')
        if completed_task == '..':
             continue
        else:
            tasks.remove(completed_task)

            print('nice work ! ')

            input('press Enter to continue...')

            pass
    
    elif choice == '5':

        print('good bye !!')

        break

    else:
            print('wrong choice')
            input('press Enter to continue...')

           
                 