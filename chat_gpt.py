from mainwindow import Ui_MainWindow
from PyQt6 import QtWidgets, QtGui, QtCore
import openai


class MainWindow_controller(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.textBrowser=self.ui.textBrowser
        self.API_KY_lineEdit = self.ui.API_KY_lineEdit
        self.Question_lineEdit = self.ui.Question_lineEdit
        self.ui.Question_Button.clicked.connect(self.Question_on_click)
        
    def API_KY_messager(self):
        self.textBrowser.clear()
        api_key=self.API_KY_lineEdit.text()

        if not api_key:
            url_link = "https://platform.openai.com/docs/api-reference/introduction"
            html = '<a href="'+url_link+'">'+'API_KEY不得為空，此為API申請網址:</a><br><a href="'+url_link+'">'+url_link+'</a>'
            self.textBrowser.setHtml(html)
            self.textBrowser.setOpenExternalLinks(True)
            #self.textBrowser.setOpenExternalLinks(Flase)
            # self.textBrowser.anchorClicked.connect(self.on_anchor_clicked)
        return api_key
    
    # def on_anchor_clicked(self, url):
    #     QtGui.QDesktopServices.openUrl(url)
       
    def Question_on_click(self):
        self.textBrowser.clear()
        API_text=self.API_KY_messager()
        Question_text=self.Question_lineEdit.text()
       
        try:
            self.Chat_text=Chat_gpt(API_text,Question_text).get_response()
            self.textBrowser.setText(self.Chat_text)
        except:
            pass
    
class Chat_gpt():
        def __init__(self,API_text,Question_text):
            super().__init__() 
            self.api_key = API_text
            self.question = Question_text
            #'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'
        def get_response(self):
            openai.api_key =  self.api_key
            response = openai.Completion.create(
              model ="text-davinci-003",
              prompt = self.question,
              temperature = 0.5,
              max_tokens = 60,
              top_p = 0.3,
              frequency_penalty = 0.5,
              presence_penalty = 0.0
            )
            
            self.completed_text = response['choices'][0]['text'].replace('\n', '<br>')
            return self.completed_text
        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow_controller()
    window.show()
    sys.exit(app.exec())    
    
