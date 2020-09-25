import cleverbotfree.cbfree
import sys
import speech_recognition as sr

""" r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said") """

#Cleverbot
cb = cleverbotfree.cbfree.Cleverbot()

def main():
    try:
        cb.browser.get(cb.url)
    except:
        cb.browser.close()
        sys.exit()
    while True:
        userInput = 0
        try:
            cb.get_form()
        except:
            sys.exit()

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak Anything internal:")
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            userInput = text
            if userInput == 'quit':
                break
            cb.send_input(userInput)
            bot = cb.get_response()
            print('Cleverbot: ', bot)            
        except:
            print("Sorry could not recognize what you said")
    cb.browser.close()

    
if __name__ == '__main__':
    main()