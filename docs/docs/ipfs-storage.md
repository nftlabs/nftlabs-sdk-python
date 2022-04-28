<a id="core.classes.ipfs_storage"></a>

# core.classes.ipfs\_storage

<a id="core.classes.ipfs_storage.IpfsStorage"></a>

## IpfsStorage Objects

```python
class IpfsStorage(ABC)
```

<a id="core.classes.ipfs_storage.IpfsStorage.get"></a>

#### get

```python
def get(hash: str) -> Dict[str, Any]
```

Gets IPFS data at a given hash and returns it as a dictionary.

**Arguments**:

- `hash`: hash of the data to get.

**Returns**:

dictionary of the data.

<a id="core.classes.ipfs_storage.IpfsStorage.get_upload_token"></a>

#### get\_upload\_token

```python
def get_upload_token(contract_address: str) -> str
```

Gets an upload token for a given contract address.

**Arguments**:

- `contract_address`: address of the contract to get the token for.

**Returns**:

upload token.

<a id="core.classes.ipfs_storage.IpfsStorage.upload"></a>

#### upload

```python
def upload(data: Union[TextIO, BinaryIO, str],
           contract_address: str = "",
           signer_address: str = "") -> str
```

Uploads data to IPFS and returns the hash of the data.

**Arguments**:

- `data`: data to upload.
- `contract_address`: optional address of the contract to get the token for.
- `signer_address`: optional address of the signer to get the token for.

**Returns**:

hash of the data.

<a id="core.classes.ipfs_storage.IpfsStorage.upload_batch"></a>

#### upload\_batch

```python
def upload_batch(files: Sequence[Union[TextIO, BinaryIO, str, Dict[str, Any]]],
                 file_start_number: int = 0,
                 contract_address: str = "",
                 signer_address: str = "") -> str
```

Uploads a list of files to IPFS and returns the hash.

**Arguments**:

- `files`: list of files to upload.
- `file_start_number`: optional number to start the file names with.
- `contract_address`: optional address of the contract to get the token for.
- `signer_address`: optional address of the signer to get the token for.

**Returns**:

hash of the data.

<a id="core.classes.ipfs_storage.IpfsStorage.upload_metadata"></a>

#### upload\_metadata

```python
def upload_metadata(metadata: Dict[str, Any],
                    contract_address: str = "",
                    signer_address: str = "") -> str
```

Uploads metadata to IPFS and returns the hash of the metadata.

**Arguments**:

- `metadata`: metadata to upload.
- `contract_address`: optional address of the contract to get the token for.
- `signer_address`: optional address of the signer to get the token for.

**Returns**:

hash of the metadata.

<a id="core.classes.ipfs_storage.IpfsStorage.upload_metadata_batch"></a>

#### upload\_metadata\_batch

```python
def upload_metadata_batch(metadatas: Sequence[Dict[str, Any]],
                          file_start_number: int = 0,
                          contract_address: str = "",
                          signer_address: str = "") -> UriWithMetadata
```

Uploads a list of metadata to IPFS and returns the hash.

**Arguments**:

- `metadatas`: list of metadata to upload.
- `file_start_number`: optional number to start the file names with.
- `contract_address`: optional address of the contract to get the token for.
- `signer_address`: optional address of the signer to get the token for.

**Returns**:

hash of the metadata.
