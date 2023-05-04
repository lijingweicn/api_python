import openai
import xdis as xdis
import xdis
import orderding
import rerunfailures

# def sugpt(input):
#     openai.api_key = open('apikey.txt','r').read()
#
#     completion = openai.ChatCompletion.create(
#         model='gpt-3.5-turbo',
#         messages=[{'role':'assistant','content':input}]
#     )
#
#     return completion.choices[0].message.content
#
# while True:
#     print(sugpt(input('我是CHATGPT，请输入您的指令：')))



openai.api_key = 'fhduisahfiuwehuih'

completion = openai.ChatCompletion.create(

    model='gpt-3.5-turbo',
    messages=[{'role': 'assistant', 'content': 'can  you give me a coin?'}]
)

print(completion)


