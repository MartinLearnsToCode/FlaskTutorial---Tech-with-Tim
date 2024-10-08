from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) # !!! True weg, wenn Production. Reruns App after changes in code