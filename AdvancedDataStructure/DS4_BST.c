#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node* left;
    struct node* right;
};

struct node *root = NULL;

void createNode(int x) {
    struct node *newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data = x;
    newnode->left = NULL;
    newnode->right = NULL;
    if (root == NULL) {
        root = newnode;
        printf("Created root node: %d\n", root->data);
    } else {
        printf("Node created: %d\n", newnode->data);
    }
}

void insert(int item) {
    if (root == NULL) {
        createNode(item);
        return;
    }
    struct node *current = root;
    struct node *parent = NULL;
    while (1) {
        parent = current;
        if (item < current->data) {
            current = current->left;
            if (current == NULL) {
                parent->left = (struct node*)malloc(sizeof(struct node));
                parent->left->data = item;
                parent->left->left = parent->left->right = NULL;
                printf("Inserted %d to the left of %d\n", item, parent->data);
                return;
            }
        } else {
            current = current->right;
            if (current == NULL) {
                parent->right = (struct node*)malloc(sizeof(struct node));
                parent->right->data = item;
                parent->right->left = parent->right->right = NULL;
                printf("Inserted %d to the right of %d\n", item, parent->data);
                return;
            }
        }
    }
}

struct node* minValueNode(struct node* node) {
    struct node* current = node;
    while (current && current->left != NULL)
        current = current->left;
    return current;
}

struct node* del(struct node* root, int item) {
    if (root == NULL) {
        printf("Node %d not found in the tree.\n", item);
        return NULL;
    }

    if (item < root->data)
        root->left = del(root->left, item);
    else if (item > root->data)
        root->right = del(root->right, item);
    else {
        if (root->left == NULL) {
            struct node* temp = root->right;
            free(root);
            return temp;
        } else if (root->right == NULL) {
            struct node* temp = root->left;
            free(root);
            return temp;
        }

        struct node* temp = minValueNode(root->right);
        root->data = temp->data;
        root->right = del(root->right, temp->data);
    }
    return root;
}

void search(int item) {
    struct node *current = root;
    while (current != NULL) {
        if (current->data == item) {
            printf("Node %d found\n", item);
            return;
        }
        current = (item < current->data) ? current->left : current->right;
    }
    printf("Node %d not found in the tree.\n", item);
}


void inorderTraversal(struct node *root) {
    if (root != NULL) {
        inorderTraversal(root->left);
        printf("%d  ", root->data);
        inorderTraversal(root->right);
    }
}

void preorderTraversal(struct node *root) {
    if (root != NULL) {
        printf("%d  ", root->data);
        preorderTraversal(root->left);
        preorderTraversal(root->right);
    }
}

void postorderTraversal(struct node *root) {
    if (root != NULL) {
        postorderTraversal(root->left);
        postorderTraversal(root->right);
        printf("%d  ", root->data);
    }
}

int main() {
    while (1) {
        int ch;
	printf("\n********* BST OPERATIONS **********\n");
        printf("\n1.Insert a Node\n2.Delete a Node\n3.Search a Node\n4.Inorder Traversal\n5.Preorder Traversal\n6.Postorder traversal\n7.Exit\n\nEnter your choice: ");
        scanf("%d", &ch);
        switch (ch) {
            case 1: {
                int x1;
                printf("\nEnter the key to be inserted: ");
                scanf("%d", &x1);
                insert(x1);
                break;
            }
            case 2: {
                int x2;
                printf("\nEnter the key to be deleted: ");
                scanf("%d", &x2);
                root = del(root, x2);
                break;
            }
            case 3: {
                int x3;
                printf("\nEnter the key to be searched: ");
                scanf("%d", &x3);
                search(x3);
                break;
            }
            case 4:
                printf("Inorder Traversal: ");
                inorderTraversal(root);
                printf("\n");
                break;
            case 5:
                printf("Preorder Traversal: ");
                preorderTraversal(root);
                printf("\n");
                break;
            case 6:
                printf("Postorder Traversal: ");
                postorderTraversal(root);
                printf("\n");
                break;
            case 7:
                printf("\nExiting !\n");
                exit(0);
            default:
                printf("INVALID CHOICE !\n");
        }
    }
    return 0;
}

