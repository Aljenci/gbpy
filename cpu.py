# Documentation: http://bgb.bircd.org/pandocs.htm

from ctypes import c_ubyte, c_ushort


class Register8:
    def __init__(self, value=0):
        self._value = c_ubyte(value)

    def get(self):
        return self._value.value

    def set(self, value):
        self._value.value = value

    v = property(get, set)


class Register16:
    def __init__(self, value=0):
        self._value = c_ushort(value)

    def get(self):
        return self._value.value

    def set(self, value):
        self._value.value = value

    v = property(get, set)


class CompoundRegister:
    def __init__(self, hi, lo):
        self._hi = hi
        self._lo = lo

    def get(self):
        return (self._hi.v << 8) | self._lo.v

    def set(self, value):
        self._hi.v = value >> 8
        self._lo.v = value

    v = property(get, set)

'''
Registers
  16bit Hi   Lo   Name/Function
  AF    A    -    Accumulator & Flags
  BC    B    C    BC
  DE    D    E    DE
  HL    H    L    HL
  SP    -    -    Stack Pointer
  PC    -    -    Program Counter/Pointer
As shown above, most registers can be accessed either as one 16bit register, or as two separate 8bit registers.

The Flag Register (lower 8bit of AF register)
  Bit  Name  Set Clr  Expl.
  7    zf    Z   NZ   Zero Flag
  6    n     -   -    Add/Sub-Flag (BCD)
  5    h     -   -    Half Carry Flag (BCD)
  4    cy    C   NC   Carry Flag
  3-0  -     -   -    Not used (always zero)
Contains the result from the recent instruction which has affected flags.
'''


class Cpu:
    def __init__(self):
        # 8 bits registers
        self._A = Register8()
        self._B = Register8()
        self._C = Register8()
        self._D = Register8()
        self._E = Register8()
        self._H = Register8()
        self._L = Register8()
        self._F = Register8()

        # Compound registers
        self._AF = CompoundRegister(self._A, self._F)
        self._BC = CompoundRegister(self._B, self._C)
        self._DE = CompoundRegister(self._D, self._E)
        self._HL = CompoundRegister(self._H, self._L)

        # 16 bits registers
        self._SP = Register16()
        self._PC = Register16()

    def get_a(self):
        return self._A.v

    def get_b(self):
        return self._B.v

    def get_c(self):
        return self._C.v

    def get_d(self):
        return self._D.v

    def get_e(self):
        return self._E.v

    def get_h(self):
        return self._H.v

    def get_l(self):
        return self._L.v

    def get_f(self):
        return self._F.v

    def get_af(self):
        return self._AF.v

    def get_bc(self):
        return self._BC.v

    def get_de(self):
        return self._DE.v

    def get_hl(self):
        return self._HL.v

    def get_sp(self):
        return self._SP.v

    def get_pc(self):
        return self._PC.v

    def set_a(self, value):
        self._A.v = value

    def set_b(self, value):
        self._B.v = value

    def set_c(self, value):
        self._C.v = value

    def set_d(self, value):
        self._D.v = value

    def set_e(self, value):
        self._E.v = value

    def set_h(self, value):
        self._H.v = value

    def set_l(self, value):
        self._L.v = value

    def set_f(self, value):
        self._F.v = value

    def set_af(self, value):
        self._AF.v = value

    def set_bc(self, value):
        self._BC.v = value

    def set_de(self, value):
        self._DE.v = value

    def set_hl(self, value):
        self._HL.v = value

    def set_sp(self, value):
        self._SP.v = value

    def set_pc(self, value):
        self._PC.v = value

    A = property(get_a, set_a)
    B = property(get_b, set_b)
    C = property(get_c, set_c)
    D = property(get_d, set_d)
    E = property(get_e, set_e)
    H = property(get_h, set_h)
    L = property(get_l, set_l)
    F = property(get_f, set_f)
    AF = property(get_af, set_af)
    BC = property(get_bc, set_bc)
    DE = property(get_de, set_de)
    HL = property(get_hl, set_hl)
    SP = property(get_sp, set_sp)
    PC = property(get_pc, set_pc)


if __name__ == "__main__":
    cpu = Cpu()
    cpu.A = 0x10
    print(cpu.A)
