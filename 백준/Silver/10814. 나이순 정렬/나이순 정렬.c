#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int age;      
    char name[101]; 
} Member;

int compare(const void* a, const void* b) {
    Member* memberA = (Member*)a;
    Member* memberB = (Member*)b;

    if (memberA->age != memberB->age) {
        return memberA->age - memberB->age; 
    }

    return 0; 
}

int main() {
    int N;
    scanf("%d", &N);

    Member* members = malloc(sizeof(Member) * N);

    for (int i = 0; i < N; i++) {
        scanf("%d %s", &members[i].age, members[i].name);
    }

    qsort(members, N, sizeof(Member), compare);

    for (int i = 0; i < N; i++) {
        printf("%d %s\n", members[i].age, members[i].name);
    }

    free(members);

    return 0;
}
