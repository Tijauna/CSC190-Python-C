#include <stdio.h>
#include <stdlib.h>

struct avlNode {
   int balance; /* -1 Left, 0 balanced, +1 Right */
   int val;
   struct avlNode *l;
   struct avlNode *r;
};
typedef struct avlNode avlNode;

struct qNode {
   avlNode *pval;
   struct qNode *nxt;
};
typedef struct qNode qNode;

int add_bst(avlNode **root,int val);
int printTreeInOrder(avlNode *root);
int printLevelOrder(avlNode *root);
int Pop(qNode **root, avlNode **returnValue);
int Push(qNode **root, avlNode *bst);
int isAVL(avlNode **root);
int depthFinder(avlNode *root);
int rotate(avlNode **root,unsigned int Left0_Right1);
int max(int a, int b);
int dblrotate(avlNode **root,unsigned int MajLMinR0_MajRMinL1);

int max(int a, int b){
  if (a>=b){
    return a;
  }
  
  else{
    return b;
  }
  
}

int dblrotate(avlNode **root,unsigned int MajLMinR0_MajRMinL1){
  if (root == NULL){
    return -1;
  }
  
  else if (*root == NULL){
    return 0;
  }
  
  /*Right first, then left LR*/
  if (MajLMinR0_MajRMinL1 == 0){
    rotate(&((*root)->r), 1);
    rotate(root, 0);
    return 0;
  }
  
  /*left first, then right RL*/
  else if (MajLMinR0_MajRMinL1 == 1){
    rotate(&((*root)->l), 0);
    rotate(root, 1);
    return 0;
  }

return -1;
}




int rotate(avlNode **root,unsigned int Left0_Right1){
  if (root == NULL){
    return -1;
  }
  
  else if (*root == NULL){
    return 0;
  }
  
  if (Left0_Right1 == 1){
    avlNode *temp1 = (*root)->l;
    avlNode *temp2 = temp1->r;
    temp1->r = *root;
    (*root)->l = temp2;

    *root = temp1;
    return 0;
  }
  
  else if (Left0_Right1 == 0){
    avlNode *temp1 = (*root)->r;
    avlNode *temp2 = temp1->l;
    temp1->l = *root;
    (*root)->r = temp2;
   
    *root = temp1;
    return 0;
  }
  
  else
  {
    return -1;
  }
}




int depthFinder(avlNode *root){
  if (root == NULL){
    return 0;
  }
  
  else{
    if (depthFinder(root->l) >= depthFinder(root->r)){
      return 1 + depthFinder(root->l);
    }
    
    else if (depthFinder(root->r) >= depthFinder(root->l)){
      return 1 + depthFinder(root->r);
    }
  }
}


int isAVL(avlNode **root){
  int rightDepth = 0;
  int leftDepth = 0;
  
  if (root == NULL){
    return -1;
  }
  
  else if (*root == NULL){
    /*empty tree*/
    return 0;
  }
  
  else
  {
    leftDepth = depthFinder((*root)->l);
    rightDepth = depthFinder((*root)->r);
    
    /*printf("\n%d L depth vs ",leftDepth);
 *     printf("%d R depth\n",rightDepth);*/
    
    if ((abs(rightDepth - leftDepth) <= 1) && (isAVL(&((*root)->l)) == 0) && (isAVL(&((*root)->r)) == 0))
    {
      /*printf ("IS AVL\n");*/
      return 0;
    }
      
    else{
      return -1;
    }
    
  }
  
  return -1;
}




int Pop(qNode **x, avlNode ** returnValue){
  
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





int Push(qNode **x, avlNode *bst){

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



int add_bst(avlNode **root,int val){
  
  if (root == NULL){
    /*printf("Fail\n");*/
    return -1;
  }
  
  else if (*root == NULL){
    *root = ( avlNode *) malloc(sizeof(avlNode));
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

int printTreeInOrder(avlNode *root){

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

int printLevelOrder(avlNode *root){

 if (root == NULL){
   return -1;
 } 
 
 else{ 
   qNode* queue = NULL;
   avlNode * temp = root;
   avlNode * returnValue = NULL;
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
