#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: double pointer to the first node of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp_front, *temp_back;
	int len = 0, i;

	temp_front = temp_back = *head;
	if (*head == NULL || head == NULL || (*head)->next == NULL)
		return (1);
	while (temp_back->next != NULL)
	{
		temp_back = temp_back->next;
		len++;
	}
	while (len >= 0)
	{
		if (temp_front->n != temp_back->n)
			return (0);
		temp_front = temp_front->next;
		temp_back = temp_front;
		len = len - 2;
		for (i = 1; i <= len; i++)
			temp_back = temp_back->next;
	}
	return (1);
}
