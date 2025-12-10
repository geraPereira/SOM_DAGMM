import numpy as np
from minisom import MiniSom

def som_train(data, x=10, y=10, sigma=1, learning_rate= 0.06, iters= 10000, dataset='else'):
    input_len = data.shape[1]
    #print("SOM training started:")
    if dataset == 'ids':
        learning_rate = 0.6
        print("Learning rate set to 0.6 for ids dataset")
    elif dataset == 'kdd':
        learning_rate = 0.8
        print("Learning rate set to 0.8 for kdd dataset")
    else:
        learning_rate = learning_rate
        print("Learning rate set to default:", learning_rate)   
    som = MiniSom(x= x, y= y, input_len=input_len, sigma=sigma, learning_rate=learning_rate, neighborhood_function = "bubble")
    som.random_weights_init(data)
    som.train_random(data, iters)
    return som

def som_pred(som_model, data, outlier_percentage):
    model = som_model
    data = data.numpy()
    quantization_errors = np.linalg.norm(model.quantization(data) - data, axis=1)
    error_threshold = np.percentile(quantization_errors, 100*(1-outlier_percentage)+5)
    is_anomaly = quantization_errors > error_threshold
    y_pred = np.multiply(is_anomaly, 1)
    return y_pred