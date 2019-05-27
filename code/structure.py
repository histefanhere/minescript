class Object:
    def __init__(self, cur_object, operation, children):
        self.cur_object = cur_object
        self.operation = operation
        self.children = children

        # TODO: get the type. get_type() will also pretify cur_object and operation
        #self.type = get_type()
