import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon

class FirstMainwin(QMainWindow):
    def __init__(self,parent=None):
        super(FirstMainwin,self).__init__(parent)
        #设置主窗口的标题
        self.setWindowTitle('第一个主窗口')
        #设置窗口尺寸
        self.resize(400,300)
        self.status=self.statusBar()
        self.status.showMessage('只存在5秒的消息',5000)#这里的单位是毫秒

if __name__=='__main__':
    app=QApplication(sys.argv)#传入参数

    #app.setWindowIcon()#设置图标
    main=FirstMainwin()
    main.show()
    sys.exit(app.exec_())