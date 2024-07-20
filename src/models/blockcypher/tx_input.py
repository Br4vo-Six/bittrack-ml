from typing import Any, Optional
from .script_type import ScriptType


class TxInput:
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

    def prev_hash(self):
        '''The previous transaction hash where this input was an output. Not present for coinbase transactions.'''
        return self._prev_hash

    def output_index(self):
        '''The index of the output being spent within the previous transaction. Not present for coinbase transactions.'''
        return self._output_index

    def output_value(self):
        '''The value of the output being spent within the previous transaction. Not present for coinbase transactions.'''
        return self._output_value

    def sequence(self):
        '''The type of script that encumbers the output corresponding to this input.'''
        return self._sequence

    def script(self):
        '''Raw hexadecimal encoding of the script.'''
        return self._script

    def script_type(self):
        '''An array of public addresses associated with the output of the previous transaction.'''
        return self._script_type

    def addresses(self):
        '''Legacy 4-byte sequence number, not usually relevant unless dealing with locktime encumbrances.'''
        return self._addresses

    def age(self):
        '''Number of confirmations of the previous transaction for which this input was an output. Currently, only returned in unconfirmed transactions.'''
        return self._age

    def wallet_name(self):
        '''Name of Wallet or HDWallet from which to derive inputs. Only used when constructing transactions via the Creating Transactions process.'''
        return self._wallet_name

    def wallet_token(self):
        '''Token associated with Wallet or HDWallet used to derive inputs. Only used when constructing transactions via the Creating Transactions process.'''
        return self._wallet_token
