from abc import ABC, abstractmethod
from datetime import datetime as dt
from typing import Optional
from .tx_output import CommonTxOutput
from .tx_input import CommonTxInput


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
        self._tx_hash = tx_hash
        self._addresses = addresses
        self._fee = fee
        self._size = size
        self._vsize = vsize
        self._inputs = inputs
        self._outputs = outputs
        self._block_timestamp = block_timestamp
        self._block_height = block_height

    @property
    def tx_hash(self):
        return self._tx_hash

    @property
    def addresses(self):
        return self._addresses

    @property
    def fee(self):
        return self._fee

    @property
    def size(self):
        return self._size

    @property
    def vsize(self):
        return self._vsize

    @property
    def inputs(self):
        return self._inputs

    @property
    def outputs(self):
        return self._outputs

    @property
    def block_timestamp(self):
        return self._block_timestamp

    @property
    def block_height(self):
        return self._block_height


class AbstractCommonTx(ABC):
    @abstractmethod
    def to_common(self) -> CommonTx:
        pass
