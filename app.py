from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
#from flask import *
from flask import Flask, request, jsonify


app = Flask(__name__)
@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save("uploaded.pdf")

        # Get form data
        goals = request.form.get('goals')
        obstacles = request.form.get('obstacles')
        skills = request.form.get('skill')

        # Create a new PDF file
        c = canvas.Canvas("output.pdf", pagesize=letter)

        # Set font and size
        c.setFont("Helvetica", 12)

        # Write form data to PDF
        c.drawString(50, 750, f"Goals: {goals}")
        c.drawString(50, 730, f"Obstacles: {obstacles}")
        c.drawString(50, 710, f"Skills: {skills}")

        # Save and close the PDF file
        c.save()

        return jsonify({"message": "success"})

if __name__ == '__main__':
    app.run(port=0)
