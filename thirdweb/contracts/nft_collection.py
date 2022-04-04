from thirdweb.constants.role import Role
from thirdweb.core.classes.contract_metadata import ContractMetadata
from thirdweb.core.classes.contract_platform_fee import ContractPlatformFee
from thirdweb.core.classes.contract_roles import ContractRoles
from thirdweb.core.classes.contract_royalty import ContractRoyalty
from thirdweb.core.classes.contract_sales import ContractPrimarySale
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.common.nft import upload_or_extract_uri, upload_or_extract_uris
from thirdweb.core.classes.erc_721 import ERC721
from thirdweb.abi import TokenERC721

from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contract import ContractType
from thirdweb.types.nft import NFTMetadataInput
from eth_account.account import LocalAccount
from web3.eth import TxReceipt
from web3 import Web3

from thirdweb.types.sdk import SDKOptions
from typing import Final, Optional, List, Union

from thirdweb.types.settings.metadata import NFTCollectionContractMetadata


class NFTCollection(ERC721):
    _abi_type = TokenERC721

    contract_type: Final[ContractType] = ContractType.NFT_COLLECTION
    contract_roles: Final[List[Role]] = [Role.ADMIN, Role.MINTER, Role.TRANSFER]

    schema = NFTCollectionContractMetadata
    metadata: ContractMetadata[TokenERC721, NFTCollectionContractMetadata]
    roles: ContractRoles
    primary_sale: ContractPrimarySale[TokenERC721]
    platform_fee: ContractPlatformFee[TokenERC721]
    royalty: ContractRoyalty[TokenERC721]

    def __init__(
        self,
        provider: Web3,
        address: str,
        storage: IpfsStorage,
        signer: Optional[LocalAccount] = None,
        options: SDKOptions = SDKOptions(),
    ):
        abi = TokenERC721(provider, address)
        contract_wrapper = ContractWrapper(abi, provider, signer, options)
        super().__init__(contract_wrapper, storage)

        self.metadata = ContractMetadata(contract_wrapper, storage, self.schema)
        self.roles = ContractRoles(contract_wrapper, self.contract_roles)
        self.primary_sale = ContractPrimarySale(contract_wrapper)
        self.platform_fee = ContractPlatformFee(contract_wrapper)
        self.royalty = ContractRoyalty(contract_wrapper, self.metadata)

    """
    WRITE FUNCTIONS
    """

    def mint(self, metadata: Union[NFTMetadataInput, str]) -> TxReceipt:
        """
        Mint a new NFT to the connected wallet

        :param metadata: metadata of the NFT to mint
        :returns: transaction receipt of the mint
        """

        return self.mint_to(self._contract_wrapper.get_signer_address(), metadata)

    def mint_to(self, to: str, metadata: Union[NFTMetadataInput, str]) -> TxReceipt:
        """
        Mint a new NFT to the specified wallet

        :param to: wallet address to mint the NFT to
        :param metadata: metadata of the NFT to mint
        :returns: transaction receipt of the mint
        """

        uri = upload_or_extract_uri(metadata, self._storage)
        return self._contract_wrapper.send_transaction("mint_to", [to, uri])

    def mint_batch(self, metadatas: List[Union[NFTMetadataInput, str]]) -> TxReceipt:
        """
        Mint a batch of new NFTs to the connected wallet

        :param metadatas: list of metadata of the NFTs to mint
        :returns: transaction receipt of the mint
        """

        return self.mint_batch_to(
            self._contract_wrapper.get_signer_address(), metadatas
        )

    def mint_batch_to(
        self, to: str, metadatas: List[Union[NFTMetadataInput, str]]
    ) -> TxReceipt:
        """
        Mint a batch of new NFTs to the specified wallet

        :param to: wallet address to mint the NFTs to
        :param metadatas: list of metadata of the NFTs to mint
        :returns: transaction receipt of the mint
        """

        uris = upload_or_extract_uris(metadatas, self._storage)

        encoded = []
        interface = self._contract_wrapper.get_contract_interface()
        for uri in uris:
            encoded.append(interface.encodeABI("mintTo", [to, uri]))

        return self._contract_wrapper.multi_call(encoded)
