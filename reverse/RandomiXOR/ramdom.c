#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#define N 25

int main()
{   
    char flag[N];
    int r[25];
    char key[25];
    char file_name[100] = "./flag.txt.enc.";;
    int i;
    int j = 0;
    int k = 0;

    FILE *file;
    file = fopen("flag.txt", "r");
    fgets(flag, N, file);
    fclose(file);

    for(i=0; i<25; ++i){
        r[i] = rand() % 31;            
    }

    for(i=0; i<25; ++i){
        flag[i] = flag[i] ^ r[i];            
    }

    for(i=0; i<25; i++){
        key[i] = r[i];
    }

    key[25] = '\0';

//    strcat(file_name , key);
//    strcat(key, "years old.");
    FILE *fp;

    fp = fopen(file_name, "w+");
    fputs(key, fp);
    fputs("\nvalue\n", fp);
//    fprintf(fp, key);
    fprintf(fp, flag);
    fclose(fp);
    return 0;
}