#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>
 
int main()
{
 
    char str[100];
    int listen_fd, comm_fd;
    int i;
    int bw;
    struct sockaddr_in servaddr;
    struct linger lo = { 1, 0 };

    printf("Server\n");
    listen_fd = socket(AF_INET, SOCK_STREAM, 0);
 
    bzero( &servaddr, sizeof(servaddr));
 
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = htons(INADDR_ANY);
    servaddr.sin_port = htons(22000);
 
    bind(listen_fd, (struct sockaddr *) &servaddr, sizeof(servaddr));
 
    listen(listen_fd, 10);
 
    comm_fd = accept(listen_fd, (struct sockaddr*) NULL, NULL);
    printf("New connection\n");
    
    setsockopt(comm_fd, SOL_SOCKET, SO_LINGER, &lo, sizeof(lo));
    
    i = 0;
    while(1)
    {
        bzero( str, 100);
        sprintf(str, "message%d", ++i);
 
        /*printf("Echoing back - %s",str);*/
        bw = write(comm_fd, str, strlen(str)+1);
        if (bw < 0)
        {
            printf("Error on write\n");    
        }
        else if (errno == EPIPE) {
            printf("EPIPE\n");
        }
        else {
            printf("[%d] bytes written = %d\n", i, bw);
        }
        sleep(4);
    }
}