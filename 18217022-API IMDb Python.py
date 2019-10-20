import requests
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

def searchbyJudul(judul):
    url = "http://www.omdbapi.com/?apikey=dbaa791d&s="+judul
    res = requests.get(url)
    ret = []

    for data in res.json()['Search']:
        tmp = {
            'ID_IMDb': data ['imdbID'],
            'Judul': data['Title'],
            'Poster': data['Poster'],
            'Tahun': data['Year'],
            'Jenis': data['Type']
        }
        ret.append(tmp)
    return jsonify(ret)

def searchbyTahun(judul,tahun):
    url = "http://www.omdbapi.com/?apikey=dbaa791d&s="+judul+"&y="+tahun
    res = requests.get(url)
    ret = []

    for data in res.json()['Search']:
        tmp = {
            'ID_IMDb': data ['imdbID'],
            'Judul': data['Title'],
            'Poster': data['Poster'],
            'Tahun': data['Year'],
            'Jenis': data['Type']
        }
        ret.append(tmp)
    return jsonify(ret)


@app.route('/movie', methods=['GET'])
def index():
    if request.args.get('judul') != None:
        if request.args.get('tahun') == None:
            return searchbyJudul(request.args.get('judul'))
        else:
            return searchbyTahun(request.args.get('judul'),request.args.get('tahun'))
    else:
        ret = {
            'code': 400,
            'description': "Bad Request. Parameter Judul Harus Terpenuhi"
        }
        return jsonify(ret)


if __name__ == '__main__':
    app.run()
