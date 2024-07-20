from typing import Any, Optional
from datetime import datetime as dt

from .tx_output import TxOutput
from .tx_input import TxInput
from utils.datetime import timestamp_to_datetime


class Tx:
    '''
    Represents the current state of a particular transaction from either a Block within a Blockchain, 
    or an unconfirmed transaction that has yet to be included in a Block. 
    Typically returned from the Unconfirmed Transactions and Transaction Hash endpoints.
    '''

    def __init__(self, data: dict[str, Any]) -> None:
        self._block_height: int = data.get('block_height')
        self._hash: str = data.get('hash')
        self._addresses: list[str] = data.get('addresses')
        self._total: int = data.get('total')
        self._fees: int = data.get('fees')
        self._size: int = data.get('size')
        self._vsize: int = data.get('vsize')
        self._preference: str = data.get('preference')
        self._relayed_by: str = data.get('relayed_by')
        self._received: Optional[dt] = timestamp_to_datetime(
            data.get('received'))
        self._ver: int = data.get('ver')
        self._lock_time: int = data.get('lock_time')
        self._double_spend: bool = data.get('double_spend')
        self._vin_sz: int = data.get('vin_sz')
        self._vout_sz: int = data.get('vout_sz')
        self._confirmations: int = data.get('confirmations')
        self._inputs: list[TxInput] = [TxInput(d) for d in data.get('inputs')]
        self._outputs: list[TxOutput] = [
            TxOutput(d) for d in data.get('outputs')]
        self._opt_in_rbf: Optional[bool] = data.get('opt_in_rbf')
        self._confidence: Optional[float] = data.get('confidence')
        self._confirmed: Optional[dt] = timestamp_to_datetime(
            data.get('confirmed'))
        self._receive_count: Optional[int] = data.get('receive_count')
        self._change_address: Optional[str] = data.get('change_address')
        self._block_hash: Optional[str] = data.get('block_hash')
        self._block_index: Optional[int] = data.get('block_index')
        self._double_of: Optional[str] = data.get('double_of')
        self._data_protocol: Optional[str] = data.get('data_protocol')
        self._hex: Optional[str] = data.get('hex')
        self._next_inputs: Optional[str] = data.get('next_inputs')
        self._next_outputs: Optional[str] = data.get('next_outputs')

    @property
    def block_height(self):
        '''Height of the block that contains this transaction. If this is an unconfirmed transaction, it will equal -1.'''
        return self._block_height

    @property
    def hash_(self):
        '''The hash of the transaction. While reasonably unique, using hashes as identifiers may be unsafe.'''
        return self._hash

    @property
    def addresses(self):
        '''Array of bitcoin public addresses involved in the transaction.'''
        return self._addresses

    @property
    def total(self):
        '''The total number of satoshis exchanged in this transaction.'''
        return self._total

    @property
    def fees(self):
        '''The total number of fees---in satoshis---collected by miners in this transaction.'''
        return self._fees

    @property
    def size(self):
        '''The size of the transaction in bytes.'''
        return self._size

    @property
    def vsize(self):
        '''The virtual size of the transaction in bytes.'''
        return self._vsize

    @property
    def preference(self):
        '''The likelihood that this transaction will make it to the next block; reflects the preference level miners have to include this transaction. Can be high, medium or low.'''
        return self._preference

    @property
    def relayed_by(self):
        '''Address of the peer that sent BlockCypher's servers this transaction.'''
        return self._relayed_by

    @property
    def received(self):
        '''Time this transaction was received by BlockCypher's servers.'''
        return self._received

    @property
    def ver(self):
        '''Version number, typically 1 for Bitcoin transactions.'''
        return self._ver

    @property
    def lock_time(self):
        '''Time when transaction can be valid. Can be interpreted in two ways: if less than 500 million, refers to block height. If more, refers to Unix epoch time.'''
        return self._lock_time

    @property
    def double_spend(self):
        '''true if this is an attempted double spend; false otherwise.'''
        return self._double_spend

    @property
    def vin_sz(self):
        '''Total number of inputs in the transaction.'''
        return self._vin_sz

    @property
    def vout_sz(self):
        '''Total number of outputs in the transaction.'''
        return self._vout_sz

    @property
    def confirmations(self):
        '''Number of subsequent blocks, including the block the transaction is in. Unconfirmed transactions have 0 confirmations.'''
        return self._confirmations

    @property
    def inputs(self):
        '''TXInput Array, limited to 20 by default.'''
        return self._inputs

    @property
    def outputs(self):
        '''TXOutput Array, limited to 20 by default.'''
        return self._outputs

    @property
    def opt_in_rbf(self):
        '''Returns true if this transaction has opted in to Replace-By-Fee (RBF), either true or not present. You can read more about Opt-In RBF here.'''
        return self._opt_in_rbf

    @property
    def confidence(self):
        '''The percentage chance this transaction will not be double-spent against, if unconfirmed. For more information, check the section on Confidence Factor.'''
        return self._confidence

    @property
    def confirmed(self):
        '''Time at which transaction was included in a block; only present for confirmed transactions.'''
        return self._confirmed

    @property
    def receive_count(self):
        '''Number of peers that have sent this transaction to BlockCypher; only present for unconfirmed transactions.'''
        return self._receive_count

    @property
    def change_address(self):
        '''Address BlockCypher will use to send back your change, if you constructed this transaction. If not set, defaults to the address from which the coins were originally sent.'''
        return self._change_address

    @property
    def block_hash(self):
        '''Hash of the block that contains this transaction; only present for confirmed transactions.'''
        return self._block_hash

    @property
    def block_index(self):
        '''Canonical, zero-indexed location of this transaction in a block; only present for confirmed transactions.'''
        return self._block_index

    @property
    def double_of(self):
        '''If this transaction is a double-spend (i.e. double_spend == true) then this is the hash of the transaction it's double-spending.'''
        return self._double_of

    @property
    def data_protocol(self):
        '''Returned if this transaction contains an OP_RETURN associated with a known data protocol. Data protocols currently detected: blockchainid ; openassets ; factom ; colu ; coinspark ; omni'''
        return self._data_protocol

    @property
    def hex_(self):
        '''Hex-encoded bytes of the transaction, as sent over the network.'''
        return self._hex

    @property
    def next_inputs(self):
        '''If there are more transaction inptus that couldn't fit into the TXInput array, this is the BlockCypher URL to query the next set of TXInputs (within a TX object).'''
        return self._next_inputs

    @property
    def next_outputs(self):
        '''If there are more transaction outputs that couldn't fit into the TXOutput array, this is the BlockCypher URL to query the next set of TXOutputs(within a TX object).'''
        return self._next_outputs
