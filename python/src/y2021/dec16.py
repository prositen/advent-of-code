import math

from python.src.common import Day, timer, Timer


class Packet(object):
    TYPE_LITERAL = 4

    OPS = {
        0: lambda x: sum(c.value for c in x.children),
        1: lambda x: math.prod(c.value for c in x.children),
        2: lambda x: min(c.value for c in x.children),
        3: lambda x: max(c.value for c in x.children),
        TYPE_LITERAL: lambda x: x._value,
        5: lambda x: (x.children[0].value > x.children[1].value),
        6: lambda x: (x.children[0].value < x.children[1].value),
        7: lambda x: (x.children[0].value == x.children[1].value)
    }

    def __init__(self, hexstring=None, bitstring=None):
        self.bitstring = bitstring
        if hexstring:
            self.decode(hexstring)
        self._last_parsed = 0
        self._version = int(self.bitstring[:3], 2)
        self._type_id = int(self.bitstring[3:6], 2)
        self._value = 0
        self.children = list()
        self.parse()

    @property
    def value(self):
        return Packet.OPS[self._type_id](self)

    def decode(self, hex_string):
        self.bitstring = ''.join(f'{int(hc, 16):>04b}' for hc in hex_string)

    @property
    def version(self):
        return self._version

    @property
    def type_id(self):
        return self._type_id

    def length_type_id(self):
        if self.type_id != self.TYPE_LITERAL:
            return int(self.bitstring[6])
        raise Exception('Literal packets have no length type id')

    def _parse_literal(self):
        value = []
        for i in range(6, len(self.bitstring), 5):
            bits = self.bitstring[i:i + 5]
            value.append(bits[1:])
            if bits[0] == '0':
                self._last_parsed = i + 5
                break
        self._value = int(''.join(value), 2)

    def _parse_sub_packets(self):
        length_type = self.length_type_id()
        values = list()
        if length_type == 0:
            length_in_bits = int(self.bitstring[7:22], 2)
            self._last_parsed = 22
            sub_packet_length = 0
            while sub_packet_length < length_in_bits:
                p = Packet(bitstring=self.bitstring[self._last_parsed + sub_packet_length:])
                sub_packet_length += p._last_parsed
                values.append(p)
        else:
            number_of_sub_packets = int(self.bitstring[7:18], 2)
            self._last_parsed = 18
            sub_packet_length = 0
            for _ in range(number_of_sub_packets):
                p = Packet(bitstring=self.bitstring[self._last_parsed + sub_packet_length:])
                sub_packet_length += p._last_parsed
                values.append(p)
        self._last_parsed += sub_packet_length
        self.children = values

    def parse(self):
        if self.type_id == self.TYPE_LITERAL:
            self._parse_literal()
        else:
            self._parse_sub_packets()


class Dec16(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 16, instructions=instructions, filename=filename)

    @staticmethod
    def parse_instructions(instructions):
        return instructions[0]

    @timer(part=1)
    def part_1(self):
        to_visit = list()
        to_visit.append(Packet(hexstring=self.instructions))
        version_sum = 0
        while to_visit:
            p = to_visit.pop(0)
            version_sum += p.version
            to_visit.extend(p.children)
        return version_sum

    @timer(part=2)
    def part_2(self):
        return Packet(hexstring=self.instructions).value


if __name__ == '__main__':
    with Timer('Total'):
        Dec16().run_day()
