#include "lists.h"

/**
 * insert_node - function that insert a number into a sorted
 * singly linked list
 * @head: double pointer to header of list
 * @number: number to insert in linked list
 * Return: adress of the new node or Null if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp, *tmp2;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	if(*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = node;
		return (node);
	}
	tmp = *head;
	while (tmp->next != NULL)
	{
		if ((tmp->n < number) && tmp->next->n >= number)
			break;
		tmp = tmp->next;
	}
	tmp2 = tmp->next;
	tmp->next = node;
	node->next = aux;
	return (node);
}
