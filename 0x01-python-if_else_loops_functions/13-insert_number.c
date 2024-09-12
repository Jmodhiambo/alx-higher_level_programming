#include "lists.h"
#include <stdlib.h>

/**
* insert_node - inserts a node in a sorted way
* @head: double pointer to the head of the node
* @number: the value of the new node
*
* Return: returns pointer to the new node
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *ptr;

	ptr = *head;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	while (ptr)
	{
		if (ptr->n > 3)
			break;
		ptr = ptr->next;
	}
	new->next = ptr->next;
	ptr->next = new;

	return (new);

}
