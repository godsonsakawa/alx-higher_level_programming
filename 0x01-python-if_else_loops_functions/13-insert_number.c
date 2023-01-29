#include "lists.h"

/**
  * insert_node - Inserts a number into a sorted singly linked list.
  * @head: A pointer to the head of a linked list.
  * @number: the number to insert.
  *
  * Return: If the funtion fails - NULL.
  *         Otherwise - a pointer to the node.
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
