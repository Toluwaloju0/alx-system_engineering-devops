#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * main - to create zombie processes
 * Return: 1 0n success, 0 else
 */

int main(void)
{
	pid_t child_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		printf("Zombie process created, PID: %d\n", child_pid);
	}
}
