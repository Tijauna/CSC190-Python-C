def quick_sort(u,ini,fin):
   
   if (ini<fin):
     pIndex = partition(u,ini,fin)

     quick_sort(u,ini,pIndex-1)
     quick_sort(u,pIndex+1,fin)
     
   return True

def partition(u,ini,fin):
   pivot = u[ini]
   
   left = ini+1
   right = fin
   finished = 0
   
   while finished != 1:
     while left <= right and u[left] <= pivot:
       left = left + 1 

     while right >= left and u[right] >= pivot:
       right = right - 1

     if right < left:
         finished = 1 
     
     #swap left and right since they are out of place 
     else:
         temp = u[left]
         u[left] = u[right]
         u[right] = temp

   temp = u[ini]
   u[ini] = u[right]
   u[right] = temp
   
   return right
   
def hanoi(n,start,tmp,final):
   if n > 0:
        hanoi(n - 1,start,final,tmp)
        final.append(start.pop())
        hanoi(n - 1,tmp,start,final)
        print start,tmp,final
        return True
   else:
        return True
