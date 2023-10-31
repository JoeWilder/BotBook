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
        "content": "Make a post about " + postPrompt
      }
    ],
    temperature=0.8,
    max_tokens=500,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  return response.choices[0].message.content


def GenerateComment(personalityPrompt, post):
  openai.api_key = os.getenv("ChatGPT")
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system",
        "content": "Use the following principles to leave a comment on a social media post:\n\n- " + personalityPrompt
      },
      {
        "role": "user",
        "content": "Make a comment about the following post:: " + post
      }
    ],
    temperature=0.8,
    max_tokens=500,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

  return response.choices[0].message.content


post = GeneratePost("-passionate\n-excited", "your favorite mario character")
print(post + "\n\n\n")
print(GenerateComment("-tired\n-supportive", post) + "\n\n\n")
print(GenerateComment("-angry\n-annoyed", post) + "\n\n\n")