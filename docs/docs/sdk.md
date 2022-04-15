<a id="core.sdk"></a>

# core.sdk

<a id="core.sdk.ThirdwebSDK"></a>

## ThirdwebSDK Objects

```python
class ThirdwebSDK(ProviderHandler)
```

<a id="core.sdk.ThirdwebSDK.__init__"></a>

#### \_\_init\_\_

```python
def __init__(provider: Web3,
             signer: Optional[LocalAccount] = None,
             options: SDKOptions = SDKOptions(),
             storage: IpfsStorage = IpfsStorage())
```

Initialize the thirdweb SDK.

**Arguments**:

- `provider`: web3 provider instance to use for getting on-chain data
- `signer`: signer to use for sending transactions
- `options`: optional SDK configuration options
- `storage`: optional IPFS storage instance to use for storing data

<a id="core.sdk.ThirdwebSDK.get_nft_collection"></a>

#### get\_nft\_collection

```python
def get_nft_collection(address: str) -> NFTCollection
```

Returns an NFT Collection contract SDK instance

**Arguments**:

- `address`: address of the NFT Collection contract

**Returns**:

NFT Collection contract SDK instance

<a id="core.sdk.ThirdwebSDK.get_edition"></a>

#### get\_edition

```python
def get_edition(address: str) -> Edition
```

Returns an Edition contract SDK instance

**Arguments**:

- `address`: address of the Edition contract

**Returns**:

Edition contract SDK instance

<a id="core.sdk.ThirdwebSDK.get_token"></a>

#### get\_token

```python
def get_token(address: str) -> Token
```

Returns a Token contract SDK instance

**Arguments**:

- `address`: address of the Token contract

**Returns**:

Token contract SDK instance

<a id="core.sdk.ThirdwebSDK.get_marketplace"></a>

#### get\_marketplace

```python
def get_marketplace(address: str) -> Marketplace
```

Returns a Marketplace contract SDK instance

**Arguments**:

- `address`: address of the Marketplace contract

**Returns**:

Marketplace contract SDK instance

<a id="core.sdk.ThirdwebSDK.get_nft_drop"></a>

#### get\_nft\_drop

```python
def get_nft_drop(address: str) -> NFTDrop
```

Returns an NFT Drop contract SDK instance

**Arguments**:

- `address`: address of the NFT Drop contract

**Returns**:

NFT Drop contract SDK instance

<a id="core.sdk.ThirdwebSDK.update_provider"></a>

#### update\_provider

```python
def update_provider(provider: Web3)
```

Update the provider instance used by the SDK.

**Arguments**:

- `provider`: web3 provider instance to use for getting on-chain data

<a id="core.sdk.ThirdwebSDK.update_signer"></a>

#### update\_signer

```python
def update_signer(signer: Optional[LocalAccount] = None)
```

Update the signer instance used by the SDK.

**Arguments**:

- `signer`: signer to use for sending transactions
