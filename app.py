from flask import Flask , render_template , request
import numpy as np
import pickle

from sklearn.preprocessing import StandardScaler


app = Flask(__name__)
model = pickle.load(open('KNeighbors_Classifier.pkl', 'rb'))

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    gender_female = 0
    gender_other = 0
    married_no = 0
    work_type_private=0
    work_type_self_employed = 0
    work_type_children = 0
    work_type_never_worked = 0
    reside_urban = 0
    smoke_never_smoked = 0
    
    if request.method == 'POST':
        gender_male=request.form['gender_male']
        if(gender_male=='male'):
            gender_male=1
            gender_female=0
            gender_other=0
        elif(gender_male=='female'):
            gender_male=0
            gender_female=1
            gender_other=0
        else:
            gender_male=0
            gender_female=0
            gender_other=1
        age = int(request.form['age'])
        hypertension_yes=request.form['hypertension_yes']
        if(hypertension_yes=='yes'):
            hypertension_yes=1
        else:
            hypertension_yes=0
        heart_disease_yes=request.form['heart_disease_yes']
        if(heart_disease_yes=='yes'):
            heart_disease_yes=1
        else:
            heart_disease_yes=0
        married_yes=request.form['married_yes']
        if(married_yes=='yes'):
            married_yes=1
            married_no=0
        else:
            married_yes=0
            married_no=1
        work_type_Govt_job=request.form['work_type_govt_job']
        if(work_type_Govt_job=='Govt_job'):
            work_type_Govt_job=1
            work_type_private=0
            work_type_self_employed=0
            work_type_children=0
            work_type_never_worked=0
        elif(work_type_Govt_job=='private'):
            work_type_Govt_job=0
            work_type_private=1
            work_type_self_employed=0
            work_type_children=0
            work_type_never_worked=0
        elif(work_type_Govt_job=='self_employed'):
            work_type_Govt_job=0
            work_type_private=0
            work_type_self_employed=1
            work_type_children=0
            work_type_never_worked=0
        elif(work_type_Govt_job=='children'):
            work_type_Govt_job=0
            work_type_private=0
            work_type_self_employed=0
            work_type_children=1
            work_type_never_worked=0
        else:
            work_type_Govt_job=0
            work_type_private=0
            work_type_self_employed=0
            work_type_children=0
            work_type_never_worked=1
        reside_rural=request.form['reside_rural']
        if(reside_rural=='rural'):
            reside_rural=1
            reside_urban=0
        else:
            reside_rural=0
            reside_urban=1
        glucose = float(request.form['glucose'])
        bmi = float(request.form['bmi'])
        smoke_smoked=request.form['smoke_smoked']
        if(smoke_smoked=='smoked'):
            smoke_smoked=1
            smoke_never_smoked=0
        else:
            smoke_smoked=0
            smoke_never_smoked=1
            
        input_data = ([[age,hypertension_yes,heart_disease_yes,glucose,bmi,gender_female,gender_male,gender_other,married_no,married_yes,work_type_Govt_job,work_type_never_worked,work_type_private,work_type_self_employed,work_type_children,reside_rural,reside_urban,smoke_never_smoked,smoke_smoked]])

        #input_data_numpy_array = np.asarray(input_data)

        #reshape_input_data = input_data_numpy_array.reshape(1,-1)

        prediction = model.predict(input_data)
        
        if(prediction[0]==0):
            return render_template('result.html',prediction_texts="You have very less chances of getting stroke!!!")
        else:
            return render_template('result.html',prediction_texts="You have very huge chances of getting stroke!!!")
    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)