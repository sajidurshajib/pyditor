from dist import Printer


class Reader:
    def __init__(self, filename):
        self.filename = filename

    def read_only(self):
        fr = open(self.filename, 'r')
        txt = fr.read()
        return txt
