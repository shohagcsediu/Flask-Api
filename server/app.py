from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/survey'
app.debug = True
db = SQLAlchemy(app)

class feedbacks(db.Model):
    __tablename__ = 'feedbacks'
    email = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=False)
    aboutus = db.Column(db.String(), nullable=False)
    consultation = db.Column(db.String(), nullable=False)
    designsugges = db.Column(db.String(), nullable=False)
    requirements = db.Column(db.String(), nullable=False)
    servicefuture = db.Column(db.String(), nullable=False)
    recommendus = db.Column(db.String(), nullable=False)
    satisfiedwithus = db.Column(db.String(), nullable=False)
    answer = db.Column(db.String(), nullable=False)
    reviewpromos = db.Column(db.String(), nullable=False)
    sendphotous = db.Column(db.String(), nullable=False)

    def __init__(self, phone, name, email, aboutus, consultation, designsugges, requirements, servicefuture, recommendus, satisfiedwithus, answer, reviewpromos, sendphotous):
        self.phone = phone
        self.name = name
        self.email = email
        self.aboutus = aboutus
        self.consultation = consultation
        self.designsugges = designsugges
        self.requirements = requirements
        self.servicefuture = servicefuture
        self.recommendus = recommendus
        self.satisfiedwithus = satisfiedwithus
        self.answer = answer
        self.reviewpromos = reviewpromos
        self.sendphotous = sendphotous

@app.route('/')
def index():
    return 'hello'

@app.route('/test', methods=['GET'])
def test():
    return{
        'test': 'test'
    }

@app.route('/feedbacks', methods=['GET'])
def getfeedback():
    gfeedbacks = feedbacks.query.all()
    output = []
    for feedback in gfeedbacks:
        currFeedback = {}
        currFeedback['phone']= feedback.phone
        currFeedback['name']= feedback.name
        currFeedback['email']= feedback.email
        currFeedback['aboutus']= feedback.aboutus
        currFeedback['consultation']= feedback.consultation
        currFeedback['designsugges']= feedback.designsugges
        currFeedback['requirements']= feedback.requirements
        currFeedback['servicefuture']= feedback.servicefuture
        currFeedback['recommendus']= feedback.recommendus
        currFeedback['satisfiedwithus']= feedback.satisfiedwithus
        currFeedback['answer']= feedback.answer
        currFeedback['reviewpromos']= feedback.reviewpromos
        currFeedback['sendphotous']= feedback.sendphotous

        output.append(currFeedback)
    return jsonify(output)

@app.route('/pfeedbacks', methods=['POST'])
def pfeedbacks():
    # bookData = request.get_json()
    feedbkData = request.get_json(force=True)
    print(' json: ', feedbkData)
    # print(bookData)
    feedback = feedbacks(phone=feedbkData['phone'], name=feedbkData['name'], email=feedbkData['email'], aboutus=feedbkData['aboutus'], consultation=feedbkData['consultation'], designsugges=feedbkData['designsugges'], requirements=feedbkData['requirements'], servicefuture=feedbkData['servicefuture'], recommendus=feedbkData['recommendus'], satisfiedwithus=feedbkData['satisfiedwithus'], answer=feedbkData['answer'], reviewpromos=feedbkData['reviewpromos'], sendphotous=feedbkData['sendphotous'])
    db.session.add(feedback)
    db.session.commit()
    return jsonify(feedbkData)
    
# app.run(port=5000)

if __name__ == '__main__':
    app.run(debug=True)