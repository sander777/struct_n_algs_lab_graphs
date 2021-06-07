import numpy as np
import io

def get_adj_matrix(path):
    res = {
        'weights': list(),
        'edges': list()
    }

    file = io.FileIO(path, 'r')
    content = file.read().decode('utf-8')
    raws = list(content.strip().split('\n'))
    for i in raws:
        i = list(i.strip().split('|'))
        w = int(i[0])
        e = list(map(lambda s: int(s.strip()), i[1].strip().split(',')))
        res['weights'].append(w)
        res['edges'].append(e)
    return res


data = get_adj_matrix("graph_mx.txt")
adj_matrix = np.matrix(data['edges'])

colors = {
    0: 'r',
    1: 'b',
    2: 'y',
    3: 'g',
    4: 'p',
    5: 'm',
}