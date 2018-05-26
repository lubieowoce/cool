### "Is that Python?"
`cool._` lets you build funky expressions:

```python
>>> from cool import _
>>> _[:].hello[_].world[:]._
_[:].hello[_].world[:]._
>>> 0|_.hey._|0
0|_.hey._|0
>>> _._._._._
_._._._._
>>> ()//-_
()//-_
```

(See cool.examples for more)

> **Note**: This interferes with the typical usage
> of `_`('last result') in interactive mode. If you want
> to get it back, just `del _`.


`cool._` (or any instance of its type, `cool.U`)
supports all python operators (unary and binary)
is callable and indexable with anything you want,
and has any property you want (implements `__getattr__`.)

It's hashable too, so you can use it as dict keys:

```python
>>> o = {{}}
>>> o[  _.cool._.foo._[::]  ] = 3
>>> o[  ()**_.bar._**()     ] = 5
>>> o[  _.cool._.foo._[::]  ]  +  o[  ()**_.bar._**()  ]
8
```

Looks much better than ordinary variable names!

Just to clarify, this module serves no real purpose -
It's only useful for building python expressions that
look like line noise. Might be useful if you need to 
obfuscate some code.