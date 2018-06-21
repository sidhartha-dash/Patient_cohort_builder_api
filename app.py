from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_restful import Resource, Api
from random import randint

app = Flask(__name__)
api = Api(app)

app.config['MONGO_DBNAME'] = 'db_cohort_builder'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/db_cohort_builder'

app.url_map.strict_slashes = False  # Disable redirecting on POST method from /star to /star/

mongo = PyMongo(app)


class MarketDefinition(Resource):
    def get(self, name):
        market_def = mongo.db.market_definition
        res = market_def.find_one({'name': name})
        if res:
            #TODO
            date = '2018-06-21'  #hard coded
            user_id = randint(1, 199)  #hard coded
            output = {'name': res['name'], 'therapy_area': res['therapy_area'],
                      'sub_therapy_area': res['sub_therapy_area'], 'description': res['description'],
                      'icd_codes': res['icd_codes'], 'hcps_codes': res['hcps_codes'], 'cpt_codes': res['cpt_codes'],
                      'ndc_codes': res['ndc_codes'], 'loinc_codes': res['loinc_codes'], 'date_creation': date,
                      'user_id': user_id}
        else:
            output = "No such name"
        return jsonify({'result': output})


class MarketDefinitionList(Resource):
    def get(self):

        # TODO
        date = '2018-06-21'  # hard coded
        user_id = randint(1, 199)  # hard coded

        market_def = mongo.db.market_definition
        output = []
        for res in market_def.find():
            output.append({'name': res['name'], 'therapy_area': res['therapy_area'],
                           'sub_therapy_area': res['sub_therapy_area'], 'description': res['description'],
                           'icd_codes': res['icd_codes'], 'hcps_codes': res['hcps_codes'],
                           'cpt_codes': res['cpt_codes'], 'ndc_codes': res['ndc_codes'],
                           'loinc_codes': res['loinc_codes'], 'date_creation': date, 'user_id': user_id})
        return jsonify({'result': output})

    def post(self):
        market_def = mongo.db.market_definition
        data = request.json

        if 'name' in data:
            name = data['name']
        else:
            name = None

        if 'therapy_area' in data:
            therapy_area = data['therapy_area']
        else:
            therapy_area = None

        if 'sub_therapy_area' in data:
            sub_therapy_area = data['sub_therapy_area']
        else:
            sub_therapy_area = None

        if 'description' in data:
            description = data['description']
        else:
            description = None

        # TODO
        if 'icd_codes' in data:
            icd_codes = data['icd_codes']  # hard coded
        else:
            icd_codes = None

        if 'hcps_codes' in data:
            hcps_codes = data['hcps_codes']  # hard coded
        else:
            hcps_codes = None

        if 'cpt_codes' in data:
            cpt_codes = data['cpt_codes']  # hard coded
        else:
            cpt_codes = None

        if 'ndc_codes' in data:
            ndc_codes = data['ndc_codes']  # hard coded
        else:
            ndc_codes = None

        if 'loinc_codes' in data:
            loinc_codes = data['loinc_codes']  # hard coded
        else:
            loinc_codes = None

        if 'date_creation' in data:
            date_creation = data['date_creation']  # hard coded
        else:
            date_creation = None

        if 'user_id' in data:
            user_id = data['user_id']  # hard coded
        else:
            user_id = None

        market_def_id = market_def.insert({'name': name, 'therapy_area': therapy_area,
                                           'sub_therapy_area': sub_therapy_area, 'description': description,
                                           'icd_codes': icd_codes, 'hcps_codes': hcps_codes, 'cpt_codes': cpt_codes,
                                           'ndc_codes': ndc_codes, 'loinc_codes': loinc_codes,
                                           'date_creation': date_creation, 'user_id': user_id})
        new_market_def = market_def.find_one({'_id': market_def_id})
        output = {'name': new_market_def['name'], 'therapy_area': new_market_def['therapy_area'],
                  'sub_therapy_area': new_market_def['sub_therapy_area'], 'description': new_market_def['description'],
                  'icd_codes': new_market_def['icd_codes'], 'hcps_codes': new_market_def['hcps_codes'],
                  'cpt_codes': new_market_def['cpt_codes'], 'ndc_codes': new_market_def['ndc_codes'],
                  'loinc_codes': new_market_def['loinc_codes'], 'date_creation': new_market_def['date_creation'],
                  'user_id': new_market_def['user_id']}
        return jsonify({'result': output})


api.add_resource(MarketDefinitionList, '/market_definition')
api.add_resource(MarketDefinition, '/market_definition/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)