#include <stdio.h>
#include <stdlib.h>

struct bstNode {
   int val;
   struct bstNode *l;
   struct bstNode *r;
};
typedef struct bstNode bstNode;

struct avlNode {
   int balance; /* -1 Left, 0 balanced, +1 Right */
   int val;
   struct avlNode *l;
   struct avlNode *r;
};
typedef struct avlNode avlNode;

struct qNode {
   bstNode *pval;
   struct qNode *nxt;
};
typedef struct qNode qNode;

int add_bst(bstNode **root,int val);
int printTreeInOrder(bstNode *root);
int printLevelOrder(bstNode *root);
int Pop(qNode **root, bstNode **returnValue);
int Push(qNode **root, bstNode *bst);



int Pop(qNode **x, bstNode ** returnValue){
  
qNode *current = NULL;

if (x == NULL){
return -1;
}

else if (*x == NULL){
/*printf("Queue is empty.\n");*/
*returnValue = NULL;
return -1;
}

else{
current = *x;

*returnValue = (*x)->pval;

*x = (*x)->nxt;

free(current);

return 0;
}
}





int Push(qNode **x, bstNode *bst){

if (x==NULL) { return -1; }

   if (*x==NULL) {
      
      *x = (qNode *) malloc(sizeof(qNode));
      (*x)->pval = bst;
      (*x)->nxt = NULL;
      return 0;
   }
   else {
      return Push(&((*x)->nxt), bst);
   }
}



int add_bst(bstNode **root,int val){
  
  if (root == NULL){
    /*printf("Fail\n");*/
    return -1;
  }
  
  else if (*root == NULL){
    *root = ( bstNode *) malloc(sizeof(bstNode));
    (*root)->val = val;
    (*root)->l = NULL;
    (*root)->r = NULL;
    return 0;
  }
  else{
    if (val < (*root)->val){
  
      return add_bst(&((*root)->l), val);
    }
    else if (val > (*root)->val){
      
      return add_bst(&((*root)->r), val);
    }
    
    return 0;
  }
  
}

int printTreeInOrder(bstNode *root){

	if (root == NULL){
		return -1;
	}
	
	
	else{

    printTreeInOrder(root->l);

		printf("%d\n",root->val);
	
		printTreeInOrder(root->r);

	
		return 0;
		
	}
}

int printLevelOrder(bstNode *root){

 if (root == NULL){
   return -1;
 } 
 
 else{ 
   qNode* queue = NULL;
   bstNode * temp = root;
   bstNode * returnValue = NULL;
   int empty = 0;
   
  Push(&queue, temp);
  

  while (empty != 1){

  /*push children*/
	if (temp->l != NULL){
	Push(&queue, temp->l);
	}	
	
	if (temp->r != NULL){
	Push(&queue, temp->r);
	}
	
	if (queue->nxt != NULL){
	Pop(&queue, &returnValue);
	printf ("%d ",returnValue->val);
	temp = queue->pval;

	}
	
	else if (queue->nxt == NULL){
	Pop(&queue, &returnValue);
	printf ("%d ",returnValue->val);
	empty = 1;
	}
	
	else{
	  empty = 1;
	}
	
  }
  
	
	return 0;
 }

 	
} 



int main(void) {
   /*bstNode *root=NULL;
 *    add_bst(&root,5);
 *       add_bst(&root,3);
 *          add_bst(&root,1);
 *             add_bst(&root,4);
 *                add_bst(&root,7);
 *                   add_bst(&root,6);
 *                      add_bst(&root,8);
 *
 *                         printTreeInOrder(root);
 *                            printLevelOrder(root);*/
   
   int n=0;
   int value=0;
   int rvalue=0;
   bstNode *root = NULL;

   while (scanf("%d",&value) != EOF) {
      n=n+1;
      add_bst(&root,value);
   }

   printTreeInOrder(root);


  return 0;

}

