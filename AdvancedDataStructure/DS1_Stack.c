#include<stdio.h>
#include<stdlib.h>
struct node{
int data ;
struct node* next;
};
struct node* top=NULL;

void push()
{
int value;
struct node*temp=(struct node*)malloc(sizeof(struct node));
printf("Enter the value to be inserted:");
scanf("%d",&value);
temp->data=value;
temp->next=top;
top=temp;
printf("%d  is inserted",value);
}

void pop()
{
int item;
struct node*temp=top;
if(top==NULL)
{
printf("Stack is empty");
}
else
{
item=top->data;
temp=top;
top=top->next;
free(temp);

printf("element popped from the stack");

}
}


void display()

{
struct node*temp=top;

if(top==NULL)
{
printf("Stack is empty");
}

else
{
printf("The Elements in Stack are:\n");
while(temp!=NULL)
{
printf("%d->",temp->data);
temp=temp->next;
}
}
}


void search()
{
struct node*temp=top;
int pos=1,found=0,elem;

 if(top==NULL)
 {
 printf("Stack is empty");
 }

 printf("Enter the Element to search:");
 scanf("%d",&elem);
  while(temp!=NULL)
 {
  if(temp->data==elem)
   {
   printf("%d found at position %d",elem,pos);
   found=1;
	break;
	}
    temp=temp->next;
   pos++;
}
if(found==0)
{
printf("%d is not found in stack",elem);
}
}




int main()
{
int choice;
printf("\nStack operations using Linked List\n");

do{
 printf("\n.......................\n1.Push\n2.pop\n3.display\n4.Search\n5.Exit\nEnter your choice:");
 scanf("%d",&choice);

  switch(choice)
{
   case 1:
    push();
    break;
   case 2:
    pop();
    break;
   case 3:
    display();
    break;
  case 4:
   search();
   break;
 case 5:
  printf("Exiting from Stack");
  break;
  default:
  printf("Invalid choice");
  break;
}
}
while(choice!=5);
return 0;
} 
