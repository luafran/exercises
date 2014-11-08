#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#ifdef SOLARIS
#define PSCMD	"ps -a -o pid,ppid,s,tty,comm"
#else
#define PSCMD	"ps -o pid,ppid,state,tty,command"
#endif

int main(void)
{
	pid_t	pid;

	if ((pid = fork()) < 0)
    {
		fprintf(stderr, "fork error\n");
        exit(1);
    }
	else if (pid == 0)
    {
        /* child */
		exit(0);
    }

	/* parent */
	sleep(4);
	system(PSCMD);

	exit(0);
}
