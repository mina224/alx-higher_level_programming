#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has
 * a cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *L;
	listint_t *prev;

	L = list;
	prev = list;
	while (list && L && L->next)
	{
		list = list->next;
		L = L->next->next;

		if (list == L)
		{
			list = prev;
			prev =  L;
			while (1)
			{
				L = prev;
				while (L->next != list && L->next != prev)
				{
					L = L->next;
				}
				if (L->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
