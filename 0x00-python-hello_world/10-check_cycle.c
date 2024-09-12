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
	listint_t *ptr, *ptr2;

	if (list == NULL || list->next == NULL)
		return (0);

	ptr = list;
	ptr2 = list->next;

	while (ptr2 != NULL && ptr2->next != NULL)
	{
		if (ptr == ptr2)
			return (1);

		ptr = ptr->next;
		ptr2 = ptr2->next->next;
	}

	return (0);
}
