import os
import openai

def GeneratePost(personalityPrompt, postPrompt):
  openai.api_key = os.getenv("ChatGPT")
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system",
        "content": "Use the following principles to create a social media post:\n\n- " + personalityPrompt
      },
      {
        "role": "user",
        "content": postPrompt
      }
    ],
    temperature=0.8,
    max_tokens=500,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

  return response.choices[0].message.content


print(GeneratePost("-passionate\n-excited", "Make a post about favorite mario character"))