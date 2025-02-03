import sys
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout,
                             QHBoxLayout, QLineEdit, QPushButton, QWidget, QSizePolicy)
from PyQt5.QtWebEngineWidgets import QWebEngineView
import qt_material


class NovaBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nova Browser")
        self.setGeometry(100, 100, 1200, 800)

        # Ana widget ve layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # Web görünümünü ÖNCE oluştur
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("about:blank"))

        # Araç çubuğunu SONRA oluştur
        self.create_navbar()

        # Layout'a ekle
        self.main_layout.addWidget(self.browser)

        # Tema ve responsive ayarları
        qt_material.apply_stylesheet(app, theme='dark_teal.xml')
        self.setup_responsive()

    def create_navbar(self):
        navbar = QHBoxLayout()

        # Butonlar
        self.back_btn = QPushButton("←")
        self.back_btn.clicked.connect(self.browser.back)

        self.forward_btn = QPushButton("→")
        self.forward_btn.clicked.connect(self.browser.forward)

        self.reload_btn = QPushButton("↻")
        self.reload_btn.clicked.connect(self.browser.reload)

        # Adres çubuğu
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("URL girin...")
        self.url_bar.returnPressed.connect(self.navigate)

        # Layout'a ekle
        navbar.addWidget(self.back_btn)
        navbar.addWidget(self.forward_btn)
        navbar.addWidget(self.reload_btn)
        navbar.addWidget(self.url_bar)
        self.main_layout.addLayout(navbar)

    def navigate(self):
        url = self.url_bar.text()
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        self.browser.setUrl(QUrl(url))

    def setup_responsive(self):
        # Boyut politikaları
        self.url_bar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.browser.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Minimum pencere boyutu
        self.setMinimumSize(800, 600)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NovaBrowser()
    window.show()
    sys.exit(app.exec_())