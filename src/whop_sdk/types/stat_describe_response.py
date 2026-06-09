# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "StatDescribeResponse",
    "DescribeRoot",
    "DescribeRootDebug",
    "DescribeRootMetric",
    "DescribeNode",
    "DescribeNodeAssociation",
    "DescribeNodeDebug",
    "DescribeNodeMetric",
    "DescribeMetric",
    "DescribeMetricDebug",
    "DescribeView",
    "DescribeViewAssociation",
    "DescribeViewDebug",
    "DescribeViewMetric",
]


class DescribeRootDebug(BaseModel):
    """Debug information."""

    request_id: Optional[str] = None
    """Unique request identifier for debugging."""


class DescribeRootMetric(BaseModel):
    """A metric available for querying."""

    name: str
    """The metric name."""

    node_path: str
    """The node path this metric operates on."""

    supported_engines: List[str]
    """Query engines that support this metric."""


class DescribeRoot(BaseModel):
    """Root schema description showing available nodes, views, and metrics."""

    debug: Optional[DescribeRootDebug] = None
    """Debug information."""

    metrics: List[DescribeRootMetric]
    """Available metrics."""

    nodes: List[str]
    """Available root nodes."""

    typename: Literal["DescribeRoot"]
    """The typename of this object"""

    views: List[str]
    """Available API resource views."""


class DescribeNodeAssociation(BaseModel):
    """An association or child path available for navigation."""

    event_name: Optional[str] = None
    """The event name (for event type)."""

    model: Optional[str] = None
    """The associated model class name (for model associations)."""

    name: str
    """The association name."""

    path: Optional[str] = None
    """The full path (for event associations)."""

    type: str
    """The type (belongs_to, has_many, has_one, event, namespace)."""


class DescribeNodeDebug(BaseModel):
    """Debug information."""

    request_id: Optional[str] = None
    """Unique request identifier for debugging."""


class DescribeNodeMetric(BaseModel):
    """A metric available for querying."""

    name: str
    """The metric name."""

    node_path: str
    """The node path this metric operates on."""

    supported_engines: List[str]
    """Query engines that support this metric."""


class DescribeNode(BaseModel):
    """Description of a node (model) including its columns and associations."""

    associations: List[DescribeNodeAssociation]
    """Available associations or child paths."""

    columns: List[str]
    """Available columns."""

    debug: Optional[DescribeNodeDebug] = None
    """Debug information."""

    engine: str
    """The query engine being used."""

    metrics: List[DescribeNodeMetric]
    """Available metrics for this node."""

    node: str
    """The node path being described."""

    sample: Optional[List[Dict[str, object]]] = None
    """Sample data rows."""

    sortable_columns: List[str]
    """Columns that can be used for sorting."""

    typename: Literal["DescribeNode"]
    """The typename of this object"""


class DescribeMetricDebug(BaseModel):
    """Debug information."""

    request_id: Optional[str] = None
    """Unique request identifier for debugging."""


class DescribeMetric(BaseModel):
    """Description of a metric including its configuration and SQL."""

    breakdownable_columns: List[str]
    """Columns that can be used for breakdowns."""

    debug: Optional[DescribeMetricDebug] = None
    """Debug information."""

    engine: str
    """The query engine being used."""

    filterable_columns: List[str]
    """Columns that can be used for filtering."""

    metric: str
    """The metric name."""

    node: str
    """The node path this metric operates on."""

    sql: Optional[str] = None
    """The generated SQL query."""

    supported_engines: List[str]
    """Query engines that support this metric."""

    timestamp_column: str
    """The timestamp column used for time filtering."""

    typename: Literal["DescribeMetric"]
    """The typename of this object"""


class DescribeViewAssociation(BaseModel):
    """An association or child path available for navigation."""

    event_name: Optional[str] = None
    """The event name (for event type)."""

    model: Optional[str] = None
    """The associated model class name (for model associations)."""

    name: str
    """The association name."""

    path: Optional[str] = None
    """The full path (for event associations)."""

    type: str
    """The type (belongs_to, has_many, has_one, event, namespace)."""


class DescribeViewDebug(BaseModel):
    """Debug information."""

    request_id: Optional[str] = None
    """Unique request identifier for debugging."""


class DescribeViewMetric(BaseModel):
    """A metric available for querying."""

    name: str
    """The metric name."""

    node_path: str
    """The node path this metric operates on."""

    supported_engines: List[str]
    """Query engines that support this metric."""


class DescribeView(BaseModel):
    """Description of an API resource view including its columns and associations."""

    associations: List[DescribeViewAssociation]
    """Available associations."""

    columns: List[str]
    """Available columns."""

    debug: Optional[DescribeViewDebug] = None
    """Debug information."""

    engine: str
    """The query engine being used."""

    metrics: List[DescribeViewMetric]
    """Available metrics."""

    model: str
    """The underlying model class."""

    resource: str
    """The API resource name."""

    sample: Optional[List[Dict[str, object]]] = None
    """Sample data rows."""

    sortable_columns: List[str]
    """Columns that can be used for sorting."""

    typename: Literal["DescribeView"]
    """The typename of this object"""

    view: str
    """The view name being described."""


StatDescribeResponse: TypeAlias = Annotated[
    Union[Optional[DescribeRoot], Optional[DescribeNode], Optional[DescribeMetric], Optional[DescribeView]],
    PropertyInfo(discriminator="typename"),
]
