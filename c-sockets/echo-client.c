#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>

#define BUF_SIZE 1024

int main(int argc,char **argv)
{
    int sockfd,n;
    int i;
    int off = 0;
    char sendline[BUF_SIZE];
    char recvline[BUF_SIZE];
    struct sockaddr_in servaddr;
    struct linger lo = { 1, 0 };

    sockfd=socket(AF_INET,SOCK_STREAM,0);
    bzero(&servaddr,sizeof servaddr);
 
    servaddr.sin_family=AF_INET;
    servaddr.sin_port=htons(22000);
    
    inet_pton(AF_INET, "127.0.0.1", &(servaddr.sin_addr));
    
    /*setsockopt(sockfd, SOL_SOCKET, SO_LINGER, &lo, sizeof(lo));*/
    /* Does not work in Mac */
    /*setsockopt(sockfd, IPPROTO_TCP, TCP_QUICKACK, &off, sizeof(off));*/
 
    connect(sockfd, (struct sockaddr *)&servaddr, sizeof(servaddr));
 
    i = 0;
    while(1)
    {
        bzero(sendline, BUF_SIZE);
        bzero(recvline, BUF_SIZE);
        
        //fgets(sendline, BUF_SIZE, stdin); /*stdin = 0 , for standard input */
        
        sprintf(sendline, "request-%d", ++i);
        
        write(sockfd, sendline, strlen(sendline)+1);
        
        n = read(sockfd,recvline,BUF_SIZE);
        printf("read = %d\n", n);
        printf("%s\n", recvline);
    }
}
