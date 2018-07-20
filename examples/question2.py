""" Robbie's second question, what does mypy output with this function forwarding code?"""
def outer(**kwargs):
    inner(**kwargs)

def inner(num: float):
    print(num * 2)

outer(num="abc")
