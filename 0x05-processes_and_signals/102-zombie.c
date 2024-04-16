#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - to cause a program to sleep
 * Return: 1
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - to create zombie processes
 * Return: 1 0n success, 0 else
 */

int main(void)
{
	pid_t child_pid;
	int i = 0;

	while (i < 5)
	{
		child_pid = fork();
		if (child_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", child_pid);
			sleep(2);
			i++;
		}
		else
		{
			exit(0);
		}
	}
	infinite_while();
	return (1);
}
