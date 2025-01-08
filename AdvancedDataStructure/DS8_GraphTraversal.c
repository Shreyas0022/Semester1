#include <stdio.h>
#include <stdbool.h>

#define MAX 10

int adj_matrix[MAX][MAX]; 
bool visited[MAX]; 
int vertex_count = 0;

void add_vertex() {
    if (vertex_count >= MAX) {
        printf("Cannot add more vertices. Maximum reached.\n");
        return;
    }
    vertex_count++;
    printf("Vertex %d added.\n", vertex_count - 1);
}

void add_edge(int start, int end) {
    if (start >= vertex_count || end >= vertex_count) {
        printf("Invalid vertex index!\n");
        return;
    }
    adj_matrix[start][end] = 1;
    printf("Edge added from %d to %d.\n", start, end);
}

void bfs(int start) {
    bool visited[MAX] = {false};
    int queue[MAX], front = 0, rear = 0;

    visited[start] = true;
    queue[rear++] = start;

    printf("BFS: ");
    while (front < rear) {
        int vertex = queue[front++];
        printf("%d ", vertex);

        for (int i = 0; i < vertex_count; i++) {
            if (adj_matrix[vertex][i] && !visited[i]) {
                visited[i] = true;
                queue[rear++] = i;
            }
        }
    }
    printf("\n");
}

void dfs_helper(int vertex) {
    visited[vertex] = true;
    printf("%d ", vertex);

    for (int i = 0; i < vertex_count; i++) {
        if (adj_matrix[vertex][i] && !visited[i]) {
            dfs_helper(i);
        }
    }
}

void dfs(int start) {
  
    for (int i = 0; i < MAX; i++) visited[i] = false;

    printf("DFS: ");
    dfs_helper(start);
    printf("\n");

  
    for (int i = 0; i < vertex_count; i++) {
        if (!visited[i]) {
            printf("DFS starting from vertex %d: ", i);
            dfs_helper(i);  
            printf("\n");
        }
    }
}


void topological_sort_helper(int vertex, int stack[], int *top) {
    visited[vertex] = true;

    for (int i = 0; i < vertex_count; i++) {
        if (adj_matrix[vertex][i] && !visited[i]) {
            topological_sort_helper(i, stack, top);
        }
    }

    stack[(*top)++] = vertex;
}

void topological_sort() {
    for (int i = 0; i < MAX; i++) visited[i] = false;

    int stack[MAX], top = 0;

    for (int i = 0; i < vertex_count; i++) {
        if (!visited[i]) {
            topological_sort_helper(i, stack, &top);
        }
    }

    printf("Topological Sort: ");
    while (top > 0) {
        printf("%d ", stack[--top]);
    }
    printf("\n");
}

int main() {
    int choice, start, end, vertex;
   printf("\n\tGRAPH TRAVERSAL- BFS & DFS\n");
    do {
        printf("\n1. Add Vertex\n2. Add Edge\n3. BFS\n4. DFS\n5. Topological Sort\n6. Exit\n\nEnter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                add_vertex();
                break;
            case 2:
                printf("Enter start and end vertex: ");
                scanf("%d %d", &start, &end);
                add_edge(start, end);
                break;
            case 3:
                printf("Enter starting vertex for BFS: ");
                scanf("%d", &vertex);
                bfs(vertex);
                break;
            case 4:
                printf("Enter starting vertex for DFS: ");
                scanf("%d", &vertex);
                dfs(vertex);
                break;
            case 5:
                topological_sort();
                break;
            case 6:
                printf("Exiting...\n");
                break;
            default:
                printf("Invalid choice! Try again.\n");
        }
    } while (choice != 6);

    return 0;
}
