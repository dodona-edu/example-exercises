#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    int sum = 0;

    for (int i = 1; i < argc; i++) {
        char *end;
        int number = strtol(argv[i], &end, 10);
        if (*end != '\0') {
            fprintf(stderr, "invalid arguments\n");
            return 1;
        }
        sum += number;
    }

    printf("%d\n", sum);
    return 0;
}
