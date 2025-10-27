from .create import NewsCreateView
from .list import NewsListView
from .retrieve import NewsRetrieveView
from .update import NewsUpdateView

__all__ = [
    "NewsCreateView",
    "NewsRetrieveView",
    "NewsUpdateView",
    "NewsListView",
]
