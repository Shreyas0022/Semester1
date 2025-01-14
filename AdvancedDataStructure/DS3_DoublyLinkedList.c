#include<stdio.h>
#include<stdlib.h>

struct node
{
        struct node * prev;
        int data;
        struct node * next;
};

struct node * head=NULL;


struct node * createnode(int item)
{
        struct node * newnode = (struct node*)malloc(sizeof(struct node));
        newnode->prev = NULL;
        newnode->data = item;
        newnode->next = NULL;
        return newnode;
}

void insertAtFront(int item)
{
        struct node * newnode = createnode(item);
        newnode->next = head;
        head = newnode;
        printf("%d Inserted!\n",item);
}

void insertAtPosition(int item,int position)
{
        if(position<1)
        {
                printf("Position cannot be <1.\n");
                return;
        }
        if(position == 1)
        {
                insertAtFront(item);
                return;
        }

        struct node * newnode = createnode(item);
        struct node * temp = head;

        for (int i = 1; i < position - 1 && temp != NULL; i++)
        {
                temp = temp->next;
        }
        if (temp == NULL)
        {
                printf("Position Not available.\n");
                free(newnode);
        }
        else
        {
                newnode->next = temp->next;
                newnode->prev = temp;
                temp->next = newnode;
                temp->next->prev = newnode;
                printf("Item Inserted at %d position!\n",position);
        }
}



void insertAtBack(int item)
{
        struct node * newnode = createnode(item);
        if(head == NULL)
        {
                head = newnode;
        }
        struct node* temp = head;
        while(temp->next != NULL)
                temp = temp->next;
                temp->next = newnode;
                newnode->prev = temp;
                newnode->next=NULL;

                printf("%d Inserted!\n",item);
}

void deleteFromFront()
{
    if(head == NULL)
    {
        printf("List is empty!\n");
        return;
    }

    struct node* temp = head;
    head = temp->next;

    if (head != NULL)
    {
        head->prev = NULL;
    }

    free(temp);
    printf("First Node Deleted!\n");
}


void deleteFromPosition(int position)
{
        if (head == NULL)
        {
                printf("List is empty.\n");
                return;
        }
        if (position < 1)
        {
                printf("Position cannot be <1.\n");
                return;
        }
        if (position == 1)
        {
                deleteFromFront();
                return;
        }

        struct node* temp = head;
        struct node* loc = NULL;

        for (int i = 1; i < position && temp != NULL; i++)
        {
                loc = temp;
                temp = temp->next;
        }
        if (temp == NULL)
        {
                printf("Position Not available.\n");
        }
        else
        {
                loc->next = temp->next;
                temp->next->prev = loc;
                free(temp);
                printf("Item deleted");
        }
}


void deleteFromBack()
{
        if(head == NULL)
        {
                printf("List is empty.\n");
                return;
        }

        struct node* temp = head;
        struct node* loc = NULL;

        if(temp->next == NULL)
        {
                free(temp);
                head = NULL;
                return;
        }

        while(temp->next != NULL)
        {
                loc=temp;
                temp = temp->next;
        }
        loc->next = NULL;
        free(temp);
        printf("Last Node Deleted!\n");
}


void display()
{
        struct node* temp = head;
        if(temp == NULL)
        {
                printf("List is empty.\n");
                return;
        }
        printf("HEAD -> ");
        while(temp != NULL)
        {
                printf("%d <-> ", temp->data);
                temp = temp->next;
        }
        printf("NULL\n");
}

int main()
{
        int choice,item,position;
        do{
		printf("\n*************DOUBLY LINKEDLIST OPERATION****************\n\n");
                printf("1.Insert at Beginning\n2.Insert at End\n3.Insert at Position\n4.Delete from Beginning\n5.Delete from End\n");
                printf("6.Delete from Position\n7.Display\n8.Exit\nEnter your choice :");
                scanf("%d",&choice);
                switch(choice)
                {
                        case(1):
                                printf("Enter item to Insert be  at Beginning of the List :");
                                scanf("%d",&item);
                                insertAtFront(item);
                                break;

                        case(2):
                                printf("Enter item to be Insert at End :");
                                scanf("%d",&item);
                                insertAtBack(item);
                                break;

			case(3):
                                printf("Enter the position :");
                                scanf("%d",&position);
                                printf("Enter item to be inserted :");
                                scanf("%d",&item);
                                insertAtPosition(item,position);
                                break;

                        case(4):
                                deleteFromFront();
                                break;

                        case(5):
                                deleteFromBack();
                                break;

                        case(6):
                                printf("Enter the position :");
                                scanf("%d",&position);
                                deleteFromPosition(position);
                                break;

                        case(7):
                                display();
                                break;
                        case(8):
                                printf("Exiting...\n");
                                break;
                        default:
                                printf("Invalid choice!Try again.\n");
                                break;
                }
        } while(choice!=8);

        return 0;
}

