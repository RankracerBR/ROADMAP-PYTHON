#Imports 
import re
import sys

#
s = 'foo123bar'

#
print('123' in s)
print('\n')

#
print(s.find('123'))
print('\n')

#
print(re.search('123',s)) #span=(3, 6) indicates the portion of <string> in which the match was found
print('\n')

#
if re.search('123',s):
    print('Found a match.')
else:
    print('No match.')
print('\n')

#
print(s[3:6])
print('\n')

#
print(re.search('[0-9][0-9][0-9]', s))
print('\n')

#
print(re.search('[0-9][0-9][0-9]','foo456bar'))
print(re.search('[0-9][0-9][0-9]','234baz'))
print(re.search('[0-9][0-9][0-9]','qux678'))
print('\n')
      
#
print(re.search('[0-9][0-9][0-9]','12foo34'))
print('\n')

#
print(re.search('1.3',s))

s = 'foo13bar'
print(re.search('1.3',s))
print('\n')

'''Specifies a specific set of characters to match.'''
#
print(re.search('ba[artz]','foobarqux'))
print(re.search('ba[artz]','foobazqux'))
print('\n')

#
print(re.search('[a-z]','FOObar'))
print('\n')

#
print(re.search('[0-9][0-9]','foo123bar'))
print('\n')

#
print(re.search('[0-9a-fA-f]','--- a0 ---'))
print('\n')

#
print(re.search('[^0-9]','12345foo'))
print('\n')

#
print(re.search('[#:^]','foo^bar:baz#qux'))
print('\n')

#
print(re.search('[-abc]','123-456'))
print(re.search('[abc-]','123-456'))
print(re.search('[ab\-c]','123-456'))
print('\n')

#
print(re.search('[]]','foo[1]'))
print(re.search('[ab\]cd]','foo[1]'))
print('\n')

#
print(re.search('[)*+|]','123*456'))
print(re.search('[)*+|]','123+456'))
print('\n')

'''Specifies a wildcard.'''
#
print(re.search('foo.bar','fooxbar'))
print(re.search('foo.bar','foobar'))
print(re.search('foo.bar','foo\nbar'))
print('\n')

'''Match based on whether a character is a word character.'''
#
print(re.search('\w','#(.a$@&'))
print(re.search('[a-zA-Z0-9_]','#(.a$@&'))
print('\n')

#
print(re.search('\W','a_1*3Qb'))
print(re.search('[^a-zA-Z0-9_]','a_1*3Qb'))
print('\n')

'''Match based on whether a character is a decimal digit.'''
#
print(re.search('\d','abc4def'))
print(re.search('\D','234Q678'))
print('\n')

'''Match based on whether a character represents whitespace.'''
#
print(re.search('\s','foo\nbar baz'))
print(re.search('\S',' \n foo \n '))
print('\n')

#
print(re.search('[\d\w\s]','---3---'))
print(re.search('[\d\w\s]','---a---'))
print(re.search('[\d\w\s]','--- ---'))
print('\n')

'''Removes the special meaning of a metacharacter'''
#
print(re.search('.','foo.bar'))
print(re.search('\.','foo.bar'))

s = r'foo\bar'
print(re.search('\\\\',s))

'''Raw String'''
print(re.search(r'\\',s))
print('\n')

'''Anchor a match to the start of <string>.'''
#
print(re.search('^foo','foobar'))
print(re.search('^foo','barfoo'))

print(re.search('\Afoo','foobar'))
print(re.search('\Afoo','barfoo'))
print('\n')

'''Anchor a match to the end of <string>.'''
#
print(re.search('bar$','foobar'))
print(re.search('bar$','barfoo'))

print(re.search('bar$','foobar\n'))
print('\n')

'''Anchors a match to a word boundary.'''
#
print(re.search(r'bbar','foo bar'))
print(re.search(r'\bbar','foo.bar'))

print(re.search(r'\bbar','foobar'))

print(re.search(r'foo\b','foo bar'))
print(re.search(r'foo\b','foo.bar'))

print(re.search(r'foo\b','foobar'))

print(re.search(r'\bbar\b','foo bar baz'))
print(re.search(r'\bbar\b','foo(bar)baz'))
print('\n')

'''Anchors a match to a location that isnt a word boundary.'''
#
print(re.search(r'\Bfoo\B', 'foo'))
print(re.search(r'\Bfoo\B','.foo.'))
print(re.search(r'\Bfoo\B','barfoobaz'))
print('\n')

'''Matches zero or more repetitions of the preceding regex.'''
# The matches --> -*
print(re.search('foo-*bar','foobar'))
print(re.search('foo-*bar','foo-bar'))
print(re.search('foo-*bar','foo--bar'))

print(re.search('foo.*bar','# foo $qux@grault % bar #'))
print('\n')

'''Matches one or more repetitions of the preceding regex.'''
#
print(re.search('foo-+bar','foobar'))
print(re.search('foo-+bar','foo-bar'))
print(re.search('foo-+bar','foo--bar'))
print('\n')

'''Matches zero or one repetitions of the preceding regex.'''
#
print(re.search('foo-?','foobar'))
print(re.search('foo-?bar','foo-bar'))
print(re.search('foo-?bar','foo-bar'))

print(re.search('foo[1-9]*bar','foobar'))
print(re.search('foo[1-9]*bar','foo42bar'))

print(re.search('foo[1-9]+bar','foobar'))
print(re.search('foo[1-9]+bar','foo42bar'))

print(re.search('foo[1-9]?bar','foobar'))
print(re.search('foo[1-9]?bar','foo42bar'))
print('\n')

'''The non-greedy (or lazy) versions of the *, +, and ? quantifiers.'''
#
print(re.search('<.*>','%<foo> <bar> <baz>%'))
print(re.search('<.*?>','% <foo> <bar> <baz>%'))

print(re.search('<.+>','%<foo> <bar> <baz>%'))
print(re.search('<.+?>','%<foo> <bar> <baz>%'))

print(re.search('ba?','baaaa'))
print(re.search('ba??','baaaa'))
print('\n')

'''Matches exactly m repetitions of the preceding regex.'''
#
print(re.search('x-{3}x','x--x'))
print(re.search('x-{3}x','x---x'))
print(re.search('x-{3}x','x----x'))
print('\n')

'''Matches any number of repetitions of the preceding regex from m to n, inclusive.'''
#
for i in range(1, 6):
    s = f"x{'-' * i}x"
    print(f'{i} {s:10}', re.search('x-{2,4}x',s))

print(re.search('x{}y','x{}y'))

print(re.search('x{foo}y','x{foo}y'))
print(re.search('x{a:b}y','x{a:b}y'))
print(re.search('x{1,3,5}y','x{1,3,5}y'))
print(re.search('x{foo,bar}y','x{foo,bar}y'))
print('\n')

'''The non-greedy (lazy) version of {m,n}.'''
#
print(re.search('a{3,5}','aaaaaaa'))
print(re.search('a{3,5}?','aaaaaaaa'))
print('\n')

'''Grouping Constructs and Backreferences'''

'''Defines a subexpression or group.'''
#
print(re.search('(bar)','foo bar baz'))
print(re.search('bar','foo bar baz'))
print('\n')

'''Treating a Group as a Unit'''
#
print(re.search('(bar)+','foo bar baz'))
print(re.search('(bar)+','foo barbar baz'))
print(re.search('(bar)+','foo barbarbarbar baz'))

print(re.search('(bar[rz]){2,4}(qux)?','bazbarbazqux'))
print(re.search('(bar[rz]){2,4}(qux)?','barbar'))

print(re.search('(foo(bar)?)+(\d\d\d)?','foofoobar'))
print(re.search('(foo(bar)?)','foofoobar123'))
print(re.search('(foo(bar)?)','foofoo123'))
print('\n')

'''Returns a tuple containing all the captured groups from a regex match.'''
#
m = re.search('(\w+),(\w+),(\w+)','foo,quux,baz')
print(m)

print(m.groups())
print('\n')

'''Returns a string containing the <n>th captured match.'''
#
m = re.search('(\w+),(\w+),(\w+)','foo,quux,baz')
m.groups()

print(m.group())
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print('\n')

'''Returns a tuple containing the specified captured matches.'''
print(m.groups())
print(m.group(2,3))
print(m.group(3,2,1))

print(m.group(3,2,1))
print(m.group(3),m.group(2),m.group(1))
print('\n')

'''Matches the contents of a previously captured group.'''
#
regex = r'(\w+),\1'

m = re.search(regex,'foo,foo')
print(m)

print(m.group(1))

m = re.search(regex,'qux,qux')
print(m)

print(m.group(1))

m = re.search(regex,'foo,qux')
print(m)

print(re.search('[a-z]#\1','d#d'))

print(oct(ord('\1')))

print(re.search(f'[a-z]#\1','d#d'))
print('\n')

'''Creates a named captured group.'''
#
m = re.search('(\w+),(\w+),(\w+)','foo,quux,baz')
print(m.groups())

print(m.group(1,2,3))

m = re.search('(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)','foo,quux,baz')

print(m.groups())

print(m.group('w1'))

print(m.group('w2'))

print(m.group('w1','w2','w3'))

m = re.search('(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)','foo,quux,baz')

print(m.group('w1'))

print(m.group(1))

print(m.group('w1', 'w2', 'w3'))

print(m.group(1, 2, 3))
print('\n')

'''Matches the contents of a previously captured named group.'''
#
m = re.search(r'(\w+),\1','foo,foo')
print(m)

print(m.group(1))

m = re.search(r'(?P<word>\w+),(?P=word)','foo,foo')
print(m)

print(m.group('word'))

m = re.search(r'(?P<num>\d+).(?P=num)','135.135')
print(m)

print(m.group('num'))
print('\n')

'''Creates a non-capturing group.'''
#
m = re.search('(\w+),(?:\w+),(\w+)','foo,quux,baz')
print(m.group())

print(m.group(1))
print(m.group(2))
print('\n')

'''Specifies a conditional match.'''
#
regex = r'^(###)?foo(?(1)bar|baz)'

print(re.search(regex,'###foobar'))
print(re.search(regex,'###foobaz'))
print(re.search(regex,'foobar'))
print(re.search(regex,'foobaz'))

regex = r'^(?P<ch>\W)?foo(?(ch)(?P=ch)|)$'

print(re.search(regex,'foo'))
print(re.search(regex,'#foo#'))
print(re.search(regex,'@foo@'))

print(re.search(regex,'#foo'))
print(re.search(regex,'foo@'))
print(re.search(regex,'#foo@'))
print(re.search(regex,'@foo#'))
print('\n')

'''Lookahead and Lookbehind Assertions'''
'''Creates a positive lookahead assertion.'''
#
print(re.search('foo(?=[a-z])','foobar'))
print(re.search('foo(?=[a-z])','foo123'))
print(re.search('foo(?=[a-z])','foobar'))
print(re.search('foo([a-z])','foobar'))

m = re.search('foo(?=[a-z])(?P<ch>.)','foobar')
print(m.group('ch'))

m = re.search('foo([a-z])(?P<ch>.)','foobar')
print(m.group('ch'))
print('\n')

'''Creates a negative lookahead assertion.'''
#
print(re.search('foo(?=[a-z])','foobar'))
print(re.search('foo(?![a-z])','foobar'))

print(re.search('foo(?=[a-z])','foo123'))
print(re.search('foo(?![a-z])','foo123'))
print('\n')

'''Creates a positive lookbehind assertion.'''
#
print(re.search('(?<=foo)bar','foobar'))
print(re.search('(?<=qux)bar','foobar'))
#print(re.search('(?<=a+)def','aaadef')) re.error: look-behind requires fixed-width pattern
print(re.search('(?<=a{3})def','aaadef'))
print('\n')

'''Creates a negative lookbehind assertion.'''
#
print(re.search('(?<!foo)bar','foobar'))
print(re.search('(?<!qux)bar','foobar'))
print('\n')

'''Miscellaneous Metacharacters'''
'''Specifies a comment.'''
#
print(re.search('bar(?#This is a comment) *baz', 'foo bar baz qux'))
print('\n')

'''Specifies a set of alternatives on which to match.'''
#
print(re.search('foo|bar|baz','bar'))
print(re.search('foo|bar|baz','baz'))
print(re.search('foo|bar|baz','quux'))

print(re.search('foo','foograult'))
print(re.search('grault','foograult'))
print(re.search('foo|grault','foograult'))

print(re.search('(foo|bar|baz)+','foofoofoo'))
print(re.search('(foo|bar|baz)+','bazbazbazbaz'))
print(re.search('(foo|bar|baz)+','barbazfoo'))

print(re.search('([0-9]+|[a-f]+)','456'))
print(re.search('([0-9]+|[a-f]+)','ffda'))
print('\n')

'''Modified Regular Expression Matching With Flags'''
'''Makes matching case insensitive.'''
#
print(re.search('a+','aaaAAA'))
print(re.search('A+','aaaAAA'))
print(re.search('a+','aaaAAA',re.I))
print(re.search('A+','aaaAAA', re.IGNORECASE))

print(re.search('[a-z]','aBcDeF'))
print(re.search('[a-z]','aBcDeF',re.I))
print('\n')

'''Causes start-of-string and end-of-string anchors to match at embedded newlines.'''
#
s = 'foo\nbar\nbaz'

print(re.search('^foo',s))
print(re.search('^bar',s))
print(re.search('^baz',s))

print(re.search('foo$',s))
print(re.search('bar$',s))
print(re.search('baz$',s))

s = 'foo\nbar\nbaz'
print(s)

print(re.search('^foo',s,re.MULTILINE))
print(re.search('^bar',s,re.MULTILINE))
print(re.search('^baz',s,re.MULTILINE))

print(re.search('foo$',s,re.M))
print(re.search('bar$',s,re.M))
print(re.search('baz$',s,re.M))

s = 'foo\nbar\nbaz'

print(re.search('^bar',s,re.MULTILINE))
print(re.search('bar$',s,re.MULTILINE))

print(re.search('\Abar',s,re.MULTILINE))
print(re.search('bar\Z',s,re.MULTILINE))
print('\n')

'''Causes the dot (.) metacharacter to match a newline.'''
#
print(re.search('foo.bar','foo\nbar'))
print(re.search('foo.bar','foo\nbar',re.DOTALL))
print(re.search('foo.bar','foo\nbar',re.S))
print('\n')

'''Allows inclusion of whitespace and comments within a regex.'''
#
regex = r'(\(\d{3}\))?\s*\d{3}[-.]\d{4}$'

print(re.search(regex,'414.9229'))
print(re.search(regex,'414-9229'))
print(re.search(regex,'(712)414-9229'))
print(re.search(regex,'(712) 414-9229'))

regex = r'''^
        (\(\d{3}\))?   
        \s*
        \d{3}
        [-.]
        \d{4}
        $
        '''

print(re.search(regex,'414.9229',re.VERBOSE))
print(re.search(regex,'414-9229',re.VERBOSE))
print(re.search(regex,'(712)414-9229',re.X))
print(re.search(regex,'(712) 414-9229',re.X))

print(re.search('foo bar','foo bar',re.VERBOSE))

print(re.search('foo\ bar','foo bar', re.VERBOSE))
print(re.search('foo[ ]bar','foo bar', re.VERBOSE))
print('\n')

'''Displays debugging information.'''
#
regex = r'^(\(\d{3}\))?\s*\d{3}[-.]\d{4}$'
print(re.search('foo.bar','fooxbar',re.DEBUG))
print(re.search(regex,'414.9229',re.DEBUG))
print(re.search('x[123]{2,4}y','x222y',re.DEBUG))
print(re.search('x[123]{foo}y','x222y',re.DEBUG))

#defining single letter version(optional/personal)
re.D = re.DEBUG
print(re.search('foo','foo',re.D))
print('\n')

'''Specify the character encoding used for parsing of special regex character classes.'''
#
s = '\u0967\u096a\u096c'
print(s)
print(re.search('\d+',s))

s = 'sch\u00f6n'
print(s)

print(re.search('\w+',s,re.ASCII))

print(re.search('\w+',s,re.UNICODE))
print(re.search('\w+',s))

'''Combining <flags> Arguments in a Function Call'''
#
print(re.search('^bar','FOO\nBAR\nBAZ',re.I|re.M))
print('\n')

'''Setting and Clearing Flags Within a Regular Expression'''
'''Sets flag value(s) for the duration of a regex.'''
#
print(re.search('^bar','FOO\nBAR\nBAZ\n',re.I|re.M))
print(re.search('(?im)^bar','FOO\nBAR\nBAZ\n'))

#print( re.search('foo.bar(?s).baz', 'foo\nbar\nbaz'))
#print(re.search('foo.bar.baz(?s)','foo\nbar\nbaz'))

print(sys.version)
#print(re.search('foo.bar.baz(?s)', 'foo\nbar\nbaz'))
print('\n')

'''Sets or removes flag value(s) for the duration of a group.'''
#
print(re.search('(?i:foo)bar','FOObar'))

print(re.search('(?i:foo)bar','FOOBAR'))

print(re.search('(?-i:foo)bar','FOOBAR',re.IGNORECASE)) #The (?-i:foo) turns off the ignorecase

s = 'sch\u00f6n'
print(s)

print(re.search('(?a:\w+)',s))
print(re.search('(?u:\w+)',s))
#print(re.search('(?-a:\w+)',s)) re.error: bad inline flags: cannot turn off flags 'a', 'u' and 'L' at position 4
