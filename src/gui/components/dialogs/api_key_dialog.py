"""
OpenAI APIキー設定用のダイアログモジュール

APIキーの入力、保存、表示を管理するダイアログウィンドウを提供します
"""

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QFormLayout,
    QPushButton, QLineEdit, QLabel, QMessageBox
)
from PyQt6.QtCore import Qt

from src.gui.resources.labels import AppLabels
from src.gui.resources.styles import AppStyles
from src.gui.resources.config import AppConfig

class APIKeyDialog(QDialog):
    """
    OpenAI APIキーを入力するためのダイアログ
    
    APIキーの入力、保存、表示を管理するダイアログウィンドウ
    """
    
    def __init__(self, parent=None, api_key=None, current_base_url=AppConfig.DEFAULT_BASE_URL):
        """
        APIKeyDialogの初期化
        
        Parameters
        ----------
        parent : QWidget, optional
            親ウィジェット
        api_key : str, optional
            初期表示するAPIキー
        current_base_url : str, optional
            初期表示するBase URL
        """
        super().__init__(parent)
        self.setWindowTitle(AppLabels.API_KEY_DIALOG_TITLE)
        self.setMinimumWidth(450) # Adjusted width for new fields
        
        # スタイルシートを設定
        self.setStyleSheet(AppStyles.API_KEY_DIALOG_STYLE)
        
        self.current_base_url = current_base_url

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # APIキー入力
        form_layout = QFormLayout()
        form_layout.setSpacing(10)

        self.api_key_input = QLineEdit()
        if api_key:
            self.api_key_input.setText(api_key)
        self.api_key_input.setEchoMode(QLineEdit.EchoMode.Password)
        form_layout.addRow(AppLabels.API_KEY_LABEL, self.api_key_input)
        
        # Base URL入力
        base_url_label = QLabel(AppLabels.AZURE_BASE_URL_LABEL)
        self.base_url_input = QLineEdit()
        self.base_url_input.setPlaceholderText(AppLabels.AZURE_BASE_URL_PLACEHOLDER)
        self.base_url_input.setText(self.current_base_url)
        form_layout.addRow(base_url_label, self.base_url_input)

        layout.addLayout(form_layout)
        
        # APIキー情報テキスト
        api_key_info_label = QLabel(AppLabels.API_KEY_INFO)
        api_key_info_label.setWordWrap(True)
        api_key_info_label.setStyleSheet(AppStyles.API_KEY_INFO_LABEL_STYLE)
        layout.addWidget(api_key_info_label)

        # Azure 情報テキスト
        azure_info_label = QLabel(AppLabels.AZURE_INFO)
        azure_info_label.setWordWrap(True)
        azure_info_label.setStyleSheet(AppStyles.API_KEY_INFO_LABEL_STYLE) # Reuse style for now
        layout.addWidget(azure_info_label)
        
        # ボタン
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        self.save_button = QPushButton(AppLabels.SAVE_BUTTON)
        self.save_button.clicked.connect(self.accept)
        
        self.cancel_button = QPushButton(AppLabels.CANCEL_BUTTON)
        self.cancel_button.setObjectName("cancelButton")
        self.cancel_button.clicked.connect(self.reject)
        
        button_layout.addStretch(1) # Add stretch to push buttons to the right
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.save_button)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
    
    def get_api_key(self):
        """
        入力されたAPIキーを返す
        
        Returns
        -------
        str
            入力されたAPIキー
        """
        return self.api_key_input.text()

    def get_base_url(self):
        """
        入力されたBase URLを返す

        Returns
        -------
        str
            入力されたBase URL
        """
        return self.base_url_input.text().strip()