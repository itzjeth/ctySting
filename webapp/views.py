from django.http import HttpResponse
from django.shortcuts import render,redirect
#from django.core.mail import send_mail
#from django.conf import settings
from webapp.forms import ReviewForm
from webapp.models import Review

#from chatterbot import ChatBot
#from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer


#bot = ChatBot('chatbot', read_only=False,
            #logic_adapters=[
                #{

                    #'import_path':'chatterbot.logic.BestMatch',
                    #'maximun_similarity_threshold':0.95

                #}
#])

#list_to_train = [
    #"i love you ",
    #"i love you too <3",
    #"hi there",
    #"What's your name?",
    #"im ",
    #"Nice to meet you",
    #"whatsyour name",
   # "I'm Sting",
    #"What is your fav food?",
    #"I like fish",
    #"What is your favorite color?",
    #"I like black",
    #"Who create sting chatbot?",
    #"The one who create me is jethro jabay",
    #"first name of cvsu bacoor?",
    #"Cavite State University Bacoor",
    #"cvsu president?",
    #"Dr. Hernando D. Robles",
    #"history of cvsu",
   # "The state university was first established by the Thomasites as an intermediate school, named Indang Intermediate School in 1906",
    #"cvsu website",
    #"Here it is https://cvsu.edu.ph/",
    #"nice one",
    #"thank you :)",
  
#]
#corpus
#ChatterBotCorpusTrainer = ChatterBotCorpusTrainer(bot)
#corpusend
#list_trainer = ListTrainer(bot)
#list_trainer.train(list_to_train)
#corpus
#ChatterBotCorpusTrainer.train('chatterbot.corpus.english')
#corpusend
def home_page(request,):
    
    #if request.method == 'POST':
        #name = request.POST['name']
        #email = request.POST['email']
       # message = request.POST['message']
       
       # send_mail(
           # name,#title
          #  message,#message
          #  'settings.EMAIL_HOST_USER', #sender if not available
          #  [email], #receiver email
          #  fail_silently=False)
    return render(request, 'pages/chatbot.html')


def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)

def userReview(request):  
     if request.method=="POST":  
        form = ReviewForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()
                return redirect('rizz/')  
            except:  
               return render(request, "error.html")
            else :
                form = ReviewForm()
                return render(request, 'home.html',{'form':form})

   
















