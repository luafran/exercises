
class MyContextManager:
    def __init__(self):
        print('init cm')

    def __enter__(self):
        print('enter cm')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit cm')
        return False


with MyContextManager() as cm:
    print('inside with')
