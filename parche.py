import tensorflow.keras.losses
import tensorflow.keras.layers

# Parches para evitar errores de importación con versiones antiguas de Keras
# Define dummies si no existen
if not hasattr(keras.losses, 'BinaryCrossentropy'):
    def BinaryCrossentropy(*args, **kwargs): pass
    keras.losses.BinaryCrossentropy = BinaryCrossentropy

if not hasattr(keras.losses, 'MeanSquaredError'):
    def MeanSquaredError(*args, **kwargs): pass
    keras.losses.MeanSquaredError = MeanSquaredError

if not hasattr(keras.layers, 'MultiHeadAttention'):
    class MultiHeadAttention:
        def __init__(self, *args, **kwargs): pass
        def __call__(self, *args, **kwargs): return self
    keras.layers.MultiHeadAttention = MultiHeadAttention

if not hasattr(keras.layers, 'LayerNormalization'):
    class LayerNormalization:
        def __init__(self, *args, **kwargs): pass
        def __call__(self, *args, **kwargs): return self
    keras.layers.LayerNormalization = LayerNormalization
