def gcd(a,b):
    if b==0:
        return a
    elif a>b:
        return gcd(b,a%b)
    else:
        return gcd(a,b%a)
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dict_ = {}
        for a in deck:
            if a in dict_:
                dict_[a]+=1
            else:
                dict_[a]=1
        arr = []
        for k,v in dict_.items():
            arr.append(v)
        flag = 0
        if len(arr)>1:
            gcd_ = gcd(arr[0],arr[1])
            if gcd_>=2:
                for i in range(2,len(arr)):
                    if gcd(arr[i],gcd_)<2:
                        flag=1
                        break
            else:
                flag=1
        elif len(arr)>0 and arr[0]>1:
            flag = 0
        else:
            flag=1
        if flag==0:
            return True
        else:
            return False