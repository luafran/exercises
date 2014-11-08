#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>


int main(void)
{
	if (open("tempfile", O_RDWR) < 0)
    {
		fprintf(stderr, "open error\n");
        exit(1);
    }
	if (unlink("tempfile") < 0)
    {
		fprintf(stderr, "unlink error\n");
        exit(1);
    }
	
    printf("file unlinked\n");
	
    sleep(15);
	
    printf("done\n");
	exit(0);
}
