import math
ranger=int(input())
result=[]
for r in range(ranger):
    poem=input()
    a=int(math.sqrt(len(poem)))
    i=a-1
    j=a-1
    count=0
    result_String=''
    while(i<=len(poem)-1):
        while(j<=len(poem)-1):
            result_String=result_String+(poem[j])
            j=j+a
            count=count+1
        if(count==len(poem)):
            result.append(result_String)
            break
        i=i-1
        j=i
for solution in result:
    print(solution)
