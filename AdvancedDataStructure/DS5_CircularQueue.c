#include <stdio.h>
#include <stdlib.h>

int *queue;
int size;
int front = -1, rear = -1;

void initializeQueue() {
    queue = (int *)malloc(size * sizeof(int));
}

void enqueue(int element) {
    if (front == (rear + 1) % size) {
        printf("Queue is full\n");
        return;
    }
    if (front == -1 && rear == -1) {
        front = rear = 0;
    } else {
        rear = (rear + 1) % size;
    }
    queue[rear] = element;
}

int dequeue() {
    int element;
    if (front == -1 && rear == -1) {
        printf("Queue is empty\n");
        return -1;
    }
    element = queue[front];
    if (front == rear) {
        front = rear = -1;
    } else {
        front = (front + 1) % size;
    }
    printf("%d dequeued from the queue\n", element);
    return element;
}

int searchElement(int element) {
    if (front == -1 && rear == -1) {
        printf("Queue is empty\n");
        return -1;
    }
    int current = front;
    int position = 1;
    do {
        if (queue[current] == element) {
            return position;
        }
        current = (current + 1) % size;
        position++;
    } while (current != (rear + 1) % size);
    return -1;
}

void displayQueue() {
    if (front == -1 && rear == -1) {
        printf("Queue is empty\n");
        return;
    }
    printf("Queue elements: ");
    int current = front;
    do {
        printf("%d ", queue[current]);
        current = (current + 1) % size;
    } while (current != (rear + 1) % size);
    printf("\n");
}

int main() {
    int choice, searchResult, element;
    printf("Enter the size of the Circular Queue: ");
    scanf("%d", &size);
    initializeQueue();

    do {
        printf("\n*Circular Queue Operations*\n");
        printf("\n1. ENQUEUE\n");
        printf("2. DEQUEUE\n");
        printf("3. SEARCH\n");
        printf("4. DISPLAY\n");
        printf("5. EXIT\n");
        printf("Enter Your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter the element to Enqueue: ");
                scanf("%d", &element);
                enqueue(element);
                break;
            case 2:
                dequeue();
                break;
            case 3:
                printf("Enter the element to search: ");
                scanf("%d", &element);
                searchResult = searchElement(element);
                if (searchResult != -1) {
                    printf("%d found at position %d\n", element, searchResult);
                } else {
                    printf("%d not found in the queue\n", element);
                }
                break;
            case 4:
                displayQueue();
                break;
            case 5:
                printf("Exiting the program.\n");
                break;
            default:
                printf("Invalid choice. Please enter a valid option.\n");
                break;
        }
    } while (choice != 5);

    free(queue);
    return 0;
}
