#main   
from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from profanity_filter import ProfanityFilter
import spacy
nlp = spacy.load("en")

app = Flask(__name__)
api = Api(app)

profanity_args = reqparse.RequestParser()
profanity_args.add_argument("comment_id", type=int, help="comment id is required", required=True)
profanity_args.add_argument("comment", type=str, help="comment is required", required=True)

comment_json = {}


class User(Resource):
    


    def post(self, profane):
        args = profanity_args.parse_args()
        comment = args['comment']
        comment_id = args['comment_id']
        pf = ProfanityFilter()
        pf.extra_profane_word_dictionaries = {
            "en": {'4r5e', '5h1t', '5hit', 'a55', 'anal', 'anus', 'ar5e', 'arrse', 'arse', 'ass', 'ass-fucker', 'asses',
                   'assfucker', 'assfukka', 'asshole', 'assholes', 'asswhole', 'a_s_s', 'b!tch', 'b00bs', 'b17ch',
                   'b1tch', 'ballbag', 'balls', 'ballsack', 'bastard', 'beastial', 'beastiality', 'bellend', 'bestial',
                   'bestiality', 'bi+ch', 'biatch', 'bitch', 'bitcher', 'bitchers', 'bitches', 'bitchin', 'bitching',
                   'bloody', 'blow', 'job', 'blowjob', 'blowjobs', 'boiolas', 'bollock', 'bollok', 'boner', 'boob',
                   'boobs', 'booobs', 'boooobs', 'booooobs', 'booooooobs', 'breasts', 'buceta', 'bugger', 'bum',
                   'fucker', 'butt', 'butthole', 'buttmunch', 'buttplug', 'c0ck', 'c0cksucker', 'muncher', 'cawk',
                   'chink', 'cipa', 'cl1t', 'clit', 'clitoris', 'clits', 'cnut', 'cock', 'cock-sucker', 'cockface',
                   'cockhead', 'cockmunch', 'cockmuncher', 'cocks', 'cocksuck', 'cocksucked', 'cocksucker',
                   'cocksucking', 'cocksucks', 'cocksuka', 'cocksukka', 'cok', 'cokmuncher', 'coksucka', 'coon', 'cox',
                   'crap', 'cum', 'cummer', 'cumming', 'cums', 'cumshot', 'cunilingus', 'cunillingus', 'cunnilingus',
                   'cunt', 'cuntlick', 'cuntlicker', 'cuntlicking', 'cunts', 'cyalis', 'cyberfuc', 'cyberfuck',
                   'cyberfucked', 'cyberfucker', 'cyberfuckers', 'cyberfucking', 'd1ck', 'damn', 'dick', 'dickhead',
                   'dildo', 'dildos', 'dink', 'dinks', 'dirsa', 'dlck', 'dog-fucker', 'doggin', 'dogging',
                   'donkeyribber', 'doosh', 'duche', 'dyke', 'ejaculate', 'ejaculated', 'ejaculates', 'ejaculating',
                   'ejaculatings', 'ejaculation', 'ejakulate', 'f', 'u', 'c', 'k', 'e', 'r', 'f4nny', 'fag', 'fagging',
                   'faggitt', 'faggot', 'faggs', 'fagot', 'fagots', 'fags', 'fanny', 'fannyflaps', 'fannyfucker',
                   'fanyy', 'fatass', 'fcuk', 'fcuker', 'fcuking', 'feck', 'fecker', 'felching', 'fellate', 'fellatio',
                   'fingerfuck', 'fingerfucked', 'fingerfucker', 'fingerfuckers', 'fingerfucking', 'fingerfucks',
                   'fistfuck', 'fistfucked', 'fistfucker', 'fistfuckers', 'fistfucking', 'fistfuckings', 'fistfucks',
                   'flange', 'fook', 'fooker', 'fuck', 'fucka', 'fucked', 'fuckers', 'fuckhead', 'fuckheads', 'fuckin',
                   'fucking', 'fuckings', 'fuckingshitmotherfucker', 'fuckme', 'fucks', 'fuckwhit', 'fuckwit', 'fudge',
                   'packer', 'fudgepacker', 'fuk', 'fuker', 'fukker', 'fukkin', 'fuks', 'fukwhit', 'fukwit', 'fux',
                   'fux0r', 'f_u_c_k', 'gangbang', 'gangbanged', 'gangbangs', 'gaylord', 'gaysex', 'goatse', 'God',
                   'god-dam', 'god-damned', 'goddamn', 'goddamned', 'hardcoresex', 'hell', 'heshe', 'hoar', 'hoare',
                   'hoer', 'homo', 'hore', 'horniest', 'horny', 'hotsex', 'jack-off', 'jackoff', 'jap', 'jerk-off',
                   'jism', 'jiz', 'jizm', 'jizz', 'kawk', 'knob', 'knobead', 'knobed', 'knobend', 'knobhead',
                   'knobjocky', 'knobjokey', 'kock', 'kondum', 'kondums', 'kum', 'kummer', 'kumming', "Lauda",
                   "laude" 'kums', 'behenchod,' 'kunilingus', 'l3i+ch', 'l3itch', 'labia', 'lmfao', 'lust', 'lusting',
                   'm0f0', 'm0fo', 'm45terbate', 'ma5terb8', 'ma5terbate', 'masochist', 'master-bate', 'masterb8',
                   'masterbat*', 'masterbat3', 'masterbate', 'masterbation', 'masterbations', 'masturbate', 'mo-fo',
                   'mof0', 'mofo', 'mothafuck', 'mothafucka', 'mothafuckas', 'mothafuckaz', 'mothafucked',
                   'mothafucker', 'mothafuckers', 'mothafuckin', 'mothafucking', 'mothafuckings', 'mothafucks',
                   'mother', 'motherfuck', 'motherfucked', 'motherfucker', 'motherfuckers', 'motherfuckin',
                   'motherfucking', 'motherfuckings', 'motherfuckka', 'motherfucks', 'muff', 'mutha', 'muthafecker',
                   'muthafuckker', 'muther', 'mutherfucker', 'n1gga', 'n1gger', 'nazi', 'nigg3r', 'nigg4h', 'nigga',
                   'niggah', 'niggas', 'niggaz', 'nigger', 'niggers', 'nob', 'jokey', 'nobhead', 'nobjocky', 'nobjokey',
                   'numbnuts', 'nutsack', 'orgasim', 'orgasims', 'orgasm', 'orgasms', 'p0rn', 'pawn', 'pecker', 'penis',
                   'penisfucker', 'phonesex', 'phuck', 'phuk', 'phuked', 'phuking', 'phukked', 'phukking', 'phuks',
                   'phuq', 'pigfucker', 'pimpis', 'piss', 'pissed', 'pisser', 'pissers', 'pisses', 'pissflaps',
                   'pissin', 'pissing', 'pissoff', 'poop', 'porn', 'porno', 'pornography', 'pornos', 'prick', 'pricks',
                   'pron', 'pube', 'pusse', 'pussi', 'pussies', 'pussy', 'pussys', 'rectum', 'retard', 'rimjaw',
                   'rimming', 's', 'hit', 's.o.b.', 'sadist', 'schlong', 'screwing', 'scroat', 'scrote', 'scrotum',
                   'semen', 'sex', 'sh!+', 'sh!t', 'sh1t', 'shag', 'shagger', 'shaggin', 'shagging', 'shemale', 'shi+',
                   'shit', 'shitdick', 'shite', 'shited', 'shitey', 'shitfuck', 'shitfull', 'shithead', 'shiting',
                   'shitings', 'shits', 'shitted', 'shitter', 'shitters', 'shitting', 'shittings', 'shitty', 'skank',
                   'slut', 'sluts', 'smegma', 'smut', 'snatch', 'son-of-a-bitch', 'spac', 'spunk', 's_h_i_t', 't1tt1e5',
                   't1tties', 'teets', 'teez', 'testical', 'testicle', 'tit', 'titfuck', 'tits', 'titt', 'tittie5',
                   'tittiefucker', 'titties', 'tittyfuck', 'tittywank', 'titwank', 'tosser', 'turd', 'tw4t', 'twat',
                   'twathead', 'twatty', 'twunt', 'twunter', 'v14gra', 'v1gra', 'vagina', 'viagra', 'vulva', 'w00se',
                   'wang', 'wank', 'wanker', 'wanky', 'whoar', 'whore', 'willies', 'willy', 'xrated', 'xxx', 'aand',
                   'aandu', 'balatkar', 'beti', 'chod', 'bhadva', 'bhadve', 'bhandve', 'bhootni', 'ke', 'bhosad',
                   'bhosadi', 'boobe', 'chakke', 'chinaal', 'chinki', 'chodu', 'bhagat', 'chooche', 'choochi', 'choot',
                   'baal', 'chootia', 'chootiya', 'chuche', 'chuchi', 'chudai', 'khanaa', 'chudan', 'chut', 'dhakkan',
                   'maarli', 'chutad', 'chutadd', 'chutan', 'chutia', 'chutiya', 'gaand', 'gaandfat', 'gaandmasti',
                   'gaandufad', 'gandu', 'gashti', 'gasti', 'ghassa', 'ghasti', 'harami', 'haramzade', 'hawas',
                   'pujari', 'hijda', 'hijra', 'jhant', 'chaatu', 'jhantu', 'kamine', 'kaminey', 'kanjar', 'kutta',
                   'kamina', 'kutte', 'ki', 'aulad', 'jat', 'kuttiya', 'loda', 'lodu', 'lund', 'choos', 'khajoor',
                   'lundtopi', 'lundure', 'maa', 'maal', 'madarchod', 'mooh', 'mein', 'le', 'mutth', 'najayaz',
                   'aulaad', 'paidaish', 'paki', 'pataka', 'patakha', 'raand', 'randi', 'saala', 'saali', 'kutti',
                   'suar', 'tatte', 'tatti', 'bhosada', 'boba', 'chusu', 'tharak', 'tharki'
                   }}
        result  = pf.is_profane(comment)
        return {'comment_id':comment_id , 'comment': comment, 'status': result}

    def get(self, profane):
        args = profanity_args.parse_args()
        return {profane: args}

    def put(self, profane):
        args = profanity_args.parse_args()
        print(args["comment"])
        return {profane: args}


api.add_resource(User, "/user/<string:profane>")

if __name__ == "__main__":
    app.run(debug=True)
