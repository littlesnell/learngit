/*************************************************************************
	> File Name: linuxc/processimage.c
	> Author: 
	> Mail: 
	> Created Time: Sat 16 May 2015 03:29:32 AM PDT
 ************************************************************************/

#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>

int main(int argc,char *argv[],char **environ)
{
    int i;
    printf("I am a process image!\n");
    printf("My pid = %d,parentpid = %d\n",getpid(),getppid());
    printf("uid = %d,gid = %d\n",getuid(),getpid());
    for(i=0;i<argc;i++)
    printf("argv[%d]:%s\n",i,argv[i]);
}


