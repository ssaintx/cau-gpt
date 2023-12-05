import config
import google.generativeai as palm
import pprint


palm.configure(api_key=config.API_KEY)

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name



def generate_text(prompt):
  completion = palm.generate_text(
      model=model,
      prompt=prompt,
      temperature=0,
      # The maximum length of the response
      max_output_tokens=800,
  )
  return completion.result
