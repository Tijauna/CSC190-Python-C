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

int main(void) {
  HeapType test;
  int o_size;
  int *output;
  int i = 0;
  int deleted = 0;
  
  initHeap(&test,8);
  

  addHeap(&test, 12);
  addHeap(&test, 11);
  addHeap(&test, 10);
  addHeap(&test, 9);
  addHeap(&test, 7);
  addHeap(&test, 8);
  addHeap(&test, 2);
  addHeap(&test, 15);
  
  
  printf("Finding: %d\n",findHeap(&test,2));
  
  delHeap(&test,&deleted);
  
  printf("%d\n",deleted);
  


  
  
  
  
   printf("inorder:\n");
   
  inorder(&test,&output,&o_size);
  
 for (i = 0; i < o_size; i++){
    printf("%d ",output[i]);
  }
  
  printf("\npreorder:\n");
  
preorder(&test,&output,&o_size);
  
 for (i = 0; i < o_size; i++){
    printf("%d ",output[i]);
  }
  
  printf("\npostorder:\n");
  
postorder(&test,&output,&o_size);
  
 for (i = 0; i < o_size; i++){
    printf("%d ",output[i]);
  }
  
  

  
  
  

   
 
}
