from flask import Flask, render_template

from my_app import create_app
import config

app = create_app(config.DevelopmentConfig)


if __name__ == '__main__':
    app.run(debug=True)