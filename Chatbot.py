import cleverbotfree.cbfree
import sys

#Speech recog
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")

#Cleverbot
cb = cleverbotfree.cbfree.Cleverbot()


def main():
    try:
        cb.browser.get(cb.url)
    except:
        cb.browser.close()
        sys.exit()
    while True:
        try:
            cb.get_form()
        except:
            sys.exit()
        userInput = input('User: ')
        if userInput == 'quit':
            break
        cb.send_input(userInput)
        bot = cb.get_response()
        print('Cleverbot: ', bot)
    cb.browser.close()

    
if __name__ == '__main__':
    main()