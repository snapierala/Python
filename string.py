'''
atext='This is a text.'
atext.endswith('ext.')

quote='A good programmer is someone who always looks both ways before crossing a one-way street'

print(quote)
print(quote.upper())
print(quote.lower())

print(quote.endswith('street'))

print(quote.upper() .isupper())

print(quote.find('one'))

print(quote.replace('one','1'))

print(quote.split(' '))

drive = 'c:\\'
folder = 'scripts\\python\\'
file = 'test.py'

path = drive + folder + file
print('\n',path)

justText = r"text with\nnewline"
print('\n',justText)

justText="Mac Donald's"
print('\n',justText)


sometgingLikeNumber = '1000'
print(sometgingLikeNumber)
print(type(sometgingLikeNumber))
'''

'''
https://en.wikipedia.org/wiki/Monty_Python
'''
article = '''
Monty Python (also collectively known as the Pythons)[2][3] were a British surreal comedy group who created their sketch comedy show Monty Python's Flying Circus, which first aired on the BBC in 1969. Forty-five episodes were made over four series. The Python phenomenon developed from the television series into something larger in scope and impact, including touring stage shows, films, numerous albums, several books, and musicals. The Pythons' influence on comedy has been compared to the Beatles' influence on music.[4][5][6] Their sketch show has been referred to as "not only one of the more enduring icons of 1970s British popular culture, but also an important moment in the evolution of television comedy".[7]
Broadcast by the BBC between 1969 and 1974, Monty Python's Flying Circus was conceived, written, and performed by its members Graham Chapman, John Cleese, Terry Gilliam, Eric Idle, Terry Jones, and Michael Palin. Loosely structured as a sketch show, but with an innovative stream-of-consciousness approach, aided by Gilliam's animation, it pushed the boundaries of what was acceptable in style and content.[8][9] A self-contained comedy team responsible for both writing and performing their work, the Pythons had creative control which allowed them to experiment with form and content, discarding rules of television comedy. Following their television work, they began making films, which include Monty Python and the Holy Grail (1975), Life of Brian (1979) and The Meaning of Life (1983). Their influence on British comedy has been apparent for years, while in North America, it has coloured the work of cult performers from the early editions of Saturday Night Live through to more recent absurdist trends in television comedy. "Pythonesque" has entered the English lexicon as a result.
In a 2005 poll of over 300 comics, comedy writers, producers and directors throughout the English-speaking world to find "The Comedian's Comedian", three of the six Pythons members were voted to be among the top 50 greatest comedians ever: Cleese at No. 2, Idle at No. 21, and Palin at No. 30.[10][11]
'''
print(article.upper())
print(article.lower().replace('monty','flying'))
print(article.split(' '))
print('word python appears',article.lower().count('python'),'times')
 
print('to print the \\ you need to put \\ twice in your text like this: \\\\')
print('The best hits of \'80s!!!')
print("The best hits of '80s!!!")
amountPLN=234
print('cur','\texchange','amount')
print('USD',"\t",3.65,"\t",amountPLN/3.65)
print('EUR','\t',4.23,"\t",amountPLN/4.23)
valueAsText = '123.45'
factor =1.23
print('value is ', valueAsText,'factor is',factor,'value*factor=',float(valueAsText)*factor)


