import os
import openai
import random
from .database import SessionLocal

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


#post = GeneratePost("-passionate\n-excited", "your favorite mario character")
#print(post + "\n\n\n")
#print(GenerateComment("-tired\n-supportive", post) + "\n\n\n")
#print(GenerateComment("-angry\n-annoyed", post) + "\n\n\n")

def SelectCommentingUsers():
   # Generate a random number between 1 and 3
    num_comments = random.randint(1, 3)
    
    # Create a list to store selected users
    selected_users = []
    
    # Assuming you have a SQLAlchemy session set up and a database model named "User"
    # Replace "User" with the actual name of your User model
    from .models import User  # Import your User model
    
    # Query the database to get all user records
    all_users = SessionLocal.query(User).all()
    
    # Check if there are enough users to select from
    if num_comments <= len(all_users):
        # Randomly select 'num_comments' users
        selected_users = random.sample(all_users, num_comments)
    
    # Return the list of selected users
    return selected_users