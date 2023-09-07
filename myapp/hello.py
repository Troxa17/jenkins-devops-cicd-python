import fire

def hello(name="World"):
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)

def tax(value):
  return value*1.17

if __value__ == '__main__'
  fire.Fire(tax)