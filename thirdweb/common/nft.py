from typing import List, Union, cast
from thirdweb.common.error import UploadException
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.nft import NFTMetadata


def fetch_token_metadata(
    token_id: int, token_uri: str, storage: IpfsStorage
) -> NFTMetadata:
    metadata = storage.get(token_uri)
    return NFTMetadata(
        token_id,
        token_uri,
        cast(str, metadata.get("name")),
        metadata.get("description"),
        metadata.get("image"),
        metadata.get("external_url"),
        metadata.get("animation_url"),
        metadata.get("background_color"),
        metadata.get("properties"),
    )


def upload_or_extract_uri(
    metadata: Union[NFTMetadata, str], storage: IpfsStorage
) -> str:
    if isinstance(metadata, str):
        return metadata
    else:
        return storage.upload_metadata(metadata)


def is_uri_list(metadatas: List[Union[NFTMetadata, str]]) -> bool:
    return all(isinstance(metadata, str) for metadata in metadatas)


def is_metadata_list(metadatas: List[Union[NFTMetadata, str]]) -> bool:
    return all(isinstance(metadata, NFTMetadata) for metadata in metadatas)


def upload_or_extract_uris(
    metadatas: List[Union[NFTMetadata, str]], storage: IpfsStorage
) -> List[str]:
    if is_uri_list(metadatas):
        return cast(List[str], metadatas)
    elif is_metadata_list(metadatas):
        uri_with_metadata = storage.upload_metadata_batch(metadatas)
        return uri_with_metadata.metadata_uris
    else:
        raise UploadException(
            "Metadata must be either a list of strings or a list of NFTMetadata"
        )