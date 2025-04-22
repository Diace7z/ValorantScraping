import random
def sys_sampling(list_id, r):
    step = int(1/r)
    init = random.sample(range(0,step),k=1)[0]
    samples = list_id[init::step]
    return samples



