#include <stdio.h>
#include <stdlib.h>


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

int bs(int *array,int size,int (*compare)(int x,int y)) { 
  int j,x,i = 0;
  int status = 0;
  if (size == 1){
   return 0; 
  }

  if (array == NULL){
    return -1;
  }
  

  for (i = 0; i < (size-1); i++){
    
    for (j= 0; j < (size-1-i); j++){
      if ((*compare)(array[j],array[j+1]) == 1){
        int temp = array[j];
        array[j] = array[j+1];
        array[j+1] = temp;
      }
    }
  }
  
  
  
  for (x= 0; x < size - 1; x++){
    if (((*compare)(array[x], array[x+1])) == 0){
      status = 0;
    }
    else{
      status = -1;
      return status;
    }
  }
  return status;
}

