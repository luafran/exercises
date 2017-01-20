#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
 
int main(int argc,char **argv)
{
    int sockfd,n;
    char sendline[100];
    char recvline[100];
    struct sockaddr_in servaddr;
    struct linger lo = { 1, 0 };

    sockfd=socket(AF_INET,SOCK_STREAM,0);
    bzero(&servaddr,sizeof servaddr);
 
    servaddr.sin_family=AF_INET;
    servaddr.sin_port=htons(22000);
    
    inet_pton(AF_INET, "127.0.0.1", &(servaddr.sin_addr));
    
    setsockopt(sockfd, SOL_SOCKET, SO_LINGER, &lo, sizeof(lo));
 
    connect(sockfd, (struct sockaddr *)&servaddr, sizeof(servaddr));
 
    while(1)
    {
        bzero(sendline, 100);
        bzero(recvline, 100);
        
        //fgets(sendline, 100, stdin); /*stdin = 0 , for standard input */
 
        //write(sockfd, sendline, strlen(sendline)+1);
        
        n = read(sockfd,recvline,100);
        printf("read = %d\n", n);
        printf("%s\n", recvline);
    }
}
