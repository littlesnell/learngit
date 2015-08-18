/*************************************************************************
	> File Name: checkerrno.c
	> Author: 
	> Mail: 
	> Created Time: Fri 29 May 2015 07:22:39 PM PDT
 ************************************************************************/

#include<stdlib.h>
#include<stdio.h>
#include<errno.h>

int main()
{
    FILE  *stream;
    char *filename = "text";
    errno = 0;
    stream = fopen(filename,"r");
    if(stream == NULL)
    {
        printf("open file %s failed,errno is %d\n",filename,errno);
    }
    else
    printf("open File %s successfully\n",filename);
}

