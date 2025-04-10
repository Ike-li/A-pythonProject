from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTextEdit,
    QLabel,
)
import sys
import binascii
from 计算机网络五层模型的模拟数据生成与收发系统 import simulate_network_communication_with_visualization


class NetworkVisualizer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OSI数据封装可视化")
        self.setGeometry(100, 100, 1200, 800)

        # 创建中心部件和布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 创建数据显示区域
        self.create_data_displays()
        layout.addLayout(self.displays_layout)

        # 创建控制按钮
        self.start_button = QPushButton("开始封装过程")
        self.start_button.clicked.connect(self.start_visualization)
        layout.addWidget(self.start_button)

    def create_data_displays(self):
        self.displays_layout = QVBoxLayout()

        # 为每一层创建显示区域
        self.layers = {
            "应用层数据": QTextEdit(),
            "传输层数据": QTextEdit(),
            "网络层数据": QTextEdit(),
            "数据链路层数据": QTextEdit(),
            "物理层数据": QTextEdit(),
        }

        for title, text_edit in self.layers.items():
            container = QWidget()
            container_layout = QVBoxLayout(container)

            label = QLabel(title)
            label.setStyleSheet("font-weight: bold;")
            container_layout.addWidget(label)

            text_edit.setReadOnly(True)
            text_edit.setFixedHeight(100)
            container_layout.addWidget(text_edit)

            self.displays_layout.addWidget(container)

    def format_bytes(self, data):
        if isinstance(data, str):
            return data
        return binascii.hexlify(data).decode("utf-8")

    def start_visualization(self):
        # 获取封装过程的数据
        packet_info = simulate_network_communication_with_visualization()

        # 更新显示
        self.layers["应用层数据"].setText(packet_info.app_data)
        self.layers["传输层数据"].setText(self.format_bytes(packet_info.transport_data))
        self.layers["网络层数据"].setText(self.format_bytes(packet_info.network_data))
        self.layers["数据链路层数据"].setText(self.format_bytes(packet_info.datalink_data))
        self.layers["物理层数据"].setText(self.format_bytes(packet_info.physical_data))


def main():
    app = QApplication(sys.argv)
    window = NetworkVisualizer()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
