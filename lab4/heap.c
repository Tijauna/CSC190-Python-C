#include <stdio.h>
#include <stdlib.h>

typedef struct {
   int *store;
   unsigned int size;
   unsigned int end;
} HeapType;

int initHeap (HeapType *pHeap,int size);
int inorder  (HeapType *pHeap, int **output, int *o_size);
int preorder (HeapType *pHeap, int **output, int *o_size);
int postorder(HeapType *pHeap, int **output, int *o_size);
void inorderHelper(HeapType *pHeap, int root, int o_size, int **output, int iteration);
int preorder(HeapType *pHeap, int **output, int *o_size);
void preorderHelper(HeapType *pHeap, int root, int o_size, int **output, int iteration);
int posteorder(HeapType *pHeap, int **output, int *o_size);
void postorderHelper(HeapType *pHeap, int root, int o_size, int **output, int iteration);
int addHeap(HeapType *pHeap, int key);
int findHeap(HeapType *pHeap, int key);
int delHeap(HeapType *pHeap, int *key);


int delHeap(HeapType *pHeap, int *key){
  int current = 0;
  int done = 0;
  int temp = 0;
  int temp2 = 0;
  int addition = 0;
  
  if (pHeap == NULL){
    return -1;
  }
  
  else{
    
    *key = pHeap->store[0];
    
    
    
    pHeap->store[0] = pHeap->store[pHeap->end-1];
    pHeap->end = pHeap->end - 1;
    
    /*printf("%d\n", pHeap->store[0]);*/
    
    pHeap->store[pHeap->end] = 0;
    
    /*there is only a left child*/
    if (pHeap->end == 1){
      if (pHeap->store[current] <= pHeap->store[(current*2) + 1]){
        temp = pHeap->store[current];
        pHeap->store[current*2+1] = pHeap->store[current];
        pHeap->store[current*2+1] = temp;
        return 0;
      }
    }
    
    else if (pHeap->end == 0){
      return 0;
    }
    
    while (done != 1){
      
      
      /*find bigger child, at least 2 children*/
      if (pHeap->store[(current*2) + 2] >= pHeap->store[(current*2) + 1]){
        /*right child is bigger*/
        /*printf("Right Child bigger\n");*/
        temp = pHeap->store[(current*2) + 2];
         /*printf("Will be moved up %d\n",temp);*/
        addition = 2;
        
      }
      
      else{
        /*left child is bigger*/
        /*printf("Left Child bigger\n");*/
        temp = pHeap->store[(current*2) + 1];
         /*printf("Will be moved up %d\n",temp);*/
        addition = 1;
      }
      
      if (pHeap->store[current] <= temp){
         /*printf("Swapping this down: %d\n",pHeap->store[current]);*/
        temp2 = pHeap->store[current];
        pHeap->store[current] = pHeap->store[current*2+addition];
        /*printf("New top: %d\n",pHeap->store[current]);*/
        pHeap->store[current*2+addition] = temp2;
        /*printf("New bottom: %d\n",pHeap->store[current*2+addition]);*/
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


int findHeap(HeapType *pHeap, int key){
  int i = 0;
  
  if (pHeap == NULL){
    return -1;
  }
  
  if (pHeap->end == 0){
    if (pHeap->store[0] == key){
      return 1;
    }
    else{
      return 0;
    }
  }
  
  for (i =0;i< (pHeap->end);i++){
    
    if (pHeap->store[i] == key){
      return 1;
    }
    
  }
  
  return 0;
}




int addHeap(HeapType *pHeap, int key){
  int end = 0;
  int temp = 0;
  int done = 0;
  
  if (pHeap == NULL){
    return -1;
  }
  
  
  pHeap->store[pHeap->end] = key;
  
  if ((pHeap->end) == 0){
    /*
 *  *     printf("Adding to first position\n");*/
  }
  else{
    
    end = pHeap->end;
    
    while (done != 1)
    {
        
      /*for odd array position, must look up to right*/
      if (end%2 != 0){
        if ((pHeap->store[(end-1)/2]) <= (pHeap->store[end])){
          /*printf("root upper right is smaller, swap\n");*/
          temp = pHeap->store[(end-1)/2];
          pHeap->store[(end-1)/2] = pHeap->store[end];
          pHeap->store[end] = temp;
          end = (end-1)/2;
        }
        else{
          /*printf("upper right already bigger\n");*/
          done = 1;
        }
      }
      
      
      /*for even array position, must look up to left*/
      else if (end%2 == 0){
        if ((pHeap->store[(end-2)/2]) <= (pHeap->store[end])){
          /*printf("root upper left is smaller\n");*/
          temp = pHeap->store[(end-2)/2];
          pHeap->store[(end-2)/2] = pHeap->store[end];
          pHeap->store[end] = temp;
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
  
  pHeap->end = pHeap->end+1;
  

  return 0;
  
}


void postorderHelper(HeapType *pHeap, int root, int o_size, int **output, int iteration){
  int i = 0;
  if(root > o_size-1){
    return;
  }
  
  postorderHelper(pHeap, root*2+1, o_size, output, iteration);

  postorderHelper(pHeap, root*2+2, o_size, output, iteration);  

  while ((*output)[i] != 0){
    i = i + 1;
  }
  
  (*output)[i] = pHeap->store[root];
  
  
}

int postorder  (HeapType *pHeap, int **output, int *o_size){
  int root = 0;
  int iteration = 0;
  int i = 0;
  
  if (pHeap == NULL){
    return -1;
  }
  
  *output = (int*)malloc(sizeof(int)*(pHeap->end));
  *o_size = pHeap->end;
  
  for (i = 0; i < *o_size; i++){
    (*output)[i] = 0;
  }
  
  postorderHelper(pHeap,root,*o_size,output,iteration);
  return 0;

}



void preorderHelper(HeapType *pHeap, int root, int o_size, int **output, int iteration){
  int i = 0;
  if(root > o_size-1){
    return;
  }
  
  

  while ((*output)[i] != 0){
    i = i + 1;
  }
  
  (*output)[i] = pHeap->store[root];
  
  preorderHelper(pHeap, root*2+1, o_size, output, iteration);

  preorderHelper(pHeap, root*2+2, o_size, output, iteration);  
}

int preorder  (HeapType *pHeap, int **output, int *o_size){
  int root = 0;
  int iteration = 0;
  int i = 0;
  
  if (pHeap == NULL){
    return -1;
  }
  
  *output = (int*)malloc(sizeof(int)*(pHeap->end));
  *o_size = pHeap->end;

  for (i = 0; i < *o_size; i++){
    (*output)[i] = 0;
  }
  
  preorderHelper(pHeap,root,*o_size,output,iteration);
  return 0;

}




void inorderHelper(HeapType *pHeap, int root, int o_size, int **output, int iteration){
  int i = 0;
  if(root > o_size-1){
    return;
  }
  
  inorderHelper(pHeap, root*2+1, o_size, output, iteration);

  while ((*output)[i] != 0){
    i = i + 1;
  }
  
  (*output)[i] = pHeap->store[root];

  inorderHelper(pHeap, root*2+2, o_size, output, iteration);  
}

int inorder  (HeapType *pHeap, int **output, int *o_size){
  int root = 0;
  int iteration = 0;
  int i = 0;
  if (pHeap == NULL){
    return -1;
  }
  
  *output = (int*)malloc(sizeof(int)*(pHeap->end));
  *o_size = pHeap->end;

  
  for (i = 0; i < *o_size; i++){
    (*output)[i] = 0;
  }
  
  inorderHelper(pHeap,root,*o_size,output,iteration);
  return 0;

}
  


int initHeap (HeapType *pHeap,int size){
  
  if (pHeap == NULL){
    return -1;
  }

  pHeap->size = size;

  pHeap->store = (int*)malloc(size*(sizeof(int)));
  pHeap->end = 0;
  return 0;
}
