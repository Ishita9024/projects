tasks_no=int(input("enter the total task : "))
i=1
a=[]
while i<=tasks_no:
    tasks_name=input("enter the tasks_name : ")
    a.append(tasks_name)
    i+=1
j=0
while j<len(a):
    print(j+1,".",a[j])
    j+=1
donetasks_no=int(input("enter the completed task no. : "))
k=1
while k<=donetasks_no:
    done_tasks=input("enter : ")
    a.remove(done_tasks)
    k+=1
l=0
while l<len(a):
    print(l+1,".",a[l])
    l+=1


    
