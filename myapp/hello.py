import fire

def hello(name="World"):
  return "Hello %s!" % name

def tax(value):
  return int(value)*1.17

if __name__ == '__main__':
  fire.Fire(tax)



