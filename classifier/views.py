from django.shortcuts import render
from django.shortcuts import render
import pickle

model = pickle.load(open('spam_model.pkl', 'rb'))
vectorizer = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))

def home(request):
    result = ""

    if request.method == "POST":
        message = request.POST['message']

        msg_tf = vectorizer.transform([message])

        prediction = model.predict(msg_tf)

        if prediction[0] == 0:
            result = "Spam"
        else:
            result = "Not Spam"

    return render(request, 'index.html', {'result': result})

# Create your views here.
