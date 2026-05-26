import logging
import traceback
from datetime import datetime

class RemoveTracebackFilter(logging.Filter):
    def filter(self, record):
        record.exc_info = None
        record.exc_text = None
        return True
