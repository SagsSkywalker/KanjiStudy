from flask import Flask, jsonify, request, render_template, redirect
import json
import os
import subprocess

#variables
js = ''
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/send', methods = ['GET','POST'])
def sendData():
	try:
		if (request.method == 'POST'):
			args = [request.args.get('id'), request.args.get('learnt')]
			command = 'Rscript'
			path2script = 'RL_r.R'
			cmd = [command, path2script] + args
			js = request.get_json()
			x = subprocess.check_call(cmd, shell=False)
			return redirect('get')
		else:
			print('GET')
			return jsonify({'res': 'OK'})
	except Exception as e:
		return jsonify({'error': e})

@app.route('/get', methods = ['GET'])
def getData():
	with open('kanji.json', encoding = 'utf-8-sig') as kan:
		jsk = json.load(kan)
		kan.close()
	with open('mvdata.json') as json_data:
		njs = []
		js = json.load(json_data)
		for i in range(len(js['clasification'])):
			njs.append(
			{
				'kanji' : jsk[i]['kanji'],
				'kun' : js['kun'][i],
				'on' : js['on'][i],
				'meaning' : js['meaning'][i],
				'strokes' : js['strokes'][i],
				'type' : js['type'][i],
				'learnt' : js['learnt'][i],
				'clasification' : js['clasification'][i]
			})
		json_data.close()
	return jsonify(njs)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 6999))
	app.run(port = port, debug = True)