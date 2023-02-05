from flask import Flask, render_template, request, session, redirect
import random
app = Flask(__name__)

history = []

def chatbot_response(input_text, history):
  
  greetings = ["Hello", "Hi", "Greetings", "Sup", "What's up", "Hey"]
  greetings_response = ["Hello", "Hi", "Greetings", "Sup", "What's up", "Hey", "Hows it going?"]

  likes = ["i like you", "i love you", "Yes!"]
  likes_response = ["I like you too", "I love you too", "Yes!"]

  hates = ["i hate you", "i don't like you"]
  hates_response = ["No, You're annoying", "I hate you too", "I don't like you either"]
  
  optionlist = [greetings, likes, hates]
  responselist = [greetings_response, likes_response, hates_response]
  
  def Answer(userInput):
    for x in range(len(optionlist)):
      
      currentList = optionlist[x]
      response_msg = responselist[x]
    
    for i in range(len(currentList) - 1):
      if currentList[i] == userInput:
        print(response_msg[random.randint(0, len(response_msg) -1)])



@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
      input_text = request.form['input_text']
      response_text = chatbot_response(input_text, history)
      # Append the input and response to the chat history
      history.append(f"Guest: {input_text}")
      history.append(f"Stanley: {response_text}")


      print(input_text)
  else:
      input_text = ''
      response_text = ''  
  return render_template('index.html', input_text=input_text, response_text=response_text, history=history)




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6969)