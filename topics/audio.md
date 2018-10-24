# Contents
1. [**Audio with Python**](#audio-with-python)
    1. [Text to speech](#text-to-speech)
    2. [Markov chain to speech](#markov-chain-to-speech)
    3. [Recording audio](#recording-audio)


# Text to speech
Install [playsound](https://pypi.org/project/playsound/)
and [gTTs](https://gtts.readthedocs.io/en/latest/)
with *pip*.
```
pip install playsound
pip install gTTs
```

Convert the text from your poem to speech with Python
using [text-to-speech.py](..\scripts\text-to-speech.py) as a guide.

# Markov chain to speech
Convert the text from your Markov chain generated poem to speech with Python
using [markovify-to-speech.py](..\scripts\markovify-to-speech.py) as a guide.

# Recording audio
Install [sounddevice](https://python-sounddevice.readthedocs.io/)
and [PySoundFile](https://pysoundfile.readthedocs.io/en/0.9.0/)
with *pip*.
```
pip install sounddevice
pip install PySoundFile
```

Read your poem aloud and record with Python
using [record-audio.py](..\scripts\record-audio.py) as a guide.

After you commit and push your poem to GitHub,
[play it](audio.html).
