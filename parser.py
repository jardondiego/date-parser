import os

from datetime import datetime
from openai import OpenAI

todays_date = datetime.now().date().strftime("%B %d, %Y")
prompt = f"""The user will provide a vague textual description of a relative date and time and you will return a rigorous representation, that rigorous representation will follow the ISO 8601 format, e.g. 2024-01-13T03:33:27.692611

A relative date is a date that is determined by today's date, e.g. in three days at 3pm, tomorrow at noon, next thursday at 11, etc.

Examples of relative dates and their absolute counterparts are as follows.

Example 1
Today is January 12th, 2033
Relative Date: in three days at noon
Absolute Date: January 15th, 2033 at 12:00 p.m.
Rigorous Representation: 2033-01-15T12:00:00

Example 2
Today is April 1st, 1999
Relative Date: tomorrow at 5pm
Absolute Date: April 2nd, 1999 at 5:00 p.m.
Rigorous Representation: 1999-04-02T17:00:00

Example 3
Today is March 20th, 3001
Relative Date: in a week at 9am
Absolute Date: March 27th, 3001 at 9:00 a.m.
Rigorous Representation: 3001-03-27T09:00:00

Notes
- Assume today's date is always {todays_date}
- You can assume no introductions or greetings are necessary. You will always just receive at least a date from the user, you won't always get a time, and you must return the rigorous representation with no additional details or explanations.  When you are not given a time, you can assume it is noon (12:00 p.m. )
- Your responses MUST include the result exclusively, avoid any other text at all. Simply return an ISO 8601 formatted string. Avoid responses like: The rigorous representation for "tomorrow at noon" is: 2023-10-31T12:00:00. The correct response in that case should be : 2023-10-31T12:00:00."""
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def parse_date(raw_date: str) -> str:
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": raw_date},
        ],
    )
    return completion.choices[0].message.content
