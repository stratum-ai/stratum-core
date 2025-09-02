from typing import Any, Dict, List, Optional, Literal

from pydantic import BaseModel, Field


# ========= Describe =========


class ColumnDescription(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None


class DescribeResponse(BaseModel):
    table: Optional[str] = None
    columns: List[ColumnDescription] = Field(default_factory=list)
    profile: Dict[str, Any] = Field(default_factory=dict)
    sample_rows: List[Dict[str, Any]] = Field(default_factory=list)
    nl_description: Optional[str] = None


# ========= Find =========


MatchKind = Literal["table", "column", "document"]


class FindMatch(BaseModel):
    kind: MatchKind
    catalog: Optional[str] = Field(
        default=None, description="For table/column results"
    )
    table: Optional[str] = Field(
        default=None, description="For table/column results: schema.table"
    )
    name: Optional[str] = Field(
        default=None, description="For column results: column name"
    )
    doc_id: Optional[str] = Field(
        default=None, description="For document results: source URI or ID"
    )
    snippet: Optional[str] = Field(
        default=None, description="For document results: short text preview"
    )
    score: Optional[float] = None


class FindResponse(BaseModel):
    query: str
    matches: List[FindMatch] = Field(default_factory=list)


# ========= Ask =========


class AskRequest(BaseModel):
    query: Optional[str] = None
    max_rows: int = 100
    catalogs: Optional[List[str]] = Field(
        default=None,
        description="Optional: restrict SQL planning/execution to specific Trino catalogs",
    )
    explain_only: bool = False
    include_passages: bool = True
    top_k_passages: int = 3


class AskMetadata(BaseModel):
    catalog: Optional[str] = None
    catalogs: Optional[List[str]] = None
    routed_reason: Optional[str] = None
    duration_ms: Optional[int] = None
    bytes_scanned: Optional[int] = None
    query_id: Optional[str] = None


class Passage(BaseModel):
    doc_id: Optional[str] = None
    page: Optional[int] = None
    snippet: Optional[str] = None
    score: Optional[float] = None


class AskStats(BaseModel):
    duration_ms: Optional[int] = None
    row_count: Optional[int] = None


class AskProvenance(BaseModel):
    tables: Optional[List[str]] = None
    documents: Optional[List[str]] = None


class Frame(BaseModel):
    name: Optional[str] = None
    rows: List[Dict[str, Any]] = Field(default_factory=list)
    provenance: Dict[str, Any] = Field(default_factory=dict)


class AskResponse(BaseModel):
    sql: Optional[str] = None
    verified: Optional[bool] = None
    engine: Optional[str] = None
    metadata: Optional[AskMetadata] = None
    rows: List[Dict[str, Any]] = Field(default_factory=list)
    passages: Optional[List[Passage]] = None
    stats: Optional[AskStats] = None
    provenance: Optional[AskProvenance] = None
    frames: Optional[List[Frame]] = None


