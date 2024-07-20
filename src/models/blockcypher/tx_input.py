from typing import Any, Optional

from models.common.tx_input import CommonTxInput, AbstractCommonTxInput
from utils.string import str_to_bytes_len
from .script_type import ScriptType


class TxInput(AbstractCommonTxInput):
    '''
    Represents an input consumed within a transaction. Typically found within an array in a `Tx`. 
    In most cases, `TXInput` are from previous UTXOs, with the most prominent exceptions being attempted double-spend and coinbase inputs.
    '''

    def __init__(self, data: dict[str, Any]):
        self._prev_hash: str = data.get('prev_hash')
        self._output_index: int = data.get('output_index')
        self._output_value: int = data.get('output_value')
        self._sequence: int = data.get('sequence')
        self._script: str = data.get('script')
        self._script_type: ScriptType = ScriptType(data.get('script_type'))
        self._addresses: list[str] = data.get('addresses')
        self._age: Optional[int] = data.get('age')
        self._wallet_name: Optional[str] = data.get('wallet_name')
        self._wallet_token: Optional[str] = data.get('wallet_token')

    @property
    def prev_hash(self):
        '''The previous transaction hash where this input was an output. Not present for coinbase transactions.'''
        return self._prev_hash

    @property
    def output_index(self):
        '''The index of the output being spent within the previous transaction. Not present for coinbase transactions.'''
        return self._output_index

    @property
    def output_value(self):
        '''The value of the output being spent within the previous transaction. Not present for coinbase transactions.'''
        return self._output_value

    @property
    def sequence(self):
        '''The type of script that encumbers the output corresponding to this input.'''
        return self._sequence

    @property
    def script(self):
        '''Raw hexadecimal encoding of the script.'''
        return self._script

    @property
    def script_type(self):
        '''An array of public addresses associated with the output of the previous transaction.'''
        return self._script_type

    @property
    def addresses(self):
        '''Legacy 4-byte sequence number, not usually relevant unless dealing with locktime encumbrances.'''
        return self._addresses

    @property
    def age(self):
        '''Number of confirmations of the previous transaction for which this input was an output. Currently, only returned in unconfirmed transactions.'''
        return self._age

    @property
    def wallet_name(self):
        '''Name of Wallet or HDWallet from which to derive inputs. Only used when constructing transactions via the Creating Transactions process.'''
        return self._wallet_name

    @property
    def wallet_token(self):
        '''Token associated with Wallet or HDWallet used to derive inputs. Only used when constructing transactions via the Creating Transactions process.'''
        return self._wallet_token

    def to_common(self) -> CommonTxInput:
        return CommonTxInput(
            prev_tx_hash=self._prev_hash,
            prev_out_idx=self._output_index,
            value=self._output_value,
            script_type=self._script_type.to_common(),
            script_sig_size=str_to_bytes_len(self._script),
            prev_addresses=self._addresses,
            age=self._age
        )
