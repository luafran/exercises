#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

char	*env_init[] = { "USER=unknown", "PATH=/tmp", NULL };

int main(void)
{
	pid_t	pid;

	if ((pid = fork()) < 0)
    {
		fprintf(stderr, "fork error\n");
        exit(1);
	}
    else if (pid == 0)
    {	/* specify pathname, specify environment */
		if (execle("/home/lafranll/work/linux_training/05_proc_control/echoall", "echoall", "myarg1", "MY ARG2", (char *)0, env_init) < 0)
        {
			fprintf(stderr, "execle error\n");
            exit(1);
        }
	}

	if (waitpid(pid, NULL, 0) < 0)
    {
		fprintf(stderr, "wait error\n");
        exit(1);
    }

	if ((pid = fork()) < 0)
    {
		fprintf(stderr, "fork error\n");
        exit(1);
	}
    else if (pid == 0)
    {	/* specify filename, inherit environment */
		if (execlp("echoall", "echoall", "only 1 arg", (char *)0) < 0)
        {
			fprintf(stderr, "execlp error\n");
            exit(1);
        }
	}

	exit(0);
}
