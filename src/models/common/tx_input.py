from abc import ABC, abstractmethod
from typing import Optional

from .script_type import CommonScriptType


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
        self._prev_tx_hash = prev_tx_hash
        self._prev_out_idx = prev_out_idx
        self._value = value
        self._script_type = script_type
        self._script_sig_size = script_sig_size
        self._prev_addresses = prev_addresses
        self._age = age

    @property
    def prev_tx_hash(self):
        return self._prev_tx_hash

    @property
    def prev_out_idx(self):
        return self._prev_out_idx

    @property
    def value(self):
        return self._value

    @property
    def script_sig_size(self):
        return self._script_sig_size

    @property
    def script_type(self):
        return self._script_type

    @property
    def prev_addresses(self):
        return self._prev_addresses

    @property
    def age(self):
        return self._age


class AbstractCommonTxInput(ABC):
    @abstractmethod
    def to_common(self) -> CommonTxInput:
        pass
