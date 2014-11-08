#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <fcntl.h>
#include <utime.h>
#include <stdlib.h>

int
main(int argc, char *argv[])
{
	int				i, fd;
	struct stat		statbuf;
	struct utimbuf	timebuf;

	for (i = 1; i < argc; i++)
    {
        /* fetch current times */
		if (stat(argv[i], &statbuf) < 0)
        {	
			fprintf(stdout, "%s: stat error\n", argv[i]);
			continue;
		}
		
        /* truncate */
        if ((fd = open(argv[i], O_RDWR | O_TRUNC)) < 0)
        {
			fprintf(stdout, "%s: open error\n", argv[i]);
			continue;
		}
		
        close(fd);

        /* reset times */
        timebuf.actime  = statbuf.st_atime;
		timebuf.modtime = statbuf.st_mtime;
        if (utime(argv[i], &timebuf) < 0)
        {	 
			fprintf(stdout, "%s: utime error\n", argv[i]);
			continue;
		}
	}

	exit(0);
}
