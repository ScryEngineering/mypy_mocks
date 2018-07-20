"""here's some ways you have annotate kwargs"""


# If all the kwargs to outer are floats we can do the following
def outer(**kwargs: float):
   inner(**kwargs)

def inner(num: float):
   print(num * 2)

outer(num="abc")
