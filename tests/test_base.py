from flask_testing import TestCase
from flask import current_app, url_for

from main import app


class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLE'] = False # hacer token  (ataque cross site request)
        
        
        return app
    
    def test_app_exists(self):
        self.assertIsNotNone(current_app) # existe la aplicación
    
    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING']) # la app está en modo de test
    
    def test_index_redirects(self): # hacer un petición y que nos redirija
        response = self.client.get(url_for('index'))
        self.assertRedirects(response, url_for('hello'))
    
    def test_hello_get(self): # cuando la respuesta es exitosa nos regresa un 200, validar eso
        response = self.client.get(url_for('hello'))
        self.assert200(response)
    
    def test_hello_post(self): # cuando la petición es post y es exitosa
        fake_form = {
            'username': 'fake',
            'password': 'fake-password'
        }
        response = self.client.post(url_for('hello'), data=fake_form)

        self.assertRedirects(response, url_for('index'))

    def test_auth_blueprint_exists(self):
        self.assertIn('auth', self.app.blueprints)
    
    def test_auth_login_get(self):
        response = self.client.get(url_for('auth.login'))

        self.assert200(response)

    def test_auth_login_template(self):
        self.client.get(url_for('auth.login'))

        self.assertTemplateUsed('login.html')
