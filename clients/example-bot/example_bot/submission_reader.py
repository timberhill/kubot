from .stream_reader import StreamReader
from datetime import datetime


class SubmissionReader(StreamReader):
    """Submission stream reader
    """
    def process(self, data):
        """Process data

        Args:
            data (dict): incoming json object
        """
        receive_time = datetime.utcnow()
        delay = receive_time - datetime.fromtimestamp(data["dispatch_time"])
        print(data["title"], delay.total_seconds() * 1000, "ms")
