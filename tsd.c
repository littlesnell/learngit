/*************************************************************************
	> File Name: tsd.c
	> Author: 
	> Mail: 
	> Created Time: Fri 29 May 2015 08:40:19 AM PDT
 ************************************************************************/

#include<stdio.h>
#include<string.h>
#include<pthread.h>

pthread_key_t key;
void *thread2(void *arg)
{
 int tsd = 5;
    printf("thread %d is running\n",pthread_self());
    pthread_setspecific(key,(void *)tsd);
    printf("thread %d returns %d\n",pthread_self(),pthread_getspecific(key));
}
void *thread1(void *arg)
{
    int tsd = 0;
    pthread_t thid2;
    printf("thread %d is running\n",pthread_self());
    pthread_setspecific(key,(void*)tsd);
    pthread_create(&thid2,NULL,thread2,NULL);
    sleep(3);
    printf("thread %d returns %d\n",pthread_self(),pthread_getspecific(key));
}
int main(void)
{
    pthread_t thid1;
    printf("main thread begins running\n");
    pthread_key_create(&key,NULL);
    pthread_create(&thid1,NULL,thread1,NULL);
    sleep(5);
    pthread_key_delete(key);
    printf("main thread exit\n");
    return 0;
}
