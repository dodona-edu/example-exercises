#include <stdio.h>

int main() {
    char naam[100];
    scanf("%99[^\n]", naam);
    printf("Hallo, %s!\n", naam);
    return 0;
}
