from __future__ import annotations

import os
from typing import List

from qdrant_client import QdrantClient
from qdrant_client.http import models as qmodels


SCHEMA_COLLECTION = "schema_objects"
VECTOR_SIZE = int(os.getenv("QDRANT_VECTOR_SIZE", "1536"))


def get_qdrant_client() -> QdrantClient:
    url = os.getenv("QDRANT_URL", "http://localhost:6333")
    return QdrantClient(url=url)


def ensure_schema_collection() -> None:
    client = get_qdrant_client()
    collections = client.get_collections()
    names = {c.name for c in collections.collections}
    if SCHEMA_COLLECTION in names:
        try:
            info = client.get_collection(SCHEMA_COLLECTION)
            # Attempt to detect size from config
            cfg = getattr(info, "config", None)
            size = None
            if cfg and getattr(cfg, "params", None):
                vectors = getattr(cfg.params, "vectors", None)
                # Vectors may be VectorParams or dict of named vectors
                if isinstance(vectors, qmodels.VectorParams):
                    size = vectors.size
                elif isinstance(vectors, dict):
                    # pick first named vector
                    for v in vectors.values():
                        if isinstance(v, qmodels.VectorParams):
                            size = v.size
                            break
            if size is not None and int(size) != VECTOR_SIZE:
                # Recreate with desired size
                client.delete_collection(SCHEMA_COLLECTION)
                client.create_collection(
                    collection_name=SCHEMA_COLLECTION,
                    vectors_config=qmodels.VectorParams(
                        size=VECTOR_SIZE,
                        distance=qmodels.Distance.COSINE,
                    ),
                )
            # else: correct size, nothing to do
            return
        except Exception:
            # Best-effort: ensure exists with desired size
            pass
    # Create if missing
    client.create_collection(
        collection_name=SCHEMA_COLLECTION,
        vectors_config=qmodels.VectorParams(
            size=VECTOR_SIZE,
            distance=qmodels.Distance.COSINE,
        ),
    )


def list_collections() -> List[str]:
    client = get_qdrant_client()
    collections = client.get_collections()
    return [c.name for c in collections.collections]


