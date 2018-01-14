/* This is an example of how to use a linked list as a
 *mic container to store data that is input with an
 * unknown number of items.
 *  *
 *   * Note how we get the data:
 *    * -while loop (because the number of iterations is unknown)
 *     * -scanf returns EOF, or End-Of-File, when "nothing" has been input
 *      * -for each iteration, we stuff the input data into a linked list
 *       *
 *        * Usage:
 *         * gcc getData.c
 *          * echo "1 2 3 4 5 6 7 8     9      10" | ./a.out
 *           * should report 10 items read and dump it out
 *            * -> white space is ignored (space, tab, return)
 *             *
 *              * Assignment:
 *               * -modify this code so that it handles input "char" data
 *                *  rather than ints (trivial modification)
 *                 * echo "abcdef" | ./a.out
 *                  * should report 7 items read
 *                   * (white space is representable by the char hence the
 *                    * final return you enter is stored as a char)
 *                     */

#include <stdio.h>
#include <stdlib.h>

struct llnode {
   char value;
   struct llnode *next;
};
typedef struct llnode llnode;


int llnode_add_to_head(llnode **x,char value){

llnode *oldhead = NULL;

if (x==NULL) {
return -1;
}

if (*x == NULL)
{

*x = (llnode*)malloc(sizeof(llnode));
(*x)->value = value;
(*x)->next = NULL;

return 0;
}

else{

oldhead = *x;
*x = (llnode *)malloc(sizeof(llnode));
(*x)->value = value;
(*x)->next = oldhead;
return 0;
}
}


int llnode_add_to_tail(llnode **x,char value) {
   if (x==NULL) { return -1; }
   if (*x==NULL) {
      *x = (llnode *) malloc(sizeof(llnode));
      (*x)->value = value;
      (*x)->next = NULL;
      return 0;
   } else {
      return llnode_add_to_tail(&((*x)->next),value);
   }
}

int llnode_print_from_head(llnode *x) {
   if (x==NULL) { return 0; }
   else {
      printf("%c\n",x->value);
      return llnode_print_from_head(x->next);
   }
}

int llnode_print_from_tail(llnode *x) {
   if (x==NULL) { return 0; }
   else {
      if (x->next == NULL) {
         printf("%c\n",x->value);
	 return 0;
      } else {
         llnode_print_from_tail(x->next);
         printf("%c\n",x->value);
	 return 0;
      }
   }
}

int push(llnode **x, char value){
int returnvalue = 0;
if (x==NULL){
return -1;
}

returnvalue = llnode_add_to_head(x, value);
return returnvalue;

}



int pop(llnode **x, char *return_value){
llnode *current = NULL;

if (x == NULL){
return -1;
}

if (*x == NULL){

return -1;
}

current = *x;

*return_value = (*x)->value;

*x = (*x)->next;

free(current);

return 0;
}

int main(void) {
   int totalinputs = 0;
   int n=0;
   int i = 0;
   char value=0;
   char *return_value = (char*)malloc(sizeof(char));
   int rvalue=0;
   int failure = 0;
   llnode *input_list=NULL;

   while (scanf("%c",&value) != EOF) {
      
      if ((value == '(') || (value == '[') || (value == '{')){
/*printf("open bracket\n");*/      
n = n +1;
totalinputs ++;
      push(&input_list,value);}

      else if ((value == ')') || (value == ']') || (value == '}')){
/*printf("close bracket\n");*/     
totalinputs ++;
      pop(&input_list,return_value);
       
      if ((*return_value == '(') && (value == ')'))  {     
failure = 0;
n = n - 1;  
    }

else if ((*return_value == '[') && (value == ']'))  {
failure = 0;
n = n - 1;
      }

else if ((*return_value == '{') && (value == '}'))  {
failure = 0;
n = n - 1;
      }

else{

printf("FAIL,%d",totalinputs-1);
failure = 1;
break;
}
}
}

if ((failure == 0)&&(n == 0)) {
printf ("PASS");

}

/*for (i = 0; i < n; i++){
    rvalue = pop(&input_list,return_value);
    printf("%c\n",*return_value); 
}*/
     return 0;
}
