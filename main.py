import openai
import config

# de esta manera, configuramos openai con nuestra api_key. Le estamos pasando nuestra api
# ya configuramos openai 
openai.api_key = config.api_key

response = openai.ChatCompletion.create(model="text-curie-001", messages=[{"role": "user", "content": "¿Que es QT?"}])
print(response)