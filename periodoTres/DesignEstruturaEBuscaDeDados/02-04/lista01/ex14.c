#include <stdio.h>
#include <ctype.h>

void maiuscula (char *s){
    int i=0;
    
    while (s[i] != '\0') {
        s[i]=toupper(s[i]); i++;
    }
    return;
}
int main() {
    char palavra[10];
    maiuscula (palavra);
    printf ("%s\n", palavra);
    scanf ("%s", palavra);
    return 0;
}