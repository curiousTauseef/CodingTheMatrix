########                                     ######## 
# Hi there, curious student.                        #
#                                                   #
# This submission script runs some tests on your    #
# code and then uploads it to Coursera for grading. #
#                                                   #
# Changing anything in this script might cause your #
# submissions to fail.                              #
########                                     ########

import io, os, sys, doctest, traceback, importlib, urllib.request, urllib.parse, urllib.error, base64, hashlib, random, ast

URL                 = 'matrix-001'
part_friendly_names = ['Vector Class']
groups              = [[('LMt7OXMcj4gJbRun', 'Vector Class, Part 1', ">>> v = Vec({'a','b','c','d', 1}, {'a':2,'c':1,'d':4})\n>>> print(test_format([v[x] for x in 'abcd']))\n>>> print(test_format(v[1]))\n>>> v = Vec({1},{1:2})\n>>> print(test_format(v[1]))\n"), ('GyW38nINeQ9JTHed', 'Vector Class, Part 2', ">>> v = Vec({'a','b','c','d'}, {'a':2,'c':1,'d':4})\n>>> v['a'] = 3\n>>> print(test_format([v[x] for x in 'abcd']))\n>>> v['b'] = 9\n>>> print(test_format([v[x] for x in 'abcd']))\n>>> v['c'] = 0\n>>> print(test_format([v[x] for x in 'abcd']))\n"), ('nDGdTq55hscA70NN', 'Vector Class, Part 3', ">>> v1 = Vec({'a','b','c','d'}, {'a':2,      'c':1,'d':4})\n>>> v2 = Vec({'a','b','c','d'}, {'a':2,'b':0,'c':1,'d':4})\n>>> v3 = Vec({'a','b','c','d'}, {'b':0,'a':2,'c':1,'d':4})\n>>> v4 = Vec({'a','b','c','d'}, {'a':3,      'c':1,'d':4})\n>>> v5 = Vec({'a','b','c','d'}, {            'c':1,'d':4})\n>>> v7 = Vec({'b','a','c','d'}, {'c':1,'a':2,'d':4,'e':1})\n>>> print(test_format(v1 == v1))\n>>> print(test_format(v1 == v2))\n>>> print(test_format(v1 == v3))\n>>> print(test_format(v1 == v4))\n>>> print(test_format(v1 == v5))\n>>> print(test_format(v1 == v7))\n>>> print(test_format(Vec({True, False}, {True: 1}) == Vec({True, False}, {False: 0})))\n"), ('JJlIn0jkR2s1ZpYz', 'Vector Class, Part 4', ">>> u = Vec({'a','b'},{'a':1})\n>>> v = Vec({'a','b'},{'b':2})\n>>> w1 = u + v\n>>> print(test_format([u['a'], u['b']]))\n>>> print(test_format([v['a'], v['b']]))\n>>> w2 = v + u\n>>> print(test_format([w1['a'], w1['b']]))\n>>> print(test_format([w2['a'], w2['b']]))\n>>> w3 = w1 + w1 + u\n>>> print(test_format([w3['a'], w3['b']]))\n>>> u2 = u + Vec(u.D, {}) \n>>> print(test_format([u2['a'], u2['b']]))\n"), ('jAfx2JAr4uCRVERt', 'Vector Class, Part 5', ">>> u = Vec({'a','b','c'}, {})\n>>> v = Vec({'a','b','c'}, {'a': 1, 'b': 2})\n>>> w = Vec({'a','b','c'}, {'c': 1, 'b': 3})\n>>> x = Vec({'a','b','c'}, {'a': -1, 'c': 1, 'b': 3})\n>>> print(test_format(dot(u, u)))\n>>> print(test_format(dot(u, v)))\n>>> print(test_format(dot(u, w)))\n>>> print(test_format(dot(v, w)))\n>>> print(test_format([u[q] for q in 'abc']))\n>>> print(test_format([v[q] for q in 'abc']))\n>>> print(test_format(dot(x, w) == dot(w, x)))\n>>> print(test_format(dot(x, v)))\n"), ('gkt6hIimmWeVvxIr', 'Vector Class, Part 6', ">>> u = -Vec({'a','b','c'}, {})\n>>> v = -Vec({'a','b','c'}, {'a': 1, 'b': 2})\n>>> print(test_format([(-u)[x] for x in 'abc']))\n>>> print(test_format(v == -v))\n>>> print(test_format([(-(-v))[x] for x in 'abc']))\n>>> print(test_format(u['a']))\n>>> print(test_format(v['b']))\n"), ('4tvH0n1dkdsP0ctt', 'Vector Class, Part 7', ">>> u = Vec({'a','b','c'}, {})\n>>> v = Vec({'a','b','c'}, {'a': 1, 'b': 2})\n>>> print(test_format([(3*u)[x] for x in 'abc']))\n>>> print(test_format([(0*v)[x] for x in 'abc']))\n>>> w = Vec({'a', 'b'}, {'a':6, 'b':10})\n>>> w2 = 1.5*w\n>>> print(test_format([w2[x] for x in 'ab']))\n>>> print(test_format([(-2*w2)[x] for x in 'ab']))\n")]]
source_files        = ['vec.py'] * len(sum(groups,[]))

try:
    import vec as solution
    test_vars = vars(solution).copy()
except Exception as exc:
    print(exc)
    print("!! It seems like you have an error in your stencil file. Please fix before submitting.")
    sys.exit(1)

def find_lines(varname):
    return list(filter(lambda l: varname in l, list(open("python_lab.py"))))

def find_line(varname):
    ls = find_lines(varname)
    return ls[0] if len(ls) else None


def use_comprehension(varname):
    lines = find_lines(varname)
    for line in lines:
        try:
            if "comprehension" in ast.dump(ast.parse(line)):
                return True
        except: pass
    return False

def double_comprehension(varname):
    line = find_line(varname)
    return ast.dump(ast.parse(line)).count("comprehension") == 2

def line_contains_substr(varname, word):
    lines = find_line(varname)
    for line in lines:
        if word in line:
            return True
    return False

def test_format(obj, precision=6):
    tf = lambda o: test_format(o, precision)
    delimit = lambda o: ', '.join(o)
    otype = type(obj)
    if otype is str:
        return "'%s'" % obj
    elif otype is float or otype is int:
        if otype is int:
            obj = float(obj)
        fstr = '%%.%df' % precision
        return fstr % obj
    elif otype is set:
        if len(obj) == 0:
            return 'set()'
        return '{%s}' % delimit(sorted(map(tf, obj)))
    elif otype is dict:
        return '{%s}' % delimit(sorted(tf(k)+': '+tf(v) for k,v in obj.items()))
    elif otype is list:
        return '[%s]' % delimit(map(tf, obj))
    elif otype is tuple:
        return '(%s%s)' % (delimit(map(tf, obj)), ',' if len(obj) is 1 else '')
    elif otype.__name__ in ['Vec','Mat']:
        entries = delimit(map(tf, sorted(filter(lambda o: o[1] != 0, obj.f.items()))))
        return '<%s %s {%s}>' % (otype.__name__, test_format(obj.D), entries)
    else:
        return str(obj)



def output(tests):
    dtst = doctest.DocTestParser().get_doctest(tests, test_vars, 0, '<string>', 0)
    runner = ModifiedDocTestRunner()
    runner.run(dtst)
    return runner.results

test_vars['test_format'] = test_vars['tf'] = test_format
test_vars['find_lines'] = find_lines
test_vars['find_line'] = find_line
test_vars['use_comprehension'] = use_comprehension
test_vars['double_comprehension'] = double_comprehension
test_vars['line_contains_substr'] = line_contains_substr

base_url = '://class.coursera.org/%s/assignment/' % URL
protocol = 'https'
colorize = False
verbose  = False

class ModifiedDocTestRunner(doctest.DocTestRunner):
    def __init__(self, *args, **kwargs):
        self.results = []
        return super(ModifiedDocTestRunner, self).__init__(*args, checker=OutputAccepter(), **kwargs)
    
    def report_success(self, out, test, example, got):
        self.results.append(got)
    
    def report_unexpected_exception(self, out, test, example, exc_info):
        exf = traceback.format_exception_only(exc_info[0], exc_info[1])[-1]
        self.results.append(exf)

class OutputAccepter(doctest.OutputChecker):
    def check_output(self, want, got, optionflags):
        return True

def submit(parts_string, login, password):   
    print('= Coding the Matrix Homework and Lab Submission')
    
    if not login:
        login = login_prompt()
    if not password:
        password = password_prompt()
    if not parts_string: 
        parts_string = parts_prompt()

    parts = parse_parts(parts_string)

    if not all([parts, login, password]):
        return

    for sid, name, part_tests in parts:
        sys.stdout.write('== Submitting "%s"' % name)

        if 'DEV' in os.environ: sid += '-dev'

        (login, ch, state, ch_aux) = get_challenge(login, sid)

        if not all([login, ch, state]):
            print('  !! Error: %s\n' % login)
            return

        # to stop Coursera's strip() from doing anything, we surround in parens
        results  = output(part_tests)
        prog_out = '(%s)' % ''.join(map(str.rstrip, results))
        token    = challenge_response(login, password, ch)
        src      = source(sid)

        feedback = submit_solution(login, token, sid, prog_out, src, state, ch_aux)

        if len(feedback.strip()) > 0:
            if colorize:
                good = 'incorrect' not in feedback.lower()
                print(': \033[1;3%dm%s\033[0m' % (2 if good else 1, feedback.strip()))
            else:
                print(': %s' % feedback.strip())
        
        if verbose:
            for t, r in zip(part_tests.split('\n'), results):
                sys.stdout.write('%s\n%s' % (t, r))
            sys.stdout.write('\n\n')


def login_prompt():
    return input('Login email address: ')


def password_prompt():
    return input("One-time password from the assignment page (NOT your own account's password): ")


def parts_prompt():
    print('These are the assignment parts that you can submit:')

    for i, name in enumerate(part_friendly_names):
        print('  %d) %s' % (i+1, name))

    return input('\nWhich parts do you want to submit? (Ex: 1, 4-7): ')

def parse_parts(string):
    def extract_range(s):
        s = s.split('-')
        if len(s) == 1: return [int(s[0])]
        else: return list(range(int(s[0]), 1+int(s[1])))
    parts = map(extract_range, string.split(','))
    flat_parts = sum(parts, [])
    return sum(list(map(lambda p: groups[p-1], flat_parts)),[])

def get_challenge(email, sid):
    """Gets the challenge salt from the server. Returns (email,ch,state,ch_aux)."""
    params = {'email_address': email, 'assignment_part_sid': sid, 'response_encoding': 'delim'}

    challenge_url = '%s%schallenge' % (protocol, base_url)
    data = urllib.parse.urlencode(params).encode('utf-8')
    req  = urllib.request.Request(challenge_url, data)
    resp = urllib.request.urlopen(req)
    text = resp.readall().decode('utf-8').strip().split('|')

    if len(text) != 9:
        print('  !! %s' % '|'.join(text))
        sys.exit(1)
  
    return tuple(text[x] for x in [2,4,6,8])


def challenge_response(email, passwd, challenge):
    return hashlib.sha1((challenge+passwd).encode('utf-8')).hexdigest()


def submit_solution(email_address, ch_resp, sid, output, source, state, ch_aux):
    b64ize = lambda s: str(base64.encodebytes(s.encode('utf-8')), 'ascii')

    values = { 'assignment_part_sid' : sid
             , 'email_address'       : email_address
             , 'submission'          : b64ize(output) 
             , 'submission_aux'      : b64ize(source)
             , 'challenge_response'  : ch_resp
             , 'state'               : state
             }

    submit_url = '%s%ssubmit' % (protocol, base_url)
    data     = urllib.parse.urlencode(values).encode('utf-8')
    req      = urllib.request.Request(submit_url, data)
    response = urllib.request.urlopen(req)

    return response.readall().decode('utf-8').strip()


def source(sid):
    src = []
    for fn in set(source_files):
        with open(fn) as source_f:
            src.append(source_f.read())
    return '\n\n'.join(src)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    env = os.environ
    helps = [ 'numbers or ranges of tasks to submit'
            , 'the email address on your Coursera account'
            , 'your ONE-TIME password'
            , 'use ANSI color escape sequences'
            , 'show the test\'s interaction with your code'
            , 'use an encrypted connection to Coursera'
            , 'use an unencrypted connection to Coursera'
            ]
    parser.add_argument('tasks',      default=env.get('COURSERA_TASKS'), nargs='*', help=helps[0])
    parser.add_argument('--email',    default=env.get('COURSERA_EMAIL'),            help=helps[1])
    parser.add_argument('--password', default=env.get('COURSERA_PASS'),             help=helps[2])
    parser.add_argument('--colorize', default=False, action='store_true',           help=helps[3])
    parser.add_argument('--verbose',  default=False, action='store_true',           help=helps[4])
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--https', dest="protocol", const="https", action="store_const", help=helps[-2])
    group.add_argument('--http',  dest="protocol", const="http",  action="store_const", help=helps[-1])
    args = parser.parse_args()
    if args.protocol: protocol = args.protocol
    colorize = args.colorize
    verbose = args.verbose
    submit(','.join(args.tasks), args.email, args.password)

