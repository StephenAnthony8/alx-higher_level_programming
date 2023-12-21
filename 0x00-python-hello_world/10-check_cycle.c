#include "lists.h"
/**
 * check_cycle - checks a linked list for a cycle
 * @list: linked list to be checked through
 * Return: 0 if no cycle, 1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast_p, *slow_p;

	slow_p = list;
	if (list)
		slow_p = list;
	else
		return (0);
	if (!list->next)
		return (0);
	if ((list->next)->next)
		fast_p = (list->next)->next;
	else
		return (0);
	while (fast_p != slow_p)
	{
		if (fast_p->next && (fast_p->next)->next)
		{
			fast_p = (fast_p->next)->next;
			slow_p = slow_p->next;
		}
		else
			return (0);
	}
	return (1);
}
