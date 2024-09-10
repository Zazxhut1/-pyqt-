from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QScrollArea, QMessageBox, QWidget, QVBoxLayout, QRadioButton, QButtonGroup, QLineEdit, QInputDialog
from PyQt6.QtGui import QKeyEvent, QMouseEvent, QPixmap, QIcon, QFont, QFontDatabase
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtWebSockets import QWebSocket, QWebSocketProtocol
from statics import Statics

class MainWin(QMainWindow):

    loli : QFont

    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initBorad()
        self.initCtrl()
        self.initGame()
        self.initChess()

    def initUI(self) -> None:
        self.setFixedSize(1570, 1000)
        self.setWindowTitle(u'六子棋对弈程序')
        icon = QPixmap()
        Statics.setlist(['soyo', 'loli'])
        icon.loadFromData(Statics.getone(), 'jpg')
        loli = QFontDatabase.addApplicationFontFromData(Statics.getone())
        self.setWindowIcon(QIcon(icon))
        MainWin.loli = QFont(QFontDatabase.applicationFontFamilies(loli))
        self.board = QLabel(self)
        self.board.setGeometry(300, 14, 970, 970)
        self.board.setStyleSheet('QLabel{background-color: #DAA520; border: 5px solid #B8860B;}')
        self.plate = QLabel(self)
        self.plate.setGeometry(15, 14, 270, 970)
        self.plate.setStyleSheet('QLabel{border: 5px solid #A9A9A9; border-radius: 7px;}')
        self.ctrlp = QLabel(self)
        self.ctrlp.setGeometry(1285, 14, 270, 970)
        self.ctrlp.setStyleSheet('QLabel{background-color: #66CCFF; border: 5px solid #FFFFFF; border-radius: 7px;}')
        self.statp = QLabel(self)
        self.statp.setGeometry(30, 29, 240, 110)
        self.statp.setStyleSheet('QLabel{background-color: #DAA520; border-radius: 7px;}')
        self.stach = QLabel(self)
        self.stach.setGeometry(55, 64, 40, 40)
        self.stala = QLabel(self)
        self.stala.setGeometry(115, 49, 130, 30)
        self.stala.setStyleSheet('QLabel{font-size: 20px;}')
        self.stala.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stala.setFont(MainWin.loli)
        self.stala.setText(u'对局未开始')
        self.playBut = QPushButton(self)
        self.playBut.setGeometry(115, 79, 130, 40)
        self.playBut.setStyleSheet('QPushButton{background-color: #66CCFF; border: 3px solid #FFFFFF; border-radius: 5px; color: #FFFFFF; font-size: 17px;}')
        self.playBut.setFont(MainWin.loli)
        self.playBut.setText(u'开始对弈')
        self.playBut.clicked.connect(self.start)
        self.shistory = QScrollArea(self)
        self.shistory.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.shistory.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.shistory.setGeometry(30, 150, 240, 820)
        self.shistory.setStyleSheet('QScrollArea{border: 3px solid #A9A9A9; border-radius: 5px;}')
        self.shistory.verticalScrollBar().rangeChanged.connect(lambda: self.shistory.verticalScrollBar().setValue(self.shistory.verticalScrollBar().maximum()))
        history = QWidget()
        history.setFixedWidth(240)
        history.setMinimumHeight(810)
        self.history = QVBoxLayout()
        self.history.setAlignment(Qt.AlignmentFlag.AlignTop)
        history.setLayout(self.history)
        self.shistory.setWidget(history)
        history.show()

    def initBorad(self) -> None:
        plate = QPixmap()
        self.white = QPixmap()
        self.black = QPixmap()
        self.black_t = QPixmap()
        self.white_t = QPixmap()
        Statics.setlist(['plate', 'white', 'black', 'whitet', 'blackt'])
        plate.loadFromData(Statics.getone(), 'png')
        self.white.loadFromData(Statics.getone(), 'png')
        self.black.loadFromData(Statics.getone(), 'png')
        self.white_t.loadFromData(Statics.getone(), 'png')
        self.black_t.loadFromData(Statics.getone(), 'png')
        self.board.setPixmap(plate)
        self.black.__setattr__('chess', 0)
        self.white.__setattr__('chess', 1)
        self.black_t.__setattr__('chess', -1)
        self.white_t.__setattr__('chess', -1)
        self.stach.setPixmap(self.black)
        self.label0 = QLabel('Connect', self)
        self.label0.setGeometry(1285, 44, 270, 40)
        self.label0.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label0.setStyleSheet('QLabel{font-size: 30px;}')
        self.label0.setFont(self.loli)
        self.label1 = QLabel(u'黑方: ', self)
        self.label1.setGeometry(1300, 90, 100, 30)
        self.label1.setStyleSheet('QLabel{font-size: 20px;}')
        self.label1.setFont(self.loli)
        self.label2 = QLabel(u'白方: ', self)
        self.label2.setGeometry(1300, 220, 100, 30)
        self.label2.setStyleSheet('QLabel{font-size: 20px;}')
        self.label2.setFont(self.loli)
        self.label3 = QLabel(u'玩家', self)
        self.label3.setGeometry(1340, 120, 100, 30)
        self.label3.setStyleSheet('QLabel{font-size: 17px;}')
        self.label3.setFont(self.loli)
        self.label4 = QLabel(u'外部AI', self)
        self.label4.setGeometry(1340, 150, 100, 30)
        self.label4.setStyleSheet('QLabel{font-size: 17px;}')
        self.label4.setFont(self.loli)
        self.label5 = QLabel(u'玩家', self)
        self.label5.setGeometry(1340, 250, 100, 30)
        self.label5.setStyleSheet('QLabel{font-size: 17px;}')
        self.label5.setFont(self.loli)
        self.label6 = QLabel(u'外部AI', self)
        self.label6.setGeometry(1340, 280, 100, 30)
        self.label6.setStyleSheet('QLabel{font-size: 17px;}')
        self.label6.setFont(self.loli)
        self.label7 = QLabel('ws://', self)
        self.label7.setGeometry(1320, 185, 40, 20)
        self.label7.setStyleSheet('QLabel{font-size: 17px;}')
        self.label7.setFont(self.loli)
        self.label8 = QLabel('ws://', self)
        self.label8.setGeometry(1320, 315, 40, 20)
        self.label8.setStyleSheet('QLabel{font-size: 17px;}')
        self.label8.setFont(self.loli)

    def initCtrl(self) -> None:
        self.rad00 = QRadioButton(self)
        self.rad00.setGeometry(1310, 125, 20, 20)
        self.rad00.setChecked(True)
        self.rad01 = QRadioButton(self)
        self.rad01.setGeometry(1310, 155, 20, 20)
        self.rads0 = QButtonGroup(self)
        self.rads0.addButton(self.rad00, 0)
        self.rads0.addButton(self.rad01, 1)
        self.rad10 = QRadioButton(self)
        self.rad10.setGeometry(1310, 255, 20, 20)
        self.rad10.setChecked(True)
        self.rad11 = QRadioButton(self)
        self.rad11.setGeometry(1310, 285, 20, 20)
        self.rads1 = QButtonGroup(self)
        self.rads1.addButton(self.rad10, 0)
        self.rads1.addButton(self.rad11, 1)
        self.aicon0 = QLineEdit(self)
        self.aicon0.setGeometry(1365, 185, 155, 20)
        self.aicon0.setDisabled(True)
        self.aicon1 = QLineEdit(self)
        self.aicon1.setGeometry(1365, 315, 155, 20)
        self.aicon1.setDisabled(True)
        self.rad00.pressed.connect(lambda: self.aicon0.setDisabled(True))
        self.rad01.pressed.connect(lambda: self.aicon0.setDisabled(False))
        self.rad10.pressed.connect(lambda: self.aicon1.setDisabled(True))
        self.rad11.pressed.connect(lambda: self.aicon1.setDisabled(False))

    def initGame(self) -> None:
        self.isBlack : bool = True
        self.isAI : bool = False
        self.isFirst : bool = True
        self.isPlay : bool = False
        self.tchess : list[int] = []
        self.isAI0 : bool = False
        self.isAI1 : bool = False
        self.AI0 : AISocket
        self.AI1 : AISocket

    def initChess(self) -> None:
        self.chesses : list[Chess] = []
        for i in range(19):
            for j in range(19):
                chess = Chess(self)
                chess.move(j*51+305, i*51+19)
                self.chesses.append(chess)
        self.layer = BoardLayer(self)
        self.layer.setGeometry(300, 14, 970, 970)

    def addHistip(self, tip : str) -> None:
        self.history.addWidget(HTips(tip))
        self.shistory.widget().adjustSize()

    def next(self) -> None:
        if self.isFirst:
            if self.tchess.__len__() != 1:
                QMessageBox.warning(self, u'错误', u'请下出足够的棋子!', QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
                return
            self.isFirst = False
            self.chesses[self.tchess[0]].setPixmap(self.black)
            self.addHistip(u'黑方: (%d, %d)'%(self.tchess[0]%19, self.tchess[0]//19))
        else:
            if self.tchess.__len__() != 2:
                QMessageBox.warning(self, u'错误', u'请下出足够的棋子!', QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
                return
            if self.isBlack:
                self.chesses[self.tchess[0]].setPixmap(self.black)
                self.addHistip(u'黑方: (%d, %d)'%(self.tchess[0]%19, self.tchess[0]//19))
                self.chesses[self.tchess[1]].setPixmap(self.black)
                self.addHistip(u'黑方: (%d, %d)'%(self.tchess[1]%19, self.tchess[1]//19))
            else:
                self.chesses[self.tchess[0]].setPixmap(self.white)
                self.addHistip(u'白方: (%d, %d)'%(self.tchess[0]%19, self.tchess[0]//19))
                self.chesses[self.tchess[1]].setPixmap(self.white)
                self.addHistip(u'白方: (%d, %d)'%(self.tchess[1]%19, self.tchess[1]//19))
        if self.check():
            if self.isBlack:
                self.addHistip(u'对局结束, 黑方胜!')
                if self.isAI0: self.AI0.sendTextMessage('winb')
                if self.isAI1: self.AI1.sendTextMessage('winb')
            else:
                self.addHistip(u'对局结束, 白方胜!')
                if self.isAI0: self.AI0.sendTextMessage('winw')
                if self.isAI1: self.AI1.sendTextMessage('winw')
            self.stop()
            return
        self.isBlack = not self.isBlack
        if self.isBlack:
            self.stach.setPixmap(self.black)
            if self.isAI0 and not self.isAI1:
                self.isPlay = False
                self.isAI = True
                self.stala.setText(u'AI 回合')
                self.playBut.clicked.disconnect()
                self.playBut.clicked.connect(lambda: None)
                self.playBut.setText(u'请等待')
            elif not self.isAI1:
                self.stala.setText(u'黑方回合')
            elif self.isAI1 and not self.isAI0:
                self.isPlay = True
                self.isAI = False
                self.stala.setText(u'黑方回合')
                self.playBut.clicked.connect(self.next)
                self.playBut.setText(u'下一回合')
            if self.isAI0:
                self.AI0.sendTextMessage(str([[i%19, i//19] for i in self.tchess]).replace(',', '').replace('[', '').replace(']', ''))
        else:
            self.stach.setPixmap(self.white)
            if self.isAI1 and not self.isAI0:
                self.isPlay = False
                self.isAI = True
                self.stala.setText(u'AI 回合')
                self.playBut.clicked.disconnect()
                self.playBut.clicked.connect(lambda: None)
                self.playBut.setText(u'请等待')
            elif not self.isAI0:
                self.stala.setText(u'白方回合')
            elif self.isAI0 and not self.isAI1:
                self.isPlay = True
                self.isAI = False
                self.stala.setText(u'白方回合')
                self.playBut.clicked.connect(self.next)
                self.playBut.setText(u'下一回合')
            if self.isAI1:
                self.AI1.sendTextMessage(str([[i%19, i//19] for i in self.tchess]).replace(',', '').replace('[', '').replace(']', ''))
        self.tchess.clear()

    def start(self) -> None:
        self.isAI0 = bool(self.rads0.checkedId())
        self.isAI1 = bool(self.rads1.checkedId())
        for i in [self.rad00, self.rad01, self.rad10, self.rad11, self.aicon0, self.aicon1]: i.setDisabled(True)
        if self.isAI0:
            self.AI0 = AISocket(self, 'AI 0')
            self.AI0.open(QUrl('ws://'+self.aicon0.text()))
        if self.isAI1:
            self.AI1 = AISocket(self, 'AI 1')
            self.AI1.open(QUrl('ws://'+self.aicon1.text()))
        if not self.isAI0:
            self.isPlay = True
            self.playBut.clicked.disconnect()
            self.playBut.clicked.connect(self.next)
            self.playBut.setText(u'下一回合')
            self.stala.setText(u'黑方回合')
        else:
            self.isAI = True
            self.playBut.clicked.disconnect()
            self.playBut.clicked.connect(lambda: None)
            self.playBut.setText(u'请等待')
            self.stala.setText(u'AI 回合')
        self.addHistip(u'对局开始')

    def stop(self) -> None:
        self.isPlay = self.isAI = False
        self.tchess.clear()
        self.playBut.clicked.disconnect()
        self.playBut.setText(u'重新开始')
        self.playBut.clicked.connect(self.restart)
        self.stala.setText(u'对局结束')
        self.addHistip(u'对局结束')
        for i in [self.rad00, self.rad01, self.rad10, self.rad11]: i.setDisabled(False)
        if self.rads0.checkedId() == 1: self.aicon0.setDisabled(False)
        if self.rads1.checkedId() == 1: self.aicon1.setDisabled(False)

    def check(self) -> bool:
        for n in self.tchess:
            x : int = n % 19
            y : int = n // 19
            s0 = s1 = s2 = s3 = 1
            for t in range(1, 6):
                if x-t < 0 or self.chesses[n-t].pixmap() is None or self.chesses[n].cname != self.chesses[n-t].cname: break
                else: s0 += 1
            for t in range(1, 6):
                if x+t >= 19 or self.chesses[n+t].pixmap() is None or self.chesses[n].cname != self.chesses[n+t].cname: break
                else: s0 += 1
            for t in range(1, 6):
                if y-t < 0 or self.chesses[n-19*t].pixmap() is None or self.chesses[n].cname != self.chesses[n-19*t].cname: break
                else: s1 += 1
            for t in range(1, 6):
                if y+t >= 19 or self.chesses[n+19*t].pixmap() is None or self.chesses[n].cname != self.chesses[n+19*t].cname: break
                else: s1 += 1
            for t in range(1, 6):
                if x-t < 0 or y-t < 0 or self.chesses[n-20*t].pixmap() is None or self.chesses[n].cname != self.chesses[n-20*t].cname: break
                else: s2 += 1
            for t in range(1, 6):
                if x-t < 0 or y+t >= 19 or self.chesses[n+18*t].pixmap() is None or self.chesses[n].cname != self.chesses[n+18*t].cname: break
                else: s3 += 1
            for t in range(1, 6):
                if x+t >= 19 or y-t < 0 or self.chesses[n-18*t].pixmap() is None or self.chesses[n].cname != self.chesses[n-18*t].cname: break
                else: s3 += 1
            for t in range(1, 6):
                if x+t >= 19 or y+t >= 19 or self.chesses[n+20*t].pixmap() is None or self.chesses[n].cname != self.chesses[n+20*t].cname: break
                else: s2 += 1
            if s0 >= 6 or s1 >= 6 or s2 >= 6 or s3 >= 6:
                return True
            else: return False
        else: return False

    def restart(self) -> None:
        for i in self.chesses: i.clear()
        self.isFirst = True
        self.isBlack = True
        self.stach.setPixmap(self.black)
        self.start()

    def clickChess(self, x : int, y : int) -> None:
        if self.isPlay:
            num : int = x + y * 19
            if not self.chesses[num].isBlank: return
            if self.isBlack:
                self.chesses[num].setPixmap(self.black_t)
            else: self.chesses[num].setPixmap(self.white_t)
            self.tchess.append(num)
            if self.isFirst:
                for i in self.tchess[:-1]:
                    self.tchess.remove(i)
                    self.chesses[i].clear()
            else:
                for i in self.tchess[:-2]:
                    self.tchess.remove(i)
                    self.chesses[i].clear()
        elif self.isAI:
            num : int = x + y * 19
            if self.isBlack:
                self.chesses[num].setPixmap(self.black_t)
            else: self.chesses[num].setPixmap(self.white_t)
            self.tchess.append(num)
            if self.isFirst or self.tchess.__len__() == 2:
                self.next()

    def keyPressEvent(self, a0: QKeyEvent) -> None:
        if a0.key() == Qt.Key.Key_Space or a0.key() == Qt.Key.Key_Enter:
            self.playBut.click()
        elif a0.key() == Qt.Key.Key_Escape:
            if QMessageBox.question(self, u'提示', u'确定要现在退出吗?', (QMessageBox.StandardButton.Apply | QMessageBox.StandardButton.Cancel), QMessageBox.StandardButton.Cancel) == QMessageBox.StandardButton.Apply:
                self.close()
        elif a0.key() == Qt.Key.Key_I:
            QMessageBox.about(self, u'为什么要按 i 键 ???', u'都是长崎素世导致的!!!!!')
        elif a0.key() == Qt.Key.Key_H:
            QMessageBox.information(self, u'帮助', u'', QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
        elif a0.key() == Qt.Key.Key_C:
            ctrl = QInputDialog.getText(self, u'连接训练服务器', u'输入服务器 websocket 地址及端口:', QLineEdit.EchoMode.Normal, 'ws://', Qt.WindowType.Dialog, Qt.InputMethodHint.ImhNone)
            if ctrl[1]:
                pass
        elif a0.key() == Qt.Key.Key_R:
            if QMessageBox.question(self, u'提示', u'确定要强制终止对局吗?', (QMessageBox.StandardButton.Apply | QMessageBox.StandardButton.Cancel), QMessageBox.StandardButton.Cancel) == QMessageBox.StandardButton.Apply:
                self.stop()

class BoardLayer(QLabel):
    def __init__(self, parent : MainWin) -> None:
        super().__init__(parent)
        self.pp : MainWin = parent

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        if ev.buttons() == Qt.MouseButton.LeftButton:
            if not self.pp.isPlay: return
            x : int = ev.pos().x() // 51
            y : int = ev.pos().y() // 51
            self.pp.clickChess(x, y)

class Chess(QLabel):
    def __init__(self, parent : QWidget) -> None:
        super().__init__(parent)
        self.setFixedSize(40, 40)
        self.__blank : bool = True
        self.cname : int = -1

    def setPixmap(self, a0: QPixmap) -> None:
        super().setPixmap(a0)
        self.__blank = False
        self.cname = a0.__getattribute__('chess')

    def clear(self) -> None:
        super().clear()
        self.__blank = True
        self.cname = -1

    @property
    def isBlank(self) -> bool:
        return self.__blank

class HTips(QLabel):
    def __init__(self, tip : str) -> None:
        super().__init__()
        self.setFixedSize(240, 30)
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setFont(MainWin.loli)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.setStyleSheet('QLabel{font-size: 20px;}')
        self.setText(u' · '+tip)

class AISocket(QWebSocket):
    def __init__(self, parent : MainWin, name : str) -> None:
        self.pp = parent
        super().__init__(name, QWebSocketProtocol.Version.VersionLatest, parent)
        self.connected.connect(self.start)
        self.disconnected.connect(lambda: self.pp.addHistip('%s disconnected.'%(self.origin())))
        self.errorOccurred.connect(lambda: QMessageBox.warning(self.pp, u'错误', u'%s 连接失败!'%(self.origin()), QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close))
        self.textMessageReceived.connect(self.unpackMsg)

    def unpackMsg(self, msg : str) -> None:
        ms = [int(i) for i in msg.split(' ')]
        if ms.__len__() == 2:
            self.pp.clickChess(ms[0], ms[1])
        elif ms.__len__() == 4:
            self.pp.clickChess(ms[0], ms[1])
            self.pp.clickChess(ms[2], ms[3])

    def start(self) -> None:
        self.pp.addHistip('%s connected.'%(self.origin()))
        self.sendTextMessage('start')