#include "lists.h"

/**
 * is_palindrome - check if a list is a palindrome.
 * @head: double pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *next;

	if (head == NULL)
		return (0);
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	next = *head;
	return (palin(head, next->next));
}

/**
 * palin - function to check if a linked list is a palindrome
 * @head: a pointer to a pointer to a linked list
 * @next: a pointer to a linked list
 * Return: true if the values are equal
 */

int palin(listint_t **head, listint_t *next)
{
	if (next->next != NULL)
		palin(head, next->next);
	if ((*head)->n == next->n)
	{
		*head = (*head)->next;
		return (1);
	}
	else
		return (0);
}
