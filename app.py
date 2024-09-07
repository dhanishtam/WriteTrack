from flask import Flask, render_template, request, jsonify
from chat import chat
import openai
message_history = []
def get_tweets(company_name, product_name, ideal_user):
    user_input = "Write the first 5 Tweets for my company" + company_name + "Our main product revolves around" + product_name + "and the ideal user is" + ideal_user + ". Rules: 1. No hashtags 2. Make sure you give each tweet in a new line."
    return chat(user_input, message_history)
def get_posts(company_name, product_name, ideal_user):
    user_input = "Write the first 2 Instagram posts for my company in the format 1. Caption 2. Slide 1 Content 3. Slide 2 Content" + company_name + "Our main product revolves around" + product_name + "and the ideal user is" + ideal_user + ". Make sure you give each post in a new line."
    return chat(user_input, message_history)

def get_blogs(company_name, product_name, ideal_user):
    user_input = "Write the first 1 blogs for my company" + company_name + "Our main product revolves around" + product_name + "and the ideal user is" + ideal_user + ". Make sure you give each blog in a new line."
    return chat(user_input, message_history)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        company_name = request.form['question1']
        product_name = request.form['question2']
        ideal_user = request.form['question3']
        #user_input = "My product is called " + product_name +". Write a PRD of a feature " + feature_name +"for my product. An overview for the feature is: " + overview
        print(message_history)
        #gpt_resp = chat(user_input, message_history)
        #splitted_gpt_resp = gpt_resp.split('\n')
        #   print(splitted_gpt_resp)
        resp = jsonify({'tweets': get_tweets(company_name, product_name, ideal_user), 'posts': get_posts(company_name, product_name, ideal_user), 'blogs': get_blogs(company_name, product_name, ideal_user)})
        print(resp)
        #for i in splitted_gpt_resp:
            #resp = jsonify({'output': i})
        return resp
    return render_template('new.html')

if __name__ == '__main__':
    app.run(debug=True)


#Liftoff
#Generating tech startups
#students wanting to learn how to deploy side projects