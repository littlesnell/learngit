#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>
int main(void)
{
  pid_t   pid;
  printf("Process Creation Study\n");
  pid = fork();
  switch(pid)
       {
        case 0:
              printf("Child process is running,CurPid is %d,ParentPid is %d\n",pid,getppid());
              break;
       case -1:
              perror("Process creation failed\n");
              break;
        default:printf("Parent process is running,Child is %d,ParentPid is %d\n",pid,getpid());
              break;
       }
  return 0; 
}
   

