#               Intersection of Two Arrays


class Solution(object):
    def binary(self,num,i,record):
        s=0
        e=len(num)-1
        if i in record:
            return True
        while(s<=e):
            mid=(s+e)//2
            if(num[mid]==i):
                if i not in record:
                    record.append(i)
                return True
            elif(num[mid]>i):
                e=mid-1
            elif(num[mid]<i):
                s=mid+1
        
        return False

    def intersection(self, nums1, nums2):
    
        if(len(nums1)>len(nums2)):
            main,sub=nums2,nums1
            
        else:
            main,sub=nums1,nums2
        record=[]
        result=[]
        print(main)
        sub.sort()
        for i in main:
            #if i in sub:
            found=self.binary(sub,i,record)
            print(sub)
            print(i," is ",found)
            
            if(found and i not in result):
                result.append(i)
        return result