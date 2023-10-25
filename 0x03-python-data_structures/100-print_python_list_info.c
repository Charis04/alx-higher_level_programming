#include <stdlib.h>
#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - function that prints some basic
 * info about Python lists
 * @p: python list
 */

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int elem;
	PyListObject * obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (elem = 0; elem < size; elem++)
		printf("Element %d: %s\n", elem, Py_TYPE(obj->ob_item[i])->tp_name);
}
