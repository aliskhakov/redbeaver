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

```python
from redbeaver.eq import Eq as eq
from redbeaver.calc import calc
```


```python
eq.eq_registry
```




    {}




```python
@eq(1)
def a(b, c):
    return b + c
```


```python
eq.eq_registry
```




    {'a': {'args': ['b', 'c'], 'fn': <function redbeaver.eq.wrapped>}}




```python
@eq(2)
def b(c):
    return 2 * c
```


```python
eq.eq_registry
```




    {'a': {'args': ['b', 'c'], 'fn': <function redbeaver.eq.wrapped>},
     'b': {'args': ['c'], 'fn': <function redbeaver.eq.wrapped>}}




```python
eq.params
```




    {}




```python
eq.params['c'] = 5
```


```python
eq.params
```




    {'c': 5}




```python
calc('a', eq)
```




    15




```python
eq.params
```




    {'a': 15, 'b': 10, 'c': 5}





License
-------
Apache License 2.0
