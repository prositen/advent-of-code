class Operator(object):
    op_code = 0
    operators = dict()
    writes = True

    POS = 0
    IMM = 1
    REL = 2

    def __init__(self, params, mode=None):
        self.mode = [self.POS] * self.operands
        if mode:
            self.mode = mode + self.mode

        self.op = params[:self.operands]
        self._int_code = ''.join(str(x) for x in mode[::-1]) if mode else ''
        self._int_code += '{:02}'.format(self.op_code)
        self._int_code += ',' + ','.join(str(op) for op in self.op)

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
        op_class = cls.operators.get(int(op_code, 10), cls)
        return op_class(params=instructions[1:], mode=mode)

    def run(self, context):
        return context.pc + self.operands + 1

    def get_value(self, param_no, context):
        if self.mode[param_no] == self.POS:
            return context.data.get(self.op[param_no], 0)
        elif self.mode[param_no] == self.IMM:
            return self.op[param_no]
        elif self.mode[param_no] == self.REL:
            return context.data.get(self.op[param_no] + context.relative_base, 0)

    def get_address(self, param_no, context):
        if self.mode[param_no] == self.POS:
            return self.op[param_no]
        else:
            return self.op[param_no] + context.relative_base

    def str(self, context):
        ops = [str(self.get_value(i, context)) for i in range(self.operands)]
        return (self.__class__.__name__ + ' ' +
                ','.join(ops)
                + '  ({})'.format(self._int_code)
                )


class Add(Operator, op_code=1, operands=3):

    def __init__(self, params, mode):
        super().__init__(params=params, mode=mode)

    def run(self, context):
        context.data[self.get_address(2, context)] = (self.get_value(0, context) +
                                                      self.get_value(1, context))
        return super().run(context)


class Multiply(Operator, op_code=2, operands=3):
    def __init__(self, params, mode):
        super().__init__(params=params, mode=mode)

    def run(self, context):
        context.data[self.get_address(2, context)] = (self.get_value(0, context) *
                                                      self.get_value(1, context))
        return super().run(context)


class Input(Operator, op_code=3, operands=1):
    def run(self, context):
        if context.input:
            context.waiting_for_input = False
            context.data[self.get_address(0, context)] = context.input.pop(0)
            return super().run(context)
        context.waiting_for_input = True
        return context.pc


class Output(Operator, op_code=4, operands=1):
    writes = False

    def run(self, context):
        context.output.append(self.get_value(0, context))
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
        context.data[self.get_address(2, context)] = (
            int(self.get_value(0, context) < self.get_value(1, context))
        )
        # context.data[self.op[2]] = int(self.get_value(0, context) < self.get_value(1, context))
        return super().run(context)


class Equals(Operator, op_code=8, operands=3):
    def run(self, context):
        context.data[self.get_address(2, context)] = (
            int(self.get_value(0, context) == self.get_value(1, context))
        )
        # context.data[self.op[2]] = int(self.get_value(0, context) == self.get_value(1, context))
        return super().run(context)


class AdjustRelativeBase(Operator, op_code=9, operands=1):
    writes = False

    def run(self, context):
        context.relative_base += self.get_value(0, context)
        return super().run(context)


class Exit(Operator, op_code=99):
    writes = False

    def run(self, context):
        return len(context.data)


class IntCode(object):
    def __init__(self, instructions, pc=0, relative_base=0):
        self.data = {index: instruction for index, instruction in enumerate(instructions)}
        self.input = []
        self.output = []
        self.pc = pc
        self.relative_base = relative_base
        self.waiting_for_input = False

    def get_output(self):
        if self.output:
            return self.output.pop(0)

    def add_input(self, data):
        if data is not None:
            self.input.append(data)

    def step(self, debug=False):
        if self.pc is not None and self.pc < len(self.data):
            operands = [self.data.get(self.pc + i, 0) for i in range(4)]
            operator = Operator.operator_from(operands)
            if debug:
                print(operator.str(self))
            self.pc = operator.run(self)

    def run(self, debug=False):
        while self.pc < len(self.data):
            self.step(debug)

    def run_and_wait(self, debug=False):
        while self.pc < len(self.data):
            self.step(debug)
            if self.waiting_for_input:
                return False
        return True

    def clone(self):
        return IntCode(instructions=self.data.values(),
                       pc=self.pc, relative_base=self.relative_base)
