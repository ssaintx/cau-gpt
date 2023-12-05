import google.generativeai as palm
import config

palm.configure(api_key=config.API_KEY)

def conversation(prompt):
  response = palm.chat(messages=prompt)
  return response.last