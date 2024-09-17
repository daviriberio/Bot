from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.json
        mensagem = data.get('mensagem', '').lower()

        if mensagem == 'oi':
            return jsonify({"resposta": "Quer um bot ou alguma coisa?"})
        elif 'site' in mensagem:
            return jsonify({"resposta": "Tá, mais quer mais alguma coisa?"})
        else:
            return jsonify({"resposta": "Não entendi, pode reformular?"})

    return "Chatbot com Flask está funcionando!"

if __name__ == '__main__':
    app.run(debug=True)