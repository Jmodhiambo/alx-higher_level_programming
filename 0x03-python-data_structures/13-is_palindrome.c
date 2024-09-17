#include "lists.h"
#include <stdlib.h>

/**
* is_palindrome - checks if a singly linked list is a palindrome
* @head: double pointer to the head of the list
* Return: 1 if palindrome, 0 otherwise
*/
int is_palindrome(listint_t **head)
{
	listint_t *ptr;
	int len = 0, i, j;
	int *list;

	if (*head == NULL)
		return (1);

	ptr = *head;
	while (ptr != NULL)
	{
		len++;
		ptr = ptr->next;
	}

	list = malloc(sizeof(int) * len);
	if (list == NULL)
		return (0);
	ptr = *head;
        for (i = 0; i < len; i++)
        {
                list[i] = ptr->n;
                ptr = ptr->next;
        }

        /* Compare the array from both ends */
        for (i = 0, j = len - 1; i < j; i++, j--)
        {
                if (list[i] != list[j])
                {
                        free(list); /* Free the allocated memory */
                        return (0);
                }
        }

        free(list); /* Free the allocated memory */
        return (1);
}
