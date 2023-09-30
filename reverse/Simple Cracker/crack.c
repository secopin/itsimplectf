#include <stdio.h>
#include <string.h>

void displayString(char str[]);
int checkFlag(char str[]);

int main()
{    
    char password[27];  //flag{p4$sw0rD_cR4cK1nG_s0fTW4Re}
    printf("Enter flag: ");
    fgets(password, sizeof(password), stdin);
    if(checkFlag(password)== 1){
        displayString(password);
    }
    else {
        printf("Try Harder!\n");
    }
    return 0;
}

void displayString(char str[])
{
    printf("Good!\nYou found flag: flag{%s}\n",str);
}

int checkFlag(char password[])
{
    int size = strlen(password);
    char flag[27];
    int n = 0;
	flag[n++] = 'p';
	flag[n++] = '4';
	flag[n++] = '$';
	flag[n++] = 's';
	flag[n++] = 'w';
	flag[n++] = '0';
	flag[n++] = 'r';
	flag[n++] = 'D';
	flag[n++] = '_';
	flag[n++] = 'c';
	flag[n++] = 'R';
	flag[n++] = '4';
	flag[n++] = 'c';
	flag[n++] = 'K';
	flag[n++] = '1';
	flag[n++] = 'n';
	flag[n++] = 'G';
	flag[n++] = '_';
	flag[n++] = 's';
	flag[n++] = '0';
	flag[n++] = 'f';
	flag[n++] = 'T';
	flag[n++] = 'W';
	flag[n++] = '4';
	flag[n++] = 'R';
	flag[n++] = 'e';

    int i;
    for(i=0; i<size; i++){
        if(flag[i] != password[i]){
                return 0;
        }
    }
    return 1;
}

