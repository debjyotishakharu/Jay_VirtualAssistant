
######DIALOGPT################
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "microsoft/DialoGPT-large"

tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left")
model = AutoModelForCausalLM.from_pretrained(model_name)


def dialogpt_conv(user_command):

    input_text = user_command
#     input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors="pt")
# # generate a bot response
#     chat_history_ids = model.generate(
#         input_ids,
#         max_length=1000,
#         do_sample=True,
#         top_k=100,
#         temperature=0.2,
#         pad_token_id=tokenizer.eos_token_id
#     )
#     #print the output
#     output = tokenizer.decode(chat_history_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
#     return output
    new_user_input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors='pt')

    # append the new user input tokens to the chat history
    bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1)
    # generated a response while limiting the total chat history to 1000 tokens, 
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    # pretty print last ouput tokens from bot
    output=tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    return output
#################################################################################
##### Google flan t5 large #####

from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-large")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-large", device_map="auto")

def flant5_conv(user_command):
    input_text = user_command
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")

    outputs = model.generate(input_ids)
    response=tokenizer.decode(outputs[0])
    return response

####################################################################################

from transformers import pipeline, Conversation
converse = pipeline("conversational")

def conversational_conv(user_command):
    conversation_1 = Conversation(user_command)
    response=converse([conversation_1])
    return response[1]["content"]
