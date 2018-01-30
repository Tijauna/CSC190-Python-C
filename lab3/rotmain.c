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

int main(void){
   avlNode *proot = NULL;
   int rvalue = 0;
   avlNode *root=NULL;
   avlNode *test2 = NULL;
   avlNode *test3 = NULL; 
   avlNode *test4 = NULL;
   avlNode *test = NULL;

   add_bst(&root,5);
   add_bst(&root,3);
   add_bst(&root,1);
   add_bst(&root,4);
   add_bst(&root,7);
   add_bst(&root,6);
   add_bst(&root,8);
   add_bst(&root,9);
   add_bst(&root,10);

  
   add_bst(&test,10);
   add_bst(&test,5);
   add_bst(&test,11);
   add_bst(&test,2);
   add_bst(&test,8);
   
  
   add_bst(&test2,5);
   add_bst(&test2,2);
   add_bst(&test2,10);
   add_bst(&test2,8);
   add_bst(&test2,11);
   
  
   add_bst(&test4, 13);
   
  
   add_bst(&test3,3);
   add_bst(&test3,5);
   add_bst(&test3,4);

   printTreeInOrder(root);
   printLevelOrder(root);
   
   rvalue = isAVL(&root);
   
   printf ("\nIs this AVL? %d\n",rvalue);
   
   printf("\nBefore rotate right: ");
   printLevelOrder(test);
   
   
   
   rotate(&test,1);
   
   printf("\nAfter rotate right: ");
   printLevelOrder(test);
   
   printf("\nBefore Left Rotation: ");
   printLevelOrder(test2);
   
   
   rotate(&test2,0);
   
   printf("\nAfter rotate left: ");
   printLevelOrder(test2);
   
   
    printf("\nBefore LR Rotation: ");
   printLevelOrder(test3);
   
   rvalue = isAVL(&test3);
   
   printf ("\nIs this AVL? %d\n",rvalue);
   
   dblrotate(&test3, 0);

   printf("After LR Rotation: ");
   printLevelOrder(test3);

   printf("\n");

   add_bst(&proot,10);
   add_bst(&proot,5);
   add_bst(&proot,14);
   add_bst(&proot,4);
   add_bst(&proot,13);
   printf("%d\n",isAVL(&proot));
   add_bst(&proot,17);
   printf("%d\n", isAVL(&proot));
   add_bst(&proot,3);
   printf("%d\n",isAVL(&proot));
   add_bst(&proot,16);
   printf("%d\n",isAVL(&proot));
   add_bst(&proot,6);
   printf("%d\n",isAVL(&proot));
   add_bst(&proot,15);
   printf("%d\n",isAVL(&proot));
   printf("SHOULD PRINT: \n0\n0\n-1\n-1\n0\n-1\n");
}
