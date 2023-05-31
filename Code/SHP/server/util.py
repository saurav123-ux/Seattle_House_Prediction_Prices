import json
import pickle
import numpy as np
__grade = None
__data_columns = None
__model = None

def get_estimated_price(grade,sqft_living,bathrooms,bedrooms):
    try:
        loc_index = __data_columns.index(grade.lower())
    except:
        loc_index=-1

    X = np.zeros(len(__data_columns))
    X[0] = sqft_living
    X[1] = bathrooms
    X[2] = bedrooms
    if loc_index >= 0:
        X[loc_index] = 1

    return  round(__model.predict([X])[0],2)


def get_grade_names():
    return __grade


def load_saved_artifacts():
    print('loading_saved_artifacts..start')
    global __data_columns
    global __grade

    with open('./artifacts/columns.json','r') as f:
        __data_columns=json.load(f)['data_columns']
        __grade=__data_columns[16:]
    global __model
    with open('./artifacts/Seattle_home_model.pickle','rb') as f:
        __model = pickle.load(f)
    print('loading saved artifacts..done')

if __name__=='__main__':
    load_saved_artifacts()
    print(get_grade_names())
    print(get_estimated_price('No_Construction',1680,3,2))
    print(get_estimated_price('high_Construction',12050 , 8, 6))


