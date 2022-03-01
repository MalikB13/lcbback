from django.apps import AppConfig
# from models import answer

class ChatbotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chatbot'

    def answer(self, sentence):
        ans = 'You just said : ' + sentence
        return ({'answer': ans,})
