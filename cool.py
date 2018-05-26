__doc__ = \
"""
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
"""


__all__ = \
['_', 'examples']
# See examples at the end of the file

# Todo: add splat
# https://stackoverflow.com/q/22365847/5534735


unary = lambda op: lambda u: U(op+repr(u))
binary = lambda op: lambda u, v: U(repr(u)+op+repr(v))
r_binary = lambda op: lambda u, v: U(repr(v)+op+repr(u))

unary_ops = {
  '__neg__': '-',
  '__invert__': '~',
}

binary_ops = {
  '__or__' : '|',
  '__and__' : '&',
  '__sub__' : '-',
  '__add__': '+',
  '__mul__': '*',
  '__truediv__': '/',
  '__mod__': '%',
  '__floordiv__': '//',
  '__xor__': '^',
  '__matmul__': '@',
  '__lshift__': '<<',
  '__rshift__': '>>',
  '__eq__': '==',
  '__lt__': '<',
  '__le__': '<=',
  '__gt__': '>',
  '__ge__': '>=',
  '__pow__': '**',
}

# add __rop__ twin for each __op__

right = lambda name: name.replace('__', '__r', 1)
r_binary_ops =\
  { right(name): binary_ops[name]
    for name in binary_ops.keys() }



class U:
  """ Underscore - the class used for building
  cool expressions. Intended usage:

  >>> _ = U()
  >>> _.hello.world._ 
  _.hello.world._ 

  (See module help or `cool.examples` for more)
  """
  def __init__(u, text='_'): u.text = text
  

  def __call__(u, *args, **kwargs):
    ps = list(map(repr, args))
    ks = ['{}={!r}'.format(k,v) for (k,v) in kwargs.items()]
    a = ', '.join(ps+ks)
    return U("{}({})".format(u.text, a))
  

  def __getitem__(u, ix):
    if type(ix) is not tuple: ixs = (ix,)
    else: ixs = ix
    a = ', '.join(_slice_repr(ix) if type(ix) is slice else repr(ix) for ix in ixs)
    return U('{}[{}]'.format(u.text, a))
  

  def __getattr__(u, attr): return U(u.text+'.'+attr)
  
  def __repr__(u): return u.text
  def __str__(u): return u.text
  
  def __hash__(u): return hash(u.text)


# inject the operators

for name, op in unary_ops.items():
  setattr(U, name, unary(op))

for name, op in binary_ops.items():
  setattr(U, name, binary(op))

for name, op in r_binary_ops.items():
  setattr(U, name, r_binary(op))
  




_ = U()


examples = [
  _._._._._,
  _|_,
  _.hello.world._,
  _._-_|_-_._,
  0|_.hey._|0,
  []-_-[],
  ()//-_,
  _.o._,
  _[:].hello[_].world[:]._,
  _(_=_,__=_,___=_,____=_),
  _(_=_, __=_//_, ___=_//_//_),
  ~_()._@_.o^_(_,_**_),
  _[:](_.hel)[_.lo:'wor'](ld=_),
  _//_.foo(bar=_|-_),
]




def _slice_repr(s):
  a = [
    repr(s.start) if s.start is not None else '',
    repr(s.stop) if s.stop is not None else '',
  ] + ([repr(s.step)] if s.step is not None else [])
  return ':'.join(a)
