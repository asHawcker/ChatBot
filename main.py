import datetime
import os
import random
import time
import webbrowser
import pyttsx3

music_folder = 'D:\Songs'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def botm(mess):
    #time.sleep(1)
    print(f'Bot : {mess}')
    speak(mess)

hour = datetime.datetime.now().hour
print('\n\n========== WELCOME TO CHATBOT ===========\n')
botm('Hi')

if hour<12:
    botm(f'Good Morning!! How are you?')
elif 12>=hour<=4:
    botm(f'Good Afternoon!! How are you?')
else:
    botm(f'Good Evening!! How are you?')

running = True

while running:
    res = input('You : ').lower()
    try:
        if 'fine' in res:
            botm('Nice to hear that..\n\t\bHow may I help you.?')

        elif 'hi' in res:
            botm('Hii!! ,\nHow may in help you')

        elif 'bye' in res or res == 'exit':
            botm('Bye,\n\t\bIt was nice meeting you.\n\t\bQuitting.')
            for i in '12345':
                print('\t.')
            running = False

        elif ('how are you' ) in res or 'whats up' in res:
            a = random.randint(0,2)
            responses = ['All of my CPU Cores are working well. Thanks for asking.',
                'I am doing good, what about you?',
                'I am programmed well by Anurag. I hope you are also doing good.'
                ]
            botm(responses[a])
        
        elif 'who made you' in res:
            botm('I was made by Anurag Sharma.\n\t\bDo you want to check out his Instagram ??')
            res2= input('You:')
            res=''
            if 'yes' in res2.lower():
                webbrowser.open('www.instagram.com/anurag_showman')
            if 'no' in res2.lower():
                botm('Ok, No Problem.')
        
        elif ('how can you help me' or 'help me') in res:
            botm('''I am still learning but I can help you with many things.\n\t\bSee my command file for all commands.
                 Should I open it?''')
            res2= input('You:')
            res=''
            if 'yes' in res2.lower():
                os.startfile('guide.txt')
            if 'no' in res2.lower():
                botm('Ok, No Problem.')
        
        elif 'search' in res:
            res = res.replace('search ','')
            webbrowser.open_new_tab(f'www.google.com/{res}')
            botm('I have searched for it. Please check your browser.')
        
        elif 'google' in res:
            res = res.replace('google ','')
            webbrowser.open_new_tab(f'www.google.com/{res}')
            botm('I have googled it. Please check your browser.')
        
        elif 'who am i' in res:
            botm('I dont know you. But my creator Anurag knows you.\n\t\bThat\'s why he sent me to you. I don\'t know people I just help them.')
            
        elif 'nice' in res:
            botm('Thanks.')

        elif ('play' in res) and (('music' or 'song') in res):
            url = music_folder
            run =True
            while run:
                snum = random.randint(0,len(os.listdir(url)))
                if os.listdir(url)[snum].endswith('.mp3'):
                    os.startfile(os.path.join(url,os.listdir(url)[snum]))
                    botm(f'Playing {os.listdir(url)[snum]}...')
                    run = False
            
        elif ('add' or 'sum') or ('difference' or 'subtract') or 'solve' or ('divide' or 'multiply') in res:
            for at in ['add' , 'sum' , 'difference' , 'subtract' , 'solve' , 'divide' , 'multiply']:
                if at in res:
                    res = res.replace(at,'')
            sol = eval(res)
            botm(sol)

        elif 'who are you' in res:
            botm('I am a chatbot. I want to have a talk with you.')


        else:
            botm('I did not understand it. Maybe its not in my coding')
    
    except SyntaxError:
        botm('Please Try Again.....')
