from application import app, greet
from flask import Flask
from flask import request


def test_quick():
  a = "jeff"
  greeting = greet(a)
  assert greeting == "Hi jeff"
  
def test_home_page():
    response = app.test_client().get('/')
    assert response.status_code == 200
    print("Done.")


