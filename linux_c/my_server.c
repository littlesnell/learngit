/*************************************************************************
> File Name: my_server.c
> Author: 
> Mail: 
> Created Time: Thu 18 Jun 2015 05:56:58 AM PDT
************************************************************************/
//Server/Client模型的服务器端

#include<stdio.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<unistd.h>
#include<string.h>
#include<netinet/in.h>
#include<arpa/inet.h>
#include<errno.h>
#include<stdlib.h>
#include"my_recv.h"    //自定义头文件

#define SERV_PORT         4507   //服务器端口
#define LISTENQ           12     //连接请求队列的最大长度
#define INALID_USERINFO   'n'    //用户信息无效
#define VALID_USERINFO    'y'    //用户信息有效
#define USERNAME           0     //接收到的是用户名
#define PASSWORD           1     //接收到的是密码

struct userinfo
{
    char username[32];
    char password[32];
};;

struct userinfo users[]={
    {"linux","unix"},
    {"4507","4508"},
    {"clh","clh"},
    {"xl","xl"},
    {" "," "}
};

//查找用户是否存在，存在返回该用户名的下标，不存在返回-1，出错返回-2
int find_name(const char *name)
{
    int i;
    if(name == NULL)
    {
        printf("in find_name,NULL pointer");
        return -2;
    }
    for(i=0;users[i].username[0] != ' ';i++)
    {
        if(strcmp(users[i].username,name) == 0)
        {
           return -1;
        }
    }
    return -1;
}

//发送请求
void send_data(int conn_fd,const char *string)
{
    if(send(conn_fd,string,strlen(string),0) < 0)
    {
        my_err("send",_LINE_);   //my_err函数在my_recv.h中声明
    }
}


int main()
{
    int sock_fd,conn_fd;
    int optval;
    int flag_recv = USERNAME;  //标识接收到的是用户名还是密码
    int ret;
    int name_num;
    pid_t pid;
    socklen_t cli_len;
    struct sockaddr_incli_addr,serv_addr;
    char recv_buf[128];


    //创建一个TCP套接字
    sock_fd = socket(AF_INET,SOCK_STREAM,0);
    if(sock_fd < 0)
    {
        my_err("socket",_LINE_);
    }


    //设置套接字使之可以重新绑定端口
    optval = 1;
    if(setsockopt(sock_fd,SOL_SOCKET,SO_REUSEADDR,(void *)&optval,sizeof(int)) < 0)
    {
        my_err("setsockopt",_LINE_);
    }

    //初始化服务端地址结构
    memset(&serv_addr,0,sizeof(struct sockaddr_in));
    serv_addr.sin_famliy = AF_INET;
    serv_addr.sin_port = htons(SERV_PORT);
    serv_addr.sin_addr.s_addr = htonl(INADDR_ANY);


    //将套接字绑定到本地端口
    if(bind(sock_fd,(struct sockaddr *)&serv_addr,sizeof(struct sockaddr_in)) < 0)
    {
        my_err("bind",_LINE_);
    }


    //将套接字转化为监听套接字
    if(listen(sock_fd,LISTENQ) < 0)
    {
        my_err("listen",_LINE_);
    }


    cli_len = sizeof(struct sockaddr_in);
   while(1)
    {
        //通过accept接受客户端的连接请求，并返回连接套接字用于收发数据
        conn_fd = accept(sock_fd,(struct sockaddr *)&cli_addr,&cli_len);
        if(conn_fd < 0)
        {
        my_err("accept",_LINE_);
        }


        printf("accept a new Client,ip:%s\n",inet_ntoa(cli_addr.sin_addr));
        //创建一个子进程处理刚刚接收到的连接请求
        if((pid = fork())==0)
        {
            while(1)
            {
               if((ret = recv(conn_fd,recv_buf,sizeof(recv_buf),0)) < 0)
                {
                    perror("recv");
                    exit(1);
                }
                recv_buf[ret-1] = '0'; //将数据结束标志'\n'替换成字符串结束标志
                if(flag_recv == USERNAME)
                {
                    name_num = find(recv_buf);
                    switch(name_num)
                    {
                        case -1:
                            send_data(conn_fd,"n\n");
                            break;
                        case -2:
                            exit(1);
                            break;
                        default:
                            send_data(conn_fd,"y\n");
                            flag_recv = PASSWORD;
                            break;
                    }
                }
                else if(flag_recv == PASSWORD)
                {
                     //接收到的是密码
                    if(strcmp(users[name_num].password,recv_buf) == 0)
                    {
                        send_data(conn_fd,"y\n");
                        send_data(conn_fd,"Welcome login my top server\n");
                        printf("%s login\n",users[name_num].username);
                        break;
                    }
                    else
                      send_data(conn_fd,"n\n");
                }
            }
             close(sock_fd);
             close(conn_fd);
             exit(0);  //结束子进程
        }
         else
        {
            //父进程关闭刚刚接收到的连接请求，执行accept等待其他连接请求
            close(conn_fd);
        }
    }
    return 0;
 }
