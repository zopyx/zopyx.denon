import os
from bottle import route, run, template
from bottle import static_file, default_app

cwd = os.path.dirname(__file__)

@route('/static/<filename>')
def server_static(filename):
        return static_file(filename, root=cwd)

@route('/denon')
def denon():
    return template(os.path.join(cwd, 'denon.pt'))

def main():
#    run(host='0.0.0.0', port=10000)
    application = default_app()
    from paste import httpserver
    httpserver.serve(application, host='0.0.0.0', port=10000)

if __name__ == '__main__':
    main()
