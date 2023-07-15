# import re
# raw_text = """, coding 1. Prioritize career development opportunities such as taking on more challenging projects or responsibilities, volunteering for new initiatives, or joining special teams.
# 2. Seek out training and certifications in emerging technologies relevant to the user's current role and their goals.
# 3. Establish a mentoring relationship with experienced personnel who can provide guidance and support in their growth as a professional
# 4. Develop soft skills which are important for team dynamics such as communication style, problem solving techniques, collaboration strategies etc. This could be done by enrolling in courses 
# or workshops related to teamwork effectiveness or attending industry conferences relevant to the user’s field of expertise .
# 5. Learn about the business side of the organization so they can understand what drives decisions within it including cost management and target compliance metrics such as quality control standards and delivery timelines
# • Improve the existing programming and development skills- Java, Splunk
# • Learn more about Kafka messaging platform & integrate it successfully
# • Take up coding challenges such as leetcode to improve coding abilities
# • Enhance domain knowledge in Account Servicing App and Login App
# • Invest time on personal projects outside of work to strengthen knowledge and skills
# • Build Confidence in PR reviews and give comments on advanced level topics
# • Identify areas for improvement during the project development process
# """

# res = re.sub(r"[0-9].|•", "\n-", raw_text)
# slice = res.find("-")
# print(res[10:])

# import openai 

# openai.api_key = "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"
# model_list = openai.Model.list()
# print(model_list)

# messages = [{"role": "system", "content": "You are a helpful assistant."}]
# messages.append({"role": "user", "content": "tell about the IT marketplace"})
# response = openai.Completion.create(
#     model= "gpt-4", #"text-davinci-003",
#     prompt=messages,
#     # prompt=prompt,
#     max_tokens=1000,
#     top_p=1,
#     frequency_penalty=0.8,
#     presence_penalty=1
#     # stop=["<h"]
# )
# print(response.get("choices")[0]['text'])

# import stripe
# stripe.api_key = "sk_test_51NPoWTFjdMNhV4DTUz5UIadz1ONudDZv7uZIxjRxlTsdytxOTnQt36mpFRcpytTkvkFamsPVw1l1wMpcYBojMd6W00qIyK2Lfz"

# created_session = stripe.checkout.Session.create(
#   success_url="https://example.com/success",
#   line_items=[
#     {
#       "price": "price_1NSJcsFjdMNhV4DT4UhixjCV",
#       "quantity": 1,
#     },
#   ],
#   mode="payment",
# )

# print(created_session["id"])


# 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

import os
import openai

openai.api_key = "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" #os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "you are career advisor"
        },
        {
            "role": "user",
            "content": "how can I level up my career"
        },
        {
            "role": "assistant",
            "content": "Leveling up your career involves various strategies and activities. Here's a roadmap to help you:\n\n1. Identify your career goals: This includes understanding"
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response.get("choices")[0]['message']['content'])