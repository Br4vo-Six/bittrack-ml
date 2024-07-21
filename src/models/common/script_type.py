from abc import ABC, abstractmethod


class CommonScriptType:
    def __init__(
        self,
        script_type_p2tr_flag: int,
        script_type_p2wpkh_flag: int,
        script_type_p2wsh_flag: int,
        script_type_p2sh_flag: int,
        script_type_p2pkh_flag: int,
        script_type_p2pk_flag: int,
        script_type_other_flag: int,
    ) -> None:
        self.__script_type_p2tr_flag = script_type_p2tr_flag
        self.__script_type_p2wpkh_flag = script_type_p2wpkh_flag
        self.__script_type_p2wsh_flag = script_type_p2wsh_flag
        self.__script_type_p2sh_flag = script_type_p2sh_flag
        self.__script_type_p2pkh_flag = script_type_p2pkh_flag
        self.__script_type_p2pk_flag = script_type_p2pk_flag
        self.__script_type_other_flag = script_type_other_flag

    @property
    def script_type_p2tr_flag(self):
        return self.__script_type_p2tr_flag

    @property
    def script_type_p2wpkh_flag(self):
        return self.__script_type_p2wpkh_flag

    @property
    def script_type_p2wsh_flag(self):
        return self.__script_type_p2wsh_flag

    @property
    def script_type_p2sh_flag(self):
        return self.__script_type_p2sh_flag

    @property
    def script_type_p2pkh_flag(self):
        return self.__script_type_p2pkh_flag

    @property
    def script_type_p2pk_flag(self):
        return self.__script_type_p2pk_flag

    @property
    def script_type_other_flag(self):
        return self.__script_type_other_flag

    @property
    def one_hot_encoding(self):
        return [
            self.__script_type_p2tr_flag,
            self.__script_type_p2wpkh_flag,
            self.__script_type_p2wsh_flag,
            self.__script_type_p2sh_flag,
            self.__script_type_p2pkh_flag,
            self.__script_type_p2pk_flag,
            self.__script_type_other_flag,
        ]


class AbstractCommonScriptType(ABC):
    @abstractmethod
    def to_common(self) -> CommonScriptType:
        pass
