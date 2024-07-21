from typing import TypeVar

T = TypeVar('T')


def reduce_to_set(obj_list: list[T], attr: str):
    coll = []
    for obj in obj_list:
        data = obj.__getattribute__(attr)
        if type(data) is not list:
            data = [data]
        coll += data
    coll_set = set(coll)
    return coll_set


def filter_by_set(obj_list: list[T], attr: str, set_condition: set):
    coll = [
        obj
        for obj in obj_list
        if obj.__getattribute__(attr) in set_condition
    ]
    return coll
