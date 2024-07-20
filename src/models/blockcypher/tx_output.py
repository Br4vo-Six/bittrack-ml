from typing import Any, Optional

from models.common.tx_output import CommonTxOutput, AbstractCommonTxOutput
from utils.string import str_to_bytes_len
from .script_type import ScriptType


class TxOutput(AbstractCommonTxOutput):
    '''
    Represents an output created by a transaction. Typically found within an array in a `Tx`.
    '''

    def __init__(self, data: dict[str, Any]):
        self._value: int = data.get('value')
        self._script: str = data.get('script')
        self._addresses: list[str] = data.get('addresses')
        self._script_type: ScriptType = ScriptType(data.get('script_type'))
        self._spent_by: Optional[str] = data.get('spent_by')
        self._data_hex: Optional[str] = data.get('data_hex')
        self._data_string: Optional[str] = data.get('data_string')

    @property
    def value(self):
        '''Value in this transaction output, in satoshis.'''
        return self._value

    @property
    def script(self):
        '''Raw hexadecimal encoding of the encumbrance script for this output.'''
        return self._script

    @property
    def addresses(self):
        '''Addresses that correspond to this output; typically this will only have a single address, and you can think of this output as having "sent" value to the address contained herein.'''
        return self._addresses

    @property
    def script_type(self):
        '''The type of encumbrance script used for this output.'''
        return self._script_type

    @property
    def spent_by(self):
        '''The transaction hash that spent this output. Only returned for outputs that have been spent. The spending transaction may be unconfirmed.'''
        return self._spent_by

    @property
    def data_hex(self):
        '''A hex-encoded representation of an OP_RETURN data output, without any other script instructions. Only returned for outputs whose script_type is null-data.'''
        return self._data_hex

    @property
    def data_string(self):
        '''An ASCII representation of an OP_RETURN data output, without any other script instructions. Only returned for outputs whose script_type is null-data and if its data falls into the visible ASCII range.'''
        return self._data_string

    def to_common(self) -> CommonTxOutput:
        return CommonTxOutput(
            next_tx_hash=self._spent_by,
            value=self._value,
            script_type=self._script_type.to_common(),
            script_sig_size=str_to_bytes_len(self._script),
            address=self._addresses[0],
        )
