from app import create_app

app = create_app()

if __name__ == '__main__':
    port = app.config.get('PORT')
    debug = app.config.get('DEBUG')
    host = app.config.get('HOST')

    app.run(debug=debug, port=port, host=host)