from kubot.client import StreamHandler


class SubmissionHandler(StreamHandler):
    port = 37998

    def process(self, data):
        print(data)
