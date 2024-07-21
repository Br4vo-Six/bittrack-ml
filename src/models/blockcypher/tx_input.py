from typing import Any, Optional

from src.models.common.tx_input import CommonTxInput, AbstractCommonTxInput
from src.utils.string_util import str_to_bytes_len
from script_type import ScriptType


class TxInput(AbstractCommonTxInput):
    """
    Represents an input consumed within a transaction. Typically found within an array in a `Tx`. In most cases,
    `TXInput` are from previous UTXOs, with the most prominent exceptions being attempted double-spend and coinbase
    inputs.
    """

    def __init__(self, data: dict[str, Any]):
        self.__prev_hash: str = data.get('prev_hash')
        self.__output_index: int = data.get('output_index')
        self.__output_value: int = data.get('output_value')
        self.__sequence: int = data.get('sequence')
        self.__script: str = data.get('script')
        self.__script_type: ScriptType = ScriptType(data.get('script_type'))
        self.__addresses: list[str] = data.get('addresses')
        self.__age: Optional[int] = data.get('age')
        self.__wallet_name: Optional[str] = data.get('wallet_name')
        self.__wallet_token: Optional[str] = data.get('wallet_token')

    @property
    def prev_hash(self):
        """The previous transaction hash where this input was an output. Not present for coinbase transactions."""
        return self.__prev_hash

    @property
    def output_index(self):
        """The index of the output being spent within the previous transaction. Not present for coinbase
        transactions."""
        return self.__output_index

    @property
    def output_value(self):
        """The value of the output being spent within the previous transaction. Not present for coinbase
        transactions."""
        return self.__output_value

    @property
    def sequence(self):
        """The type of script that encumbers the output corresponding to this input."""
        return self.__sequence

    @property
    def script(self):
        """Raw hexadecimal encoding of the script."""
        return self.__script

    @property
    def script_type(self):
        """An array of public addresses associated with the output of the previous transaction."""
        return self.__script_type

    @property
    def addresses(self):
        """Legacy 4-byte sequence number, not usually relevant unless dealing with locktime encumbrances."""
        return self.__addresses

    @property
    def age(self):
        """Number of confirmations of the previous transaction for which this input was an output. Currently,
        only returned in unconfirmed transactions."""
        return self.__age

    @property
    def wallet_name(self):
        """Name of Wallet or HDWallet from which to derive inputs. Only used when constructing transactions via the
        Creating Transactions process."""
        return self.__wallet_name

    @property
    def wallet_token(self):
        """Token associated with Wallet or HDWallet used to derive inputs. Only used when constructing transactions
        via the Creating Transactions process."""
        return self.__wallet_token

    def to_common(self) -> CommonTxInput:
        return CommonTxInput(
            prev_tx_hash=self.__prev_hash,
            prev_out_idx=self.__output_index,
            value=self.__output_value,
            script_type=self.__script_type.to_common(),
            script_sig_size=str_to_bytes_len(self.__script),
            prev_addresses=self.__addresses,
            age=self.__age
        )
