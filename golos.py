import speech_recognition as sr

r = sr.Recognizer()
A = '12345678'
B = 'ABCDEFGH'



def main():
    while True:
        try:
            while True:
                i = 0
                with sr.Microphone() as mic:
                    r.adjust_for_ambient_noise(source=mic, duration=0.5)
                    audio = r.listen(source=mic)
                    vvod = r.recognize_google(audio_data=audio, language='ru-RU').upper()
                if vvod == 'СТАРТ' and i == 0:
                    i += 1
                    return vvod
                #elif vvod != 'СТАРТ' and i == 0:
                   # print('Неверная команда')
                else:
                    if vvod[:9] == 'ДЕЛАЙ ХОД':
                        vvod = vvod[9:]
                        vvod = vvod.replace(' ', '')
                        vvod = vvod.replace('ОДИН', '1')
                        vvod = vvod.replace('ДВА', '2')
                        vvod = vvod.replace('ТРИ', '3')
                        vvod = vvod.replace('ЧЕТЫРЕ', '4')
                        vvod = vvod.replace('ПЯТЬ', '5')
                        vvod = vvod.replace('ШЕСТЬ', '6')
                        vvod = vvod.replace('СЕМЬ', '7')
                        vvod = vvod.replace('ВОСЕМЬ', '8')
                        vvod = vvod.replace('И', 'I')
                        vvod = vvod.replace('Б', 'B')
                        vvod = vvod.replace('А', 'A')
                        vvod = vvod.replace('Ц', 'C')
                        vvod = vvod.replace('Ф', 'F')
                        vvod = vvod.replace('Е','E')
                        if len(vvod) < 4:
                            print('Неверные координаты, повторите еще раз')
                        else:
                            if vvod[0] in B and vvod[2] in B and vvod[1] in A and vvod[3] in A:
                                return vvod
                            else:
                                print('Неверные координаты')
                    else:
                        print('Неверная команда')
        except sr.UnknownValueError:
            print('Нечеткий ввод, повторите еще раз')
        except sr.RequestError:
            print("Check your Internet Connection, please")
        except sr.WaitTimeoutError:
            print("Проверьте ваш микрофон")
main()