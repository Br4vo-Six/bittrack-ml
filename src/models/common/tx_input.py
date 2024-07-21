from abc import ABC, abstractmethod
from typing import Optional

from script_type import CommonScriptType


class CommonTxInput:
    def __init__(
        self,
        prev_tx_hash: str,
        prev_out_idx: int,
        value: int,
        script_type: CommonScriptType,
        script_sig_size: int,
        prev_addresses: list[str],
        age: Optional[int],
    ) -> None:
        self.__prev_tx_hash = prev_tx_hash
        self.__prev_out_idx = prev_out_idx
        self.__value = value
        self.__script_type = script_type
        self.__script_sig_size = script_sig_size
        self.__prev_addresses = prev_addresses
        self.__age = age

    @property
    def prev_tx_hash(self):
        return self.__prev_tx_hash

    @property
    def prev_out_idx(self):
        return self.__prev_out_idx

    @property
    def value(self):
        return self.__value

    @property
    def script_sig_size(self):
        return self.__script_sig_size

    @property
    def script_type(self):
        return self.__script_type

    @property
    def prev_addresses(self):
        return self.__prev_addresses

    @property
    def age(self):
        return self.__age


class AbstractCommonTxInput(ABC):
    @abstractmethod
    def to_common(self) -> CommonTxInput:
        pass
