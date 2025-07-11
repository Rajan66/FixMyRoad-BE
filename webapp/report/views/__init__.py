from .bulk import CreateBulkReportView
from .create import CreateReportView
from .delete import DestroyReportView
from .list import ListReportView
from .retrieve import RetrieveReportView
from .update import UpdateReportView

__all__ = [
    "CreateReportView",
    "ListReportView",
    "UpdateReportView",
    "DestroyReportView",
    "RetrieveReportView",
    "CreateBulkReportView",
]
