#
# This file is part of LiteX-Boards.
#
# Copyright (c) 2020 David Shah <dave@ds0.me>
# Copyright (c) 2020 Florent Kermarrec <florent@enjoy-digital.fr>
# SPDX-License-Identifier: BSD-2-Clause

from litex.build.generic_platform import Pins, Subsignal, IOStandard, Misc
from litex.build.xilinx import XilinxPlatform, VivadoProgrammer

# IOs ----------------------------------------------------------------------------------------------

_io = [
    # clk
    ("clk300", 0,
        Subsignal("n", Pins("AY38"), IOStandard("DIFF_SSTL12")),
        Subsignal("p", Pins("AY37"), IOStandard("DIFF_SSTL12")),
    ),

    # led
    ("user_led", 0, Pins("BC21"), IOStandard("LVCMOS12")),
    ("user_led", 1, Pins("BB21"), IOStandard("LVCMOS12")),
    ("user_led", 2, Pins("BA20"), IOStandard("LVCMOS12")),

    # serial
    ("serial", 0,
        Subsignal("rx", Pins("BF18"), IOStandard("LVCMOS12")),
        Subsignal("tx", Pins("BB20"), IOStandard("LVCMOS12")),
    ),

    # pcie
    ("pcie_x4", 0,
        Subsignal("rst_n", Pins("BD21"), IOStandard("LVCMOS12")),
        Subsignal("clk_n", Pins("AM10")),
        Subsignal("clk_p", Pins("AM11")),
        Subsignal("rx_n",  Pins("AF1 AG3 AH1 AJ3")),
        Subsignal("rx_p",  Pins("AF2 AG4 AH2 AJ4")),
        Subsignal("tx_n",  Pins("AF6 AG8 AH6 AJ8")),
        Subsignal("tx_p",  Pins("AF7 AG9 AH7 AJ9")),
    ),

    # ddram
    ("ddram", 0,
        Subsignal("a", Pins(
            "AT36 AV36 AV37 AW35 AW36 AY36 AY35 BA40",
            "BA37 BB37 AR35 BA39 BB40 AN36"),
            IOStandard("SSTL12_DCI")),
        Subsignal("act_n", Pins("BB39"), IOStandard("SSTL12_DCI")),
        Subsignal("ba",    Pins("AT35 AT34"), IOStandard("SSTL12_DCI")),
        Subsignal("bg",    Pins("BC37 BC39"), IOStandard("SSTL12_DCI")),
        Subsignal("cas_n", Pins("AP36"), IOStandard("SSTL12_DCI")),
        Subsignal("cke",   Pins("BC38"), IOStandard("SSTL12_DCI")),
        Subsignal("clk_n", Pins("AW38"), IOStandard("DIFF_SSTL12_DCI")),
        Subsignal("clk_p", Pins("AV38"), IOStandard("DIFF_SSTL12_DCI")),
        Subsignal("cs_n",  Pins("AR33"), IOStandard("SSTL12_DCI")),
        Subsignal("dm",    Pins("AM31 AP30 AL28 AR30 AU29 AY27 BE35 BE31"),
            IOStandard("POD12_DCI")),
        Subsignal("dq", Pins(
            "AW28 AW29 BA28 BA27 BB29 BA29 BC27 BB27",
            "BE28 BF28 BE30 BD30 BF27 BE27 BF30 BF29",
            "BB31 BB32 AY32 AY33 BC32 BC33 BB34 BC34",
            "AV31 AV32 AV34 AW34 AW31 AY31 BA35 BA34",
            "AL30 AM30 AU32 AT32 AN31 AN32 AR32 AR31",
            "AP29 AP28 AN27 AM27 AN29 AM29 AR27 AR28",
            "AT28 AV27 AU27 AT27 AV29 AY30 AW30 AV28",
            "BD34 BD33 BE33 BD35 BF32 BF33 BF34 BF35"),
            IOStandard("POD12_DCI"),
            Misc("PRE_EMPHASIS=RDRV_240"),
            Misc("EQUALIZATION=EQ_LEVEL2")),
        Subsignal("dqs_n", Pins("BB30 BC26 BD29 BE26 BB36 BD31 AW33 BA33"),
            IOStandard("DIFF_POD12"),
            Misc("PRE_EMPHASIS=RDRV_240"),
            Misc("EQUALIZATION=EQ_LEVEL2")),
        Subsignal("dqs_p", Pins("BA30 BB26 BD28 BD26 BB35 BC31 AV33 BA32"),
            IOStandard("DIFF_POD12"),
            Misc("PRE_EMPHASIS=RDRV_240"),
            Misc("EQUALIZATION=EQ_LEVEL2")),
        Subsignal("odt",     Pins("AP34"), IOStandard("SSTL12_DCI")),
        Subsignal("ras_n",   Pins("AR36"), IOStandard("SSTL12_DCI")),
        Subsignal("reset_n", Pins("AU31"), IOStandard("LVCMOS12")),
        Subsignal("we_n",    Pins("AP35"), IOStandard("SSTL12_DCI")),
        Misc("SLEW=FAST")
    ),
    ("ddram", 1,
        Subsignal("a", Pins(
            "AN24 AT24 AW24 AN26 AY22 AY23 AV24 BA22",
            "AY25 BA23 AM26 BA25 BB22 AL24"),
            IOStandard("SSTL12_DCI")),
        Subsignal("act_n", Pins("AW25"), IOStandard("SSTL12_DCI")),
        Subsignal("ba",    Pins("AU24 AP26"), IOStandard("SSTL12_DCI")),
        Subsignal("bg",    Pins("BC22 AW26"), IOStandard("SSTL12_DCI")),
        Subsignal("cas_n", Pins("AM25"), IOStandard("SSTL12_DCI")),
        Subsignal("cke",   Pins("BB25"), IOStandard("SSTL12_DCI")),
        Subsignal("clk_n", Pins("AU25"), IOStandard("DIFF_SSTL12_DCI")),
        Subsignal("clk_p", Pins("AT25"), IOStandard("DIFF_SSTL12_DCI")),
        Subsignal("cs_n",  Pins("AV23"), IOStandard("SSTL12_DCI")),
        Subsignal("dm",    Pins("BE12 BE15 BC13 BB14 AV18 AW16 AP16 AM17"),
            IOStandard("POD12_DCI")),
        Subsignal("dq", Pins(
            "BD9 BD7 BC7 BD8 BD10 BE10 BE7 BF7",
            "AU13 AV13 AW13 AW14 AU14 AY11 AV14 BA11",
            "BA12 BB12 BA13 BA14 BC9 BB9 BA7 BA8",
            "AN13 AR13 AM13 AP13 AM14 AR15 AL14 AT15",
            "BE13 BD14 BF12 BD13 BD15 BD16 BF14 BF13",
            "AY17 BA17 AY18 BA18 BA15 BB15 BC11 BD11",
            "AV16 AV17 AU16 AU17 BB17 BB16 AT18 AT17",
            "AM15 AL15 AN17 AN16 AR18 AP18 AL17 AL16"),
            IOStandard("POD12_DCI"),
            Misc("PRE_EMPHASIS=RDRV_240"),
            Misc("EQUALIZATION=EQ_LEVEL2")),
        Subsignal("dqs_n", Pins("BF9 BF8 AY15 AY12 BB10 BA9 AT13 AP14"),
            IOStandard("DIFF_POD12"),
            Misc("PRE_EMPHASIS=RDRV_240"),
            Misc("EQUALIZATION=EQ_LEVEL2")),
        Subsignal("dqs_p", Pins("BF10 BE8 AW15 AY13 BB11 BA10 AT14 AN14"),
            IOStandard("DIFF_POD12"),
            Misc("PRE_EMPHASIS=RDRV_240"),
            Misc("EQUALIZATION=EQ_LEVEL2")),
        Subsignal("odt",     Pins("AW23"), IOStandard("SSTL12_DCI")),
        Subsignal("ras_n",   Pins("AN23"), IOStandard("SSTL12_DCI")),
        Subsignal("reset_n", Pins("AR17"), IOStandard("LVCMOS12")),
        Subsignal("we_n",    Pins("AL25"), IOStandard("SSTL12_DCI")),
        Misc("SLEW=FAST")
    ),
    ("ddram", 2,
        Subsignal("a", Pins(
            "L29 A33 C33 J29 H31 G31 C32 B32",
            "A32 D31 A34 E31 M30 F33"),
            IOStandard("SSTL12_DCI")),
        Subsignal("act_n", Pins("B31"), IOStandard("SSTL12_DCI")),
        Subsignal("ba",    Pins("D33 B36"), IOStandard("SSTL12_DCI")),
        Subsignal("bg",    Pins("C31 J30"), IOStandard("SSTL12_DCI")),
        Subsignal("cas_n", Pins("G32"), IOStandard("SSTL12_DCI")),
        Subsignal("cke",   Pins("G30"), IOStandard("SSTL12_DCI")),
        Subsignal("clk_n", Pins("B34"), IOStandard("DIFF_SSTL12_DCI")),
        Subsignal("clk_p", Pins("C34"), IOStandard("DIFF_SSTL12_DCI")),
        Subsignal("cs_n",  Pins("B35"), IOStandard("SSTL12_DCI")),
        Subsignal("dm",    Pins("E39 G37 N31 T30 L35 M34 J38 H33"),
            IOStandard("POD12_DCI")),
        Subsignal("dq", Pins(
            "R25 P25 M25 L25 P26 R26 N27 N28",
            "J28 H29 H28 G29 K25 L27 K26 K27",
            "F27 E27 E28 D28 G27 G26 F28 F29",
            "D26 C26 B27 B26 A29 A30 C27 C28",
            "F35 E38 D38 E35 E36 E37 F38 G38",
            "P30 R30 P29 N29 L32 M32 P31 N32",
            "J35 K35 L33 K33 J34 J33 N34 P34",
            "H36 G36 H37 J36 K37 K38 G35 G34"),
            IOStandard("POD12_DCI"),
            Misc("PRE_EMPHASIS=RDRV_240"),
            Misc("EQUALIZATION=EQ_LEVEL2")),
        Subsignal("dqs_n", Pins("M26 P28 J26 L28 D30 H27 A28 B29"),
            IOStandard("DIFF_POD12"),
            Misc("PRE_EMPHASIS=RDRV_240"),
            Misc("EQUALIZATION=EQ_LEVEL2")),
        Subsignal("dqs_p", Pins("N26 R28 J25 M27 D29 H26 A27 C29"),
            IOStandard("DIFF_POD12"),
            Misc("PRE_EMPHASIS=RDRV_240"),
            Misc("EQUALIZATION=EQ_LEVEL2")),
        Subsignal("odt",     Pins("E33"), IOStandard("SSTL12_DCI")),
        Subsignal("ras_n",   Pins("K30"), IOStandard("SSTL12_DCI")),
        Subsignal("reset_n", Pins("D36"), IOStandard("LVCMOS12")),
        Subsignal("we_n",    Pins("A35"), IOStandard("SSTL12_DCI")),
        Misc("SLEW=FAST")
    ),
    ("ddram", 4,
        Subsignal("a", Pins(
            "K15 B15 F14 A15 C14 A14 B14 E13",
            "F13 A13 D14 C13 B13 K16"),
            IOStandard("SSTL12_DCI")),
        Subsignal("act_n", Pins("H13"), IOStandard("SSTL12_DCI")),
        Subsignal("ba",    Pins("J15 H14"), IOStandard("SSTL12_DCI")),
        Subsignal("bg",    Pins("D13 J13"), IOStandard("SSTL12_DCI")),
        Subsignal("cas_n", Pins("E15"), IOStandard("SSTL12_DCI")),
        Subsignal("cke",   Pins("K13"), IOStandard("SSTL12_DCI")),
        Subsignal("clk_n", Pins("L13"), IOStandard("DIFF_SSTL12_DCI")),
        Subsignal("clk_p", Pins("L14"), IOStandard("DIFF_SSTL12_DCI")),
        Subsignal("cs_n",  Pins("B16"), IOStandard("SSTL12_DCI")),
        Subsignal("dm",    Pins("A25 D24 C17 B19 F18 H19 F23 H23"),
            IOStandard("POD12_DCI")),
        Subsignal("dq", Pins(
            "P24 N24 T24 R23 N23 P21 P23 R21",
            "J24 J23 H24 G24 L24 L23 K22 K21",
            "G20 H17 F19 G17 J20 L19 L18 J19",
            "M19 M20 R18 R17 R20 T20 N18 N19",
            "A23 A22 B24 B25 B22 C22 C24 C23",
            "C19 C18 C21 B21 A18 A17 A20 B20",
            "E17 F20 E18 E20 D19 D20 H18 J18",
            "F22 E22 G22 G21 F24 E25 F25 G25"),
            IOStandard("POD12_DCI"),
            Misc("PRE_EMPHASIS=RDRV_240"),
            Misc("EQUALIZATION=EQ_LEVEL2")),
        Subsignal("dqs_n", Pins("R22 N21 H21 L22 K20 K17 P18 M17"),
            IOStandard("DIFF_POD12"),
            Misc("PRE_EMPHASIS=RDRV_240"),
            Misc("EQUALIZATION=EQ_LEVEL2")),
        Subsignal("dqs_p", Pins("T22 N22 J21 M22 L20 K18 P19 N17"),
            IOStandard("DIFF_POD12"),
            Misc("PRE_EMPHASIS=RDRV_240"),
            Misc("EQUALIZATION=EQ_LEVEL2")),
        Subsignal("odt",     Pins("C16"), IOStandard("SSTL12_DCI")),
        Subsignal("ras_n",   Pins("F15"), IOStandard("SSTL12_DCI")),
        Subsignal("reset_n", Pins("D21"), IOStandard("LVCMOS12")),
        Subsignal("we_n",    Pins("D15"), IOStandard("SSTL12_DCI")),
        Misc("SLEW=FAST")
    ),
]

_connectors = []

# Platform -----------------------------------------------------------------------------------------

class Platform(XilinxPlatform):
    default_clk_name   = "clk300"
    default_clk_period = 1e9/300e6

    def __init__(self):
        XilinxPlatform.__init__(self, "xcvu9p-fsgd2104-2l-e", _io, _connectors, toolchain="vivado")

    def create_programmer(self):
        return VivadoProgrammer()

    def do_finalize(self, fragment):
        XilinxPlatform.do_finalize(self, fragment)
        self.add_period_constraint(self.lookup_request("clk300", 0, loose=True), 1e9/300e6)
        # For passively cooled boards, overheating is a significant risk if airflow isn't sufficient
        self.add_platform_command("set_property BITSTREAM.CONFIG.OVERTEMPSHUTDOWN ENABLE [current_design]")
        # Reduce programming time
        self.add_platform_command("set_property BITSTREAM.GENERAL.COMPRESS TRUE [current_design]")
        # DDR4 memory channel C0 Internal Vref
        self.add_platform_command("set_property INTERNAL_VREF 0.84 [get_iobanks 41]")
        self.add_platform_command("set_property INTERNAL_VREF 0.84 [get_iobanks 42]")
        self.add_platform_command("set_property INTERNAL_VREF 0.84 [get_iobanks 43]")
        # DDR4 memory channel C1 Internal Vref
        self.add_platform_command("set_property INTERNAL_VREF 0.84 [get_iobanks 65]")
        self.add_platform_command("set_property INTERNAL_VREF 0.84 [get_iobanks 66]")
        self.add_platform_command("set_property INTERNAL_VREF 0.84 [get_iobanks 67]")
        # DDR4 memory channel C2 Internal Vref
        self.add_platform_command("set_property INTERNAL_VREF 0.84 [get_iobanks 46]")
        self.add_platform_command("set_property INTERNAL_VREF 0.84 [get_iobanks 47]")
        self.add_platform_command("set_property INTERNAL_VREF 0.84 [get_iobanks 48]")
        # DDR4 memory channel C3 Internal Vref
        self.add_platform_command("set_property INTERNAL_VREF 0.84 [get_iobanks 70]")
        self.add_platform_command("set_property INTERNAL_VREF 0.84 [get_iobanks 71]")
        self.add_platform_command("set_property INTERNAL_VREF 0.84 [get_iobanks 72]")
