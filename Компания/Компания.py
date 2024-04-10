import speech_recognition as sr


def recording():
    r = sr.Recognizer()

    with sr.Microphone(device_index=1) as voice:
        r.adjust_for_ambient_noise(voice)
        print('Слушаю...')
        audio = r.listen(voice, timeout=2)
        print(audio)

    try:
        speech = r.recognize_google(audio, language='ru-RU')
        print(f'Сказано: {speech}\nЗапись сохранена')

        # with open('File.txt', 'r+', encoding='utf-8') as file:
        #     file.write(f'{len(file.readlines()) + 1}. {speech}\n')
    except sr.UnknownValueError:
        print('Речь не распознана')


recording()
