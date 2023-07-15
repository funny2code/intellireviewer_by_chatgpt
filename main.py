
from fileinput import filename
from flask import *
from io import BytesIO
from werkzeug.utils import secure_filename
import json
import os
import stripe


app = Flask(__name__)

from backend import get_details, career_dev_ops, recommend_courses, highlight_action_items
from PyPDF2 import PdfReader
from pdfwrite import export_pdf
import markdown
from faq import faq_data

stripe_keys = {
   "secret_key": "sk_test_51NPoWTFjdMNhV4DTUz5UIadz1ONudDZv7uZIxjRxlTsdytxOTnQt36mpFRcpytTkvkFamsPVw1l1wMpcYBojMd6W00qIyK2Lfz",
   "publishable_key": "pk_test_51NPoWTFjdMNhV4DTiH6DB9aBrcjwmuMKUDwlub5yVeiLjxTTzBwZNROrDuA4ov8niIJniKYdrqBtrecDAzyTRep800DpwtTyDt",
}

stripe.api_key = stripe_keys["secret_key"]



def check_payment(session_id):
   stripe.api_key = stripe_keys["secret_key"]
   rep = stripe.checkout.Session.retrieve(session_id)
   if rep.get("payment_status") == "paid":
      return True
   return False


def get_pdf_text(filename='uploaded_pdf', start=0, finish=1):
   reader = PdfReader('uploaded.pdf')
   pages = len(reader.pages)
   text = ""
   while(start<finish):
      text += reader.pages[start].extract_text()
      start +=1
   return text

@app.route('/')
def get():
   return render_template('index.html')

@app.route('/success', methods=['GET'])
def success():
   args = request.args
   session_id = args.get("session_id")
   payment_status = check_payment(session_id)
   if payment_status:
      return render_template('index.html', session_id = session_id)
   
   redirect('/')
   
@app.route('/tabs')
def get_tabs():
   return render_template('tabs.html')

@app.route('/download', methods=['POST'])
def get_pdf():
   if request.method == 'POST':
      user_details = request.form.get("details")
      
      session_id = request.form.get("session_id")
      if check_payment(session_id):   
         # Get all tabs data
         details1 = get_details(get_pdf_text())
         details2 = career_dev_ops(get_pdf_text(start=1, finish=3), details=user_details)
         details3 = recommend_courses(get_pdf_text(start=1, finish=3), details=user_details)
         details4 = highlight_action_items(get_pdf_text(start=1, finish=3), details=user_details)
         details5 = highlight_action_items(get_pdf_text(start=1, finish=3), details=user_details)

         # return jsonify({"message": "success"})
         pdf_buff = export_pdf({
            "Details": details1.replace("\n", "<br/>"), 
            "Career Oppurtunities": details2.replace("\n", "<br/>"),
            "Recommended Courses": details3.replace("\n", "<br/>"),
            "Action Items": details4.replace("\n", "<br/>"),
            "Optimizer": details5.replace("\n", "<br/>")
         })
         
         return send_file(
            BytesIO(pdf_buff),
            mimetype="application/pdf",
            download_name = "Intelli Review Solutions.pdf",
            as_attachment=False
         )

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        goals = request.form.get('goals')
        obstacles = request.form.get('obstacles')
        skills = request.form.get('skill')
        session_id = request.form.get("session_id")
        
        f = request.files.get('file')
        if f is None or f.filename == '':
            return "No file selected"

        filename = secure_filename("uploaded.pdf")
        f.save("uploaded.pdf")

        details = f"Use this data to grab more understanding about the user:\nUser's Goals: {goals}\nWhat the user thinks as Obstacles: {obstacles}\nUser's Skills: {skills}"

        return render_template('tabs.html', details=details, session_id=session_id)
    else:
        return render_template('index.html')
   
@app.route('/details')
def details():
   print(request.args.get("session_id"))
   details = get_details(get_pdf_text())
   return markdown.markdown(details)

@app.route('/tab2', methods=['POST'])
def dev_ops():
   user_details = request.form.get("details")
   session_id = request.form.get("session_id")
   if check_payment(session_id):   
      print("user_details TYPE:", type(user_details))
      details = career_dev_ops(get_pdf_text(start=1, finish=3), details=user_details)
      return markdown.markdown(details)
   return markdown.markdown({})

@app.route('/tab3', methods=['POST'])
def rec_courses():
   user_details = request.form.get("details")
   
   session_id = request.form.get("session_id")
   if check_payment(session_id):   
      print("user_details TYPE:", type(user_details))
      details = recommend_courses(get_pdf_text(start=1, finish=3), details=user_details)
      return markdown.markdown(details)
      
   return markdown.markdown({})

@app.route('/tab4', methods=['POST'])
def action_items():
   user_details = request.form.get("details")
   
   session_id = request.form.get("session_id")
   if check_payment(session_id):   
      print("user_details TYPE:", type(user_details))
      details = highlight_action_items(get_pdf_text(start=1, finish=3), details=user_details)
      return markdown.markdown(details)
      
   return markdown.markdown({})

@app.route('/tab5', methods=['POST'])
def optimizer():
   user_details = request.form.get("details")

   session_id = request.form.get("session_id")
   if check_payment(session_id):   
      print("user_details TYPE:", type(user_details))
      details = highlight_action_items(get_pdf_text(start=1, finish=3), details=user_details)
      return markdown.markdown(details)
      
   return markdown.markdown({})

@app.route("/config")
def get_publishable_key():
    stripe_config = {"publicKey": stripe_keys["publishable_key"]}
    return jsonify(stripe_config)
@app.route("/faq")
def faq():
   container_style = 'background-color: #FFFFFF;'
   return render_template('faq.html', faq_data=faq_data, container_style=container_style)

@app.route("/create-checkout-session")
def create_checkout_session():
    domain_url = "http://127.0.0.1:5000/"
    stripe.api_key = stripe_keys["secret_key"]

    try:        
        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url + "/success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=domain_url + "cancelled",
            payment_method_types=["card"],
            mode="payment",
            line_items=[
                {
                    "price": "price_1NSJcsFjdMNhV4DT4UhixjCV",
                    "quantity": 1,
                  #   "currency": "usd",
                  #   "amount": "10",
                }
            ]
        )
        return jsonify({"sessionId": checkout_session["id"]})
    except Exception as e:
        return jsonify(error=str(e)), 403



if __name__ == '__main__':
   app.run(debug = True,host='0.0.0.0', port=0)
