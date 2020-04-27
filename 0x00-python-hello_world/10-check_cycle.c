#include "lists.h"

/**
 * check_cycle - function that check if a singly linked list has a cycle
 * @list: pointer list to check
 * Return: 0 if there is no cycle or 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp1 = list;
	listint_t *tmp2 = list;

	if (list == NULL)
		return (0);
	while (tmp1 != NULL && tmp2 != NULL && tmp2->next != NULL)
	{
		tmp1 = tmp1->next;
		tmp2 = tmp2->next->next;
		if (tmp1 == tmp2)
			return (1);
	}
	return (0);
}
