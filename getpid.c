/*************************************************************************
	> File Name: linuxc/getpid.c
	> Author: 
	> Mail: 
	> Created Time: Sat 16 May 2015 05:22:56 AM PDT
 ************************************************************************/

#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>
#include<stdlib.h>

int main()
{
    pid_t  pid;
    if(pid = fork() == -1)
    {
        printf("fork error!\n");
        exit(1);
    }
    if(pid == 0)
    printf("getpid return %d\n",getpid());
    exit(0);
}
