#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class quiz:

    def __init__(self):
        
        print()
        print('WELCOME TO EDYODA QUIZ APPLICATION')
        print("----------------------------------")
        self.question_input = []
        self.topic = []
2        self.difficulty = []
        self.options = []
        self.answer = {}
        self.question_no = 1
        self.total_score = 0
        self.user={}
        self.admint={}
        
        self.register()
        self.role()


    def question(self):
        sitansu= True
        while sitansu== True:
            question = input('Enter your question:\n')
            self.question_input.append(question)
            topic_input = input('Enter Section:\n')
            self.topic.append(topic_input)
            df = input('Enter Difficulty:\n')
            self.difficulty.append(df)
            a = []
            print('Enter the Options:\n')
            for i in range(4):
                a.append(input('Option '+str((i+1))+': '))
            self.options.append(a)
            

            self.answer[self.question_no]=int(input('Enter the correct option: \n'))
            self.question_no += 1
            

            new = input('Press Y to add more question or N to stop:\n')
            if new == 'N' or new == 'n':
                sitansu= False
                print()
                self.admin_menu()
            else:
                pass



    def display(self):
        print('Here are the total number of questions:',len(self.question_input))
        print()
        for i in range(len(self.question_input)):
            print('Question: '+self.question_input[i])
            for j in range(len(self.options[i])):
                print(str(j+1)+')'+str(self.options[i][j]))
            print()
        self.role()
    
    def admin(self):
        name = input('Enter Name:\n')
        if name in self.admint:
            ID = input('Enter passID:\n')
            if ID==self.admint[name]:
                print('Hello! Welcome Mr',name)
                self.admin_menu()
            else:
                print("invalid credential provide correct password")
                self.role()
        else:
            print("invalid cedential try with correct details")
            self.role()
    def admin_menu(self):
        print('1.create Quiz\n2.View Quiz\n3.Edit quiz\n4.Delete Quiz\n5.Create Topic\n6.View Topic\n7.Edit Topic\n8.Delete Topic\n9.Log Out')
        n=int(input())
        if n==1:
            self.question()
        elif n==2:
            self.display()
        elif n==3:
            self.editq()
        elif n==4:
            self.delq()
        elif n==5:
            self.createtopic()
        elif n==6:
            self.viewtopic()
        elif n==7:
            self.edittopic()
        elif n==8:
            self.deltopic()
        elif n==9:
            self.role()
            
        else:
            print('Enter valid choice')
            self.admin_menu()
    
    def student(self):
        name = input('Enter Name:\n')
        if name in self.user:
            ID =input('Enter Id:\n')
            if ID==self.user[name]:
                print('Hello',name)
                print('Your Quiz is ready!')
                print()
                self.student_menu()
            else:
                print("incorrect password")
                self.role()
        else:
            print("invalid credential try with correct name")
            self.role()
            
    def student_menu(self):
        print('1.View Sections\n2.Give Test\n3.Exit')
        f=int(input())
        if f==1:
            self.view_sections()
        elif f==2:
            self.give_test()
        elif f==3:
            self.role()
        else:
            print('Enter valid choice')
            self.student_menu()



    def view_sections(self):
        x=set(self.topic)
        print('Sections:\n',x)
        print("***************")
        self.student_menu()

    def give_test(self):
        print()
        print('Welcome to your quiz!')
        print('The marking system for the following quiz is pretty simple.')
        print('For easy questions - 1 marks\nFor medium questions - 2 marks\nFor hard questions - 3 marks')
        print('All the best!')
        print()
        score = 0

        for i in range(len(self.question_input)):
            print('Section:'+self.topic[i])
            print('Level of Difficulty:',self.difficulty[i])
            print()
            print(self.question_input[i])
            for j in range(len(self.options[i])):
                print('Option '+str(j+1)+')'+str(self.options[i][j]))
            
            print()
            std_choice = int(input('Enter option number:'))
            print()

            if std_choice == self.answer[i+1]:
                
                if self.difficulty[i] == 'easy':
                    score += 1
                elif self.difficulty[i] == 'medium':
                    score += 2
                elif self.difficulty[i] == 'hard':
                    score += 3
                    
            self.total_score = 0
            for h in self.difficulty:
                if h == 'easy':
                    self.total_score += 1
                elif h == 'medium':
                    self.total_score += 2
                elif h == 'hard':
                    self.total_score += 3


        print('You scored',str(score),'out of',self.total_score)
        print('Have a nice day! :)')
        self.student_menu()
        
    def editq(self):
        sitansu=True
        while sitansu==True:
            selectq=int(input("enter question no to edit:"))
            self.question_input[selectq-1]=input('type the edited question:')
            new=print("want to edit more press 1:")
            if new!=1:
                sitansu=False
                self.admin_menu()
            else:
                pass
            
            
    def delq(self):
        select=int(input("enter question no to delete:"))
        del self.question_input[select-1]
   
    def createtopic(self):
        n=int(input("enter no of topics to be added:"))
        for i in range(n+1):
            tp=input("enter name of topic:")
            self.topic.append(tp)
        self.admin_menu()
        
    def viewtopic(self):
        for i in range(1,len(self.topic)):
            print("TOPIC",i,self.topic[i])
        self.admin_menu()
        
        
    def edittopic(self):
        a=int(input("topic no to be edited:"))
        self.topic[a-1]=input("give edited topic name:")
        self.admin_menu()
    
    def deltopic(self):
        t=input("enter topic name to be deleted:")
        if t in self.topic:
            self.topic.remove(t)
        self.admin_menu()

        
        
            

    def register(self):
        
        user_or_admin=input("Press 1 for register as user and 2 for register as admin: ")
        if user_or_admin=='1':
            usernames=input("\n Enter username: ")
            password=input("Enter password: ")
            self.user[usernames]=password
            self.role()
      
        elif user_or_admin=='2':
            username=input("\n Enter username: ")
            password=input("Enter password: ")
            self.admint[username]=password
            self.role()
        
          
               
    
    def role(self):
        print('\nChoose your role: \n1.Admin \n2.Student\n3.rgister')
        choice = int(input())
        if choice == 1:
            self.admin()
        elif choice == 2:
            self.student()
        elif choice==3:
            self.register()
        
a =quiz()

