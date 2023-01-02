import os
import openai
from dotenv import load_dotenv

load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")

title = "Apple iPad Pro Models With 11.1-Inch and 13-Inch OLED Displays to Launch in 2024"
keywords = '[ipad, mini, Pro, models, discusses]'
prompt_text = title + " -> " + keywords + "\n\n###\n\n"

def write_up(title, keywords):
    prompt_text = f"{title} -> {[keywords]}\n\n###\n\n"
    response = openai.Completion.create(
                    # model="curie:ft-personal-2022-12-30-07-35-15",
                    model="davinci:ft-personal-2022-12-30-09-42-41", 
                    prompt=prompt_text,
                    temperature=0.89,
                    max_tokens=1200,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0.6,
                    stop=["\n\n\nEND"]
      )

    return response["choices"][0]["text"]