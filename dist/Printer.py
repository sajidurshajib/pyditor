class Printer:
    def __init__(self, text_body):
        self.text_body = text_body

    def print_only(self, strip: bool = False):

        if strip:
            print(self.text_body.strip())
        else:
            print(self.text_body)
