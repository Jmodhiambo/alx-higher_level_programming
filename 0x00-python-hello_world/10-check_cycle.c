#include "lists.h"
#include <stdlib.h>

/**
* check_cycle - checks is the list is a cycle
* @list: pointer to the head of the list
*
* Return: 0 for not cycle and 1 for cycle list
*/

int check_cycle(listint_t *list)
{
	listint_t *ptr;

	ptr = list;

	if (list == NULL)
		return (0);

	while (ptr != NULL)
	{
		ptr = ptr->next;
		if (ptr == list)
			return (1);
	}

	return (0);

}
