import sys 
from PyQt5.QtWidgets import QApplication,QWidget

if __name__=='__main__':
    #创建qApplication类实例
    app=QApplication(sys.argv)
    #创建一个窗口
    w=QWidget()
    #设置窗口尺寸
    w.resize(400,200)
    #移动窗口
    w.move(300,300)
    #创建标题
    w.setWindowTitle('这是第一个pyqt5程序')
    w.show()
    #进入主程序循环，并通过exit确保程序安全结束
    sys.exit(app.exec_())



