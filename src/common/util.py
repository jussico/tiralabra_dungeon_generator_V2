
class FileLogger:

    def __init__(self):
        my_name = type(self).__name__
        print(f"@init {my_name}")

    def logita(self, jotain):
        with open('logia.txt', 'a') as logia:
            print(jotain, file=logia)
        logia.close()

# tests

