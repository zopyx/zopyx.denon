import os
from bottle import route, run, template
from bottle import static_file

@route('/static/<filename>')
def server_static(filename):
        return static_file(filename, root=os.getcwd())

@route('/denon')
def denon():
    return template('denon.pt')

def main():
    run(host='0.0.0.0', port=10000)

if __name__ == '__main__':
    main()
