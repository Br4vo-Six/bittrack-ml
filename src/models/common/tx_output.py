from abc import ABC, abstractmethod
from typing import Optional

from .script_type import CommonScriptType


class CommonTxOutput:
    def __init__(
        self,
        next_tx_hash: Optional[str],
        value: int,
        script_type: CommonScriptType,
        script_sig_size: int,
        address: str,
    ) -> None:
        self.__next_tx_hash = next_tx_hash
        self.__value = value
        self.__script_type = script_type
        self.__script_sig_size = script_sig_size
        self.__address = address

    @property
    def next_tx_hash(self):
        return self.__next_tx_hash

    @property
    def address(self):
        return self.__address

    @property
    def value(self):
        return self.__value

    @property
    def script_sig_size(self):
        return self.__script_sig_size

    @property
    def script_type(self):
        return self.__script_type


class AbstractCommonTxOutput(ABC):
    @abstractmethod
    def to_common(self) -> CommonTxOutput:
        pass
