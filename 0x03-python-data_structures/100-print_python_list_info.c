#include "Python.h"
void print_python_list_info(PyObject *p);
/**
 * print_python_list_info - returns information about a list
 * @p: python List
 */
void print_python_list_info(PyObject *p)
{
	PyObject *item = NULL;
	int l_list = 0, i = 0;

	l_list = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", l_list);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (; i < l_list; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, (Py_TYPE(item))->tp_name);
	}
}
