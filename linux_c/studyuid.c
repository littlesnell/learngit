/*************************************************************************
	> File Name: linuxc/studyuid.c
	> Author: 
	> Mail: 
	> Created Time: Sat 16 May 2015 05:29:01 AM PDT
 ************************************************************************/

#include<stdio.h>
#include<unistd.h>
#include<fcntl.h>
#include<errno.h>
#include<stdlib.h>

extern int errno;
int main()
{
    int fd;
    printf("uid study:\n");
    printf("Process's uid = %d,euid = %d\n",getuid(),geteuid());
    if((fd = open("test.c",O_RDWR)) == -1)
    {
        printf("Open failure,errno is %d : %d \n",errno,strerror(errno));
        exit(1);
    }
    else
    {
    printf("Open successfully!\n");
    }
    close(fd);
    exit(0);
}
