#include <Python.h>

static PyObject* ext_fibo(PyObject* self, PyObject *args){
    int n;
    int i = 0;
    int a = 0, b = 1, c = 0;

    PyArg_ParseTuple(args, "I", &n);

    if (n < 2){
        return PyLong_FromLong(n);
        }

    while(i < n){
        c=a;
        a=b; b=c+b;
        i++;
        }

    return PyLong_FromLong(a);
}

static PyMethodDef module_methods[] = {
   { "ext_fibo", (PyCFunction)ext_fibo, METH_VARARGS, "Extension Fibo"},
   { NULL, NULL, 0, NULL }
};

static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT, "ext_fibo",
    NULL, -1, module_methods
};

PyMODINIT_FUNC PyInit_ext_fibo(){
    return PyModule_Create(&moduledef);
}
