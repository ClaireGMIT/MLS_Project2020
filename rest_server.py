from flask import Flask, url_for, request, redirect, abort, jsonify
from Tablets2DAO import tabletsDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')

#@app.route('/')
#def index():
#    return "hello"

#get all
# curl http://127.0.0.1:5000/tablets
@app.route('/tablets')
def getAll():
    return jsonify(tabletsDAO.getAll())

# find by Batch_No
@app.route('/tablets/<Batch_No>')
def findByID(Batch_No):
    return jsonify(tabletsDAO.findByID(Batch_No))

#Create
#curl -X POST -d "{\"Batch_No\":1000, \"API_Lot_No\":\"AA\", \"API_Particle_Size\":\"Large\", \"Screen_Size\":5, \"Blend_Time\":15, \"Compressor\":\"Compress2\", \"Inlet_Temp\":110, \"Spray_Rate\":400, \"Dissolution\":75}" -H Content-Type:application/json http://127.0.0.1:5000/tablets
@app.route('/tablets', methods=['POST'])
def create():
    if not request.json:
        abort(400)
    tabprdn = {
        "Batch_No": request.json["Batch_No"], 
        "API_Lot_No": request.json["API_Lot_No"],
        "API_Particle_Size": request.json["API_Particle_Size"], 
        "Screen_Size": request.json["Screen_Size"], 
        "Blend_Time": request.json["Blend_Time"], 
        "Compressor": request.json["Compressor"], 
        "Inlet_Temp": request.json["Inlet_Temp"], 
        "Spray_Rate": request.json["Spray_Rate"], 
        "Dissolution": request.json["Dissolution"] 
    }
    return jsonify(tabletsDAO.create(tabprdn))
    return "served by create"


#update
# curl -X PUT -d "{\"API_Lot_No\":\"AB\", \"API_Particle_Size\":\"Large\", \"Screen_Size\":\"5\", \"Blend_Time\":89, \"Compressor\":\"Compress1\", \"Inlet_Temp\":110, \"Spray_Rate\":400, \"Dissolution\":75}" -H Content-Type:application/json http://127.0.0.1:5000/tablets/1000
@app.route('/tablets/<Batch_No>', methods=['PUT'])
def update(Batch_No):
    foundBatch=tabletsDAO.findByID(Batch_No)
    print(foundBatch)
    if foundBatch == {}:
        return jsonify({}), 404
    currentBatch = foundBatch
    if 'Batch_No' in request.json:
        currentBatch['Batch_No'] = request.json['Batch_No']
    if 'API_Lot_No' in request.json:
        currentBatch['API_Lot_No'] = request.json['API_Lot_No']
    if 'API_Particle_Size' in request.json:
        currentBatch['API_Particle_Size'] = request.json['API_Particle_Size']    
    if 'Screen_Size' in request.json:
        currentBatch['Screen_Size'] = request.json['Screen_Size']        
    if 'Blend_Time' in request.json:
        currentBatch['Blend_Time'] = request.json['Blend_Time']  
    if 'Compressor' in request.json:
        currentBatch['Compressor'] = request.json['Compressor'] 
    if 'Inlet_Temp' in request.json:
        currentBatch['Inlet_Temp'] = request.json['Inlet_Temp'] 
    if 'Spray_Rate' in request.json:
        currentBatch['Spray_Rate'] = request.json['Spray_Rate'] 
    if 'Dissolution' in request.json:
        currentBatch['Dissolution'] = request.json['Dissolution'] 
    tabletsDAO.update(currentBatch)
    #return jsonify(currentBatch)
    return jsonify(tabletsDAO.update(tabprdn))

#delete
# curl -X DELETE http://127.0.0.1:5000/tablets/1000
@app.route('/tablets/<Batch_No>', methods=['DELETE'])
def delete(Batch_No):
    tabletsDAO.delete(Batch_No)
    return jsonify({"done":True})


if __name__ == "__main__":
    app.run(debug=True)