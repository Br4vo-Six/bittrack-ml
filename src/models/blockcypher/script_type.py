from models.common.script_type import CommonScriptType, AbstractCommonScriptType


_script_type_list = [
    'pay-to-taproot',
    'pay-to-witness-pubkey-hash',
    'pay-to-witness-script-hash',
    'pay-to-script-hash',
    'pay-to-pubkey-hash',
    'pay-to-pubkey',
]


class ScriptType(AbstractCommonScriptType):
    def __init__(self, script_type: str) -> None:
        self._script_type = script_type if script_type in _script_type_list else 'other'

    @property
    def value(self):
        '''
        Transaction script type. Some common transaction types are
        - `pay-to-taproot` = P2TR
        - `pay-to-witness-pubkey-hash` = P2WPKH
        - `pay-to-witness-script-hash` = P2WSH
        - `pay-to-script-hash` = P2SH
        - `pay-to-pubkey-hash` = P2PKH
        - `pay-to-pubkey` = P2PK
        - `other` = otherwise
        '''
        return self._script_type

    def _get_flag(self, type: str):
        return 1 if self._script_type == type else 0

    def to_common(self) -> CommonScriptType:
        return CommonScriptType(
            script_type_p2tr_flag=self._get_flag('pay-to-taproot'),
            script_type_p2wpkh_flag=self._get_flag(
                'pay-to-witness-pubkey-hash'),
            script_type_p2wsh_flag=self._get_flag(
                'pay-to-witness-script-hash'),
            script_type_p2sh_flag=self._get_flag('pay-to-script-hash'),
            script_type_p2pkh_flag=self._get_flag('pay-to-pubkey-hash'),
            script_type_p2pk_flag=self._get_flag('pay-to-pubkey'),
            script_type_other_flag=self._get_flag('other'),
        )
