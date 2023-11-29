import os
import re
import openai

def GeneratePost(personalityPrompt, postPrompt):
  openai.api_key = os.getenv("ChatGPT")
  response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system",
        "content": "Use the following principles to create a very brief social media post:\n\n- " + personalityPrompt
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

  message_content = response.choices[0].message.content

  result = re.sub(r'^"|"$', '', message_content)
    
  return result


def GenerateComment(personalityPrompt, post):
  openai.api_key = os.getenv("ChatGPT")
  response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system",
        "content": "Use the following principles to leave a very brief comment on a social media post:\n\n- " + personalityPrompt
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

  message_content = response.choices[0].message.content

  result = re.sub(r'^"|"$', '', message_content)
    
  return result


