#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

/**
 * print_python_bytes - Prints info about Python bytes objects.
 * @p: A PyObject representing a bytes object.
 */
void print_python_bytes(PyObject *p)
{
        long int size;
        int i;
        char *str;

        printf("[.] bytes object info\n");
        if (!PyBytes_Check(p))
        {
                printf("  [ERROR] Invalid Bytes Object\n");
                return;
        }

        size = ((PyVarObject *)p)->ob_size;
        str = ((PyBytesObject *)p)->ob_sval;

        printf("  size: %ld\n", size);
        printf("  trying string: %s\n", str);
        if (size > 10)
                size = 10;
        else
                size++;
        printf("  first %ld bytes:", size);
        for (i = 0; i < size; i++)
                printf(" %02x", (unsigned char)str[i]);
        printf("\n");
}

/**
 * print_python_list - Prints info about Python list objects.
 * @p: A PyObject representing a list object.
 */
void print_python_list(PyObject *p)
{
        long int size;
        long int alloc;
        int i;
        PyObject *item;

        size = ((PyVarObject *)p)->ob_size;
        alloc = ((PyListObject *)p)->allocated;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", alloc);

        for (i = 0; i < size; i++)
        {
                item = ((PyListObject *)p)->ob_item[i];
                printf("Element %d: %s\n", i, item->ob_type->tp_name);
                if (PyBytes_Check(item))
                        print_python_bytes(item);
        }
}
