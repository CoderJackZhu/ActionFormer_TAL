datasets = {}
def register_dataset(name):
    def decorator(cls):
        datasets[name] = cls
        return cls

    return decorator

def make_dataset(name, is_training, split, **kwargs):
    """
       A simple dataset builder
   """
    dataset = datasets[name](is_training, split, **kwargs)
    return dataset

@register_dataset("anet")
class hello:
    def __init__(self, is_training, split, **kwargs):
        self.is_training = is_training
        print(f'hello function {is_training}')

set1 = make_dataset("anet", True, ['training'])
print(set1)
