from PyPDF2 import PdfReader
import openai 
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm, inch

openai.api_key = "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"

def call_openai(prompt, max_tokens=2300):


    
    response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=max_tokens,
            top_p=1,
            frequency_penalty=0.8,
            presence_penalty=1,
            # stop=["<h"]
        )

    return response.get("choices")[0]['text']

def get_pdf_text(filename='uploaded_pdf', start=0, finish=1):
   reader = PdfReader('uploaded.pdf')
   pages = len(reader.pages)
   text = ""
   while(start<finish):
      text += reader.pages[start].extract_text()
      start +=1
   return text

# prompt1 = """Return the answer a JSON Object. As an attentive reader, meticulously extract the employee's name, organization, manager, and evaluator from the performance review document. 
#         You will find the employee's name displayed prominently at the top, preceding the year. Present this vital information as concise bullet points, separated by line breaks:
#     """

# prompt2 = """Return the answer a JSON object. Analyze the employee's performance review to identify areas where they can contribute to the team's goals. 
#             Suggest targeted measures to create a high-performance environment, and recommend prioritized action items for the next year based on their performance review.
#             List recommendational Action items consicely.
#             Return an array of at least 3 action items in a JSON object.If impossible for Json format, return in array format.c
#             """

# prompt3 ="""
#         Return the answer a JSON object. Analyze the employee's performance review to identify strengths and growth areas. 
#         Recommend relevant courses from Udemy or LinkedIn Learning to help them maximize potential and address development needs. 
#         List the course recommendations concisely:
#         Return an array of 3 courses in a JSON Object. If impossible for Json format, return in array format. 
#         """
# prompt4 = """Return the answer a JSON object. Analyze the employee's performance review and identify career development opportunities:
#             List possible opportunity recommendationas concisely.
#             Return an array of 3 opportunities in a JSON Object. If impossible for Json format, return in array format.
#             """
prompt ="""Analyze the employee's performance review and identify career development opportunities.
        Create a valid JSON object with the possible opportunities.
        {
            "Opportunity1" : "{string}",
            "Opportunity2" : "{string}",
            "Opportunity3" : "{string}",
        }
        """
details = """{
    goals: "get promoted",
    obstracle: "no budget or skills",
    skill: "java"
}"""
prompt += f"use this details to grab more ideas about the user in oreder to recommend courses {details}"
# prompt1 += f"use this details to grab more ideas about the user in oreder to recommend courses {details}"
# prompt2 += f"use this details to grab more ideas about the user in oreder to recommend courses {details}"
# prompt3 += f"use this details to grab more ideas about the user in oreder to recommend courses {details}"
# prompt4 += f"use this details to grab more ideas about the user in oreder to recommend courses {details}"

text = get_pdf_text(start=1, finish=3)

# response1 = call_openai(f"{text}\n\n{prompt1}")
# response2 = call_openai(f"{text}\n\n{prompt2}")
# response3 = call_openai(f"{text}\n\n{prompt3}")
# response4 = call_openai(f"{text}\n\n{prompt4}")
# response = call_openai(f"{text}\n\n{prompt}")
# print("RESPONSE: ", response1)
# print("RESPONSE: ", response2)
# print("RESPONSE: ", response3)
# print("RESPONSE: ", response4)
# print("RESPONSE: ", response)

sample_style_sheet = getSampleStyleSheet()
sample_style_sheet.list()
