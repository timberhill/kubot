from kubot.client import StreamHandler


class CommentHandler(StreamHandler):
    port = 37999

    def process(self, data):
        print(data)
