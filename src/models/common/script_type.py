from typing import Literal
from abc import ABC, abstractmethod


class CommonScriptType:
    def __init__(
        self,
        script_type_p2tr_flag: Literal[0, 1],
        script_type_p2wpkh_flag: Literal[0, 1],
        script_type_p2wsh_flag: Literal[0, 1],
        script_type_p2sh_flag: Literal[0, 1],
        script_type_p2pkh_flag: Literal[0, 1],
        script_type_p2pk_flag: Literal[0, 1],
        script_type_other_flag: Literal[0, 1],
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


class AbstractCommonScriptType(ABC):
    @abstractmethod
    def to_common(self) -> CommonScriptType:
        pass
