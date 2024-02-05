# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class Age(str, enum.Enum):
    YOUNG = "young"
    MIDDLE_AGED = "middle_aged"
    OLD = "old"

    def visit(
        self,
        young: typing.Callable[[], T_Result],
        middle_aged: typing.Callable[[], T_Result],
        old: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Age.YOUNG:
            return young()
        if self is Age.MIDDLE_AGED:
            return middle_aged()
        if self is Age.OLD:
            return old()
