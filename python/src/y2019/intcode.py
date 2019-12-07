class Operator(object):
    op_code = 0
    operators = dict()
    writes = True

    POS = 0
    IMM = 1

    def __init__(self, params, mode=None, *args):
        self.mode = [self.POS] * self.operands
        if mode:
            self.mode = mode + self.mode
        if self.writes:
            # Parameters that an instruction writes to will
            # never be in immediate mode
            self.mode[self.operands - 1] = self.POS

        self.op = params[:self.operands]

    def __init_subclass__(cls, op_code=None, operands=0, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.operands = operands
        cls.op_code = op_code
        cls.operators[op_code] = cls

    @classmethod
    def operator_from(cls, instructions):
        # Look up correct operator to use using op_code
        op_code = str(instructions[0])
        if len(op_code) > 2:
            mode = [int(x) for x in op_code[:-2][::-1]]
            op_code = op_code[-2:]
        else:
            mode = None
        op_class = cls.operators.get(int(op_code), cls)
        return op_class(params=instructions[1:], mode=mode)

    def run(self, context):
        return context.pc + self.operands + 1

    def get_value(self, param_no, context):
        if self.mode[param_no] == self.IMM:
            return self.op[param_no]
        else:
            return context.data[self.op[param_no]]

    def str(self, context):
        ops = [str(self.get_value(i, context)) for i in range(self.operands)]
        return (self.__class__.__name__ + ' ' +
                ','.join(ops)
                )


class Add(Operator, op_code=1, operands=3):

    def __init__(self, params, mode):
        super().__init__(params=params, mode=mode)

    def run(self, context):
        context.data[self.op[2]] = self.get_value(0, context) + self.get_value(1, context)
        return super().run(context)


class Multiply(Operator, op_code=2, operands=3):
    def __init__(self, params, mode):
        super().__init__(params=params, mode=mode)

    def run(self, context):
        context.data[self.op[2]] = self.get_value(0, context) * self.get_value(1, context)
        return super().run(context)


class Input(Operator, op_code=3, operands=1):
    def run(self, context):
        if context.input:
            context.data[self.op[0]] = context.input.pop(0)
            return super().run(context)
        return context.pc


class Output(Operator, op_code=4, operands=1):
    writes = False

    def run(self, context):
        context.output = self.get_value(0, context)
        return super().run(context)


class JumpIfTrue(Operator, op_code=5, operands=2):
    writes = False

    def run(self, context):
        if self.get_value(0, context):
            return self.get_value(1, context)
        else:
            return super().run(context)


class JumpIfFalse(Operator, op_code=6, operands=2):
    writes = False

    def run(self, context):
        if not self.get_value(0, context):
            return self.get_value(1, context)
        else:
            return super().run(context)


class LessThan(Operator, op_code=7, operands=3):
    def run(self, context):
        context.data[self.op[2]] = int(self.get_value(0, context) < self.get_value(1, context))
        return super().run(context)


class Equals(Operator, op_code=8, operands=3):
    def run(self, context):
        context.data[self.op[2]] = int(self.get_value(0, context) == self.get_value(1, context))
        return super().run(context)


class Exit(Operator, op_code=99):
    writes = False

    def run(self, context):
        return len(context.data)


class IntCode(object):
    def __init__(self, instructions):
        self.data = [i for i in instructions]
        self.input = []
        self.output = None
        self.pc = 0

    def step(self, debug=False):
        if self.pc is not None and self.pc < len(self.data):
            operator = Operator.operator_from(self.data[self.pc:])
            if debug:
                print(operator.str(self))
            self.pc = operator.run(self)

    def run(self, debug=False):
        while self.pc < len(self.data):
            self.step(debug)
