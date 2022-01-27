""" Interact with the NFT module of the app"""
import copy
from typing import Dict, List
import json

import web3
from thirdweb.abi.erc20 import ERC20
from thirdweb.constants import NativeAddress, ZeroAddress

from thirdweb_web3 import Web3

from thirdweb.types.role import Role

from ..abi.nft import SignatureMint721 as NFT
from ..types.nft import BatchGeneratedSignature, MintArg, MintRequestStructOutput, NewSignaturePayload, SignaturePayload
from ..types.nft import NftMetadata as NftType
from .base import BaseModule
import uuid
import binascii


class NftModule(BaseModule):
    """ Interact with the NFT module of the app"""

    address: str
    """
    Address of the module
    """
    __abi_module: NFT

    def __init__(self, address: str, client: Web3):
        """
        :param address: The address of the module
        :param client: Web3 client

        Initializes the module
        """
        super().__init__()
        self.address = address
        """
        NFT module contract address [https://thirdweb.com/: Dashboard: Project ➝ NFT Module]
        """

        self.__abi_module = NFT(client, address)
        """
        The ABI makes calls the EVM. Client is default 'Web3' and Address is nft module contract address.
        """

    def mint(self, arg: MintArg) -> NftType:
        """
        :param arg: the `MintArg` object
        :return: the metadata of the token

        Mints a new token to the signer. 
        - Arguments passed: Note, a class is used -> MintArg(name, description, image_uri, properties)
        - Returns the `NftMetadata(name,description,image,properties,id,uri)`
        """
        return self.mint_to(self.get_signer_address(), arg)

    def mint_to(
        self,
        to_address: str,
        arg: MintArg,
    ) -> NftType:
        """
        :param to_address: the address to mint the token to
        :param arg: the `name`, `description`, `image_uri`, `properties` of the token
        :return: the metadata of the token


        Mints a new token to an address
        - Arguments passed: `to_address` and a class -> `MintArg(name, description, image_uri, properties)`
        - Returns the `NftMetadata(name,description,image,properties,id,uri)` 
        """
        final_properties: Dict
        if arg.properties is None:
            final_properties = {}
        else:
            final_properties = copy.copy(arg.properties)

        if arg.image == "":
            arg.image = arg.image_uri

        meta = {
            'name': arg.name,
            'description': arg.description,
            'image': arg.image,
            'properties': final_properties
        }

        uri = self.upload_metadata(meta)
        tx = self.__abi_module.mint_to.build_transaction(
            to_address, uri, self.get_transact_opts()
        )
        receipt = self.execute_tx(tx)
        result = self.__abi_module.get_token_minted_event(
            receipt.transactionHash.hex()
        )
        token_id = result[0]["args"]["tokenIdMinted"]
        return self.get(token_id)

    def total_supply(self) -> int:
        """
        :return: the total supply of the NFT module

        Returns the total supply
        """
        return self.__abi_module.total_supply.call()

    def get(self, token_id: int) -> NftType:
        """
        :param token_id: the id of the token
        :return: the metadata of the token

        Returns the Metadata of a token
        """
        uri = self.__get_metadata_uri(token_id)
        meta = self.get_storage().get(uri)
        meta_obj: NftType = NftType.from_json(meta)
        meta_obj.id = token_id
        meta_obj.uri = uri
        return meta_obj

    def __get_metadata_uri(self, token_id: int):
        """
        :param token_id: the id of the token
        :return: the uri of the token metadata

        Returns the uri of the metadata of a token
        """
        uri = self.__abi_module.token_uri.call(token_id)
        if uri == "":
            raise Exception(
                "Could not find NFT metadata, are you sure it exists?")
        return uri

    def burn(self, token_id: int):
        """
        :param token_id: the id of the token
        :return: the metadata of the token

        Burns a given token
        """
        tx = self.__abi_module.burn.build_transaction(
            token_id, self.get_transact_opts()
        )
        self.execute_tx(tx)

    def transfer_from(self, from_address: str, to_address: str, token_id: int):
        """
        :param from_address: the address to transfer the token from
        :param to_address: the address to transfer the token to
        :param token_id: the id of the token

        Transfers a token from one address to another
        """
        tx = self.__abi_module.transfer_from.build_transaction(
            from_address, to_address, token_id, self.get_transact_opts()
        )
        self.execute_tx(tx)

    def transfer(self, to_address: str, token_id: int):
        """
        :param to_address: the address to transfer the token to
        :param token_id: the id of the token
        :return: the metadata of the token


        Transfers NFT from the current signers wallet to another wallet
        """
        tx = self.__abi_module.safe_transfer_from1.build_transaction(
            self.get_signer_address(), to_address, token_id, self.get_transact_opts()
        )
        self.execute_tx(tx)

    def set_royalty_bps(self, amount: int):
        """
        :param amount: the amount of BPS to set
        :return: the metadata of the token

        Sets the royalty percentage for the NFT
        """
        tx = self.__abi_module.set_royalty_bps.build_transaction(
            amount, self.get_transact_opts()
        )

        self.execute_tx(tx)

    def get_all(self) -> List[NftType]:
        """
        :return: the metadata of all the tokens

        Returns all the NFTs in the system
        """
        max_id = self.__abi_module.next_token_id_to_mint.call()
        return [self.get(i) for i in range(max_id)]

    def get_owned(self, address: str = "") -> List[NftType]:
        """
        :param address: The address to fetch the NFTs for.
        :return: A list of NFTs owned by the given address

        Defaults to fetching the NFTs owned by the current signer (as indicated by the private key)
        if the address parameter is not supplied
        """
        if address == "":
            address = self.get_signer_address()

        balance = self.__abi_module.balance_of.call(address)
        owned_tokens = [
            self.__token_of_owner_by_index(address, i) for i in range(balance)
        ]
        return [self.get(i) for i in owned_tokens]

    def __token_of_owner_by_index(self, address: str, token_id: int) -> int:
        return self.__abi_module.token_of_owner_by_index.call(address, token_id)

    def balance(self) -> int:
        """
        :return: The balance of the current signers wallet

        Returns balance of the current signers wallet
        - Use-case: Use this method if you want to use the currently connected wallet
        - Dashboard: Project ➝ NFT Module ➝ Total amount of NFT's
        """

        return self.__abi_module.balance_of.call(self.get_signer_address())

    def balance_of(self, address: str) -> int:
        """
        :param address: The address to fetch the NFTs for.
        :return: The balance of the given address

        Returns balance of the given addressss
        - Use-case: Use this method if you don't want to use the connected wallet, but want to check another wallet.
        - Dashboard: Project ➝ NFT Module ➝ Total amount of NFT's 
        """
        return self.__abi_module.balance_of.call(address)

    def owner_of(self, token_id: int) -> str:
        """
        :param token_id: The token id to fetch the owner for.
        :return: The owner of the given token

        Returns the owner of the given token

        """
        return self.__abi_module.owner_of.call(token_id)

    def get_metadata(self, token_id: int) -> NftType:
        """
        :param token_id: The token id to fetch the metadata for.
        :return: The metadata of the given token

        Returns the metadata of the given token

        """
        uri = self.__get_metadata_uri(token_id)
        meta = self.get_storage().get(uri)
        meta_obj: NftType = NftType.from_json(meta)
        meta_obj.id = token_id
        meta_obj.uri = uri
        return meta_obj

    def is_approved(self, address: str, operator: str) -> bool:
        """
        :param address: The address to check
        :param operator: The operator to check
        :return: Whether the given address is approved

        Returns whether the given address is approved

        """
        return self.__abi_module.is_approved_for_all.call(address, operator)

    def set_approval(self, operator: str, approved: bool = True):
        """
        :param operator: The operator to set approval for
        :param approved: Whether to grant approval or revoke it

        Sets approval for specified operator, defaults to grant approval

        """
        tx = self.__abi_module.set_approval_for_all.build_transaction(
            operator, approved, self.get_transact_opts()
        )
        self.execute_tx(tx)

    def set_restricted_transfer(self, restricted: bool = True):
        """
        :param restricted: Whether to grant restricted transfer or revoke it

        Sets restricted transfer for the NFT, defaults to restricted.

        """
        self.execute_tx(
            self.__abi_module.set_restricted_transfer.build_transaction(
                restricted, self.get_transact_opts()
            )
        )

    def __map_payload(req: SignaturePayload or NewSignaturePayload) -> MintRequestStructOutput:
        return MintRequestStructOutput(
            to=req.to,
            price=req.price,
            currency=req.currency_address,
            validity_end_timestamp=req.mint_end_time_epoch_seconds,
            validity_start_timestamp=req.mint_start_time_epoch_seconds,
            uid=req.id,
        )

    def __set_allowance(
        self,
        value: int,
        currency_address: str
    ):
        params = self.get_transact_opts()
        if currency_address == ZeroAddress or currency_address == NativeAddress:
            params["value"] = value
        else:
            erc20 = ERC20(self.get_client(), currency_address)
            owner = self.get_signer_address()
            spender = self.address
            allownace = erc20.allowance(owner, spender)
            if allownace < value:
                tx = erc20.increase_allowance.build_transaction(
                    owner, value - allownace, params)
                self.execute_tx(tx)
        return params

    def mint_with_signature(self, req: NewSignaturePayload, signature: str) -> int:
        message = self.__map_payload(req)
        overrides = self.get_transact_opts()
        self.__set_allowance(req.price, req.currency_address)
        tx = self.__abi_module.mint_with_signature.build_transaction(
            message, signature, overrides)
        receipt = self.execute_tx(tx)
        logs = self.__abi_module.get_mint_with_signature_event(
            receipt.transactionHash.hex())
        result = logs[0]['args']['tokenIdMinted']
        return result

    def verify(self, mint_request: SignaturePayload, signature: str) -> bool:
        message = self.__map_payload(mint_request)
        return self.__abi_module.verify.call(message, signature)[0]

    def generate_signature_batch(self, payloads: list) -> list:
        def resolve_id(mint_request: NewSignaturePayload):
            if not mint_request.id:
                print("mint_request.id is empty, generating uuid-v4")
                generated_id = uuid.uuid4().hex
                return generated_id
            else:
                return binascii.hexlify(mint_request.id).decode()

        if not self.get_signer_address() in self.get_role_members(Role.minter):
            raise Exception("You are not a minter")
        storage = self.get_storage()

        def generate_sign(payload: NewSignaturePayload):
            resolved_id = resolve_id(payload)
            uri = storage.upload(payload.metadata, self.address, self.get_signer_address())
            payload.id = resolved_id
            payload.uri = uri
            chain_id = self.get_client().eth.chain_id
            message = self.__map_payload(payload)
            message["uri"] = uri
            message["uid"] = resolved_id
            return BatchGeneratedSignature(payload=payload,
                                           signature=self.get_client().eth.sign_typed_data(
                                               {
                                                   "name": "SignatureMint721",
                                                   "version": "1",
                                                   "chainId": chain_id,
                                                   "verifyingContract": self.address,
                                               },
                                               {
                                                   "MintRequest": [
                                                       {"name": "to",
                                                           "type": "address"},
                                                       {"name": "uri",
                                                           "type": "string"},
                                                       {"name": "price",
                                                           type: "uint256"},
                                                       {"name": "currency",
                                                           type: "address"},
                                                       {"name": "validityStartTimestamp",
                                                           type: "uint128"},
                                                       {"name": "validityEndTimestamp",
                                                           type: "uint128"},
                                                       {"name": "uid",
                                                           type: "bytes32"},
                                                   ]
                                               },
                                               message
                                           )
                                           )
        return [generate_sign(payload) for payload in payloads]

    def generate_signature(self, mint_request: NewSignaturePayload):
        return self.generate_signature_batch([mint_request])[0]

    def get_with_owner(self, token_id: int):
        """
        :param token_id: The token id to fetch the NFT for
        :return: The NFT with the given token id and owner

        Returns the NFT with the given token id and owner

        """
        owner = self.owner_of(token_id)
        meta = self.get_metadata(token_id)
        return {owner: owner, meta: meta}

    def set_module_metadata(self, metadata: str):
        """
        :param metadata: The metadata to set

        Sets the metadata for the module

        """
        uri = self.get_storage().upload_metadata(
            metadata, self.address, self.get_signer_address()
        )
        tx = self.__abi_module.set_contract_uri.build_transaction(
            uri, self.get_transact_opts()
        )
        self.execute_tx(tx)

    def get_abi_module(self) -> NFT:
        """
        :return: The ABI module for the NFT

        Returns the ABI for the NFT module
        """
        return self.__abi_module
