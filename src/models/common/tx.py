from abc import ABC, abstractmethod
from datetime import datetime as dt
from typing import Optional
from tx_output import CommonTxOutput
from tx_input import CommonTxInput


class CommonTx:
    def __init__(
        self,
        tx_hash: str,
        addresses: list[str],
        fee: int,
        size: int,
        vsize: int,
        inputs: list[CommonTxInput],
        outputs: list[CommonTxOutput],
        block_timestamp: Optional[dt],
        block_height: Optional[int]
    ) -> None:
        self.__tx_hash = tx_hash
        self.__addresses = addresses
        self.__fee = fee
        self.__size = size
        self.__vsize = vsize
        self.__inputs = inputs
        self.__outputs = outputs
        self.__block_timestamp = block_timestamp
        self.__block_height = block_height

    @property
    def tx_hash(self):
        return self.__tx_hash

    @property
    def addresses(self):
        return self.__addresses

    @property
    def fee(self):
        return self.__fee

    @property
    def size(self):
        return self.__size

    @property
    def vsize(self):
        return self.__vsize

    @property
    def inputs(self):
        return self.__inputs

    @property
    def outputs(self):
        return self.__outputs

    @property
    def block_timestamp(self):
        return self.__block_timestamp

    @property
    def block_height(self):
        return self.__block_height


class AbstractCommonTx(ABC):
    @abstractmethod
    def to_common(self) -> CommonTx:
        pass
