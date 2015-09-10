Redbeaver
=========
[![Build Status](https://travis-ci.org/aliskhakov/redbeaver.svg?branch=master)](https://travis-ci.org/aliskhakov/redbeaver)

Installation
------------
Download the source and run
```sh
$ python setup.py install
```
or install the latest stable release with
```sh
$ pip install redbeaver
```

Usage
-----

#### Adding functions to Formula


```python
from redbeaver.formula import Formula
```


```python
f = Formula()
```


```python
print f
```




    {'fn_registry': {}, 'num_registry': {}, 'param_registry': {}}




```python
@f(1)
def a(b, c):
    return b + c
```

```python
print f
```




    {'fn_registry': {'a': (('args', ['b', 'c']), ('src', ([u'@f4(1)\n', u'def a(b, c):\n', u'    return b + c\n'], 1)), ('call', <function wrapped_fn at 0x10fb28ed8>))}, 'num_registry': {1: <function wrapped_fn at 0x10fb28ed8>}, 'param_registry': {}}




```python
@f(2)
def b(c):
    return 2 * c
```

```python
print f
```




    {'fn_registry': {'a': (('args', ['b', 'c']), ('src', ([u'@f4(1)\n', u'def a(b, c):\n', u'    return b + c\n'], 1)), ('call', <function wrapped_fn at 0x10fb28ed8>)), 'b': (('args', ['c']), ('src', ([u'@f4(2)\n', u'def b(c):\n', u'    return 2 * c\n'], 1)), ('call', <function wrapped_fn at 0x10fab9ed8>))}, 'num_registry': {1: <function wrapped_fn at 0x10fb28ed8>, 2: <function wrapped_fn at 0x10fab9ed8>}, 'param_registry': {}}




```python
f(2)
```




    <function __main__.wrapped_fn>




```python
f('b')
```




    (('args', ['c']),
     ('src', ([u'@f4(2)\n', u'def b(c):\n', u'    return 2 * c\n'], 1)),
     ('call', <function __main__.wrapped_fn>))




```python
f('a')
```




    (('args', ['b', 'c']),
     ('src', ([u'@f4(1)\n', u'def a(b, c):\n', u'    return b + c\n'], 1)),
     ('call', <function __main__.wrapped_fn>))




#### Parameters setting


```python
f({'c': 5, 'd': 7})
```

```python
f.get_params()
```




    {'c': 5, 'd': 7}




```python
f('c')
```




    5




#### Formula calculation


```python
from redbeaver.calc import Calc
```

```python
calc = Calc(f)
```

```python
calc('a')
```




    15




```python
f.get_params()
```




    {'a': 15, 'b': 10, 'c': 5, 'd': 7}





#### Working with iterable params


```python
f = Formula
```

```python
calc = Calc(f)
```

```python                                                                                
@f(1)                                               
def a(b):                                           
    return b * 2                                    
```

```python                                                    
@f(2)                                               
def b(c):                                           
    return c * 2                                    
```

```python                                                    
f({'c': range(5)})                                  
```

```python                                                    
calc('a', iterate_param='c')
```



    [0, 4, 8, 12, 16]





```python
f.get_params()
```




    {'a': [0, 4, 8, 12, 16], 'c': [0, 1, 2, 3, 4], 'b': [0, 2, 4, 6, 8]}





License
-------
Apache License 2.0
