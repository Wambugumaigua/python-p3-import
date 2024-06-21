def pytest_itemcollected(item):
    parent = item.parent.obj  
    test_func = item.obj  
    
    
    if parent.__doc__:
        prefix = parent.__doc__.strip()
    else:
        prefix = parent.__class__.__name__
    
    
    if test_func.__doc__:
        suffix = test_func.__doc__.strip()
    else:
        suffix = test_func.__name__
    
    
    if prefix and suffix:
        item._nodeid = f"{prefix} {suffix}"
    elif prefix:
        item._nodeid = prefix
    elif suffix:
        item._nodeid = suffix
