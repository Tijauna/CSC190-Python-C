#include <stdio.h>
#include <stdlib.h>

typedef struct {
   int *store;
   unsigned int size;
   unsigned int end;
   int (*compare)(int x,int y);
} intHeap_T;

int store(intHeap_T* heap,int value);
int retrieve(intHeap_T* heap,int *rvalue);
intHeap_T heapify(int *newX, int size,int (*compare)(int x,int y));


int lt(int x,int y) {
  if (x < y){
    return 1;
  }
  return 0;
}

int gt(int x,int y) {
  if (x > y){
    return 1;
  }
  return 0;
}

intHeap_T heapify(int *newX, int size,int (*compare)(int x,int y)){
  int i = 0;
  int returnvalue = 0;
  intHeap_T heap;
  heap.store=(int *)malloc(size*sizeof(int));
  heap.size=size;
  heap.end=0; /* empty heap condition; obey this spec */
  heap.compare = compare; /* assuming lt was defined as in part A */
  
  /*heap it */
  for (i=0;i<size;i++){
    store(&heap,newX[i]);

  } 
  
  return heap;

}

int hs(int *x,int size,int (*compare)(int x,int y)) {
  int temp;
  int i,j = 0;
  int rvalue;
  int* newArray = (int *)malloc(size*sizeof(int));
  int* tempArray = (int *)malloc(size*sizeof(int));
  int newSize = size;
  
  intHeap_T heap = heapify (x,size,compare);
  
  for (i = 0;i<size;i++){
  
    retrieve(&heap,&rvalue);
    
    printf("%d ",rvalue);
    newArray[i] = rvalue;
    
    newSize = newSize - 1;
   
    for (j = 0; j<newSize; j++){
      tempArray[j] = heap.store[j];
    }
    
    heap = heapify(tempArray,newSize,compare);
    
  }
  
  for (j = 0; j<size; j++){
    x[j] = newArray[j];
  }
  
  for (j = 0; j<size; j++){
    printf("\n%d\n",x[j]);
  }
  return 0;
  
  

} 
    
int retrieve(intHeap_T* heap,int *rvalue) {

  int current = 0;
  int done = 0;
  int temp = 0;
  int temp2 = 0;
  int addition = 0;
  
  if (heap == NULL){
    return -1;
  }
  
  else if (heap->end == 0){
    return -1;
  }
  else{
    
    *rvalue = heap->store[0];
    
    
    
    heap->store[0] = heap->store[heap->end-1];
    heap->end = heap->end - 1;
    
    /*printf("%d\n", heap->store[0]);*/
    
    heap->store[heap->end] = 0;
    
    /*there is only a left child*/
    if (heap->end == 1){
      if (heap->store[current] <= heap->store[(current*2) + 1]){
        temp = heap->store[current];
        heap->store[current*2+1] = heap->store[current];
        heap->store[current*2+1] = temp;
        return 0;
      }
    }
    
    else if (heap->end == 0){
      return 0;
    }
    
    while (done != 1){
      
      
      /*find bigger child, at least 2 children*/
      if (heap->store[(current*2) + 2] >= heap->store[(current*2) + 1]){
        /*right child is bigger*/
        /*printf("Right Child bigger\n");*/
        temp = heap->store[(current*2) + 2];
         /*printf("Will be moved up %d\n",temp);*/
        addition = 2;
        
      }
      
      else{
        /*left child is bigger*/
        /*printf("Left Child bigger\n");*/
        temp = heap->store[(current*2) + 1];
         /*printf("Will be moved up %d\n",temp);*/
        addition = 1;
      }
      
      if (heap->store[current] <= temp){
         /*printf("Swapping this down: %d\n",heap->store[current]);*/
        temp2 = heap->store[current];
        heap->store[current] = heap->store[current*2+addition];
        /*printf("New top: %d\n",heap->store[current]);*/
        heap->store[current*2+addition] = temp2;
        /*printf("New bottom: %d\n",heap->store[current*2+addition]);*/
        current = current*2 + addition;
        addition = 0;
      }

      
      else{
        done = 1;
      }
      
    }
    return 0;
  }
 
  
}



int store(intHeap_T *heap, int value){
  int end = 0;
  int temp = 0;
  int done = 0;
  
  if (heap == NULL){
    return -1;
  }
  
  if (heap->end == heap->size){
    return -1;
  }

  
  heap->store[heap->end] = value;
  
  if ((heap->end) == 0){
    /*
 *  *  *     printf("Adding to first position\n");*/
  }
  else{
    
    end = heap->end;
    
    while (done != 1)
    {
        
      /*for odd array position, must look up to right*/
      if (end%2 != 0){
        if (((heap->compare)(heap->store[(end-1)/2], heap->store[end])) == 1){
        
          /*printf("root upper right is smaller, swap\n");*/
          temp = heap->store[(end-1)/2];
          heap->store[(end-1)/2] = heap->store[end];
          heap->store[end] = temp;
          end = (end-1)/2;
        }
        else{
          /*printf("upper right already bigger\n");*/
          done = 1;
        }
      }
      
      
      /*for even array position, must look up to left*/
      else if (end%2 == 0){
        if (((heap->compare)(heap->store[(end-2)/2], heap->store[end])) == 1){
          
          /*printf("root upper left is smaller\n");*/
          temp = heap->store[(end-2)/2];
          heap->store[(end-2)/2] = heap->store[end];
          heap->store[end] = temp;
          end = (end-2)/2;
        }
        
        else{
          /*printf("upper left already bigger\n");*/
          done = 1;
        }
        
      }
      
     if (end == 0){
        done = 1;
      }
    
    }

  }
  
  heap->end = heap->end+1;
  

  return 0;
  
}
