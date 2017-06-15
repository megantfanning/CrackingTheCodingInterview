#include <stdio.h>
//reverse a null terminated string

int main( ) {
    char str[100];

    printf( "Enter a string :");
    gets( str );
    printf( "\nYou entered: ");
    puts( str );
    int len = 0;
    //get length
    while(str[len] != '\n'){
        len++;
    }
    char temp;
    //decriment length to exclude terminator
    len--;
    printf( "\nstring length: %d \n",len);

    for(int i=0; i < (len/2) ; i ++ ) {
        temp = str[i];
        str[i]=str[len-i];
        str[len-i]=temp;
    }
    printf( "reversed String: ");
    puts( str );


   return 0;
}
