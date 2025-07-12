print("MY TO-DO LIST!!")                                                                          
task_numbers=int(input("How many tasks you want to enter: "))                                     
tasks=[]                                                                                          
if task_numbers>0:                                                                                
    for i in range(1, task_numbers + 1):                                                          
        task =input(f"Enter Task {i}: ")                                                          
        tasks.append(f"Task {i}: {task}")                                                         
    print(f"{task_numbers} Tasks added successfully!✅")                                           
    print("\n📋Your Current Task list:")                                                           
    for task in tasks:                                                                            
        print(task)                                                                               
    print("Complete Your tasks!👍")                                                                
    if task_numbers==0:                                                                           
        print("Add at least one task!!")                                                          
else:                                                                                             
    print("INVALID!")                                                                             
while True:                                                                                       
    choice=input("\nDo you want to Update your task list? (yes/no): ")                            
                                                                                                  
    if choice=="yes":                                                                             
        task_num=int(input("Which task number you want to update? \n"))                           
                                                                                                  
        if 1<=task_num<=task_numbers:                                                             
            new_task=input("Enter the updated task: ")                                            
            tasks[task_num-1]= f"Task {task_num}: {new_task}"                                     
            print("Your task is updated successfully!✅")                                          
                                                                                                  
                                                                                                  
            print("\n📋Your Final Task List: ")                                                    
            for task in tasks:                                                                    
                print(task)                                                                       
            print("You are good to go!☻")                                                         
        else:                                                                                     
            print("❌ That task doesn't exist! Please enter a number between 1 and", task_numbers) 
                                                                                                  
    elif choice == "no" :                                                                         
        print("👍 Exiting update mode.")                                                           
        break                                                                                     
    else:                                                                                         
       print("❗ Please type 'yes' or 'no'.")                                                      
while True:                                                                                       
    track =input("\nDo you want to track your list? (yes/no): ")                                  
                                                                                                  
    if track == "yes":                                                                            
        tsk_num=int(input("Which task number did you complete? \n"))                              
                                                                                                  
        if 1<=tsk_num<=task_numbers:                                                              
            mark1= "Completed"                                                                    
            tasks[tsk_num-1]= f"[✓] Task {tsk_num} -> {mark1}"                                    
            print("Tracking done 👍")                                                              
                                                                                                  
            print("\nMy To-Do List: ")                                                            
            for task in tasks:                                                                    
                print(task)                                                                       
            print("🎉 Congo!! for completing the task!☻")                                          
        else:                                                                                     
            print("❌ That task doesn't exist! Please enter a number between 1 and", task_numbers) 
                                                                                                  
    elif track == "no" :                                                                          
         print("👍 Exiting tracking mode.")                                                        
         break                                                                                    
    else:                                                                                         
         print("❗ Please type 'yes' or 'no'.")                                                    
