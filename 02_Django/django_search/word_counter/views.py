from django.shortcuts import render


# Create your views here.
def counter(request):
    text = request.GET['word_count_text']
    count_text = len(text.split())
    return render(request, 'word_counter.html', {'data': count_text})
