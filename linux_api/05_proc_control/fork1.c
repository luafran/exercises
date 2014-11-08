#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int		global = 6;		/* external variable in initialized data */
char	buf[] = "a write to stdout\n";

int
main(void)
{
	int		var;		/* automatic variable on the stack */
	pid_t	pid;

	var = 88;
	if (write(STDOUT_FILENO, buf, sizeof(buf)-1) != sizeof(buf)-1)
    {
		fprintf(stderr, "write error\n");
        exit(1);
    }
	printf("before fork\n");	/* we don't flush stdout */

	if ((pid = fork()) < 0)
    {
		fprintf(stderr, "fork error\n");
        exit(1);
	}
    else if (pid == 0)
    {		/* child */
		global++;					/* modify variables */
		var++;
	}
    else
    {
		sleep(2);				/* parent */
	}

	printf("pid = %d, global = %d, var = %d\n", getpid(), global, var);
	exit(0);
}
