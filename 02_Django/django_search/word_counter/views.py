from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'word_counter_index.html')


def counter(request):
    words = request.GET['word_count_text']
    count_text = len(words.split())
    return render(request, 'word_counter.html', {'data': count_text})
