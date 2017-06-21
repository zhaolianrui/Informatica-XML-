# Informatica-XML
Informatica XML配置文件批量生成工具

1.图标资源文件生成步骤:
首先新建一个 images.qrc 文件，内容格式大体如下:
<RCC>
  <qresource prefix="/" >
    <file>img/image1.png</file>
    <file>img/image2.png</file>
    <file>img/image3.png</file>
  </qresource>
</RCC>
>>pyrcc5 -o images_qr.py images.qrc
# your code
import images_qr
self.setWindowIcon(QtGui.QIcon(':/img/image1.png'))

2.>>pyinstaller -F -w TestDataGen.py
  >>pyinstaller -F -w -i gen.ico TestDataGen.py
3.>>python -m PyQt5.uic.pyuic -o ui.py *.ui
