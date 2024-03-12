#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: 1 if there is a cycle, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
    listint_t *slow, *fast;

    if (list == NULL || list->next == NULL)
        return (0);

    slow = list->next;
    fast = list->next->next;

    while (slow && fast && fast->next)
    {
        if (slow == fast)
            return (1);

        slow = slow->next;
        fast = fast->next->next;
    }

    return (0);
}
