from json import *
import json
import numpy as np
import base64

def to_json(obj):
    if isinstance(obj, (np.ndarray, np.generic)):
        if isinstance(obj, np.ndarray):
            return {
                '__ndarray__': base64.b64encode(obj.tostring()),
                'dtype': obj.dtype.str,
                'shape': obj.shape,
            }
        elif isinstance(obj, (np.bool_, np.number)):
            return {
                '__npgeneric__': base64.b64encode(obj.tostring()),
                'dtype': obj.dtype.str,
            }
    if isinstance(obj, set):
        return {'__set__': list(obj)}
    if isinstance(obj, tuple):
        return {'__tuple__': list(obj)}
    if isinstance(obj, complex):
        return {'__complex__': obj.__repr__()}

    # Let the base class default method raise the TypeError
    raise TypeError('Unable to serialise object of type {}'.format(type(obj)))