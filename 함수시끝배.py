s=int(input("시작 값을 입력하세요:"))
e=int(input("끝 값을 입력하세요:"))
b=int(input("배수를 입력하세요:"))

def cal_hap(s, e, b):
    sum=0
    i=s
    while i<=e:
            if i%b==0:
                sum=sum+i
            i=i+1
    return sum


print(cal_hap(s, e, b))
    
