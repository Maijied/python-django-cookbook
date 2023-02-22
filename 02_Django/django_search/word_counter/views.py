from django.shortcuts import render


# Create your views here.
# This code renders the word_counter_index.html page when the index route is requested.
def index(request):
    return render(request, 'word_counter_index.html')


# This code is a view function for a Django web application. It takes in a request object and returns an HTML page
# with the number of words in the text provided in the request. The code first retrieves the text from the request
# object, then counts the number of words in it using the split() method. Finally, it renders an HTML page with the
# word count as data.
def counter(request):
    words = request.GET['word_count_text']
    count_text = len(words.split())
    return render(request, 'word_counter.html', {'data': count_text})


# This code is a view function for a Django web application. It takes in a POST request from the user, which contains
# text in the 'word_count_text' field. The function then splits the text into words and counts them, before rendering
# the 'word_counter.html' template with the count of words as data.
def counter_post(request):
    words = request.POST['word_count_text']
    count_text = len(words.split())
    return render(request, 'word_counter.html', {'data': count_text})
