from typing import Optional

from web3 import Web3
from eth_account.account import LocalAccount
from thirdweb.core.classes.factory import ContractFactory
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.core.classes.provider_handler import ProviderHandler
from thirdweb.core.classes.registry import ContractRegistry
from thirdweb.types.sdk import SDKOptions


class ContractDeployer(ProviderHandler):
    __factory: ContractFactory
    __registry: ContractRegistry

    _storage: IpfsStorage

    def __init__(
        self,
        provider: Web3,
        signer: Optional[LocalAccount] = None,
        options: SDKOptions = SDKOptions(),
        storage: IpfsStorage = IpfsStorage(),
    ):
        super().__init__(provider, signer, options)
        self._storage = storage