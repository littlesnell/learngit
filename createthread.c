/*************************************************************************
	> File Name: createthread.c
	> Author: 
	> Mail: 
	> Created Time: Tue 26 May 2015 06:37:56 AM PDT
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<pthread.h>

int *thread(void *arg)
{
    pthread_t newthid;

    newthid = pthread_self();
    printf("this is new thread,thread ID = %u\n",(int)newthid);
    return NULL;
}
int main()
{
    pthread_t thid;

    printf("main thread,ID is %u\n",(int)pthread_self());
    if(pthread_create(&thid,NULL,(void *)thread,NULL) != 0)
    {
        printf("thread creation failed\n");
        exit(1);
    }
    sleep(1);
    exit(0);
}
