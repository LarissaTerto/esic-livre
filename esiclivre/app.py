#!/usr/bin/env python
# coding: utf-8

import os
import subprocess

import cuidando_utils
from .views import api
from .browser import ESicLivre
from .sender import send_update_notifications


def create_app(settings_folder):
    app = cuidando_utils.create_app(settings_folder, api, init_sv='public')

    # TODO: colocar isso em um lugar descente...
    # @app.route('/static/<path:path>')
    # def send_templates(path):
    #     return send_from_directory('static/', path)

    # @app.route('/captcha')
    # def send_captcha():
    #     return send_file('static/captcha.jpg')

    @app.cli.command()
    def run_browser():
        '''Run browser.'''
        subprocess.check_call('Xvfb :10 -ac &', shell=True)
        os.environ['DISPLAY'] = ':10'
        ESicLivre(
            firefox=app.config['FIREFOX_PATH'],
            email=app.config['ESIC_EMAIL'],
            senha=app.config['ESIC_PASSWORD'],
            pasta=app.config['DOWNLOADS_PATH'],
        ).run()
        subprocess.check_call('killall Xvfb', shell=True)
        subprocess.check_call('killall firefox', shell=True)

    @app.cli.command()
    def send_notifications():
        '''Send notifications about Execucao updates.'''
        send_update_notifications()

    return app


def configure_logging(app):
    """Configure file(info) and email(error) logging."""

    if app.debug or app.testing:
        # Skip debug and test mode. Just check standard output.
        return

    import logging
    import logging.handlers

    # Set info level on logger, which might be overwritten by handers.
    # Suppress DEBUG messages.
    app.logger.setLevel(logging.INFO)

    info_log = os.path.join(app.config['LOG_FOLDER'], 'info.log')
    info_file_handler = logging.handlers.RotatingFileHandler(
        info_log, maxBytes=100000, backupCount=10)
    info_file_handler.setLevel(logging.INFO)
    info_file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]')
    )
    app.logger.addHandler(info_file_handler)
