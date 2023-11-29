#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/**
 * insert_node - insert a number into a sorted linked list.
 * @head: pointer to pointer to head
 * @number: number to insert.
 * Return: Address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *tmp;

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL ||  number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
		tmp = *head;

		while (tmp->next != NULL && tmp->next->n <= number)
			tmp = tmp->next;

		new->next = tmp->next;
		tmp->next = new;

		return (new);
}
