#include <stdio.h>
#include <string.h>

void e(char *q, int n) {
    char *p = q;
    int i = 0;
    while (*p) {
        *p = ((((*p + n) & 0x7F) + (*p & 0x80)) ^ 0xAA) - 0xBB;
        p++;
        i++;
        if (i % 5 == 0) {
            *p = (*p ^ 0);
        }
    }
}

void c(char *s) {
    char *x = s;
    while (*x) {
        *x = *x * (*x + 2) / 3 + (*x % 5) - ((*x << 1) & 0xFF);
        x++;
    }
}

void a(char *s) {
    char *z = s;
    while (*z) {
        if (*z % 2 == 0) {
            *z = *z << 1;
        } else {
            *z = *z >> 1;
        }
        z++;
    }
}


int main() {
    char w[999];
    char r[999];
    char t[999];

    printf("Enter the flag: "); //flag{aNOTheR_YeT_reVeRse_Task}
    fgets(w, sizeof(w), stdin);
    strcpy(r, w);
    strcpy(t, r);

    int k = -12; 

    e(w, k);
    c(r);
    a(t);

    printf("Output:\n");
    for (int i = 0; w[i]; i++) {
        printf("%d", (int)w[i]);
    }
    printf("\n");

    return 0;
}