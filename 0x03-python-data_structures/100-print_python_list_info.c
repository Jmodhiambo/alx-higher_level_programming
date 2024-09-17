#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: PyObject list
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size;
    Py_ssize_t allocated;
    Py_ssize_t i;
    PyObject *item;

    /* Ensure the passed object is a list */
    if (!PyList_Check(p))
    {
        fprintf(stderr, "Invalid PyObject passed, it is not a list.\n");
        return;
    }

    size = PyList_Size(p);  /* Get the size of the list */
    allocated = ((PyListObject *)p)->allocated;  /* Get the allocated size */

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    /* Loop through list elements */
    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);  /* Print the type of the element */
    }
}
