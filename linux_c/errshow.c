/*************************************************************************
	> File Name: errshow.c
	> Author: 
	> Mail: 
	> Created Time: Fri 29 May 2015 07:30:11 PM PDT
 ************************************************************************/

#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<errno.h>

FILE *open_file(char * filename)
{
    FILE *stream;
    errno = 0;
    stream = fopen(filename,"r");
    if(stream == NULL)
    {
        printf("can not open the file %s reason: %s\n",filename,strerror(errno));
        exit(-1);
    }
    else 
    return stream;
}

int main(void)
{
    char *filename = "text";
    open_file(filename);
    return 0;
}
