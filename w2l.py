from talon import speech_system
from talon.engines.w2l import W2lEngine

# engine = W2lEngine(language='en_US-original-model', debug=False)
engine = W2lEngine(language='en_US-sconv-large-b2', debug=True)

# engine.register('', print)
speech_system.add_engine(engine)
speech_system.set_priority(['wav2letter'])
