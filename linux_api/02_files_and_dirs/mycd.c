#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void)
{
	if (chdir("/tmp") < 0)
    {
		fprintf(stderr, "chdir failed\n");
        exit(1);
    }

	printf("chdir to /tmp succeeded\n");
	
    exit(0);
}
