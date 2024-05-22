from django.http import HttpResponse

def about (request):
    return HttpResponse('<h1>Akulenko Alina</h1>'
                        '<h2>Date of birth</h2>'
                        '<p>21.05.2003</p>'
                        '<h2>Age</h2>'
                        '<p>21</p>'
                        '<h2>Phone number</h2>'
                        '<p>0956967060</p>'
                        '<h2>Summary</h2>'
                        '<p>I`m happy and crative persen who can do everything that people wantind from me</p>'
                        '<h2>Education</h2>'
                        '<p>I am learning the Cybersusurity in the Kharkiv National University of economics named by Simon Kuznets.</p>'
                        '<p>Ended education in Kharkiv Liceum #168.</p>'
                        '')
def home (request):
    return HttpResponse('<h1>Django</h1>'
                        '<p>Django — це високорівневий веб-фреймворк Python, який заохочує швидку розробку та чистий, прагматичний дизайн. Створений досвідченими розробниками, він впорається з більшою частиною клопоту веб-розробки, тому ви можете зосередитися на написанні свого додатка без потреби винаходити колесо. Це безкоштовно та з відкритим кодом.</p>'
                        '<h2>Швидко</h2>'
                        '<p>Django було розроблено, щоб допомогти розробникам якнайшвидше перевести додатки від концепції до завершення.</p>'
                        '<h2>Безпечно</h2>'
                        '<p>Django серйозно ставиться до безпеки та допомагає розробникам уникати багатьох типових помилок безпеки</p>'
                        '<h2>Масштабовано</h2>'
                        '<p>Деякі з найзавантаженіших веб-сайтів використовують здатність Django швидко та гнучко .lмасштабуватися</p>')