#include "lists.h"
#include <stdlib.h>

/**
 * insert_node -  inserts a number into a sorted singly linked list
 * @head: pointer to the first node
 * @number: data for the new node to be inserted
 * Return:  address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *curr;

	curr = *head;
	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
	{
		return (NULL);
	}
	newnode->n = number;
	newnode->next = NULL;
	if (curr == NULL || curr->n > number)
	{
		newnode->next = curr;
		*head = newnode;
		return (newnode);
	}
	while  (curr->next && curr->next->n < number)
		curr = curr->next;
	newnode->next = curr->next;
	curr->next = newnode;
	return (newnode);
}
