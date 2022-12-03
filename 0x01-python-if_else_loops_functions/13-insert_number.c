#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_node -  inserts a number into a sorted singly linked list
 * @head: pointer to the first node
 * @number: data for the new node to be inserted
 * Return:  address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *prev, *curr;

	prev = curr = *head;
	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
	{
		free(newnode);
		return (NULL);
	}
	newnode->n = number;
	newnode->next = NULL;
	if (*head == NULL)
	{
		curr->next = newnode;
		return (newnode);
	}
	if (newnode->n < curr->n)
	{
		newnode->next = curr->next;
		curr->next = newnode;
	}
	curr = curr->next;
	while (curr != NULL)
	{
		if ((curr->n > newnode->n) && ((prev->n == newnode->n) || (prev->n < newnode->n)))
		{
			newnode->next = curr;
			prev->next = newnode;
			return (newnode);
		}
		curr = curr->next;
		prev = prev->next;
	}
	curr->next = newnode;
	return (newnode);
}
