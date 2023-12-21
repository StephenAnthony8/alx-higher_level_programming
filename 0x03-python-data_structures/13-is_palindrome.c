#include "lists.h"
/**
 * is_palindrome - checks a list if it has a palindrom
 * @head: initial list
 * Return: 1 if palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *start_p = *head, *end_p = *head, *last = NULL, *next_p = NULL;
	listint_t *mid = *head, *prev = NULL;
	int i = 1, rtn = 0;

	for (; end_p && end_p->next != NULL; i++)
	{
		end_p = end_p->next;
		if (i % 2 == 0)
			mid = mid->next;
	}
	last = mid;
	while (last != NULL)
	{
		next_p = last; /* assigns pii to the moving pointer */
		last = last->next; /* moves uninterrupted to the end node */
		next_p->next = prev; /* assigns pii to the previous p */
		prev = next_p;/*sets pii as new previous p */
	}
	prev = NULL;
	while (end_p != NULL)
	{
		if (start_p != NULL)
			if (end_p->n != start_p->n)
				rtn++;
		next_p = end_p;
		end_p = end_p->next;
		start_p = (start_p != NULL ? start_p->next : NULL);
		next_p->next = prev;
		prev = next_p;
	}
	return ((rtn == 0 ? 1 : 0));
}


