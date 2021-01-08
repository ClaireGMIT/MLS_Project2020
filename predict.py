def predict():
    if not request.json:
      abort(400)
    # read iris data set
    df = pd.read_csv("https://raw.githubusercontent.com/ClaireGMIT/MLS_Project2020/main/powerproduction.csv") 
    X = df['speed']
    y = df['power']
    #Best fit straight line
    X_avg = np.mean(X)
    y_avg = np.mean(y)
    X_zero = X - X_avg
    y_zero = y - y_avg
    m = np.sum(X_zero * y_zero)/(np.sum(X_zero * X_zero))
    c = y_avg - m * X_avg
    f = lambda x: m * X + c

    model = kr.models.Sequential()
    model.add(kr.layers.Dense(1, input_shape=(1,), activation="linear", kernel_initializer='ones', bias_initializer='zeros'))
    model.compile('adam', loss='mean_squared_error')
    model.fit(X, y)