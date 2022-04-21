"""Generated wrapper for ITokenERC20 Solidity contract."""

# pylint: disable=too-many-arguments

import json
from typing import (  # pylint: disable=unused-import
    Any,
    List,
    Optional,
    Tuple,
    Union,
)

from eth_utils import to_checksum_address
from mypy_extensions import TypedDict  # pylint: disable=unused-import
from hexbytes import HexBytes
from web3 import Web3
from web3.contract import ContractFunction
from web3.datastructures import AttributeDict
from web3.providers.base import BaseProvider

from zero_ex.contract_wrappers.bases import ContractMethod, Validator
from zero_ex.contract_wrappers.tx_params import TxParams


# Try to import a custom validator class definition; if there isn't one,
# declare one that we can instantiate for the default argument to the
# constructor for ITokenERC20 below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        ITokenERC20Validator,
    )
except ImportError:

    class ITokenERC20Validator(  # type: ignore
        Validator
    ):
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass





class AllowanceMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the allowance method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, owner: str, spender: str):
        """Validate the inputs to the allowance method."""
        self.validator.assert_valid(
            method_name='allowance',
            parameter_name='owner',
            argument_value=owner,
        )
        owner = self.validate_and_checksum_address(owner)
        self.validator.assert_valid(
            method_name='allowance',
            parameter_name='spender',
            argument_value=spender,
        )
        spender = self.validate_and_checksum_address(spender)
        return (owner, spender)

    def call(self, owner: str, spender: str, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (owner, spender) = self.validate_and_normalize_inputs(owner, spender)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(owner, spender).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(self, owner: str, spender: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (owner, spender) = self.validate_and_normalize_inputs(owner, spender)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, spender).transact(tx_params.as_dict())

    def build_transaction(self, owner: str, spender: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (owner, spender) = self.validate_and_normalize_inputs(owner, spender)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, spender).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, owner: str, spender: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (owner, spender) = self.validate_and_normalize_inputs(owner, spender)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, spender).estimateGas(tx_params.as_dict())

class ApproveMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the approve method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, spender: str, amount: int):
        """Validate the inputs to the approve method."""
        self.validator.assert_valid(
            method_name='approve',
            parameter_name='spender',
            argument_value=spender,
        )
        spender = self.validate_and_checksum_address(spender)
        self.validator.assert_valid(
            method_name='approve',
            parameter_name='amount',
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (spender, amount)

    def call(self, spender: str, amount: int, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (spender, amount) = self.validate_and_normalize_inputs(spender, amount)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(spender, amount).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(self, spender: str, amount: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (spender, amount) = self.validate_and_normalize_inputs(spender, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(spender, amount).transact(tx_params.as_dict())

    def build_transaction(self, spender: str, amount: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (spender, amount) = self.validate_and_normalize_inputs(spender, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(spender, amount).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, spender: str, amount: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (spender, amount) = self.validate_and_normalize_inputs(spender, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(spender, amount).estimateGas(tx_params.as_dict())

class BalanceOfMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the balanceOf method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, account: str):
        """Validate the inputs to the balanceOf method."""
        self.validator.assert_valid(
            method_name='balanceOf',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (account)

    def call(self, account: str, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(account).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(self, account: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).transact(tx_params.as_dict())

    def build_transaction(self, account: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, account: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).estimateGas(tx_params.as_dict())

class BurnMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the burn method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, amount: int):
        """Validate the inputs to the burn method."""
        self.validator.assert_valid(
            method_name='burn',
            parameter_name='amount',
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (amount)

    def call(self, amount: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (amount) = self.validate_and_normalize_inputs(amount)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(amount).call(tx_params.as_dict())

    def send_transaction(self, amount: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (amount) = self.validate_and_normalize_inputs(amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount).transact(tx_params.as_dict())

    def build_transaction(self, amount: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (amount) = self.validate_and_normalize_inputs(amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, amount: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (amount) = self.validate_and_normalize_inputs(amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(amount).estimateGas(tx_params.as_dict())

class BurnFromMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the burnFrom method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, account: str, amount: int):
        """Validate the inputs to the burnFrom method."""
        self.validator.assert_valid(
            method_name='burnFrom',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        self.validator.assert_valid(
            method_name='burnFrom',
            parameter_name='amount',
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (account, amount)

    def call(self, account: str, amount: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account, amount) = self.validate_and_normalize_inputs(account, amount)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(account, amount).call(tx_params.as_dict())

    def send_transaction(self, account: str, amount: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account, amount) = self.validate_and_normalize_inputs(account, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, amount).transact(tx_params.as_dict())

    def build_transaction(self, account: str, amount: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (account, amount) = self.validate_and_normalize_inputs(account, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, amount).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, account: str, amount: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (account, amount) = self.validate_and_normalize_inputs(account, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account, amount).estimateGas(tx_params.as_dict())

class DecimalsMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the decimals method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return int(returned)

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())

class MintToMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the mintTo method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, to: str, amount: int):
        """Validate the inputs to the mintTo method."""
        self.validator.assert_valid(
            method_name='mintTo',
            parameter_name='to',
            argument_value=to,
        )
        to = self.validate_and_checksum_address(to)
        self.validator.assert_valid(
            method_name='mintTo',
            parameter_name='amount',
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (to, amount)

    def call(self, to: str, amount: int, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (to, amount) = self.validate_and_normalize_inputs(to, amount)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(to, amount).call(tx_params.as_dict())

    def send_transaction(self, to: str, amount: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (to, amount) = self.validate_and_normalize_inputs(to, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, amount).transact(tx_params.as_dict())

    def build_transaction(self, to: str, amount: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (to, amount) = self.validate_and_normalize_inputs(to, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, amount).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, to: str, amount: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (to, amount) = self.validate_and_normalize_inputs(to, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, amount).estimateGas(tx_params.as_dict())

class NameMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the name method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return str(returned)

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())

class SymbolMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the symbol method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return str(returned)

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())

class TotalSupplyMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the totalSupply method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return int(returned)

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())

class TransferMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the transfer method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, to: str, amount: int):
        """Validate the inputs to the transfer method."""
        self.validator.assert_valid(
            method_name='transfer',
            parameter_name='to',
            argument_value=to,
        )
        to = self.validate_and_checksum_address(to)
        self.validator.assert_valid(
            method_name='transfer',
            parameter_name='amount',
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (to, amount)

    def call(self, to: str, amount: int, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (to, amount) = self.validate_and_normalize_inputs(to, amount)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(to, amount).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(self, to: str, amount: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (to, amount) = self.validate_and_normalize_inputs(to, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, amount).transact(tx_params.as_dict())

    def build_transaction(self, to: str, amount: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (to, amount) = self.validate_and_normalize_inputs(to, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, amount).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, to: str, amount: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (to, amount) = self.validate_and_normalize_inputs(to, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(to, amount).estimateGas(tx_params.as_dict())

class TransferFromMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the transferFrom method."""

    def __init__(self, web3_or_provider: Union[Web3, BaseProvider], contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, _from: str, to: str, amount: int):
        """Validate the inputs to the transferFrom method."""
        self.validator.assert_valid(
            method_name='transferFrom',
            parameter_name='from',
            argument_value=_from,
        )
        _from = self.validate_and_checksum_address(_from)
        self.validator.assert_valid(
            method_name='transferFrom',
            parameter_name='to',
            argument_value=to,
        )
        to = self.validate_and_checksum_address(to)
        self.validator.assert_valid(
            method_name='transferFrom',
            parameter_name='amount',
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (_from, to, amount)

    def call(self, _from: str, to: str, amount: int, tx_params: Optional[TxParams] = None) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (_from, to, amount) = self.validate_and_normalize_inputs(_from, to, amount)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(_from, to, amount).call(tx_params.as_dict())
        return bool(returned)

    def send_transaction(self, _from: str, to: str, amount: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (_from, to, amount) = self.validate_and_normalize_inputs(_from, to, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, amount).transact(tx_params.as_dict())

    def build_transaction(self, _from: str, to: str, amount: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (_from, to, amount) = self.validate_and_normalize_inputs(_from, to, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, amount).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, _from: str, to: str, amount: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (_from, to, amount) = self.validate_and_normalize_inputs(_from, to, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(_from, to, amount).estimateGas(tx_params.as_dict())

# pylint: disable=too-many-public-methods,too-many-instance-attributes
class ITokenERC20:
    """Wrapper class for ITokenERC20 Solidity contract."""
    allowance: AllowanceMethod
    """Constructor-initialized instance of
    :class:`AllowanceMethod`.
    """

    approve: ApproveMethod
    """Constructor-initialized instance of
    :class:`ApproveMethod`.
    """

    balance_of: BalanceOfMethod
    """Constructor-initialized instance of
    :class:`BalanceOfMethod`.
    """

    burn: BurnMethod
    """Constructor-initialized instance of
    :class:`BurnMethod`.
    """

    burn_from: BurnFromMethod
    """Constructor-initialized instance of
    :class:`BurnFromMethod`.
    """

    decimals: DecimalsMethod
    """Constructor-initialized instance of
    :class:`DecimalsMethod`.
    """

    mint_to: MintToMethod
    """Constructor-initialized instance of
    :class:`MintToMethod`.
    """

    name: NameMethod
    """Constructor-initialized instance of
    :class:`NameMethod`.
    """

    symbol: SymbolMethod
    """Constructor-initialized instance of
    :class:`SymbolMethod`.
    """

    total_supply: TotalSupplyMethod
    """Constructor-initialized instance of
    :class:`TotalSupplyMethod`.
    """

    transfer: TransferMethod
    """Constructor-initialized instance of
    :class:`TransferMethod`.
    """

    transfer_from: TransferFromMethod
    """Constructor-initialized instance of
    :class:`TransferFromMethod`.
    """


    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: ITokenERC20Validator = None,
    ):
        """Get an instance of wrapper for smart contract.

        :param web3_or_provider: Either an instance of `web3.Web3`:code: or
            `web3.providers.base.BaseProvider`:code:
        :param contract_address: where the contract has been deployed
        :param validator: for validation of method inputs.
        """
        # pylint: disable=too-many-statements

        self.contract_address = contract_address

        if not validator:
            validator = ITokenERC20Validator(web3_or_provider, contract_address)

        web3 = None
        if isinstance(web3_or_provider, BaseProvider):
            web3 = Web3(web3_or_provider)
        elif isinstance(web3_or_provider, Web3):
            web3 = web3_or_provider
        else:
            raise TypeError(
                "Expected parameter 'web3_or_provider' to be an instance of either"
                + " Web3 or BaseProvider"
            )

        # if any middleware was imported, inject it
        try:
            MIDDLEWARE
        except NameError:
            pass
        else:
            try:
                for middleware in MIDDLEWARE:
                    web3.middleware_onion.inject(
                         middleware['function'], layer=middleware['layer'],
                    )
            except ValueError as value_error:
                if value_error.args == ("You can't add the same un-named instance twice",):
                    pass

        self._web3_eth = web3.eth

        functions = self._web3_eth.contract(address=to_checksum_address(contract_address), abi=ITokenERC20.abi()).functions

        self.allowance = AllowanceMethod(web3_or_provider, contract_address, functions.allowance, validator)

        self.approve = ApproveMethod(web3_or_provider, contract_address, functions.approve, validator)

        self.balance_of = BalanceOfMethod(web3_or_provider, contract_address, functions.balanceOf, validator)

        self.burn = BurnMethod(web3_or_provider, contract_address, functions.burn, validator)

        self.burn_from = BurnFromMethod(web3_or_provider, contract_address, functions.burnFrom, validator)

        self.decimals = DecimalsMethod(web3_or_provider, contract_address, functions.decimals)

        self.mint_to = MintToMethod(web3_or_provider, contract_address, functions.mintTo, validator)

        self.name = NameMethod(web3_or_provider, contract_address, functions.name)

        self.symbol = SymbolMethod(web3_or_provider, contract_address, functions.symbol)

        self.total_supply = TotalSupplyMethod(web3_or_provider, contract_address, functions.totalSupply)

        self.transfer = TransferMethod(web3_or_provider, contract_address, functions.transfer, validator)

        self.transfer_from = TransferFromMethod(web3_or_provider, contract_address, functions.transferFrom, validator)

    def get_approval_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Approval event.

        :param tx_hash: hash of transaction emitting Approval event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=ITokenERC20.abi()).events.Approval().processReceipt(tx_receipt)
    def get_tokens_minted_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for TokensMinted event.

        :param tx_hash: hash of transaction emitting TokensMinted event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=ITokenERC20.abi()).events.TokensMinted().processReceipt(tx_receipt)
    def get_transfer_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Transfer event.

        :param tx_hash: hash of transaction emitting Transfer event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=ITokenERC20.abi()).events.Transfer().processReceipt(tx_receipt)

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"mintedTo","type":"address"},{"indexed":false,"internalType":"uint256","name":"quantityMinted","type":"uint256"}],"name":"TokensMinted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burnFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"mintTo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )

# pylint: disable=too-many-lines
