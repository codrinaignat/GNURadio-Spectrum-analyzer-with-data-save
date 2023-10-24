#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Receptor/Analizor cu salvare date
# Author: Codrina Lisaru
# GNU Radio version: 3.8.2.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import eng_notation
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio.qtgui import Range, RangeWidget
import osmosdr
import time

from gnuradio import qtgui

class Apl4_Receptor_Analizor_cu_salvare_date_Codrina_Lisaru(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Receptor/Analizor cu salvare date")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Receptor/Analizor cu salvare date")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "Apl4_Receptor_Analizor_cu_salvare_date_Codrina_Lisaru")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.volume = volume = 0.5
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = '1.766 GHz'
        self.variable_qtgui_chooser_0 = variable_qtgui_chooser_0 = 8
        self.step = step = 100
        self.squelch = squelch = -50
        self.samp_rate = samp_rate = 2e6
        self.recordsamprate = recordsamprate = 48000
        self.receiverchooser = receiverchooser = 0
        self.RF_Gain = RF_Gain = 40
        self.Center_frequency = Center_frequency = 126944900
        self.Bandwidth = Bandwidth = 4800

        ##################################################
        # Blocks
        ##################################################
        self._step_range = Range(10, 200000, 1, 100, 200)
        self._step_win = RangeWidget(self._step_range, self.set_step, 'Center freq step size in Hz', "counter_slider", float)
        self.top_grid_layout.addWidget(self._step_win, 1, 2, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._volume_range = Range(0, 1, 0.001, 0.5, 200)
        self._volume_win = RangeWidget(self._volume_range, self.set_volume, 'Volume', "counter_slider", float)
        self.top_grid_layout.addWidget(self._volume_win, 0, 3, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        # Create the options list
        self._variable_qtgui_chooser_0_options = (8, 16, 32, 64, )
        # Create the labels list
        self._variable_qtgui_chooser_0_labels = ('8 bits', '16 bits', '32 bits', '64 bits', )
        # Create the combo box
        self._variable_qtgui_chooser_0_tool_bar = Qt.QToolBar(self)
        self._variable_qtgui_chooser_0_tool_bar.addWidget(Qt.QLabel('Bits per sample - wav file record' + ": "))
        self._variable_qtgui_chooser_0_combo_box = Qt.QComboBox()
        self._variable_qtgui_chooser_0_tool_bar.addWidget(self._variable_qtgui_chooser_0_combo_box)
        for _label in self._variable_qtgui_chooser_0_labels: self._variable_qtgui_chooser_0_combo_box.addItem(_label)
        self._variable_qtgui_chooser_0_callback = lambda i: Qt.QMetaObject.invokeMethod(self._variable_qtgui_chooser_0_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._variable_qtgui_chooser_0_options.index(i)))
        self._variable_qtgui_chooser_0_callback(self.variable_qtgui_chooser_0)
        self._variable_qtgui_chooser_0_combo_box.currentIndexChanged.connect(
            lambda i: self.set_variable_qtgui_chooser_0(self._variable_qtgui_chooser_0_options[i]))
        # Create the radio buttons
        self.top_grid_layout.addWidget(self._variable_qtgui_chooser_0_tool_bar, 1, 4, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.tab_widget = Qt.QTabWidget()
        self.tab_widget_widget_0 = Qt.QWidget()
        self.tab_widget_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_widget_0)
        self.tab_widget_grid_layout_0 = Qt.QGridLayout()
        self.tab_widget_layout_0.addLayout(self.tab_widget_grid_layout_0)
        self.tab_widget.addTab(self.tab_widget_widget_0, 'Spectrum Analyzer without data record')
        self.tab_widget_widget_1 = Qt.QWidget()
        self.tab_widget_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_widget_1)
        self.tab_widget_grid_layout_1 = Qt.QGridLayout()
        self.tab_widget_layout_1.addLayout(self.tab_widget_grid_layout_1)
        self.tab_widget.addTab(self.tab_widget_widget_1, 'Spectrum Analyzer with data record')
        self.tab_widget_widget_2 = Qt.QWidget()
        self.tab_widget_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_widget_2)
        self.tab_widget_grid_layout_2 = Qt.QGridLayout()
        self.tab_widget_layout_2.addLayout(self.tab_widget_grid_layout_2)
        self.tab_widget.addTab(self.tab_widget_widget_2, 'Different type of receiver')
        self.top_grid_layout.addWidget(self.tab_widget, 6, 0, 1, 5)
        for r in range(6, 7):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._squelch_range = Range(-110, 0, 1, -50, 200)
        self._squelch_win = RangeWidget(self._squelch_range, self.set_squelch, 'Squelch [NBFM Use Only]', "counter_slider", float)
        self.top_grid_layout.addWidget(self._squelch_win, 0, 2, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        # Create the options list
        self._recordsamprate_options = (16000, 22050, 32000, 44100, 48000, )
        # Create the labels list
        self._recordsamprate_labels = ('16 kHz', '22.05 kHz', '32 kHz', '44.1 kHz', '48 kHz', )
        # Create the combo box
        self._recordsamprate_tool_bar = Qt.QToolBar(self)
        self._recordsamprate_tool_bar.addWidget(Qt.QLabel('Wav samp rate' + ": "))
        self._recordsamprate_combo_box = Qt.QComboBox()
        self._recordsamprate_tool_bar.addWidget(self._recordsamprate_combo_box)
        for _label in self._recordsamprate_labels: self._recordsamprate_combo_box.addItem(_label)
        self._recordsamprate_callback = lambda i: Qt.QMetaObject.invokeMethod(self._recordsamprate_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._recordsamprate_options.index(i)))
        self._recordsamprate_callback(self.recordsamprate)
        self._recordsamprate_combo_box.currentIndexChanged.connect(
            lambda i: self.set_recordsamprate(self._recordsamprate_options[i]))
        # Create the radio buttons
        self.top_grid_layout.addWidget(self._recordsamprate_tool_bar, 0, 4, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        # Create the options list
        self._receiverchooser_options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # Create the labels list
        self._receiverchooser_labels = ["Spectrum analyzer without data record","Spectrum analyzer with data record","Mono FM Receiver without data record","Mono FM Receiver with data record","Stereo FM Receiver without data record","Stereo FM Receiver with data record","AM receiver without data record","AM receiver with data record","NBFM receiver without data record","NBFM receiver with data record"]
        # Create the combo box
        self._receiverchooser_tool_bar = Qt.QToolBar(self)
        self._receiverchooser_tool_bar.addWidget(Qt.QLabel('Choose Receiver Type' + ": "))
        self._receiverchooser_combo_box = Qt.QComboBox()
        self._receiverchooser_tool_bar.addWidget(self._receiverchooser_combo_box)
        for _label in self._receiverchooser_labels: self._receiverchooser_combo_box.addItem(_label)
        self._receiverchooser_callback = lambda i: Qt.QMetaObject.invokeMethod(self._receiverchooser_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._receiverchooser_options.index(i)))
        self._receiverchooser_callback(self.receiverchooser)
        self._receiverchooser_combo_box.currentIndexChanged.connect(
            lambda i: self.set_receiverchooser(self._receiverchooser_options[i]))
        # Create the radio buttons
        self.top_grid_layout.addWidget(self._receiverchooser_tool_bar, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._RF_Gain_range = Range(0, 50, 0.5, 40, 200)
        self._RF_Gain_win = RangeWidget(self._RF_Gain_range, self.set_RF_Gain, 'RF Gain in dB', "counter_slider", float)
        self.top_grid_layout.addWidget(self._RF_Gain_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._Center_frequency_range = Range(100e3, 6e9, step, 126944900, 200)
        self._Center_frequency_win = RangeWidget(self._Center_frequency_range, self.set_Center_frequency, 'Center frequency in Hz', "counter_slider", float)
        self.top_grid_layout.addWidget(self._Center_frequency_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._Bandwidth_range = Range(1, 100e6, 100, 4800, 200)
        self._Bandwidth_win = RangeWidget(self._Bandwidth_range, self.set_Bandwidth, 'Display bandwidth in Hz', "counter_slider", float)
        self.top_grid_layout.addWidget(self._Bandwidth_win, 1, 3, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._variable_qtgui_label_0_tool_bar = Qt.QToolBar(self)

        if None:
            self._variable_qtgui_label_0_formatter = None
        else:
            self._variable_qtgui_label_0_formatter = lambda x: str(x)

        self._variable_qtgui_label_0_tool_bar.addWidget(Qt.QLabel('Frequency Start for RTL-SDR blue stick is 24 MHz and stop frequency ' + ": "))
        self._variable_qtgui_label_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0)))
        self._variable_qtgui_label_0_tool_bar.addWidget(self._variable_qtgui_label_0_label)
        self.top_grid_layout.addWidget(self._variable_qtgui_label_0_tool_bar, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.rational_resampler_xxx_1_0 = filter.rational_resampler_fff(
                interpolation=48,
                decimation=int(500e3/1e4),
                taps=None,
                fractional_bw=None)
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=48,
                decimation=int(500e3/1e4),
                taps=None,
                fractional_bw=None)
        self.rational_resampler_xxx_0_1_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=int(samp_rate/500e3),
                taps=None,
                fractional_bw=None)
        self.rational_resampler_xxx_0_1 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=int(samp_rate/500e3),
                taps=None,
                fractional_bw=None)
        self.rational_resampler_xxx_0_0_0_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=int(samp_rate/500e3),
                taps=None,
                fractional_bw=None)
        self.rational_resampler_xxx_0_0_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=int(samp_rate/500e3),
                taps=None,
                fractional_bw=None)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=12,
                decimation=50,
                taps=None,
                fractional_bw=None)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=12,
                decimation=50,
                taps=None,
                fractional_bw=None)
        self.qtgui_waterfall_sink_x_1 = qtgui.waterfall_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            Center_frequency, #fc
            Bandwidth, #bw
            "Waterfall (Spectrogram)", #name
            1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_1.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_1.enable_grid(False)
        self.qtgui_waterfall_sink_x_1.enable_axis_labels(True)

        self.qtgui_waterfall_sink_x_1.disable_legend()


        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_1.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_1.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_1.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_1_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_1.pyqwidget(), Qt.QWidget)
        self.tab_widget_grid_layout_2.addWidget(self._qtgui_waterfall_sink_x_1_win, 8, 0, 1, 2)
        for r in range(8, 9):
            self.tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 2):
            self.tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0_0 = qtgui.waterfall_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            Center_frequency, #fc
            Bandwidth, #bw
            "Waterfall (Spectrogram)", #name
            1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_0.enable_axis_labels(True)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.tab_widget_grid_layout_1.addWidget(self._qtgui_waterfall_sink_x_0_0_win, 8, 0, 1, 2)
        for r in range(8, 9):
            self.tab_widget_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 2):
            self.tab_widget_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            Center_frequency, #fc
            Bandwidth, #bw
            "Waterfall (Spectrogram)", #name
            1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)

        self.qtgui_waterfall_sink_x_0.disable_legend()


        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tab_widget_grid_layout_0.addWidget(self._qtgui_waterfall_sink_x_0_win, 8, 0, 1, 2)
        for r in range(8, 9):
            self.tab_widget_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 2):
            self.tab_widget_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_2 = qtgui.time_sink_c(
            1024, #size
            samp_rate, #samp_rate
            "Time domain representation", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_2.set_update_time(0.10)
        self.qtgui_time_sink_x_2.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_2.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_2.enable_tags(True)
        self.qtgui_time_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_2.enable_autoscale(True)
        self.qtgui_time_sink_x_2.enable_grid(False)
        self.qtgui_time_sink_x_2.enable_axis_labels(True)
        self.qtgui_time_sink_x_2.enable_control_panel(False)
        self.qtgui_time_sink_x_2.enable_stem_plot(False)

        self.qtgui_time_sink_x_2.disable_legend()

        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_2.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_2.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_2_win = sip.wrapinstance(self.qtgui_time_sink_x_2.pyqwidget(), Qt.QWidget)
        self.tab_widget_grid_layout_1.addWidget(self._qtgui_time_sink_x_2_win, 9, 0, 1, 2)
        for r in range(9, 10):
            self.tab_widget_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 2):
            self.tab_widget_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_c(
            1024, #size
            samp_rate, #samp_rate
            "Time domain representation", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(True)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)

        self.qtgui_time_sink_x_1.disable_legend()

        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.tab_widget_grid_layout_0.addWidget(self._qtgui_time_sink_x_1_win, 9, 0, 1, 2)
        for r in range(9, 10):
            self.tab_widget_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 2):
            self.tab_widget_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
            1024, #size
            samp_rate, #samp_rate
            "Time domain representation", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        self.qtgui_time_sink_x_0.disable_legend()

        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tab_widget_grid_layout_2.addWidget(self._qtgui_time_sink_x_0_win, 9, 0, 1, 2)
        for r in range(9, 10):
            self.tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 2):
            self.tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_2 = qtgui.freq_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            Center_frequency, #fc
            Bandwidth, #bw
            "Real time spectrum", #name
            1
        )
        self.qtgui_freq_sink_x_2.set_update_time(0.01)
        self.qtgui_freq_sink_x_2.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_2.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_2.enable_autoscale(True)
        self.qtgui_freq_sink_x_2.enable_grid(False)
        self.qtgui_freq_sink_x_2.set_fft_average(0.05)
        self.qtgui_freq_sink_x_2.enable_axis_labels(True)
        self.qtgui_freq_sink_x_2.enable_control_panel(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_2.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_2_win = sip.wrapinstance(self.qtgui_freq_sink_x_2.pyqwidget(), Qt.QWidget)
        self.tab_widget_grid_layout_2.addWidget(self._qtgui_freq_sink_x_2_win, 7, 0, 1, 2)
        for r in range(7, 8):
            self.tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 2):
            self.tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            Center_frequency, #fc
            Bandwidth, #bw
            "Real time spectrum", #name
            1
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(True)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(0.05)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)

        self.qtgui_freq_sink_x_1.disable_legend()


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.tab_widget_grid_layout_1.addWidget(self._qtgui_freq_sink_x_1_win, 7, 0, 1, 2)
        for r in range(7, 8):
            self.tab_widget_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 2):
            self.tab_widget_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            Center_frequency, #fc
            Bandwidth, #bw
            "Real time spectrum", #name
            1
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        self.qtgui_freq_sink_x_0.disable_legend()


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tab_widget_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_win, 7, 0, 1, 2)
        for r in range(7, 8):
            self.tab_widget_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 2):
            self.tab_widget_grid_layout_0.setColumnStretch(c, 1)
        self.osmosdr_source_0 = osmosdr.source(
            args="numchan=" + str(1) + " " + ""
        )
        self.osmosdr_source_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(Center_frequency, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(RF_Gain, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
        self.low_pass_filter_0_1_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                100e3,
                1e6,
                firdes.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_1 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                100e3,
                1e6,
                firdes.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_0_1 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                100e3,
                1e6,
                firdes.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_0_0_1 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                100e3,
                1e6,
                firdes.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_0_0_0 = filter.fir_filter_ccf(
            10,
            firdes.low_pass(
                1,
                samp_rate,
                10000,
                5000,
                firdes.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_0_0 = filter.fir_filter_ccf(
            10,
            firdes.low_pass(
                1,
                samp_rate,
                10000,
                5000,
                firdes.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(
            10,
            firdes.low_pass(
                10,
                samp_rate,
                5000,
                7500,
                firdes.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            10,
            firdes.low_pass(
                10,
                samp_rate,
                5000,
                7500,
                firdes.WIN_HAMMING,
                6.76))
        self.blocks_wavfile_sink_1_0 = blocks.wavfile_sink('M:\\OneDrive\\02_Master\\2_2\\02_Disertatie\\GNU Radio implementation\\Aplicatia 4 - Receptor_Analizor cu salvare de date\\StereoRecorder.wav', 2, recordsamprate, variable_qtgui_chooser_0)
        self.blocks_wavfile_sink_1 = blocks.wavfile_sink('M:\\OneDrive\\02_Master\\2_2\\02_Disertatie\\GNU Radio implementation\\Aplicatia 4 - Receptor_Analizor cu salvare de date\\SpectrumAnalyzerData.wav', 2, recordsamprate, variable_qtgui_chooser_0)
        self.blocks_wavfile_sink_0_0_0 = blocks.wavfile_sink('M:\\OneDrive\\02_Master\\2_2\\02_Disertatie\\GNU Radio implementation\\Aplicatia 4 - Receptor_Analizor cu salvare de date\\MonoRecorder.wav', 1, recordsamprate, variable_qtgui_chooser_0)
        self.blocks_wavfile_sink_0_0 = blocks.wavfile_sink('M:\\OneDrive\\02_Master\\2_2\\02_Disertatie\\GNU Radio implementation\\Aplicatia 4 - Receptor_Analizor cu salvare de date\\NBFMRecordedData.wav', 1, recordsamprate, variable_qtgui_chooser_0)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink('M:\\OneDrive\\02_Master\\2_2\\02_Disertatie\\GNU Radio implementation\\Aplicatia 4 - Receptor_Analizor cu salvare de date\\AMRecordedData.wav', 1, recordsamprate, variable_qtgui_chooser_0)
        self.blocks_selector_0 = blocks.selector(gr.sizeof_gr_complex*1,0,receiverchooser)
        self.blocks_selector_0.set_enabled(True)
        self.blocks_multiply_const_vxx_0_1_0 = blocks.multiply_const_ff(volume)
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_ff(volume)
        self.blocks_multiply_const_vxx_0_0_1_0 = blocks.multiply_const_ff(volume)
        self.blocks_multiply_const_vxx_0_0_1 = blocks.multiply_const_ff(volume)
        self.blocks_multiply_const_vxx_0_0_0_1 = blocks.multiply_const_ff(volume)
        self.blocks_multiply_const_vxx_0_0_0_0_0 = blocks.multiply_const_ff(volume)
        self.blocks_multiply_const_vxx_0_0_0_0 = blocks.multiply_const_ff(volume)
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_ff(volume)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_ff(volume)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(volume)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, 'M:\\OneDrive\\02_Master\\2_2\\02_Disertatie\\GNU Radio implementation\\Aplicatia 4 - Receptor_Analizor cu salvare de date\\filename', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_mag_0_0 = blocks.complex_to_mag(1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.audio_sink_0_1_0 = audio.sink(48000, '', True)
        self.audio_sink_0_1 = audio.sink(48000, '', True)
        self.audio_sink_0_0_1 = audio.sink(48000, '', True)
        self.audio_sink_0_0_0_1 = audio.sink(48000, '', True)
        self.audio_sink_0_0_0_0 = audio.sink(48000, '', True)
        self.audio_sink_0_0_0 = audio.sink(48000, '', True)
        self.audio_sink_0_0 = audio.sink(48000, '', True)
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_wfm_rcv_pll_0_0 = analog.wfm_rcv_pll(
        	demod_rate=500e3,
        	audio_decimation=10,
        )
        self.analog_wfm_rcv_pll_0 = analog.wfm_rcv_pll(
        	demod_rate=500e3,
        	audio_decimation=10,
        )
        self.analog_wfm_rcv_0_0 = analog.wfm_rcv(
        	quad_rate=500e3,
        	audio_decimation=10,
        )
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=500e3,
        	audio_decimation=10,
        )
        self.analog_simple_squelch_cc_0_0 = analog.simple_squelch_cc(squelch, 1)
        self.analog_simple_squelch_cc_0 = analog.simple_squelch_cc(squelch, 1)
        self.analog_nbfm_rx_0_0 = analog.nbfm_rx(
        	audio_rate=48000,
        	quad_rate=192000,
        	tau=75e-6,
        	max_dev=5e3,
          )
        self.analog_nbfm_rx_0 = analog.nbfm_rx(
        	audio_rate=48000,
        	quad_rate=192000,
        	tau=75e-6,
        	max_dev=5e3,
          )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_rx_0, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))
        self.connect((self.analog_nbfm_rx_0_0, 0), (self.blocks_multiply_const_vxx_0_0_0_0, 0))
        self.connect((self.analog_simple_squelch_cc_0, 0), (self.analog_nbfm_rx_0, 0))
        self.connect((self.analog_simple_squelch_cc_0_0, 0), (self.analog_nbfm_rx_0_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.analog_wfm_rcv_0_0, 0), (self.rational_resampler_xxx_1_0, 0))
        self.connect((self.analog_wfm_rcv_pll_0, 1), (self.blocks_multiply_const_vxx_0_0_0_1, 0))
        self.connect((self.analog_wfm_rcv_pll_0, 0), (self.blocks_multiply_const_vxx_0_0_1, 0))
        self.connect((self.analog_wfm_rcv_pll_0_0, 1), (self.blocks_multiply_const_vxx_0_0_0_0_0, 0))
        self.connect((self.analog_wfm_rcv_pll_0_0, 0), (self.blocks_multiply_const_vxx_0_0_1_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_wavfile_sink_1, 1))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_wavfile_sink_1, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_complex_to_mag_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.audio_sink_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_wavfile_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.audio_sink_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_0_0, 0), (self.audio_sink_0_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_0_0, 0), (self.blocks_wavfile_sink_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_0_0_0, 0), (self.audio_sink_0_0_1, 1))
        self.connect((self.blocks_multiply_const_vxx_0_0_0_0_0, 0), (self.blocks_wavfile_sink_1_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0_0_0_1, 0), (self.audio_sink_0_0_0_1, 1))
        self.connect((self.blocks_multiply_const_vxx_0_0_1, 0), (self.audio_sink_0_0_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_1_0, 0), (self.audio_sink_0_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_1_0, 0), (self.blocks_wavfile_sink_1_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.audio_sink_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1_0, 0), (self.audio_sink_0_1_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1_0, 0), (self.blocks_wavfile_sink_0_0_0, 0))
        self.connect((self.blocks_selector_0, 1), (self.blocks_complex_to_float_0, 0))
        self.connect((self.blocks_selector_0, 1), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_selector_0, 6), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_selector_0, 7), (self.low_pass_filter_0_0, 0))
        self.connect((self.blocks_selector_0, 8), (self.low_pass_filter_0_0_0, 0))
        self.connect((self.blocks_selector_0, 9), (self.low_pass_filter_0_0_0_0, 0))
        self.connect((self.blocks_selector_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_selector_0, 1), (self.qtgui_freq_sink_x_1, 0))
        self.connect((self.blocks_selector_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_selector_0, 1), (self.qtgui_time_sink_x_2, 0))
        self.connect((self.blocks_selector_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.blocks_selector_0, 1), (self.qtgui_waterfall_sink_x_0_0, 0))
        self.connect((self.blocks_selector_0, 4), (self.rational_resampler_xxx_0_0_0, 0))
        self.connect((self.blocks_selector_0, 5), (self.rational_resampler_xxx_0_0_0_0, 0))
        self.connect((self.blocks_selector_0, 2), (self.rational_resampler_xxx_0_1, 0))
        self.connect((self.blocks_selector_0, 3), (self.rational_resampler_xxx_0_1_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.low_pass_filter_0_0_0, 0), (self.analog_simple_squelch_cc_0, 0))
        self.connect((self.low_pass_filter_0_0_0_0, 0), (self.analog_simple_squelch_cc_0_0, 0))
        self.connect((self.low_pass_filter_0_0_0_1, 0), (self.analog_wfm_rcv_pll_0_0, 0))
        self.connect((self.low_pass_filter_0_0_1, 0), (self.analog_wfm_rcv_pll_0, 0))
        self.connect((self.low_pass_filter_0_1, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.low_pass_filter_0_1_0, 0), (self.analog_wfm_rcv_0_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_selector_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.qtgui_freq_sink_x_2, 0))
        self.connect((self.osmosdr_source_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.qtgui_waterfall_sink_x_1, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_complex_to_mag_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0, 0), (self.low_pass_filter_0_0_1, 0))
        self.connect((self.rational_resampler_xxx_0_0_0_0, 0), (self.low_pass_filter_0_0_0_1, 0))
        self.connect((self.rational_resampler_xxx_0_1, 0), (self.low_pass_filter_0_1, 0))
        self.connect((self.rational_resampler_xxx_0_1_0, 0), (self.low_pass_filter_0_1_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_multiply_const_vxx_0_1, 0))
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.blocks_multiply_const_vxx_0_1_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Apl4_Receptor_Analizor_cu_salvare_date_Codrina_Lisaru")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self.blocks_multiply_const_vxx_0.set_k(self.volume)
        self.blocks_multiply_const_vxx_0_0.set_k(self.volume)
        self.blocks_multiply_const_vxx_0_0_0.set_k(self.volume)
        self.blocks_multiply_const_vxx_0_0_0_0.set_k(self.volume)
        self.blocks_multiply_const_vxx_0_0_0_0_0.set_k(self.volume)
        self.blocks_multiply_const_vxx_0_0_0_1.set_k(self.volume)
        self.blocks_multiply_const_vxx_0_0_1.set_k(self.volume)
        self.blocks_multiply_const_vxx_0_0_1_0.set_k(self.volume)
        self.blocks_multiply_const_vxx_0_1.set_k(self.volume)
        self.blocks_multiply_const_vxx_0_1_0.set_k(self.volume)

    def get_variable_qtgui_label_0(self):
        return self.variable_qtgui_label_0

    def set_variable_qtgui_label_0(self, variable_qtgui_label_0):
        self.variable_qtgui_label_0 = variable_qtgui_label_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0))

    def get_variable_qtgui_chooser_0(self):
        return self.variable_qtgui_chooser_0

    def set_variable_qtgui_chooser_0(self, variable_qtgui_chooser_0):
        self.variable_qtgui_chooser_0 = variable_qtgui_chooser_0
        self._variable_qtgui_chooser_0_callback(self.variable_qtgui_chooser_0)

    def get_step(self):
        return self.step

    def set_step(self, step):
        self.step = step

    def get_squelch(self):
        return self.squelch

    def set_squelch(self, squelch):
        self.squelch = squelch
        self.analog_simple_squelch_cc_0.set_threshold(self.squelch)
        self.analog_simple_squelch_cc_0_0.set_threshold(self.squelch)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(10, self.samp_rate, 5000, 7500, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(10, self.samp_rate, 5000, 7500, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 10000, 5000, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 10000, 5000, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0_0_1.set_taps(firdes.low_pass(1, self.samp_rate, 100e3, 1e6, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0_1.set_taps(firdes.low_pass(1, self.samp_rate, 100e3, 1e6, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(1, self.samp_rate, 100e3, 1e6, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_0.set_taps(firdes.low_pass(1, self.samp_rate, 100e3, 1e6, firdes.WIN_HAMMING, 6.76))
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_2.set_samp_rate(self.samp_rate)

    def get_recordsamprate(self):
        return self.recordsamprate

    def set_recordsamprate(self, recordsamprate):
        self.recordsamprate = recordsamprate
        self._recordsamprate_callback(self.recordsamprate)

    def get_receiverchooser(self):
        return self.receiverchooser

    def set_receiverchooser(self, receiverchooser):
        self.receiverchooser = receiverchooser
        self._receiverchooser_callback(self.receiverchooser)
        self.blocks_selector_0.set_output_index(self.receiverchooser)

    def get_RF_Gain(self):
        return self.RF_Gain

    def set_RF_Gain(self, RF_Gain):
        self.RF_Gain = RF_Gain
        self.osmosdr_source_0.set_gain(self.RF_Gain, 0)

    def get_Center_frequency(self):
        return self.Center_frequency

    def set_Center_frequency(self, Center_frequency):
        self.Center_frequency = Center_frequency
        self.osmosdr_source_0.set_center_freq(self.Center_frequency, 0)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.Center_frequency, self.Bandwidth)
        self.qtgui_freq_sink_x_1.set_frequency_range(self.Center_frequency, self.Bandwidth)
        self.qtgui_freq_sink_x_2.set_frequency_range(self.Center_frequency, self.Bandwidth)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.Center_frequency, self.Bandwidth)
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.Center_frequency, self.Bandwidth)
        self.qtgui_waterfall_sink_x_1.set_frequency_range(self.Center_frequency, self.Bandwidth)

    def get_Bandwidth(self):
        return self.Bandwidth

    def set_Bandwidth(self, Bandwidth):
        self.Bandwidth = Bandwidth
        self.qtgui_freq_sink_x_0.set_frequency_range(self.Center_frequency, self.Bandwidth)
        self.qtgui_freq_sink_x_1.set_frequency_range(self.Center_frequency, self.Bandwidth)
        self.qtgui_freq_sink_x_2.set_frequency_range(self.Center_frequency, self.Bandwidth)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.Center_frequency, self.Bandwidth)
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.Center_frequency, self.Bandwidth)
        self.qtgui_waterfall_sink_x_1.set_frequency_range(self.Center_frequency, self.Bandwidth)





def main(top_block_cls=Apl4_Receptor_Analizor_cu_salvare_date_Codrina_Lisaru, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
