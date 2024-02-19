from django.shortcuts import render
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large")
# model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large")
# chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer)

# def chat(request):
#     if request.method == 'POST':
#         user_message = request.POST.get('message')
#         print(user_message, "useeeeer")
#         bot_message = chatbot(user_message)[0]['generated_text']
#         print(bot_message, "meeeeeeeesage")
#         context = {'bot_message': bot_message}
#     else:
#         context = {}
#     return render(request, 'message.html', context)

# testing
# Load tokenizer and model
# print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large")
# print(tokenizer)

# print("Loading model...")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large")
# print(model)

# Create chatbot pipeline
# print("Creating chatbot pipeline...")
chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer, max_length=50)
# print(chatbot)

# Test chatbot with a default input
user_input = "Hello"
# print("User input:", user_input)
bot_response = chatbot(user_input)#[0]['generated_text']
for reply in bot_response:
    print(reply['generated_text'])
# print("Bot response:", bot_response)