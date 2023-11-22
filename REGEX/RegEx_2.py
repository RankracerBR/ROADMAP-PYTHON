import re

'''Scans a string for a regex match.'''
#
print(re.search(r'(\d+)','foo123bar'))
print(re.search(r'[a-z]+','123FOO456',flags=re.IGNORECASE))

print(re.search(r'\d+','foo.bar'))
print('\n')

'''Looks for a regex match at the beginning of a string.'''
#
print(re.search(r'\d+','123foobar'))
print(re.search(r'\d+','foo123bar'))

print(re.match(r'\d+','123foobar'))
print(re.match(r'\d+','foo123bar'))

s = 'foo\nbar\nbaz'

print(re.search('^foo',s))
print(re.search('^bar',s,re.MULTILINE))

print(re.match('^foo',s))
print(re.match('^bar',s,re.MULTILINE))
print('\n')

'''Looks for a regex match on an entire string.'''
#
print(re.fullmatch(r'\d+','123foo'))
print(re.fullmatch(r'\d+','foo123'))
print(re.fullmatch(r'\d+','foo123bar'))
print(re.fullmatch(r'\d+','123'))
print(re.fullmatch(r'^\d+$','123'))
print('\n')

'''Returns a list of all matches of a regex in a string.'''
#
print(re.findall(r'\w+','...foo,,,,bar:%$baz//|'))
print(re.findall(r'#(\w+)#','#foo#.#bar#.#baz#'))

print(re.findall(r'(\w+),(\w+)','foo,bar,baz,qux,corge'))
print(re.findall(r'(\w+),(\w+),(\w+)','foo,bar,baz,qux,quux,corge'))
print('\n')

'''Returns an iterator that yields regex matches.'''
#
it = re.finditer(r'\w+','...foo,,,,bar:%$baz//|')
print(next(it))
print(next(it))
print(next(it))
#print(next(it)) StopIteration
print('\n')

'''Substitution Functions'''
'''Returns a new string that results from performing replacements on a search string.'''
'''Substitution by String'''
#
s = 'foo.123.bar.789.baz'

print(re.sub('\d+','#',s))
print(re.sub('[a-z]+','(*)',s))

print(re.sub(r'(\w+),bar,baz,(\w+)',
             r'\2,bar,baz,\1',
             'foo,bar,baz,qux'))

print(re.sub(r'foo,(?P<w1>\w+),(?P<w2>\w+),qux',
             r'foo,\g<w2>,\g<w1>,qux',
             'foo,bar,baz,qux'))

print(re.sub(r'foo,(\w+),(\w+),qux',
             r'foo,\g<2>,\g<1>,qux',
             'foo,bar,baz,qux'))

#print(re.sub(r'(\d+)',r'\10','foo 123 bar')) sre_constants.error: invalid group reference 10 at position 1

print(re.sub(r'(\d+)',r'\g<1>0','foo 123 bar'))

print(re.sub(r'\d+','/\g<0>/','foo 123 bar'))

print(re.sub('x*','-','foo'))
print('\n')

'''Substitution by Function'''
#
def f(match_obj):
    s = match_obj.group(0) 
    
    if s.isdigit():
        return str(int(s)*10)
    else:
        return s.upper()

print(re.sub(r'\w+',f,'foo.10.bar.20.baz.30'))
print('\n')

'''Limiting the Number of Replacements'''
#
print(re.sub(r'\w+','xxx','foo.bar.baz.qux'))
print(re.sub(r'\w+','xxx','foo.bar.baz.qux', count=2))
print('\n')

'''Returns a new string that results from performing replacements on a search string and also returns the number of substitutions made.'''
#
print(re.subn(r'\w+','xxx','foo.bar.baz.qux'))
print(re.subn(r'\w+','xxx','foo.bar.baz.qux',count = 2))

def f(match_obj):
    m = match_obj.group(0)
    
    if m.isdigit():
        return str(int(m) * 10)
    else:
        return m.upper()

print(re.subn(r'\w+',f,'foo.10.baz.20.baz.30'))
print('\n')

'''Utility Functions'''
'''Splits a string into substrings.'''
#
print(re.split('\s*[,;/]\s*','foo,bar ; baz / qux'))

string = 'foo,bar ; baz / qux'
regex = r'(\s*[,;/]\s*)'
a = re.split(regex,string)

print(a)

for i,s in enumerate(a):
    
    if not re.fullmatch(regex,s):
        a[i] = f'<{s}>'

print(''.join(a))

string = 'foo,bar ; baz / qux'
regex = r'(?:\s*[,;/]\s*)'
print(re.split(regex,string))

s = 'foo, bar, baz, qux, quux, corge'

print(re.split(r',\s*',s))
print(re.split(r',\s*',s,maxsplit=3))

print(re.split('(/)','/foo/bar/baz/'))
print('\n')

'''Escapes characters in a regex.'''
#
print(re.match('foo^bar(baz)|qux','foo^bar(baz)|qux'))
print(re.match('foo\^bar\(baz\)\|qux','foo^bar(baz)|qux'))

print(re.escape('foo^bar(baz)|qux') == 'foo\^bar\(baz\)\|qux')
print(re.escape('foo^bar(baz)|qux'), 'foo^bar(baz)|qux')
print('\n')

'''Compiled Regex Objects in Python'''
'''Compiles a regex into a regular expression object.'''
#
'''
re_obj = re.compile('<regex>, <flags>')
result = re.search(re_obj, '<string>')

result2 = re_obj.search('<string>')

result3 = re.search('<regex>,<string>,<flags>')
'''

print(re.search(r'(\d+)','foo123bar'))

re_obj = re.compile(r'(\d+)')
print(re.search(re_obj,'foo123bar'))
print(re_obj.search('foo123bar'))

r1 = re.search('ba[rz]','FOOBARBAZ', flags=re.I)

re_obj = re.compile('ba[rz]',flags=re.I)
r2 = re.search(re_obj,'FOOBARBAZ')
r3 = re_obj.search('FOOBARBAZ')

print(r1)

print(r2)

print(r3)
print('\n')

s1,s2,s3,s4 = 'foo.bar', 'foo123bar', 'baz99', 'qux & grault'

print(re.search('\d+',s1))
print(re.search('\d+',s2))
print(re.search('\d+',s3))
print(re.search('\d+',s4))

#More maintainable
s1,s2,s3,s4 = 'foo.bar', 'foo123bar', 'baz99', 'qux & grault'
re_obj = re.compile('\d+')

print(re_obj.search(s1))
print(re_obj.search(s2))
print(re_obj.search(s3))
print(re_obj.search(s4))

s1,s2,s3,s4 = 'foo.bar', 'foo123bar', 'baz99', 'qux & grault'
regex = '\d+'

print(re.search(regex, s1))
print(re.search(regex, s2))
print(re.search(regex, s3))
print(re.search(regex, s4))
print('\n')

'''Regular Expression Object Methods'''
#
re_obj = re.compile(r'\d+')
s = 'foo123barbaz'

re_obj.search(s)

print(s[6:9])

print(re_obj.search(s, 6, 9))

re_obj = re.compile('^bar')
s = 'foobarbaz'

print(s[3:])

print(re_obj.search(s, 3))
print('\n')

'''Regular Expression Object Attributes'''
#
re_obj = re.compile(r'(?m)(\w+),(\w+)', re.I)
print(re_obj.flags)

re.I|re.M|re.UNICODE
print(re_obj.groups)

print(re_obj.pattern)

re_obj = re.compile(r'(?P<w1>),(?P<w2>)')
print(re_obj.groupindex)

print(re_obj.groupindex['w1'])
print(re_obj.groupindex['w2'])
print('\n')

'''Match Object Methods and Attributes'''
#
m = re.search('bar','foo.bar.baz')
print(m)

print(bool(m))

if re.search('bar','foo.bar.baz'):
    print('Found a match')
print('\n')

'''Match Object Methods'''
'''Returns the specified captured group(s) from a match.'''
#
m = re.search(r'(\w+),(\w+),(\w+)', 'foo,bar,baz')

print(m.group(1))

print(m.group(3))

m = re.match(r'(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)','quux,corge,grault')

print(m.group(1))

print(m.group(2))

m = re.search(r'(\w+),(\w+),(\w+)','foo,bar,baz')

print(m.group(1, 3))

print(m.group(3, 3, 1, 1, 2, 2))

m = re.search(r'(\w+),(\w+),(\w+)','foo,bar,baz')
#print(m.group(4)) IndexError: no such group

m = re.match(r'(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)','quux,corge,grault')
#print(m.group('foo')) IndexError: no such group

m = re.search(r'(\w+),(\w+),(\w+)?','foo,bar,')
print(m)

print(m.group(1, 2))

print(m.group(3))

m = re.match(r'(\w{3},)+', 'foo,bar,baz,qux')
print(m)

print(m.group(1))

m = re.search(r'(\w+),(\w+),(\w+)', 'foo,bar,baz')
print(m)

print(m.group(0))

print(m.group())
print('\n')

'''Returns a captured group from a match.'''
#
m = re.search(r'(\w+),(\w+),(\w+)', 'foo,bar,baz')
print(m.group(2))

print(m.__getitem__(2))

m = re.match(
    r'foo,(?P<w1>\w+),(?P<w2>\w+),qux',
    'foo,bar,baz,qux')

print(m[2])

print(m['w2'])
print('\n')

'''Returns all captured groups from a match.'''
#
m = re.search(r'(\w+),(\w+),(\w+)','foo,bar,baz')
print(m.groups())

m = re.search(r'(\w+),(\w+),(\w+)?','foo,bar,')
print(m)

print(m.group(3))

print(m.groups())

print(m.groups(default='---'))
print('\n')

'''Returns a dictionary of named captured groups.'''
m = re.match(
    r'foo,(?P<w1>\w+),(?P<w2>\w+),qux',
    'foo,bar,baz,qux')

print(m.groupdict())

print(m.groupdict()['w2'])

m = re.match(
    r'foo,(?P<w1>\w+),(?P<w2>\w+)?,qux',
    'foo,bar,,qux')

print(m.groupdict())

print(m.groupdict(default='---'))
print('\n')

'''Performs backreference substitutions from a match.'''
#
m = re.search(r'(\w+),(\w+),(\w+)','foo,bar,baz')
print(m)

print(m.groups())

print(m.expand(r'\2'))

print(m.expand(r'[\3] -> [\1]'))

m = re.search(r'(?P<num>\d+)','foo123qux')
print(m)

print(m.group(1))

print(m.expand(r'--- \g<num> ---'))
print('\n')

'''Return the starting and ending indices of the match.'''
#
s = 'foo123bar456baz'
m = re.search('\d+',s)
print(m)

print(m.start())

print(m.end())

print(s[m.start():m.end()])

s = 'foo123bar456baz'
m = re.search(r'(\d+)\D*(?P<num>\d+)',s)

print(m.group(1))

print(m.start(1),m.end(1))

print(m.group('num'))

print(m.start('num'), m.end('num'))

print(s[m.start('num'):m.end('num')])

m = re.search('foo(\d*)bar','foobar')
print(m[1])

print(m.start(1), m.end(1))

m = re.search('(\w+),(\w+),(\w+)?','foo,bar,')
print(m.group(3))

print(m.start(3), m.end(3))
print('\n')

'''Returns both the starting and ending indices of the match.'''
#
s = 'foo123bar456baz'
m = re.search(r'(\d+)\D*(?P<num>\d+)',s)
print(m)

print(m[0])
print(m.span())

print(m[1])
print(m.span(1))

print(m['num'])
print(m.span('num'))
print('\n')

'''Match Object Attributes'''
'''Contain the effective values of <pos> and <endpos> for the search.'''
#
re_obj = re.compile(r'\d+')
m = re_obj.search('foo123bar', 2, 7)
print(m)

print(m.pos, m.endpos)

re_obj = re.compile(r'\d+')
m = re_obj.search('foo123bar')
print(m)

print(m.pos, m.endpos)

m = re.search(r'\d+','foo123bar')
print(m)

print(m.pos, m.endpos)
print('\n')

'''Contains the index of the last captured group.'''
#
m = re.search(r'(\w+),(\w+),(\w+)', 'foo,bar,baz')
print(m.lastindex)

print(m[m.lastindex])

m = re.search(r'(\w+),(\w+),(\w+)?', 'foo,bar,baz')
print(m.groups())
print(m.lastindex, m[m.lastindex])

m = re.search(r'(\w+),(\w+),(\w+)?','foo,bar,')
print(m.groups())

print(m.lastindex, m[m.lastindex])

m = re.match('((a)(b))','ab')
print(m.groups())

print(m.lastindex)

print(m[m.lastindex])
print('\n')

'''Contains the name of the last captured group.'''
#
s = 'foo123bar456baz'
m = re.search(r'(?P<n1>\d+)\D*(?P<n2>\d+)', s)
print(m.lastgroup)

s = 'foo123bvar456baz'

m = re.search(r'(\d+)\D*(\d+)', s)
print(m.groups())
print(m.lastgroup)

m = re.search(r'\d+\D*\d+', s)
print(m.groups())

print(m.lastgroup)
print('\n')

'''Contains the regular expression object for the match.'''
#
regex = r'(\w+),(\w+),(\w+)'

m1 = re.search(regex,'foo,bar,baz')
print(m1)
print(m1.re)

re_obj = re.compile(regex)
print(re_obj)
print(re_obj is m1.re)

m2 = re_obj.search('qux,quux,corge')
print(m2)
print(m2.re)
print(m2.re is re_obj is m1.re)

print(m1.re.groups)

print(m1.re.pattern)

print(m1.re.pattern == regex)

print(m1.re.flags)

m = re.search(r'(\w+),(\w+),(\w+)','foo,bar,baz')
print(m.re)

print(m.re.match('quux,corge,grault'))
print('\n')

'''Contains the search string for a match.'''
#
m = re.search(r'(\w+),(\w+),(\w+)', 'foo,bar,baz')
print(m.string)

re_obj = re.compile(r'(\w+),(\w+),(\w+)')
m = re_obj.search('foo,bar,baz')