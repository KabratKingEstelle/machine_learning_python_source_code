# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 9:40 下午
# @Author  : Estelle
# @File    : Logistic$.py

class Logistic:
    '''
        Sig=1/(1+exp(-x))
    '''

    def Sigmoid(z):
        G_of_z = float(1.0 / float((1.0 + math.exp(-1.0 * z))))
        return G_of_z

    '''
        y = Sig(Theta*X)
    '''

    def Hypothesis(theta, x):
        z = 0
        for i in range(len(theta)):
            z += x[i] * theta[i]
        return Sigmoid(z)

    '''
       logloss=y*ln(pred)+(1-y)*ln(1-pred) 
       logloss_m = yln(pred_k)+(1-y)*ln(1-pred_k) k=1,2,3,...m, m: sample size
       pred = Hypothesis(theta)
    '''

    def Cost_Function(X, Y, theta, m):
        sumofErrors = 0
        for i in range(m):
            xi = X[i]
            hi = Hypothesis(theta, xi)
            if Y[i] == 1:
                error = Y[i] * math.log(hi)
            elif Y[i] == 0:
                error = (1 - Y[i]) * math.log(1 - hi)
            sumofErrors += error
        const = -1 / m
        J = const * sumofErrors
        print('cost is ', J)
        return J

    ''' 
      Deriva_logloss = (y-Sigmoid(Theta,X))/(Sigmoid(Theta,X)*(1-Sigmoid(Theta,X)))
      Deriva_sigmoid = Sigmoid(Theta,X)*(1-Sigmoid(Theta,X))
      Deriva_theta = Deriva_logloss*Deriva_sigmoid
                   = (y-Sigmoid(Theta,X))*X

    '''

    def Cost_Function_Derivative(X, Y, theta, j, m, alpha):
        sumErrors = 0
        for i in range(m):
            xi = X[i]
            xij = xi[j]
            hi = Hypothesis(theta, X[i])
            error = (hi - Y[i]) * xij
            sumErrors += error
        m = len(Y)
        constant = float(alpha) / float(m)
        J = constant * sumErrors
        return J

    ''' 
     Update all samples
    '''

    def Gradient_Descent(X, Y, theta, m, alpha):
        new_theta = []
        for j in range(len(theta)):
            CFDerivative = Cost_Function_Derivative(X, Y, theta, j, m, alpha)
            new_theta_value = theta[j] - CFDerivative
            new_theta.append(new_theta_value)
        return new_theta

    def Logistic_Regression(X, Y, theta, num_iters):
        m = len(Y)
        for x in range(num_iters):
            new_theta = Gradient_Descent(X, Y, theta, m, alpha)
            theta = new_theta
            if x % 100 == 0:
                print('theta', theta)
                print('cost is', Cost_Function(X, Y, theta, m))

    def Declare_Winner(base_model, X_test, Y_test, theta):
        score = 0
        winner = ''
        scikit_score = base_model.score(X_test, Y_test)
        length = len(X_test)
        for i in range(X_test):
            prediction = round(Hypothesis(X_test[i], theta))
            answer = Y_test[i]
            if prediction_answer:
                score += 1
        my_score = float(score) / float(length)
        if my_score > scikit_score:
            print('You wein')
        elif my_score == scikit_score:
            print('Its a tie')
        else:
            print('Scikit won')
        print('Your Score: ', my_score)
        print('Scikits Score: ', scikit_score)
