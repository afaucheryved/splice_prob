#general importation
from spliceai.utils import one_hot_encode
import numpy as np
import numpy as np
from functools import wraps
from keras.models import load_model
from pkg_resources import resource_filename
import time as t

#local importation
from app.schemas.typing import genome

def one_hot_encoder(dico_data: dict[str, genome], context: int =10000)->np.ndarray[np.float32]:
        """
        One-hot encode each sequence with flanking CONTEXT, then stack into a batch
        """
        padding = 'N' * (context // 2)
        for seq in dico_data.values():
            print(len(seq))
        encoded = [one_hot_encode(padding + seq + padding) for seq in dico_data.values()]
        x = np.stack(encoded, axis=0)  # shape: (batch_size, seq_len + context, 4)
        return x

def wrapp_calcul(calcul_function):
    @wraps(calcul_function)
    def wrapper(*args, **kwargs):
        print(f"\n---> START calculing {calcul_function.__name__}...\n")
        start = t.perf_counter()
        output = calcul_function(*args, **kwargs)
        end = t.perf_counter()
        print(f"\n---> END calculing {calcul_function.__name__} in {end-start:.4f} secondes\n")
        return output
    return wrapper

@wrapp_calcul
def calcul_y(dico_data: dict[str, genome], CONTEXT: int = 10000)->tuple[list[int], list[int], list[int]]:
    """
    Run prediction on the whole batch through each model and average
    calcul the y vector :
    y[a, b, c] --> a : batch number
                b : base position in the sequence
                c : [Acceptor Gain, Donor Gain, Acceptor Loss, Donor Loss]
    """
    x = one_hot_encoder(dico_data, CONTEXT)
    paths = ('models/spliceai{}.h5'.format(x) for x in range(1, 6))
    models = [load_model(resource_filename('spliceai', x)) for x in paths]
    y = np.mean([models[m].predict(x, batch_size=len(dico_data)) for m in range(5)], axis=0)[0]
    return y
