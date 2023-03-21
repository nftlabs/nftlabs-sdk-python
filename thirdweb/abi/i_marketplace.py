"""Generated wrapper for IMarketplace Solidity contract."""

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
# constructor for IMarketplace below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        IMarketplaceValidator,
    )
except ImportError:

    class IMarketplaceValidator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class IMarketplaceListing(TypedDict):
    """Python representation of a tuple or struct.

    Solidity compiler output does not include the names of structs that appear
    in method definitions.  A tuple found in an ABI may have been written in
    Solidity as a literal, anonymous tuple, or it may have been written as a
    named `struct`:code:, but there is no way to tell from the compiler
    output.  This class represents a tuple that appeared in a method
    definition.  Its name is derived from a hash of that tuple's field names,
    and every method whose ABI refers to a tuple with that same list of field
    names will have a generated wrapper method that refers to this class.

    Any members of type `bytes`:code: should be encoded as UTF-8, which can be
    accomplished via `str.encode("utf_8")`:code:
    """

    listingId: int

    tokenOwner: str

    assetContract: str

    tokenId: int

    startTime: int

    endTime: int

    quantity: int

    currency: str

    reservePricePerToken: int

    buyoutPricePerToken: int

    tokenType: int

    listingType: int


class IMarketplaceListingParameters(TypedDict):
    """Python representation of a tuple or struct.

    Solidity compiler output does not include the names of structs that appear
    in method definitions.  A tuple found in an ABI may have been written in
    Solidity as a literal, anonymous tuple, or it may have been written as a
    named `struct`:code:, but there is no way to tell from the compiler
    output.  This class represents a tuple that appeared in a method
    definition.  Its name is derived from a hash of that tuple's field names,
    and every method whose ABI refers to a tuple with that same list of field
    names will have a generated wrapper method that refers to this class.

    Any members of type `bytes`:code: should be encoded as UTF-8, which can be
    accomplished via `str.encode("utf_8")`:code:
    """

    assetContract: str

    tokenId: int

    startTime: int

    secondsUntilEndTime: int

    quantityToList: int

    currencyToAccept: str

    reservePricePerToken: int

    buyoutPricePerToken: int

    listingType: int


class AcceptOfferMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the acceptOffer method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(
        self, listing_id: int, offeror: str, currency: str, total_price: int
    ):
        """Validate the inputs to the acceptOffer method."""
        self.validator.assert_valid(
            method_name="acceptOffer",
            parameter_name="_listingId",
            argument_value=listing_id,
        )
        # safeguard against fractional inputs
        listing_id = int(listing_id)
        self.validator.assert_valid(
            method_name="acceptOffer",
            parameter_name="_offeror",
            argument_value=offeror,
        )
        offeror = self.validate_and_checksum_address(offeror)
        self.validator.assert_valid(
            method_name="acceptOffer",
            parameter_name="_currency",
            argument_value=currency,
        )
        currency = self.validate_and_checksum_address(currency)
        self.validator.assert_valid(
            method_name="acceptOffer",
            parameter_name="_totalPrice",
            argument_value=total_price,
        )
        # safeguard against fractional inputs
        total_price = int(total_price)
        return (listing_id, offeror, currency, total_price)

    def call(
        self,
        listing_id: int,
        offeror: str,
        currency: str,
        total_price: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            listing_id,
            offeror,
            currency,
            total_price,
        ) = self.validate_and_normalize_inputs(
            listing_id, offeror, currency, total_price
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            listing_id, offeror, currency, total_price
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        listing_id: int,
        offeror: str,
        currency: str,
        total_price: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            listing_id,
            offeror,
            currency,
            total_price,
        ) = self.validate_and_normalize_inputs(
            listing_id, offeror, currency, total_price
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            listing_id, offeror, currency, total_price
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        listing_id: int,
        offeror: str,
        currency: str,
        total_price: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            listing_id,
            offeror,
            currency,
            total_price,
        ) = self.validate_and_normalize_inputs(
            listing_id, offeror, currency, total_price
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            listing_id, offeror, currency, total_price
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        listing_id: int,
        offeror: str,
        currency: str,
        total_price: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            listing_id,
            offeror,
            currency,
            total_price,
        ) = self.validate_and_normalize_inputs(
            listing_id, offeror, currency, total_price
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            listing_id, offeror, currency, total_price
        ).estimateGas(tx_params.as_dict())


class BuyMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the buy method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(
        self,
        listing_id: int,
        buy_for: str,
        quantity: int,
        currency: str,
        total_price: int,
    ):
        """Validate the inputs to the buy method."""
        self.validator.assert_valid(
            method_name="buy",
            parameter_name="_listingId",
            argument_value=listing_id,
        )
        # safeguard against fractional inputs
        listing_id = int(listing_id)
        self.validator.assert_valid(
            method_name="buy",
            parameter_name="_buyFor",
            argument_value=buy_for,
        )
        buy_for = self.validate_and_checksum_address(buy_for)
        self.validator.assert_valid(
            method_name="buy",
            parameter_name="_quantity",
            argument_value=quantity,
        )
        # safeguard against fractional inputs
        quantity = int(quantity)
        self.validator.assert_valid(
            method_name="buy",
            parameter_name="_currency",
            argument_value=currency,
        )
        currency = self.validate_and_checksum_address(currency)
        self.validator.assert_valid(
            method_name="buy",
            parameter_name="_totalPrice",
            argument_value=total_price,
        )
        # safeguard against fractional inputs
        total_price = int(total_price)
        return (listing_id, buy_for, quantity, currency, total_price)

    def call(
        self,
        listing_id: int,
        buy_for: str,
        quantity: int,
        currency: str,
        total_price: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            listing_id,
            buy_for,
            quantity,
            currency,
            total_price,
        ) = self.validate_and_normalize_inputs(
            listing_id, buy_for, quantity, currency, total_price
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            listing_id, buy_for, quantity, currency, total_price
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        listing_id: int,
        buy_for: str,
        quantity: int,
        currency: str,
        total_price: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            listing_id,
            buy_for,
            quantity,
            currency,
            total_price,
        ) = self.validate_and_normalize_inputs(
            listing_id, buy_for, quantity, currency, total_price
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            listing_id, buy_for, quantity, currency, total_price
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        listing_id: int,
        buy_for: str,
        quantity: int,
        currency: str,
        total_price: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            listing_id,
            buy_for,
            quantity,
            currency,
            total_price,
        ) = self.validate_and_normalize_inputs(
            listing_id, buy_for, quantity, currency, total_price
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            listing_id, buy_for, quantity, currency, total_price
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        listing_id: int,
        buy_for: str,
        quantity: int,
        currency: str,
        total_price: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            listing_id,
            buy_for,
            quantity,
            currency,
            total_price,
        ) = self.validate_and_normalize_inputs(
            listing_id, buy_for, quantity, currency, total_price
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            listing_id, buy_for, quantity, currency, total_price
        ).estimateGas(tx_params.as_dict())


class CancelDirectListingMethod(
    ContractMethod
):  # pylint: disable=invalid-name
    """Various interfaces to the cancelDirectListing method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, listing_id: int):
        """Validate the inputs to the cancelDirectListing method."""
        self.validator.assert_valid(
            method_name="cancelDirectListing",
            parameter_name="_listingId",
            argument_value=listing_id,
        )
        # safeguard against fractional inputs
        listing_id = int(listing_id)
        return listing_id

    def call(
        self, listing_id: int, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (listing_id) = self.validate_and_normalize_inputs(listing_id)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(listing_id).call(tx_params.as_dict())

    def send_transaction(
        self, listing_id: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (listing_id) = self.validate_and_normalize_inputs(listing_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, listing_id: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (listing_id) = self.validate_and_normalize_inputs(listing_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, listing_id: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (listing_id) = self.validate_and_normalize_inputs(listing_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id).estimateGas(
            tx_params.as_dict()
        )


class CloseAuctionMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the closeAuction method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, listing_id: int, close_for: str):
        """Validate the inputs to the closeAuction method."""
        self.validator.assert_valid(
            method_name="closeAuction",
            parameter_name="_listingId",
            argument_value=listing_id,
        )
        # safeguard against fractional inputs
        listing_id = int(listing_id)
        self.validator.assert_valid(
            method_name="closeAuction",
            parameter_name="_closeFor",
            argument_value=close_for,
        )
        close_for = self.validate_and_checksum_address(close_for)
        return (listing_id, close_for)

    def call(
        self,
        listing_id: int,
        close_for: str,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (listing_id, close_for) = self.validate_and_normalize_inputs(
            listing_id, close_for
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(listing_id, close_for).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        listing_id: int,
        close_for: str,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (listing_id, close_for) = self.validate_and_normalize_inputs(
            listing_id, close_for
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, close_for).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self,
        listing_id: int,
        close_for: str,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (listing_id, close_for) = self.validate_and_normalize_inputs(
            listing_id, close_for
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, close_for).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        listing_id: int,
        close_for: str,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (listing_id, close_for) = self.validate_and_normalize_inputs(
            listing_id, close_for
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(listing_id, close_for).estimateGas(
            tx_params.as_dict()
        )


class ContractTypeMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the contractType method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return Union[bytes, str](returned)

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
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


class ContractUriMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the contractURI method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
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

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
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


class ContractVersionMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the contractVersion method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
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

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
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


class CreateListingMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the createListing method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(
        self, params: IMarketplaceListingParameters
    ):
        """Validate the inputs to the createListing method."""
        self.validator.assert_valid(
            method_name="createListing",
            parameter_name="_params",
            argument_value=params,
        )
        return params

    def call(
        self,
        params: IMarketplaceListingParameters,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (params) = self.validate_and_normalize_inputs(params)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(params).call(tx_params.as_dict())

    def send_transaction(
        self,
        params: IMarketplaceListingParameters,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (params) = self.validate_and_normalize_inputs(params)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(params).transact(tx_params.as_dict())

    def build_transaction(
        self,
        params: IMarketplaceListingParameters,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (params) = self.validate_and_normalize_inputs(params)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(params).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self,
        params: IMarketplaceListingParameters,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (params) = self.validate_and_normalize_inputs(params)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(params).estimateGas(tx_params.as_dict())


class GetPlatformFeeInfoMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the getPlatformFeeInfo method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> Tuple[str, int]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return (
            returned[0],
            returned[1],
        )

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
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


class OfferMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the offer method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(
        self,
        listing_id: int,
        quantity_wanted: int,
        currency: str,
        price_per_token: int,
        expiration_timestamp: int,
    ):
        """Validate the inputs to the offer method."""
        self.validator.assert_valid(
            method_name="offer",
            parameter_name="_listingId",
            argument_value=listing_id,
        )
        # safeguard against fractional inputs
        listing_id = int(listing_id)
        self.validator.assert_valid(
            method_name="offer",
            parameter_name="_quantityWanted",
            argument_value=quantity_wanted,
        )
        # safeguard against fractional inputs
        quantity_wanted = int(quantity_wanted)
        self.validator.assert_valid(
            method_name="offer",
            parameter_name="_currency",
            argument_value=currency,
        )
        currency = self.validate_and_checksum_address(currency)
        self.validator.assert_valid(
            method_name="offer",
            parameter_name="_pricePerToken",
            argument_value=price_per_token,
        )
        # safeguard against fractional inputs
        price_per_token = int(price_per_token)
        self.validator.assert_valid(
            method_name="offer",
            parameter_name="_expirationTimestamp",
            argument_value=expiration_timestamp,
        )
        # safeguard against fractional inputs
        expiration_timestamp = int(expiration_timestamp)
        return (
            listing_id,
            quantity_wanted,
            currency,
            price_per_token,
            expiration_timestamp,
        )

    def call(
        self,
        listing_id: int,
        quantity_wanted: int,
        currency: str,
        price_per_token: int,
        expiration_timestamp: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            listing_id,
            quantity_wanted,
            currency,
            price_per_token,
            expiration_timestamp,
        ) = self.validate_and_normalize_inputs(
            listing_id,
            quantity_wanted,
            currency,
            price_per_token,
            expiration_timestamp,
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            listing_id,
            quantity_wanted,
            currency,
            price_per_token,
            expiration_timestamp,
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        listing_id: int,
        quantity_wanted: int,
        currency: str,
        price_per_token: int,
        expiration_timestamp: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            listing_id,
            quantity_wanted,
            currency,
            price_per_token,
            expiration_timestamp,
        ) = self.validate_and_normalize_inputs(
            listing_id,
            quantity_wanted,
            currency,
            price_per_token,
            expiration_timestamp,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            listing_id,
            quantity_wanted,
            currency,
            price_per_token,
            expiration_timestamp,
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        listing_id: int,
        quantity_wanted: int,
        currency: str,
        price_per_token: int,
        expiration_timestamp: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            listing_id,
            quantity_wanted,
            currency,
            price_per_token,
            expiration_timestamp,
        ) = self.validate_and_normalize_inputs(
            listing_id,
            quantity_wanted,
            currency,
            price_per_token,
            expiration_timestamp,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            listing_id,
            quantity_wanted,
            currency,
            price_per_token,
            expiration_timestamp,
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        listing_id: int,
        quantity_wanted: int,
        currency: str,
        price_per_token: int,
        expiration_timestamp: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            listing_id,
            quantity_wanted,
            currency,
            price_per_token,
            expiration_timestamp,
        ) = self.validate_and_normalize_inputs(
            listing_id,
            quantity_wanted,
            currency,
            price_per_token,
            expiration_timestamp,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            listing_id,
            quantity_wanted,
            currency,
            price_per_token,
            expiration_timestamp,
        ).estimateGas(tx_params.as_dict())


class SetContractUriMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the setContractURI method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, uri: str):
        """Validate the inputs to the setContractURI method."""
        self.validator.assert_valid(
            method_name="setContractURI",
            parameter_name="_uri",
            argument_value=uri,
        )
        return uri

    def call(self, uri: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (uri) = self.validate_and_normalize_inputs(uri)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(uri).call(tx_params.as_dict())

    def send_transaction(
        self, uri: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (uri) = self.validate_and_normalize_inputs(uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri).transact(tx_params.as_dict())

    def build_transaction(
        self, uri: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (uri) = self.validate_and_normalize_inputs(uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, uri: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (uri) = self.validate_and_normalize_inputs(uri)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(uri).estimateGas(tx_params.as_dict())


class SetPlatformFeeInfoMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the setPlatformFeeInfo method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(
        self, platform_fee_recipient: str, platform_fee_bps: int
    ):
        """Validate the inputs to the setPlatformFeeInfo method."""
        self.validator.assert_valid(
            method_name="setPlatformFeeInfo",
            parameter_name="_platformFeeRecipient",
            argument_value=platform_fee_recipient,
        )
        platform_fee_recipient = self.validate_and_checksum_address(
            platform_fee_recipient
        )
        self.validator.assert_valid(
            method_name="setPlatformFeeInfo",
            parameter_name="_platformFeeBps",
            argument_value=platform_fee_bps,
        )
        # safeguard against fractional inputs
        platform_fee_bps = int(platform_fee_bps)
        return (platform_fee_recipient, platform_fee_bps)

    def call(
        self,
        platform_fee_recipient: str,
        platform_fee_bps: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            platform_fee_recipient,
            platform_fee_bps,
        ) = self.validate_and_normalize_inputs(
            platform_fee_recipient, platform_fee_bps
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(platform_fee_recipient, platform_fee_bps).call(
            tx_params.as_dict()
        )

    def send_transaction(
        self,
        platform_fee_recipient: str,
        platform_fee_bps: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            platform_fee_recipient,
            platform_fee_bps,
        ) = self.validate_and_normalize_inputs(
            platform_fee_recipient, platform_fee_bps
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            platform_fee_recipient, platform_fee_bps
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        platform_fee_recipient: str,
        platform_fee_bps: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            platform_fee_recipient,
            platform_fee_bps,
        ) = self.validate_and_normalize_inputs(
            platform_fee_recipient, platform_fee_bps
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            platform_fee_recipient, platform_fee_bps
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        platform_fee_recipient: str,
        platform_fee_bps: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            platform_fee_recipient,
            platform_fee_bps,
        ) = self.validate_and_normalize_inputs(
            platform_fee_recipient, platform_fee_bps
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            platform_fee_recipient, platform_fee_bps
        ).estimateGas(tx_params.as_dict())


class UpdateListingMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the updateListing method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(
        self,
        listing_id: int,
        quantity_to_list: int,
        reserve_price_per_token: int,
        buyout_price_per_token: int,
        currency_to_accept: str,
        start_time: int,
        seconds_until_end_time: int,
    ):
        """Validate the inputs to the updateListing method."""
        self.validator.assert_valid(
            method_name="updateListing",
            parameter_name="_listingId",
            argument_value=listing_id,
        )
        # safeguard against fractional inputs
        listing_id = int(listing_id)
        self.validator.assert_valid(
            method_name="updateListing",
            parameter_name="_quantityToList",
            argument_value=quantity_to_list,
        )
        # safeguard against fractional inputs
        quantity_to_list = int(quantity_to_list)
        self.validator.assert_valid(
            method_name="updateListing",
            parameter_name="_reservePricePerToken",
            argument_value=reserve_price_per_token,
        )
        # safeguard against fractional inputs
        reserve_price_per_token = int(reserve_price_per_token)
        self.validator.assert_valid(
            method_name="updateListing",
            parameter_name="_buyoutPricePerToken",
            argument_value=buyout_price_per_token,
        )
        # safeguard against fractional inputs
        buyout_price_per_token = int(buyout_price_per_token)
        self.validator.assert_valid(
            method_name="updateListing",
            parameter_name="_currencyToAccept",
            argument_value=currency_to_accept,
        )
        currency_to_accept = self.validate_and_checksum_address(
            currency_to_accept
        )
        self.validator.assert_valid(
            method_name="updateListing",
            parameter_name="_startTime",
            argument_value=start_time,
        )
        # safeguard against fractional inputs
        start_time = int(start_time)
        self.validator.assert_valid(
            method_name="updateListing",
            parameter_name="_secondsUntilEndTime",
            argument_value=seconds_until_end_time,
        )
        # safeguard against fractional inputs
        seconds_until_end_time = int(seconds_until_end_time)
        return (
            listing_id,
            quantity_to_list,
            reserve_price_per_token,
            buyout_price_per_token,
            currency_to_accept,
            start_time,
            seconds_until_end_time,
        )

    def call(
        self,
        listing_id: int,
        quantity_to_list: int,
        reserve_price_per_token: int,
        buyout_price_per_token: int,
        currency_to_accept: str,
        start_time: int,
        seconds_until_end_time: int,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (
            listing_id,
            quantity_to_list,
            reserve_price_per_token,
            buyout_price_per_token,
            currency_to_accept,
            start_time,
            seconds_until_end_time,
        ) = self.validate_and_normalize_inputs(
            listing_id,
            quantity_to_list,
            reserve_price_per_token,
            buyout_price_per_token,
            currency_to_accept,
            start_time,
            seconds_until_end_time,
        )
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(
            listing_id,
            quantity_to_list,
            reserve_price_per_token,
            buyout_price_per_token,
            currency_to_accept,
            start_time,
            seconds_until_end_time,
        ).call(tx_params.as_dict())

    def send_transaction(
        self,
        listing_id: int,
        quantity_to_list: int,
        reserve_price_per_token: int,
        buyout_price_per_token: int,
        currency_to_accept: str,
        start_time: int,
        seconds_until_end_time: int,
        tx_params: Optional[TxParams] = None,
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (
            listing_id,
            quantity_to_list,
            reserve_price_per_token,
            buyout_price_per_token,
            currency_to_accept,
            start_time,
            seconds_until_end_time,
        ) = self.validate_and_normalize_inputs(
            listing_id,
            quantity_to_list,
            reserve_price_per_token,
            buyout_price_per_token,
            currency_to_accept,
            start_time,
            seconds_until_end_time,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            listing_id,
            quantity_to_list,
            reserve_price_per_token,
            buyout_price_per_token,
            currency_to_accept,
            start_time,
            seconds_until_end_time,
        ).transact(tx_params.as_dict())

    def build_transaction(
        self,
        listing_id: int,
        quantity_to_list: int,
        reserve_price_per_token: int,
        buyout_price_per_token: int,
        currency_to_accept: str,
        start_time: int,
        seconds_until_end_time: int,
        tx_params: Optional[TxParams] = None,
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (
            listing_id,
            quantity_to_list,
            reserve_price_per_token,
            buyout_price_per_token,
            currency_to_accept,
            start_time,
            seconds_until_end_time,
        ) = self.validate_and_normalize_inputs(
            listing_id,
            quantity_to_list,
            reserve_price_per_token,
            buyout_price_per_token,
            currency_to_accept,
            start_time,
            seconds_until_end_time,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            listing_id,
            quantity_to_list,
            reserve_price_per_token,
            buyout_price_per_token,
            currency_to_accept,
            start_time,
            seconds_until_end_time,
        ).buildTransaction(tx_params.as_dict())

    def estimate_gas(
        self,
        listing_id: int,
        quantity_to_list: int,
        reserve_price_per_token: int,
        buyout_price_per_token: int,
        currency_to_accept: str,
        start_time: int,
        seconds_until_end_time: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Estimate gas consumption of method call."""
        (
            listing_id,
            quantity_to_list,
            reserve_price_per_token,
            buyout_price_per_token,
            currency_to_accept,
            start_time,
            seconds_until_end_time,
        ) = self.validate_and_normalize_inputs(
            listing_id,
            quantity_to_list,
            reserve_price_per_token,
            buyout_price_per_token,
            currency_to_accept,
            start_time,
            seconds_until_end_time,
        )
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(
            listing_id,
            quantity_to_list,
            reserve_price_per_token,
            buyout_price_per_token,
            currency_to_accept,
            start_time,
            seconds_until_end_time,
        ).estimateGas(tx_params.as_dict())


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class IMarketplace:
    """Wrapper class for IMarketplace Solidity contract."""

    accept_offer: AcceptOfferMethod
    """Constructor-initialized instance of
    :class:`AcceptOfferMethod`.
    """

    buy: BuyMethod
    """Constructor-initialized instance of
    :class:`BuyMethod`.
    """

    cancel_direct_listing: CancelDirectListingMethod
    """Constructor-initialized instance of
    :class:`CancelDirectListingMethod`.
    """

    close_auction: CloseAuctionMethod
    """Constructor-initialized instance of
    :class:`CloseAuctionMethod`.
    """

    contract_type: ContractTypeMethod
    """Constructor-initialized instance of
    :class:`ContractTypeMethod`.
    """

    contract_uri: ContractUriMethod
    """Constructor-initialized instance of
    :class:`ContractUriMethod`.
    """

    contract_version: ContractVersionMethod
    """Constructor-initialized instance of
    :class:`ContractVersionMethod`.
    """

    create_listing: CreateListingMethod
    """Constructor-initialized instance of
    :class:`CreateListingMethod`.
    """

    get_platform_fee_info: GetPlatformFeeInfoMethod
    """Constructor-initialized instance of
    :class:`GetPlatformFeeInfoMethod`.
    """

    offer: OfferMethod
    """Constructor-initialized instance of
    :class:`OfferMethod`.
    """

    set_contract_uri: SetContractUriMethod
    """Constructor-initialized instance of
    :class:`SetContractUriMethod`.
    """

    set_platform_fee_info: SetPlatformFeeInfoMethod
    """Constructor-initialized instance of
    :class:`SetPlatformFeeInfoMethod`.
    """

    update_listing: UpdateListingMethod
    """Constructor-initialized instance of
    :class:`UpdateListingMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: IMarketplaceValidator = None,
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
            validator = IMarketplaceValidator(
                web3_or_provider, contract_address
            )

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
                        middleware["function"],
                        layer=middleware["layer"],
                    )
            except ValueError as value_error:
                if value_error.args == (
                    "You can't add the same un-named instance twice",
                ):
                    pass

        self._web3_eth = web3.eth

        functions = self._web3_eth.contract(
            address=to_checksum_address(contract_address),
            abi=IMarketplace.abi(),
        ).functions

        self.accept_offer = AcceptOfferMethod(
            web3_or_provider,
            contract_address,
            functions.acceptOffer,
            validator,
        )

        self.buy = BuyMethod(
            web3_or_provider, contract_address, functions.buy, validator
        )

        self.cancel_direct_listing = CancelDirectListingMethod(
            web3_or_provider,
            contract_address,
            functions.cancelDirectListing,
            validator,
        )

        self.close_auction = CloseAuctionMethod(
            web3_or_provider,
            contract_address,
            functions.closeAuction,
            validator,
        )

        self.contract_type = ContractTypeMethod(
            web3_or_provider, contract_address, functions.contractType
        )

        self.contract_uri = ContractUriMethod(
            web3_or_provider, contract_address, functions.contractURI
        )

        self.contract_version = ContractVersionMethod(
            web3_or_provider, contract_address, functions.contractVersion
        )

        self.create_listing = CreateListingMethod(
            web3_or_provider,
            contract_address,
            functions.createListing,
            validator,
        )

        self.get_platform_fee_info = GetPlatformFeeInfoMethod(
            web3_or_provider, contract_address, functions.getPlatformFeeInfo
        )

        self.offer = OfferMethod(
            web3_or_provider, contract_address, functions.offer, validator
        )

        self.set_contract_uri = SetContractUriMethod(
            web3_or_provider,
            contract_address,
            functions.setContractURI,
            validator,
        )

        self.set_platform_fee_info = SetPlatformFeeInfoMethod(
            web3_or_provider,
            contract_address,
            functions.setPlatformFeeInfo,
            validator,
        )

        self.update_listing = UpdateListingMethod(
            web3_or_provider,
            contract_address,
            functions.updateListing,
            validator,
        )

    def get_auction_buffers_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for AuctionBuffersUpdated event.

        :param tx_hash: hash of transaction emitting AuctionBuffersUpdated
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IMarketplace.abi(),
            )
            .events.AuctionBuffersUpdated()
            .processReceipt(tx_receipt)
        )

    def get_auction_closed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for AuctionClosed event.

        :param tx_hash: hash of transaction emitting AuctionClosed event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IMarketplace.abi(),
            )
            .events.AuctionClosed()
            .processReceipt(tx_receipt)
        )

    def get_listing_added_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ListingAdded event.

        :param tx_hash: hash of transaction emitting ListingAdded event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IMarketplace.abi(),
            )
            .events.ListingAdded()
            .processReceipt(tx_receipt)
        )

    def get_listing_removed_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ListingRemoved event.

        :param tx_hash: hash of transaction emitting ListingRemoved event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IMarketplace.abi(),
            )
            .events.ListingRemoved()
            .processReceipt(tx_receipt)
        )

    def get_listing_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ListingUpdated event.

        :param tx_hash: hash of transaction emitting ListingUpdated event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IMarketplace.abi(),
            )
            .events.ListingUpdated()
            .processReceipt(tx_receipt)
        )

    def get_new_offer_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for NewOffer event.

        :param tx_hash: hash of transaction emitting NewOffer event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IMarketplace.abi(),
            )
            .events.NewOffer()
            .processReceipt(tx_receipt)
        )

    def get_new_sale_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for NewSale event.

        :param tx_hash: hash of transaction emitting NewSale event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IMarketplace.abi(),
            )
            .events.NewSale()
            .processReceipt(tx_receipt)
        )

    def get_platform_fee_info_updated_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for PlatformFeeInfoUpdated event.

        :param tx_hash: hash of transaction emitting PlatformFeeInfoUpdated
            event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=IMarketplace.abi(),
            )
            .events.PlatformFeeInfoUpdated()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"timeBuffer","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"bidBufferBps","type":"uint256"}],"name":"AuctionBuffersUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"listingId","type":"uint256"},{"indexed":true,"internalType":"address","name":"closer","type":"address"},{"indexed":true,"internalType":"bool","name":"cancelled","type":"bool"},{"indexed":false,"internalType":"address","name":"auctionCreator","type":"address"},{"indexed":false,"internalType":"address","name":"winningBidder","type":"address"}],"name":"AuctionClosed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"listingId","type":"uint256"},{"indexed":true,"internalType":"address","name":"assetContract","type":"address"},{"indexed":true,"internalType":"address","name":"lister","type":"address"},{"components":[{"internalType":"uint256","name":"listingId","type":"uint256"},{"internalType":"address","name":"tokenOwner","type":"address"},{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"startTime","type":"uint256"},{"internalType":"uint256","name":"endTime","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"},{"internalType":"address","name":"currency","type":"address"},{"internalType":"uint256","name":"reservePricePerToken","type":"uint256"},{"internalType":"uint256","name":"buyoutPricePerToken","type":"uint256"},{"internalType":"enum IMarketplace.TokenType","name":"tokenType","type":"uint8"},{"internalType":"enum IMarketplace.ListingType","name":"listingType","type":"uint8"}],"indexed":false,"internalType":"struct IMarketplace.Listing","name":"listing","type":"tuple"}],"name":"ListingAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"listingId","type":"uint256"},{"indexed":true,"internalType":"address","name":"listingCreator","type":"address"}],"name":"ListingRemoved","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"listingId","type":"uint256"},{"indexed":true,"internalType":"address","name":"listingCreator","type":"address"}],"name":"ListingUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"listingId","type":"uint256"},{"indexed":true,"internalType":"address","name":"offeror","type":"address"},{"indexed":true,"internalType":"enum IMarketplace.ListingType","name":"listingType","type":"uint8"},{"indexed":false,"internalType":"uint256","name":"quantityWanted","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"totalOfferAmount","type":"uint256"},{"indexed":false,"internalType":"address","name":"currency","type":"address"}],"name":"NewOffer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"listingId","type":"uint256"},{"indexed":true,"internalType":"address","name":"assetContract","type":"address"},{"indexed":true,"internalType":"address","name":"lister","type":"address"},{"indexed":false,"internalType":"address","name":"buyer","type":"address"},{"indexed":false,"internalType":"uint256","name":"quantityBought","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"totalPricePaid","type":"uint256"}],"name":"NewSale","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"platformFeeRecipient","type":"address"},{"indexed":false,"internalType":"uint256","name":"platformFeeBps","type":"uint256"}],"name":"PlatformFeeInfoUpdated","type":"event"},{"inputs":[{"internalType":"uint256","name":"_listingId","type":"uint256"},{"internalType":"address","name":"_offeror","type":"address"},{"internalType":"address","name":"_currency","type":"address"},{"internalType":"uint256","name":"_totalPrice","type":"uint256"}],"name":"acceptOffer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_listingId","type":"uint256"},{"internalType":"address","name":"_buyFor","type":"address"},{"internalType":"uint256","name":"_quantity","type":"uint256"},{"internalType":"address","name":"_currency","type":"address"},{"internalType":"uint256","name":"_totalPrice","type":"uint256"}],"name":"buy","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_listingId","type":"uint256"}],"name":"cancelDirectListing","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_listingId","type":"uint256"},{"internalType":"address","name":"_closeFor","type":"address"}],"name":"closeAuction","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"contractType","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"contractURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"contractVersion","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"pure","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"assetContract","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"startTime","type":"uint256"},{"internalType":"uint256","name":"secondsUntilEndTime","type":"uint256"},{"internalType":"uint256","name":"quantityToList","type":"uint256"},{"internalType":"address","name":"currencyToAccept","type":"address"},{"internalType":"uint256","name":"reservePricePerToken","type":"uint256"},{"internalType":"uint256","name":"buyoutPricePerToken","type":"uint256"},{"internalType":"enum IMarketplace.ListingType","name":"listingType","type":"uint8"}],"internalType":"struct IMarketplace.ListingParameters","name":"_params","type":"tuple"}],"name":"createListing","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getPlatformFeeInfo","outputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_listingId","type":"uint256"},{"internalType":"uint256","name":"_quantityWanted","type":"uint256"},{"internalType":"address","name":"_currency","type":"address"},{"internalType":"uint256","name":"_pricePerToken","type":"uint256"},{"internalType":"uint256","name":"_expirationTimestamp","type":"uint256"}],"name":"offer","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"string","name":"_uri","type":"string"}],"name":"setContractURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_platformFeeRecipient","type":"address"},{"internalType":"uint256","name":"_platformFeeBps","type":"uint256"}],"name":"setPlatformFeeInfo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_listingId","type":"uint256"},{"internalType":"uint256","name":"_quantityToList","type":"uint256"},{"internalType":"uint256","name":"_reservePricePerToken","type":"uint256"},{"internalType":"uint256","name":"_buyoutPricePerToken","type":"uint256"},{"internalType":"address","name":"_currencyToAccept","type":"address"},{"internalType":"uint256","name":"_startTime","type":"uint256"},{"internalType":"uint256","name":"_secondsUntilEndTime","type":"uint256"}],"name":"updateListing","outputs":[],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
