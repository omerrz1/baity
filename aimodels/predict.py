
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import numpy  as np 
import pickle

def predictEmotion(text):

    emotions = [
    'admiration',
    'amusement',
    'anger',
    'annoyance',
    'approval',
    'caring',
    'confusion',
    'curiosity',
    'desire',
    'disappointment',
    'disapproval',
    'disgust',
    'embarrassment',
    'excitement',
    'fear',
    'gratitude',
    'grief',
    'joy',
    'love',
    'nervousness',
    'optimism',
    'pride',
    'realization',
    'relief',
    'remorse',
    'sadness',
    'surprise',
    'neutral']

    model = load_model('mods/emotions.h5')
    tokeniser = pickle.load(open('mods/emotions_tokeniser.pickle','rb'))

    seq =tokeniser.texts_to_sequences([text])
    padded_seq = pad_sequences(seq,maxlen=50,padding='post')

    predictions = model.predict(padded_seq)

    return emotions[np.argmax(predictions)]
