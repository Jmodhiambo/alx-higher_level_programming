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
	listint_t *ptr, *ptr2;

	ptr = *head;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	while (ptr->n < number)
	{
		ptr2 = ptr;
		ptr = ptr->next;
	}
	new->next = ptr2->next;
	ptr2->next = new;

	return (new);

}
