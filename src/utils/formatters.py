import json
import logging
from datetime import datetime, UTC
import socket
import os

DEFAULT_LOG_RECORD_ATTRS = set(
    logging.makeLogRecord({}).__dict__.keys()
)
DEFAULT_LOG_RECORD_ATTRS.update({
    "message",
    "asctime",
})

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "pid": os.getpid(),
            "timestamp": datetime.fromtimestamp(record.created, tz=UTC).isoformat(),
            "hostname": socket.gethostname(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }

        if record.exc_info:
            log_record["traceback"] = self.formatException(record.exc_info)

        extra_fields = {
            key: value
            for key, value in record.__dict__.items()
            if key not in DEFAULT_LOG_RECORD_ATTRS
        }

        log_record.update(extra_fields)

        return json.dumps(log_record, ensure_ascii=False)


class UtcFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        dt = datetime.fromtimestamp(record.created, tz=UTC)

        if datefmt:
            return dt.strftime(datefmt)

        return dt.isoformat()