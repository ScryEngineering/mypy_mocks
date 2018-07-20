"""here's some ways you have annotate kwargs"""


# If all the kwargs to outer are floats we can do the following
def outer(**kwargs: float):
    inner(**kwargs)

def inner(num: float):
    print(num * 2)

outer(num="abc")



# If however we are using kwargs to dispatch on types we have to do something different
from typing import List, overload


@overload
def outer2(num: float) -> None:
    ...

@overload
def outer2(num: List[float]) -> None:
    ...

def outer2(**kwargs):
    if isinstance(kwargs['num'], list):
        inner_lists(**kwargs)
    else:
        inner_floats(**kwargs)

def inner_lists(num: List[float]):
    for item in num:
        print(num * 2)

def inner_floats(num: float):
    print(num * 2)


# OK
outer2(num=0.1)

# OK
outer2(num=[0.2,0.3])

# bad
outer2(num="abc")

