from keras.datasets import boston_housing
from keras import models
from keras import layers
import numpy as np
#######################################################
# 读取数据
def load_data(path='boston_housing.npz', test_split=0.2, seed=113):
    """Loads the Boston Housing dataset.

    # Arguments
        path: path where to cache the dataset locally
            (relative to ~/.keras/datasets).
        test_split: fraction of the data to reserve as test set.
        seed: Random seed for shuffling the data
            before computing the test split.

    # Returns
        Tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`.
    """
    assert 0 <= test_split < 1
    f = np.load(path)
    x = f['x']
    y = f['y']
    f.close()

    np.random.seed(seed)
    indices = np.arange(len(x))
    np.random.shuffle(indices)
    x = x[indices]
    y = y[indices]
    x_train = np.array(x[:int(len(x) * (1 - test_split))])
    y_train = np.array(y[:int(len(x) * (1 - test_split))])
    x_test = np.array(x[int(len(x) * (1 - test_split)):])
    y_test = np.array(y[int(len(x) * (1 - test_split)):])
    return (x_train, y_train), (x_test, y_test)
#######################################################

# 数据处理
(train_data, train_traget), (test_data, test_targets) = load_data()
mean = train_data.mean(axis=0)  # mean是求平均值，axis=0那么输出矩阵是1行，是求一列的平均值
train_data -= mean
std = train_data.std(axis=0)  # std是求标准差 axis=0计算每一列的标准差
train_data /= std
test_data -= mean
test_data /= std
##

# 构建网络
def build_model():
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu',
                           input_shape=(train_data.shape[1],)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    return model
##
# k折验证方法
k = 4
num_val_samples = len(train_data)//k
num_epochs = 100
all_scores = []
for i in range(k):
    print("processing fold #", i)
    val_data = train_data[i*num_val_samples:(i+1)*num_val_samples]
    val_targets = train_traget[i*num_val_samples:(i+1)*num_val_samples]
    partial_train_data = np.concatenate([
        train_data[:i*num_val_samples],
        train_data[(i+1)*num_val_samples:]],
        axis=0
    )
    partial_train_targets = np.concatenate(
        [train_traget[:i*num_val_samples],
         train_traget[(i+1)*num_val_samples:]],
        axis=0
    )
    model = build_model()
    model.fit(partial_train_data, partial_train_targets,
            epochs=num_epochs, batch_size=1, verbose=0)
    val_mse, val_mae = model.evaluate(val_data, val_targets, verbose=0)
    all_scores.append(val_mae)
print(all_scores)
