#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: double pointer to the first node of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int len = 0, l, h;

	if (*head == NULL)
		return (1);
	while (temp != NULL)
	{
		temp = temp->next;
		len++;
	}
	if (len == 1)
		return (1);
	int data[len];

	temp = *head;
	h = len - 1;
	len = l = 0;
	while (temp != NULL)
	{
		data[len] = temp->n;
		temp = temp->next;
		len++;
	}
	while (h > l)
	{
		if (data[h] != data[l])
		{
			return (0);
		}
		h--;
		l++;
	}
	return (1);

}
