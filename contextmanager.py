from contextlib import contextmanager

# in this example
# "else" block is executed before the "finally" block
# this means that the conn will be close after
# the processing of yield values

@contextmanager
def somefunc(*args, **kwargs):
  conn = None
  res = None
  try:
    conn = open(*args)
    res = conn.exec(*kwargs)
  except Exception as e:
    pass # log error
  finally:
    if conn:
      try:
        conn.close()
      except Exception as e:
        pass # log error
  else:
    yield res
    
    
        
