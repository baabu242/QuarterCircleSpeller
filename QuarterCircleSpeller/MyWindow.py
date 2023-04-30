from qc import Ui_MainWindow
import sys, time
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer
from pylsl import resolve_stream, StreamInlet


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load()
        self.stage1()
        self.cursor = self.ui.textEdit.textCursor()
        self.ui.right_button.clicked.connect(self.onRight)
        self.ui.left_button.clicked.connect(self.onLeft)
        self.file = open("File.txt", "a")

        self.left_count = 0
        self.right_count = 0
        self.currtime = time.time()
        self.stream = resolve_stream('type', 'Predictions')
        self.inlet = StreamInlet(self.stream[0])

    def stage1(self):
        self.ui.qc1.setVisible(True)
        self.ui.qc2.setVisible(True)
        self.ui.qc3.setVisible(True)
        self.ui.qc4.setVisible(True)
        self.ui.up_pointer.setVisible(True)

        self.ui.qc1.setEnabled(True)
        self.ui.qc2.setEnabled(False)
        self.ui.qc3.setEnabled(False)
        self.ui.qc4.setEnabled(False)

    def stage21(self):
        self.ui.qc11.setVisible(True)
        self.ui.qc12.setVisible(True)
        self.ui.qc13.setVisible(True)
        self.ui.back.setVisible(True)
        self.ui.up_pointer.setVisible(True)

        self.ui.qc11.setEnabled(True)
        self.ui.qc12.setEnabled(False)
        self.ui.qc13.setEnabled(False)
        self.ui.back.setEnabled(False)

    def stage22(self):
        self.ui.qc21.setVisible(True)
        self.ui.qc22.setVisible(True)
        self.ui.qc23.setVisible(True)
        self.ui.back.setVisible(True)
        self.ui.up_pointer.setVisible(True)

        self.ui.qc21.setEnabled(True)
        self.ui.qc22.setEnabled(False)
        self.ui.qc23.setEnabled(False)
        self.ui.back.setEnabled(False)

    def stage23(self):
        self.ui.qc31.setVisible(True)
        self.ui.qc32.setVisible(True)
        self.ui.qc33.setVisible(True)
        self.ui.back.setVisible(True)
        self.ui.up_pointer.setVisible(True)

        self.ui.qc31.setEnabled(True)
        self.ui.qc32.setEnabled(False)
        self.ui.qc33.setEnabled(False)
        self.ui.back.setEnabled(False)

    def stage24(self):
        self.ui.qc41.setVisible(True)
        self.ui.qc42.setVisible(True)
        self.ui.qc43.setVisible(True)
        self.ui.back.setVisible(True)
        self.ui.up_pointer.setVisible(True)

        self.ui.qc41.setEnabled(True)
        self.ui.qc42.setEnabled(False)
        self.ui.qc43.setEnabled(False)
        self.ui.back.setEnabled(False)

    def load(self):
        self.ui.up_pointer.setVisible(False)
        self.ui.left_pointer.setVisible(False)
        self.ui.right_pointer.setVisible(False)
        self.ui.down_pointer.setVisible(False)
        self.ui.qc1.setVisible(False)
        self.ui.qc2.setVisible(False)
        self.ui.qc3.setVisible(False)
        self.ui.qc4.setVisible(False)

        self.ui.qc1.setEnabled(False)
        self.ui.qc2.setEnabled(False)
        self.ui.qc3.setEnabled(False)
        self.ui.qc4.setEnabled(False)
        
        self.ui.qc11.setVisible(False)
        self.ui.qc21.setVisible(False)
        self.ui.qc31.setVisible(False)
        self.ui.qc41.setVisible(False)
        self.ui.qc12.setVisible(False)
        self.ui.qc22.setVisible(False)
        self.ui.qc32.setVisible(False)
        self.ui.qc42.setVisible(False)
        self.ui.qc13.setVisible(False)
        self.ui.qc23.setVisible(False)
        self.ui.qc33.setVisible(False)
        self.ui.qc43.setVisible(False)
        self.ui.back.setVisible(False)

        self.ui.qc11.setEnabled(False)
        self.ui.qc21.setEnabled(False)
        self.ui.qc31.setEnabled(False)
        self.ui.qc41.setEnabled(False)
        self.ui.qc12.setEnabled(False)
        self.ui.qc22.setEnabled(False)
        self.ui.qc32.setEnabled(False)
        self.ui.qc42.setEnabled(False)
        self.ui.qc13.setEnabled(False)
        self.ui.qc23.setEnabled(False)
        self.ui.qc33.setEnabled(False)
        self.ui.qc43.setEnabled(False)
        self.ui.back.setEnabled(False)

        self.ui.a.setVisible(False)
        self.ui.b.setVisible(False)
        self.ui.c.setVisible(False)
        self.ui.d.setVisible(False)
        self.ui.e.setVisible(False)
        self.ui.f.setVisible(False)
        self.ui.g.setVisible(False)
        self.ui.h.setVisible(False)
        self.ui.i.setVisible(False)
        self.ui.j.setVisible(False)
        self.ui.k.setVisible(False)
        self.ui.l.setVisible(False)
        self.ui.m.setVisible(False)
        self.ui.n.setVisible(False)
        self.ui.o.setVisible(False)
        self.ui.p.setVisible(False)
        self.ui.q.setVisible(False)
        self.ui.r.setVisible(False)
        self.ui.s.setVisible(False)
        self.ui.t.setVisible(False)
        self.ui.u.setVisible(False)
        self.ui.v.setVisible(False)
        self.ui.w.setVisible(False)
        self.ui.x.setVisible(False)
        self.ui.y.setVisible(False)
        self.ui.z.setVisible(False)

        self.ui.a.setEnabled(False)
        self.ui.b.setEnabled(False)
        self.ui.c.setEnabled(False)
        self.ui.d.setEnabled(False)
        self.ui.e.setEnabled(False)
        self.ui.f.setEnabled(False)
        self.ui.g.setEnabled(False)
        self.ui.h.setEnabled(False)
        self.ui.i.setEnabled(False)
        self.ui.j.setEnabled(False)
        self.ui.k.setEnabled(False)
        self.ui.l.setEnabled(False)
        self.ui.m.setEnabled(False)
        self.ui.n.setEnabled(False)
        self.ui.o.setEnabled(False)
        self.ui.p.setEnabled(False)
        self.ui.q.setEnabled(False)
        self.ui.r.setEnabled(False)
        self.ui.s.setEnabled(False)
        self.ui.t.setEnabled(False)
        self.ui.u.setEnabled(False)
        self.ui.v.setEnabled(False)
        self.ui.w.setEnabled(False)
        self.ui.x.setEnabled(False)
        self.ui.y.setEnabled(False)
        self.ui.z.setEnabled(False)

        self.ui.exit.setVisible(False)
        self.ui.qsn.setVisible(False)
        self.ui.comma.setVisible(False)
        self.ui.dot.setVisible(False)
        self.ui.backspace.setVisible(False)
        self.ui.space.setVisible(False)
        self.ui.left.setVisible(False)
        self.ui.left_left.setVisible(False)
        self.ui.right.setVisible(False)
        self.ui.right_right.setVisible(False)

        self.ui.exit.setEnabled(False)
        self.ui.qsn.setEnabled(False)
        self.ui.comma.setEnabled(False)
        self.ui.dot.setEnabled(False)
        self.ui.backspace.setEnabled(False)
        self.ui.space.setEnabled(False)
        self.ui.left.setEnabled(False)
        self.ui.left_left.setEnabled(False)
        self.ui.right.setEnabled(False)
        self.ui.right_right.setEnabled(False)

    def onRight(self):
        # Stage 1
        if self.ui.qc1.isEnabled():
            self.ui.qc1.setEnabled(False)
            self.ui.qc2.setEnabled(True)
            self.ui.up_pointer.setVisible(False)
            self.ui.right_pointer.setVisible(True)
        elif self.ui.qc2.isEnabled():
            self.ui.qc2.setEnabled(False)
            self.ui.qc3.setEnabled(True)
            self.ui.right_pointer.setVisible(False)
            self.ui.down_pointer.setVisible(True)
        elif self.ui.qc3.isEnabled():
            self.ui.qc3.setEnabled(False)
            self.ui.qc4.setEnabled(True)
            self.ui.down_pointer.setVisible(False)
            self.ui.left_pointer.setVisible(True)

        elif self.ui.qc4.isEnabled():
            self.ui.qc4.setEnabled(False)
            self.ui.qc1.setEnabled(True)
            self.ui.left_pointer.setVisible(False)
            self.ui.up_pointer.setVisible(True)

        # Stage 2 [SPACE, E, A, R, I, O, T, N, U]
        elif self.ui.qc11.isEnabled():
            self.ui.qc11.setEnabled(False)
            self.ui.qc12.setEnabled(True)
            self.ui.up_pointer.setVisible(False)
            self.ui.right_pointer.setVisible(True)
        elif self.ui.qc12.isEnabled():
            self.ui.qc12.setEnabled(False)
            self.ui.qc13.setEnabled(True)
            self.ui.right_pointer.setVisible(False)
            self.ui.down_pointer.setVisible(True)
        elif self.ui.qc13.isEnabled():
            self.ui.qc13.setEnabled(False)
            self.ui.back.setEnabled(True)
            self.ui.down_pointer.setVisible(False)
            self.ui.left_pointer.setVisible(True)

        # Stage 2 [S, L, C, P, M, H, D, X, V]
        elif self.ui.qc21.isEnabled():
            self.ui.qc21.setEnabled(False)
            self.ui.qc22.setEnabled(True)
            self.ui.up_pointer.setVisible(False)
            self.ui.right_pointer.setVisible(True)
        elif self.ui.qc22.isEnabled():
            self.ui.qc22.setEnabled(False)
            self.ui.qc23.setEnabled(True)
            self.ui.right_pointer.setVisible(False)
            self.ui.down_pointer.setVisible(True)
        elif self.ui.qc23.isEnabled():
            self.ui.qc23.setEnabled(False)
            self.ui.back.setEnabled(True)
            self.ui.down_pointer.setVisible(False)
            self.ui.left_pointer.setVisible(True)

        # Stage 2 [F, B, G, K, W, Y, Q, J, Z]
        elif self.ui.qc31.isEnabled():
            self.ui.qc31.setEnabled(False)
            self.ui.qc32.setEnabled(True)
            self.ui.up_pointer.setVisible(False)
            self.ui.right_pointer.setVisible(True)
        elif self.ui.qc32.isEnabled():
            self.ui.qc32.setEnabled(False)
            self.ui.qc33.setEnabled(True)
            self.ui.right_pointer.setVisible(False)
            self.ui.down_pointer.setVisible(True)
        elif self.ui.qc33.isEnabled():
            self.ui.qc33.setEnabled(False)
            self.ui.back.setEnabled(True)
            self.ui.down_pointer.setVisible(False)
            self.ui.left_pointer.setVisible(True)

        # Stage [Qsn, Dot, Backspace, Comma, left, Right, Left-Left, Right-Right, Exit]
        elif self.ui.qc41.isEnabled():
            self.ui.qc41.setEnabled(False)
            self.ui.qc42.setEnabled(True)
            self.ui.up_pointer.setVisible(False)
            self.ui.right_pointer.setVisible(True)
        elif self.ui.qc42.isEnabled():
            self.ui.qc42.setEnabled(False)
            self.ui.qc43.setEnabled(True)
            self.ui.right_pointer.setVisible(False)
            self.ui.down_pointer.setVisible(True)
        elif self.ui.qc43.isEnabled():
            self.ui.qc43.setEnabled(False)
            self.ui.back.setEnabled(True)
            self.ui.down_pointer.setVisible(False)
            self.ui.left_pointer.setVisible(True)

        # Stage 3
        elif self.ui.space.isEnabled():
            self.ui.space.setEnabled(False)
            self.ui.e.setEnabled(True)
            self.ui.up_pointer.setVisible(False)
            self.ui.right_pointer.setVisible(True)
        elif self.ui.e.isEnabled():
            self.ui.e.setEnabled(False)
            self.ui.a.setEnabled(True)
            self.ui.right_pointer.setVisible(False)
            self.ui.down_pointer.setVisible(True)
        elif self.ui.a.isEnabled():
            self.ui.a.setEnabled(False)
            self.ui.back.setEnabled(True)
            self.ui.down_pointer.setVisible(False)
            self.ui.left_pointer.setVisible(True)

        elif self.ui.r.isEnabled():
            self.ui.r.setEnabled(False)
            self.ui.i.setEnabled(True)
            self.ui.up_pointer.setVisible(False)
            self.ui.right_pointer.setVisible(True)
        elif self.ui.i.isEnabled():
            self.ui.i.setEnabled(False)
            self.ui.o.setEnabled(True)
            self.ui.right_pointer.setVisible(False)
            self.ui.down_pointer.setVisible(True)
        elif self.ui.o.isEnabled():
            self.ui.o.setEnabled(False)
            self.ui.back.setEnabled(True)
            self.ui.down_pointer.setVisible(False)
            self.ui.left_pointer.setVisible(True)

        elif self.ui.t.isEnabled():
            self.ui.t.setEnabled(False)
            self.ui.n.setEnabled(True)
            self.ui.up_pointer.setVisible(False)
            self.ui.right_pointer.setVisible(True)
        elif self.ui.n.isEnabled():
            self.ui.n.setEnabled(False)
            self.ui.u.setEnabled(True)
            self.ui.right_pointer.setVisible(False)
            self.ui.down_pointer.setVisible(True)
        elif self.ui.u.isEnabled():
            self.ui.u.setEnabled(False)
            self.ui.back.setEnabled(True)
            self.ui.down_pointer.setVisible(False)
            self.ui.left_pointer.setVisible(True)

        elif self.ui.s.isEnabled():
            self.ui.s.setEnabled(False)
            self.ui.l.setEnabled(True)
            self.ui.up_pointer.setVisible(False)
            self.ui.right_pointer.setVisible(True)
        elif self.ui.l.isEnabled():
            self.ui.l.setEnabled(False)
            self.ui.c.setEnabled(True)
            self.ui.right_pointer.setVisible(False)
            self.ui.down_pointer.setVisible(True)
        elif self.ui.c.isEnabled():
            self.ui.c.setEnabled(False)
            self.ui.back.setEnabled(True)
            self.ui.down_pointer.setVisible(False)
            self.ui.left_pointer.setVisible(True)

        elif self.ui.p.isEnabled():
            self.ui.p.setEnabled(False)
            self.ui.m.setEnabled(True)
            self.ui.up_pointer.setVisible(False)
            self.ui.right_pointer.setVisible(True)
        elif self.ui.m.isEnabled():
            self.ui.m.setEnabled(False)
            self.ui.h.setEnabled(True)
            self.ui.right_pointer.setVisible(False)
            self.ui.down_pointer.setVisible(True)
        elif self.ui.h.isEnabled():
            self.ui.h.setEnabled(False)
            self.ui.back.setEnabled(True)
            self.ui.down_pointer.setVisible(False)
            self.ui.left_pointer.setVisible(True)

        elif self.ui.d.isEnabled():
            self.ui.d.setEnabled(False)
            self.ui.x.setEnabled(True)
            self.ui.up_pointer.setVisible(False)
            self.ui.right_pointer.setVisible(True)
        elif self.ui.x.isEnabled():
            self.ui.x.setEnabled(False)
            self.ui.v.setEnabled(True)
            self.ui.right_pointer.setVisible(False)
            self.ui.down_pointer.setVisible(True)
        elif self.ui.v.isEnabled():
            self.ui.v.setEnabled(False)
            self.ui.back.setEnabled(True)
            self.ui.down_pointer.setVisible(False)
            self.ui.left_pointer.setVisible(True)

        elif self.ui.g.isEnabled():
            self.ui.g.setEnabled(False)
            self.ui.b.setEnabled(True)
            self.ui.up_pointer.setVisible(False)
            self.ui.right_pointer.setVisible(True)
        elif self.ui.b.isEnabled():
            self.ui.b.setEnabled(False)
            self.ui.f.setEnabled(True)
            self.ui.right_pointer.setVisible(False)
            self.ui.down_pointer.setVisible(True)
        elif self.ui.f.isEnabled():
            self.ui.f.setEnabled(False)
            self.ui.back.setEnabled(True)
            self.ui.down_pointer.setVisible(False)
            self.ui.left_pointer.setVisible(True)

        elif self.ui.y.isEnabled():
            self.ui.y.setEnabled(False)
            self.ui.w.setEnabled(True)
            self.ui.up_pointer.setVisible(False)
            self.ui.right_pointer.setVisible(True)
        elif self.ui.w.isEnabled():
            self.ui.w.setEnabled(False)
            self.ui.k.setEnabled(True)
            self.ui.right_pointer.setVisible(False)
            self.ui.down_pointer.setVisible(True)
        elif self.ui.k.isEnabled():
            self.ui.k.setEnabled(False)
            self.ui.back.setEnabled(True)
            self.ui.down_pointer.setVisible(False)
            self.ui.left_pointer.setVisible(True)

        elif self.ui.z.isEnabled():
            self.ui.z.setEnabled(False)
            self.ui.j.setEnabled(True)
            self.ui.up_pointer.setVisible(False)
            self.ui.right_pointer.setVisible(True)
        elif self.ui.j.isEnabled():
            self.ui.j.setEnabled(False)
            self.ui.q.setEnabled(True)
            self.ui.right_pointer.setVisible(False)
            self.ui.down_pointer.setVisible(True)
        elif self.ui.q.isEnabled():
            self.ui.q.setEnabled(False)
            self.ui.back.setEnabled(True)
            self.ui.down_pointer.setVisible(False)
            self.ui.left_pointer.setVisible(True)

        elif self.ui.backspace.isEnabled():
            self.ui.backspace.setEnabled(False)
            self.ui.dot.setEnabled(True)
            self.ui.up_pointer.setVisible(False)
            self.ui.right_pointer.setVisible(True)
        elif self.ui.dot.isEnabled():
            self.ui.dot.setEnabled(False)
            self.ui.qsn.setEnabled(True)
            self.ui.right_pointer.setVisible(False)
            self.ui.down_pointer.setVisible(True)
        elif self.ui.qsn.isEnabled():
            self.ui.qsn.setEnabled(False)
            self.ui.back.setEnabled(True)
            self.ui.down_pointer.setVisible(False)
            self.ui.left_pointer.setVisible(True)

        elif self.ui.left.isEnabled():
            self.ui.left.setEnabled(False)
            self.ui.right.setEnabled(True)
            self.ui.up_pointer.setVisible(False)
            self.ui.right_pointer.setVisible(True)
        elif self.ui.right.isEnabled():
            self.ui.right.setEnabled(False)
            self.ui.comma.setEnabled(True)
            self.ui.right_pointer.setVisible(False)
            self.ui.down_pointer.setVisible(True)
        elif self.ui.comma.isEnabled():
            self.ui.comma.setEnabled(False)
            self.ui.back.setEnabled(True)
            self.ui.down_pointer.setVisible(False)
            self.ui.left_pointer.setVisible(True)

        elif self.ui.left_left.isEnabled():
            self.ui.left_left.setEnabled(False)
            self.ui.right_right.setEnabled(True)
            self.ui.up_pointer.setVisible(False)
            self.ui.right_pointer.setVisible(True)
        elif self.ui.right_right.isEnabled():
            self.ui.right_right.setEnabled(False)
            self.ui.exit.setEnabled(True)
            self.ui.right_pointer.setVisible(False)
            self.ui.down_pointer.setVisible(True)
        elif self.ui.exit.isEnabled():
            self.ui.exit.setEnabled(False)
            self.ui.back.setEnabled(True)
            self.ui.down_pointer.setVisible(False)
            self.ui.left_pointer.setVisible(True)

        elif self.ui.back.isEnabled():
            if self.ui.qc11.isVisible():
                self.load()
                self.stage21()

            elif self.ui.qc21.isVisible():
                self.load()
                self.stage22()

            elif self.ui.qc31.isVisible():
                self.load()
                self.stage23()

            elif self.ui.qc41.isVisible():
                self.load()
                self.stage24()

            elif self.ui.space.isVisible():
                self.load()
                self.ui.space.setVisible(True)
                self.ui.e.setVisible(True)
                self.ui.a.setVisible(True)
                self.ui.back.setVisible(True)
                self.ui.up_pointer.setVisible(True)

                self.ui.space.setEnabled(True)
                self.ui.e.setEnabled(False)
                self.ui.a.setEnabled(False)
                self.ui.back.setEnabled(False)

            elif self.ui.r.isVisible():
                self.load()
                self.ui.r.setVisible(True)
                self.ui.i.setVisible(True)
                self.ui.o.setVisible(True)
                self.ui.back.setVisible(True)
                self.ui.up_pointer.setVisible(True)

                self.ui.r.setEnabled(True)
                self.ui.i.setEnabled(False)
                self.ui.o.setEnabled(False)
                self.ui.back.setEnabled(False)

            elif self.ui.t.isVisible():
                self.load()
                self.ui.t.setVisible(True)
                self.ui.n.setVisible(True)
                self.ui.u.setVisible(True)
                self.ui.back.setVisible(True)
                self.ui.up_pointer.setVisible(True)

                self.ui.t.setEnabled(True)
                self.ui.n.setEnabled(False)
                self.ui.u.setEnabled(False)
                self.ui.back.setEnabled(False)

            elif self.ui.s.isVisible():
                self.load()
                self.ui.s.setVisible(True)
                self.ui.l.setVisible(True)
                self.ui.c.setVisible(True)
                self.ui.back.setVisible(True)
                self.ui.up_pointer.setVisible(True)

                self.ui.s.setEnabled(True)
                self.ui.l.setEnabled(False)
                self.ui.c.setEnabled(False)
                self.ui.back.setEnabled(False)

            elif self.ui.p.isVisible():
                self.load()
                self.ui.p.setVisible(True)
                self.ui.m.setVisible(True)
                self.ui.h.setVisible(True)
                self.ui.back.setVisible(True)
                self.ui.up_pointer.setVisible(True)

                self.ui.p.setEnabled(True)
                self.ui.m.setEnabled(False)
                self.ui.h.setEnabled(False)
                self.ui.back.setEnabled(False)

            elif self.ui.d.isVisible():
                self.load()
                self.ui.d.setVisible(True)
                self.ui.x.setVisible(True)
                self.ui.v.setVisible(True)
                self.ui.back.setVisible(True)
                self.ui.up_pointer.setVisible(True)

                self.ui.d.setEnabled(True)
                self.ui.x.setEnabled(False)
                self.ui.v.setEnabled(False)
                self.ui.back.setEnabled(False)

            elif self.ui.g.isVisible():
                self.load()
                self.ui.g.setVisible(True)
                self.ui.b.setVisible(True)
                self.ui.f.setVisible(True)
                self.ui.back.setVisible(True)
                self.ui.up_pointer.setVisible(True)

                self.ui.g.setEnabled(True)
                self.ui.b.setEnabled(False)
                self.ui.f.setEnabled(False)
                self.ui.back.setEnabled(False)

            elif self.ui.y.isVisible():
                self.load()
                self.ui.y.setVisible(True)
                self.ui.w.setVisible(True)
                self.ui.k.setVisible(True)
                self.ui.back.setVisible(True)
                self.ui.up_pointer.setVisible(True)

                self.ui.y.setEnabled(True)
                self.ui.w.setEnabled(False)
                self.ui.k.setEnabled(False)
                self.ui.back.setEnabled(False)

            elif self.ui.z.isVisible():
                self.load()
                self.ui.z.setVisible(True)
                self.ui.j.setVisible(True)
                self.ui.q.setVisible(True)
                self.ui.back.setVisible(True)
                self.ui.up_pointer.setVisible(True)

                self.ui.z.setEnabled(True)
                self.ui.j.setEnabled(False)
                self.ui.q.setEnabled(False)
                self.ui.back.setEnabled(False)

            elif self.ui.backspace.isVisible():
                self.load()
                self.ui.backspace.setVisible(True)
                self.ui.dot.setVisible(True)
                self.ui.qsn.setVisible(True)
                self.ui.back.setVisible(True)
                self.ui.up_pointer.setVisible(True)

                self.ui.backspace.setEnabled(True)
                self.ui.dot.setEnabled(False)
                self.ui.qsn.setEnabled(False)
                self.ui.back.setEnabled(False)

            elif self.ui.left.isVisible():
                self.load()
                self.ui.left.setVisible(True)
                self.ui.right.setVisible(True)
                self.ui.comma.setVisible(True)
                self.ui.back.setVisible(True)
                self.ui.up_pointer.setVisible(True)

                self.ui.left.setEnabled(True)
                self.ui.right.setEnabled(False)
                self.ui.comma.setEnabled(False)
                self.ui.back.setEnabled(False)

            elif self.ui.left_left.isVisible():
                self.load()
                self.ui.left_left.setVisible(True)
                self.ui.right_right.setVisible(True)
                self.ui.exit.setVisible(True)
                self.ui.back.setVisible(True)
                self.ui.up_pointer.setVisible(True)

                self.ui.left_left.setEnabled(True)
                self.ui.right_right.setEnabled(False)
                self.ui.exit.setEnabled(False)
                self.ui.back.setEnabled(False)

    def onLeft(self):
        if self.ui.qc1.isEnabled():
            self.load()
            self.ui.qc11.setVisible(True)
            self.ui.qc12.setVisible(True)
            self.ui.qc13.setVisible(True)
            self.ui.back.setVisible(True)
            self.ui.up_pointer.setVisible(True)
            self.ui.qc11.setEnabled(True)

        elif self.ui.qc11.isEnabled():
            self.load()
            self.ui.space.setVisible(True)
            self.ui.e.setVisible(True)
            self.ui.a.setVisible(True)
            self.ui.back.setVisible(True)
            self.ui.up_pointer.setVisible(True)
            self.ui.space.setEnabled(True)

        elif self.ui.space.isEnabled():
            self.ui.textEdit.insertPlainText(" ")
            self.load()
            self.stage1()

        elif self.ui.e.isEnabled():
            self.ui.textEdit.insertPlainText("E")
            self.load()
            self.stage1()
        elif self.ui.a.isEnabled():
            self.ui.textEdit.insertPlainText("A")
            self.load()
            self.stage1()

        elif self.ui.qc12.isEnabled():
            self.load()
            self.ui.r.setVisible(True)
            self.ui.i.setVisible(True)
            self.ui.o.setVisible(True)
            self.ui.back.setVisible(True)
            self.ui.up_pointer.setVisible(True)
            self.ui.r.setEnabled(True)

        elif self.ui.r.isEnabled():
            self.ui.textEdit.insertPlainText("R")
            self.load()
            self.stage1()

        elif self.ui.i.isEnabled():
            self.ui.textEdit.insertPlainText("I")
            self.load()
            self.stage1()
        elif self.ui.o.isEnabled():
            self.ui.textEdit.insertPlainText("O")
            self.load()
            self.stage1()

        elif self.ui.qc13.isEnabled():
            self.load()
            self.ui.t.setVisible(True)
            self.ui.n.setVisible(True)
            self.ui.u.setVisible(True)
            self.ui.back.setVisible(True)
            self.ui.up_pointer.setVisible(True)
            self.ui.t.setEnabled(True)

        elif self.ui.t.isEnabled():
            self.ui.textEdit.insertPlainText("T")
            self.load()
            self.stage1()

        elif self.ui.n.isEnabled():
            self.ui.textEdit.insertPlainText("N")
            self.load()
            self.stage1()
        elif self.ui.u.isEnabled():
            self.ui.textEdit.insertPlainText("U")
            self.load()
            self.stage1()

        elif self.ui.qc2.isEnabled():
            self.load()
            self.ui.qc21.setVisible(True)
            self.ui.qc22.setVisible(True)
            self.ui.qc23.setVisible(True)
            self.ui.back.setVisible(True)
            self.ui.up_pointer.setVisible(True)
            self.ui.qc21.setEnabled(True)

        elif self.ui.qc21.isEnabled():
            self.load()
            self.ui.s.setVisible(True)
            self.ui.l.setVisible(True)
            self.ui.c.setVisible(True)
            self.ui.back.setVisible(True)
            self.ui.up_pointer.setVisible(True)
            self.ui.s.setEnabled(True)

        elif self.ui.s.isEnabled():
            self.ui.textEdit.insertPlainText("S")
            self.load()
            self.stage1()

        elif self.ui.l.isEnabled():
            self.ui.textEdit.insertPlainText("L")
            self.load()
            self.stage1()
        elif self.ui.c.isEnabled():
            self.ui.textEdit.insertPlainText("C")
            self.load()
            self.stage1()

        elif self.ui.qc22.isEnabled():
            self.load()
            self.ui.p.setVisible(True)
            self.ui.m.setVisible(True)
            self.ui.h.setVisible(True)
            self.ui.back.setVisible(True)
            self.ui.up_pointer.setVisible(True)
            self.ui.p.setEnabled(True)

        elif self.ui.p.isEnabled():
            self.ui.textEdit.insertPlainText("P")
            self.load()
            self.stage1()

        elif self.ui.m.isEnabled():
            self.ui.textEdit.insertPlainText("M")
            self.load()
            self.stage1()
        elif self.ui.h.isEnabled():
            self.ui.textEdit.insertPlainText("H")
            self.load()
            self.stage1()

        elif self.ui.qc23.isEnabled():
            self.load()
            self.ui.d.setVisible(True)
            self.ui.x.setVisible(True)
            self.ui.v.setVisible(True)
            self.ui.back.setVisible(True)
            self.ui.up_pointer.setVisible(True)
            self.ui.d.setEnabled(True)

        elif self.ui.d.isEnabled():
            self.ui.textEdit.insertPlainText("D")
            self.load()
            self.stage1()

        elif self.ui.x.isEnabled():
            self.ui.textEdit.insertPlainText("X")
            self.load()
            self.stage1()
        elif self.ui.v.isEnabled():
            self.ui.textEdit.insertPlainText("V")
            self.load()
            self.stage1()

        elif self.ui.qc3.isEnabled():
            self.load()
            self.ui.qc31.setVisible(True)
            self.ui.qc32.setVisible(True)
            self.ui.qc33.setVisible(True)
            self.ui.back.setVisible(True)
            self.ui.up_pointer.setVisible(True)
            self.ui.qc31.setEnabled(True)

        elif self.ui.qc31.isEnabled():
            self.load()
            self.ui.g.setVisible(True)
            self.ui.b.setVisible(True)
            self.ui.f.setVisible(True)
            self.ui.back.setVisible(True)
            self.ui.up_pointer.setVisible(True)
            self.ui.g.setEnabled(True)

        elif self.ui.g.isEnabled():
            self.ui.textEdit.insertPlainText("G")
            self.load()
            self.stage1()

        elif self.ui.b.isEnabled():
            self.ui.textEdit.insertPlainText("B")
            self.load()
            self.stage1()
        elif self.ui.f.isEnabled():
            self.ui.textEdit.insertPlainText("F")
            self.load()
            self.stage1()

        elif self.ui.qc32.isEnabled():
            self.load()
            self.ui.y.setVisible(True)
            self.ui.w.setVisible(True)
            self.ui.k.setVisible(True)
            self.ui.back.setVisible(True)
            self.ui.up_pointer.setVisible(True)
            self.ui.y.setEnabled(True)

        elif self.ui.y.isEnabled():
            self.ui.textEdit.insertPlainText("Y")
            self.load()
            self.stage1()

        elif self.ui.w.isEnabled():
            self.ui.textEdit.insertPlainText("W")
            self.load()
            self.stage1()
        elif self.ui.k.isEnabled():
            self.ui.textEdit.insertPlainText("K")
            self.load()
            self.stage1()

        elif self.ui.qc33.isEnabled():
            self.load()
            self.ui.z.setVisible(True)
            self.ui.j.setVisible(True)
            self.ui.q.setVisible(True)
            self.ui.back.setVisible(True)
            self.ui.up_pointer.setVisible(True)
            self.ui.z.setEnabled(True)

        elif self.ui.z.isEnabled():
            self.ui.textEdit.insertPlainText("Z")
            self.load()
            self.stage1()

        elif self.ui.j.isEnabled():
            self.ui.textEdit.insertPlainText("J")
            self.load()
            self.stage1()
        elif self.ui.q.isEnabled():
            self.ui.textEdit.insertPlainText("Q")
            self.load()
            self.stage1()

        elif self.ui.qc4.isEnabled():
            self.load()
            self.ui.qc41.setVisible(True)
            self.ui.qc42.setVisible(True)
            self.ui.qc43.setVisible(True)
            self.ui.back.setVisible(True)
            self.ui.up_pointer.setVisible(True)
            self.ui.qc41.setEnabled(True)

        elif self.ui.qc41.isEnabled():
            self.load()
            self.ui.backspace.setVisible(True)
            self.ui.dot.setVisible(True)
            self.ui.qsn.setVisible(True)
            self.ui.back.setVisible(True)
            self.ui.up_pointer.setVisible(True)
            self.ui.backspace.setEnabled(True)

        elif self.ui.backspace.isEnabled():
            oText = self.ui.textEdit.toPlainText()
            nText = oText[:-1]
            self.ui.textEdit.setText(nText)
            self.ui.textEdit.moveCursor(self.cursor.MoveOperation.End)
            self.load()
            self.stage1()

        elif self.ui.dot.isEnabled():
            self.ui.textEdit.insertPlainText(".")
            self.load()
            self.stage1()
        elif self.ui.qsn.isEnabled():
            self.ui.textEdit.insertPlainText("?")
            self.load()
            self.stage1()

        elif self.ui.qc42.isEnabled():
            self.load()
            self.ui.left.setVisible(True)
            self.ui.right.setVisible(True)
            self.ui.comma.setVisible(True)
            self.ui.back.setVisible(True)
            self.ui.up_pointer.setVisible(True)
            self.ui.left.setEnabled(True)

        elif self.ui.left.isEnabled():
            if not self.cursor.atStart():
                self.ui.textEdit.moveCursor(self.cursor.MoveOperation.Left)
            self.load()
            self.stage1()

        elif self.ui.right.isEnabled():
            if not self.cursor.atEnd():
                self.ui.textEdit.moveCursor(self.cursor.MoveOperation.Right)
            self.load()
            self.stage1()
        elif self.ui.comma.isEnabled():
            self.ui.textEdit.insertPlainText(",")
            self.load()
            self.stage1()

        elif self.ui.qc43.isEnabled():
            self.load()
            self.ui.left_left.setVisible(True)
            self.ui.right_right.setVisible(True)
            self.ui.exit.setVisible(True)
            self.ui.back.setVisible(True)
            self.ui.up_pointer.setVisible(True)
            self.ui.left_left.setEnabled(True)

        elif self.ui.left_left.isEnabled():
            self.ui.textEdit.moveCursor(self.cursor.MoveOperation.Start)
            self.load()
            self.stage1()

        elif self.ui.right_right.isEnabled():
            self.ui.textEdit.moveCursor(self.cursor.MoveOperation.End)
            self.load()
            self.stage1()
        elif self.ui.exit.isEnabled():
            oText = self.ui.textEdit.toPlainText()
            self.file.writelines(oText)
            self.file.write("\n")
            self.file.close()
            self.close()

        elif self.ui.back.isEnabled():
            if self.ui.qc11.isVisible():
                self.load()
                self.stage1()

            elif self.ui.qc21.isVisible():
                self.load()
                self.stage1()

            elif self.ui.qc31.isVisible():
                self.load()
                self.stage1()

            elif self.ui.qc41.isVisible():
                self.load()
                self.stage1()

            elif self.ui.space.isVisible():
                self.load()
                self.stage21()

            elif self.ui.r.isVisible():
                self.load()
                self.stage21()

            elif self.ui.t.isVisible():
                self.load()
                self.stage21()

            elif self.ui.s.isVisible():
                self.load()
                self.stage22()

            elif self.ui.p.isVisible():
                self.load()
                self.stage22()

            elif self.ui.d.isVisible():
                self.load()
                self.stage22()

            elif self.ui.g.isVisible():
                self.load()
                self.stage23()

            elif self.ui.y.isVisible():
                self.load()
                self.stage23()

            elif self.ui.z.isVisible():
                self.load()
                self.stage23()

            elif self.ui.backspace.isVisible():
                self.load()
                self.stage24()

            elif self.ui.left.isVisible():
                self.load()
                self.stage24()

            elif self.ui.left_left.isVisible():
                self.load()
                self.stage24()

    def updateWindow(self):
        try:
            data, time_stamp = self.inlet.pull_sample()
            if data[0] == 0:
                print("Make a left movement")
                self.onLeft()
                self.show()
            elif data[0] == 1:
                print("Make a right movement")
                self.onRight()
                self.show()
        except Exception as e:
            self.close()