import requests
from flask import Flask, render_template


app = Flask(__name__)
app.secret_key = 'super secret'

@app.route('/', methods=['GET', 'POST'])
def index():
    query = '''query{
        cryptofish{
            id
            name
            status
            size
            cost
            planet {
                id
                name
            }
            owner{
                name
            }
            
        }
    }
    '''
    url = "http://localhost:5000/graphql"
    response = requests.post(url, json={'query': query})
    # convert to dict
    response = response.json()
    # get the data
    all_cryptofish = response['data']['cryptofish']
    for fish in all_cryptofish:
        fish['art'] = cryptofish_art(fish)
        print(fish['art'])
    # print(data)
    return render_template('index.html', all_cryptofish = all_cryptofish)

def cryptofish_art(cryptofish):
    art = '+------------+<br>'
    if cryptofish['planet']['id'] == '1':
        art += '|-°-rth-42-°-|<br>'
    elif cryptofish['planet']['id'] == '2':
        art += '|~".lab"².-"~|<br>'
    elif cryptofish['planet']['id'] == '3':
        art += '|-({m-wn².})-|<br>'
    elif cryptofish['planet']['id'] == '5':
        art += '|/x-!2``2!-x\|<br>'
    elif cryptofish['planet']['id'] == '4':
        art += '|=@c=.!.²=s@=|<br>'
    elif cryptofish['planet']['id'] == '6':
        art += '|-0o.m--54*>-|<br>'
    elif cryptofish['planet']['id'] == '7':
        art += '|^°ProT°oOd°^|<br>'

    if cryptofish['status'] == 'hungry':
        art += '|(+_+)hH(-3-)|<br>'
    elif cryptofish['status'] == 'sleepy':
        art += '|(-.-)zZz.ZZz|<br>'
    elif cryptofish['status'] == 'bored':
        art += '|(._.)bBb(:|)|<br>'
    elif cryptofish['status'] == 'playful':
        art += '|(-^o^-)/*°*p|<br>'
    elif cryptofish['status'] == 'happy':
        art += '|o("o")hahaha|<br>'
    elif cryptofish['status'] == 'grumpy':
        art += '|gRR(-_-")gRR|<br>'
    elif cryptofish['status'] == 'lonely':
        art += '|(;_;)l°n3r5.|<br>'

    if cryptofish['size'] == 'molecular':
        art += '|............|<br>'
    if cryptofish['size'] == 'tiny':
        art += '|°.°°..°°°...|<br>'
    elif cryptofish['size'] == 'small':
        art += '|°°°°°°°°°°°°|<br>'
    elif cryptofish['size'] == 'medium':
        art += '|o°o°°o°°°ooo|<br>'
    elif cryptofish['size'] == 'large':
        art += '|oooooooooooo|<br>'
    elif cryptofish['size'] == 'giant':
        art += '|oOoOOooOOOoo|<br>'
    elif cryptofish['size'] == 'colossal':
        art += '|ÔOOOOOOOOOOO|<br>'

    art += '+------|{}|<br>'.format(cryptofish['name'])


    

    return art



if __name__ == '__main__':
    app.run(debug=False, port=5002)