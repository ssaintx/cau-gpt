import main
import text
import time
import model
import config
import telebot
import chatgpt
import background

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.reply_to(message, "Ask me any question. I will try to answer it.")

# CHAT GPT
@bot.message_handler(commands=['chatgpt'])
def chat_gpt(message):
  bot.reply_to(message, "Enter your request.")
  bot.register_next_step_handler(message, process_chat_gpt_request)

def process_chat_gpt_request(message):
  if message.text:
    
    bot.send_chat_action(message.chat.id, 'typing')
    
    wait = bot.send_message(message.chat.id, 'Please wait...')
    response = chatgpt.get_completion(message.text)
    
    bot.reply_to(message, response)
    
    bot.delete_message(message.chat.id, wait.message_id)
  else:
    bot.reply_to(message, "Please enter a text message.")



# MENU
@bot.message_handler(commands=['menu'])
def menu(message):
  bot.send_chat_action(message.chat.id, 'typing')
  time.sleep(0.5)
  bot.reply_to(message, text.MENU)


# # PALM AI CHAT
# @bot.message_handler(commands=['chat'])
# def chat_palm(message):
#   bot.reply_to(message, "Type any text to start a conversation")
#   bot.register_next_step_handler(message, process_chat_palm_request)

# def process_chat_palm_request(message):
#   if message.text:
#     bot.send_chat_action(message.chat.id, 'typing')
#     wait = bot.send_message(message.chat.id, 'Please wait...')
#     response = chat.conversation(message.text)
#     bot.reply_to(message, response)
#     bot.delete_message(message.chat.id, wait.message_id)

#   else:
#     bot.reply_to(message, "Please enter a text message.")

# PALM AI
@bot.message_handler(func=lambda message: True)
def send_text(message):
  if message.text:
    bot.send_chat_action(message.chat.id, 'typing')

    wait = bot.reply_to(message, "Generating an answer...")
    
    bot.reply_to(message, model.generate_text(message.text))
    bot.delete_message(message.chat.id, wait.message_id)
  
  else:
    bot.send_chat_action(message.chat.id, 'typing')
    bot.reply_to(message, "Please, enter a text. I can't recognise a pictures.")





if __name__ == '__main__':
  background.keep_alive()
  bot.polling(non_stop=True, interval=0)