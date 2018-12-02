from flask import Flask, jsonify, request, render_template, redirect
import json
import os
import subprocess

#variables
js = ''
app = Flask(__name__)

@app.route('/send', methods = ['GET','POST'])
def sendData():
	try:
		if (request.method == 'POST'):
			print('POST')
			command = 'Rscript'
			path2script = 'RL_r.R'
			cmd = [command, path2script]
			js = request.get_json()
			x = subprocess.check_call(cmd, shell=False)
			return redirect('get')
		else:
			print('GET')
			return render_template('temp.html')
	except Exception as e:
		return jsonify({'error': e})

@app.route('/get', methods = ['GET'])
def getData():
	with open('mvdata.json') as json_data:
		js = json.load(json_data)
		json_data.close()
	return jsonify(js)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 6999))
	app.run(host = '192.168.0.254', port = port, debug = True)