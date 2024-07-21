from typing import Any, Optional

from src.models.common.tx_output import CommonTxOutput, AbstractCommonTxOutput
from src.utils.string_util import str_to_bytes_len
from script_type import ScriptType


class TxOutput(AbstractCommonTxOutput):
    """
    Represents an output created by a transaction. Typically found within an array in a `Tx`.
    """

    def __init__(self, data: dict[str, Any]):
        self.__value: int = data.get('value')
        self.__script: str = data.get('script')
        self.__addresses: list[str] = data.get('addresses')
        self.__script_type: ScriptType = ScriptType(data.get('script_type'))
        self.__spent_by: Optional[str] = data.get('spent_by')
        self.__data_hex: Optional[str] = data.get('data_hex')
        self.__data_string: Optional[str] = data.get('data_string')

    @property
    def value(self):
        """Value in this transaction output, in satoshis."""
        return self.__value

    @property
    def script(self):
        """Raw hexadecimal encoding of the encumbrance script for this output."""
        return self.__script

    @property
    def addresses(self):
        """Addresses that correspond to this output; typically this will only have a single address, and you can
        think of this output as having "sent" value to the address contained herein."""
        return self.__addresses

    @property
    def script_type(self):
        """The type of encumbrance script used for this output."""
        return self.__script_type

    @property
    def spent_by(self):
        """The transaction hash that spent this output. Only returned for outputs that have been spent. The spending
        transaction may be unconfirmed."""
        return self.__spent_by

    @property
    def data_hex(self):
        """A hex-encoded representation of an OP_RETURN data output, without any other script instructions. Only
        returned for outputs whose script_type is null-data."""
        return self.__data_hex

    @property
    def data_string(self):
        """An ASCII representation of an OP_RETURN data output, without any other script instructions. Only returned
        for outputs whose script_type is null-data and if its data falls into the visible ASCII range."""
        return self.__data_string

    def to_common(self) -> CommonTxOutput:
        return CommonTxOutput(
            next_tx_hash=self.__spent_by,
            value=self.__value,
            script_type=self.__script_type.to_common(),
            script_sig_size=str_to_bytes_len(self.__script),
            address=self.__addresses[0],
        )
