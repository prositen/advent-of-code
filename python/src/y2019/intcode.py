class Operator(object):
    op_code = 0
    operators = dict()

    def __init__(self, *args):
        pass

    def __init_subclass__(cls, op_code=None, **kwargs):
        # Add mapping between class mapping and class type
        super().__init_subclass__(**kwargs)
        cls.op_code = op_code
        cls.operators[op_code] = cls

    @classmethod
    def operator_from(cls, instructions):
        # Lookup right operator to use from op_code
        op_code = instructions[0]
        op_class = cls.operators.get(op_code, cls)
        return op_class(instructions[1:])

    def run(self, context):
        """

        :param context: Current instruction / data set
        :return: number of steps to increase program counter
        """
        return 1


class Add(Operator, op_code=1):
    def __init__(self, instructions):
        super().__init__()
        self.op1, self.op2, self.target = instructions[0:3]

    def run(self, context):
        context[self.target] = context[self.op1] + context[self.op2]
        return 4


class Multiply(Operator, op_code=2):
    def __init__(self, instructions):
        super().__init__()
        self.op1, self.op2, self.target = instructions[0:3]

    def run(self, context):
        context[self.target] = context[self.op1] * context[self.op2]
        return 4


class Exit(Operator, op_code=99):
    def run(self, context):
        return len(context)


class IntCode(object):
    def __init__(self, instructions):
        self.instructions = [i for i in instructions]

    def run(self):
        pc = 0
        while pc < len(self.instructions):
            operator = Operator.operator_from(self.instructions[pc:])
            pc += operator.run(self.instructions)
        return self.instructions[0]
