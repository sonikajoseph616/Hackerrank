''' # que.1

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
output = list(student_marks[query_name])    
per = sum(output)/len(output);
print("%.2f" % per);   

# que.2
def split_and_join(line):
    # write your code here
    line = line.split()
    line = "-".join(line)
    return line
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# que.3
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s=set(map(int,input().split()))
m=int(input())
r=set(map(int,input().split()))
print(len(s.intersection(r)))

# que.4
if __name__=="__main__":
    n = int(input())
    arr = map(int, input().split())
    arr = list(set(list(arr)))
    ar = len(arr)
    arr = sorted(arr)
    print(arr[ar-2])

# que.5
def swap_case(s):
    return s.swapcase()


if __name__ == '__main__':

# que.6

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

# que.7
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(int(a/b))
    print(float(a/b))

# que.8
n = int(input())
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

# que 9
Result =[]
scorelist = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Result+=[[name,score]]
        scorelist+=[score]
    b=sorted(list(set(scorelist)))[1] 
    for a,c in sorted(Result):
        if c==b:
            print(a)
    
# que 10
if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i*i)

# que 11
def is_leap(year):
    
    # variable to check the leap year
    leap = False
    
    # One if statement that contains multiple conditions
    if ((year % 400 == 0) and (year % 100 == 0)) | ((year % 4 ==0) and (year % 100 != 0)):
        
       # change leap to True
        leap = True

    
    return leap
# que.12
def count_substring(string, sub_string):
    count=0
    for i in range(len(string)):
        if string[i:i+len(sub_string)]==sub_string:
            count+=1
    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

# que. 13
if __name__ == '__main__':
    N = int(input())
    L=[];
    for i in range(0,N):
        cmd=input().split();
        if cmd[0] == "insert":
            L.insert(int(cmd[1]),int(cmd[2]))
        elif cmd[0] == "append":
            L.append(int(cmd[1]))
        elif cmd[0] == "pop":
            L.pop();
        elif cmd[0] == "print":
            print(L)
        elif cmd[0] == "remove":
            L.remove(int(cmd[1]))
        elif cmd[0] == "sort":
            L.sort();
        else:
            L.reverse();
            '''
