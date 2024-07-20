_script_type_list = [
    'pay-to-taproot',
    'pay-to-witness-pubkey-hash',
    'pay-to-witness-script-hash',
    'pay-to-script-hash',
    'pay-to-pubkey-hash',
    'pay-to-pubkey',
]


class ScriptType:
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
    
    @property
    def bool_map(self):
        map = {t: self._script_type == t for t in _script_type_list}
        map['other'] = self._script_type == 'other'
        return map
    
    @property
    def one_hot_encoding(self):
        one_hot = [1 if truthy else 0 for truthy in self.bool_map.values()]
        return one_hot
