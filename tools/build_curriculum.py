"""Maintain the curriculum, contracts, and test cases; contains no exercise solutions."""
from pathlib import Path
from dataclasses import dataclass
import textwrap

ROOT = Path(__file__).resolve().parents[1]
DAYS = []

@dataclass
class File:
    content: str

@dataclass
class ObjectChecks:
    steps: list

@dataclass
class Database:
    script: str

def task(signature, contract, *cases, mode=None):
    return dict(signature=signature, contract=contract, cases=cases, mode=mode)

def day(slug, title, explanation, example, *tasks):
    assert len(tasks) == 3
    DAYS.append(dict(slug=slug, title=title, explanation=explanation, example=example, tasks=tasks))

# Cases pair a tuple of positional arguments with an expected value or exception type.
day('values', 'Values and return statements',
    'Variables bind names to values. A function returns a value to its caller; printing only displays it. Start with short, explicit expressions.',
    'city = "Amsterdam"\nvisitors = 4\nprint(city, visitors)\nprint(type(city).__name__)',
    task('greet(name)', 'Return "Hello, NAME!" with name inserted exactly as supplied.', (( 'Ada',), 'Hello, Ada!'), (('',), 'Hello, !'), (('Lin Chen',), 'Hello, Lin Chen!')),
    task('describe(name, age)', 'Return "NAME is AGE years old." Assume age is a nonnegative integer.', (('Ada',36), 'Ada is 36 years old.'), (('Bo',0), 'Bo is 0 years old.'), (('Cy',101), 'Cy is 101 years old.')),
    task('swap_values(left, right)', 'Return a tuple containing right then left, preserving their types.', ((1,2),(2,1)), (('x',None),(None,'x')), ((True,3),(3,True))))
day('arithmetic', 'Arithmetic and numeric types',
    'Integers represent whole numbers; floats approximate real numbers. Compare / with // and %. Parentheses make calculation order explicit.',
    'print(17 / 4)\nprint(17 // 4, 17 % 4)\nprint(2 ** 5)',
    task('minutes_to_seconds(minutes)', 'Return minutes multiplied by 60. Accept nonnegative integers.', ((0,),0), ((3,),180), ((125,),7500)),
    task('rectangle_area(width, height)', 'Return width times height; dimensions are nonnegative numbers.', ((3,4),12), ((0,9),0), ((2.5,4),10.0)),
    task('split_seconds(total)', 'Return (hours, minutes, seconds) with minutes and seconds in 0..59. total is a nonnegative integer.', ((0,),(0,0,0)), ((3661,),(1,1,1)), ((90061,),(25,1,1))))
day('strings', 'Strings and formatting',
    'Strings are immutable sequences of characters. Methods return new strings. Formatting lets you combine text and values without changing the originals.',
    'label = "  Python  "\nprint(label.strip().lower())\nprint(f"Length: {len(label)}")',
    task('shout(text)', 'Return text converted to uppercase.', (('hello',),'HELLO'), (('',),''), (('Hi 2!',),'HI 2!')),
    task('initials(first, last)', 'Strip surrounding whitespace and return uppercase first letters joined by a dot and ending with a dot. Both stripped names are nonempty.', (('ada','lovelace'),'A.L.'), ((' Bo ',' chen '),'B.C.'), (('éva','smith'),'É.S.')),
    task('frame(text, border)', 'Return three lines: border repeated len(text)+4 times, then "B TEXT B", then the border line. border is one character; text has no newline.', (('Hi','*'),'******\n* Hi *\n******'), (('','#'),'####\n#  #\n####'), (('cat','-'),'-------\n- cat -\n-------')))
day('booleans', 'Booleans and comparisons',
    'Comparisons produce True or False. Use and, or, and not to combine conditions. Pay attention to inclusive and exclusive boundaries.',
    'temperature = 18\nprint(10 <= temperature < 25)\nprint(bool(""), bool("ready"))',
    task('is_even(number)', 'Return whether integer number is even.', ((2,),True), ((-3,),False), ((0,),True)),
    task('in_range(value, low, high)', 'Return whether low <= value <= high. Assume low <= high.', ((5,1,5),True), ((0,1,5),False), ((2,2,2),True)),
    task('can_enter(age, has_ticket, accompanied)', 'Return whether a person has a ticket and is at least 18 or is accompanied. Accompaniment never replaces a ticket.', ((18,True,False),True), ((12,True,True),True), ((30,False,True),False), ((17,True,False),False)))
day('conditions', 'Conditional decisions',
    'An if/elif/else chain chooses one branch. Put narrower conditions before broader ones when they overlap. Define boundary behavior before coding.',
    'wind = 12\nif wind >= 20:\n    print("strong")\nelif wind >= 10:\n    print("breezy")\nelse:\n    print("calm")',
    task('sign(number)', 'Return "positive", "negative", or "zero".', ((5,),'positive'), ((-1,),'negative'), ((0,),'zero')),
    task('grade(score)', 'For an integer score in 0..100, return A for >=90, B for >=80, C for >=70, D for >=60, otherwise F. Raise ValueError outside 0..100.', ((90,),'A'), ((79,),'C'), ((59,),'F'), ((101,),ValueError), ((-1,),ValueError)),
    task('shipping_cost(total, member)', 'Reject negative totals with ValueError. Shipping is 0 for totals >=50, otherwise 2 for members and 5 for others.', ((50,False),0), ((49,True),2), ((0,False),5), ((-1,True),ValueError)))
day('loops', 'Loops and accumulators',
    'A for loop visits items in order. Accumulators collect a running result. range excludes its stop value, so inspect small examples before choosing bounds.',
    'running = 0\nfor amount in [4, 7, 2]:\n    running += amount\n    print(running)',
    task('sum_to(n)', 'Return the sum of integers from 1 through n. n is nonnegative. Practice a loop.', ((0,),0), ((1,),1), ((5,),15)),
    task('count_multiples(n, divisor)', 'Count numbers in 1..n divisible by divisor. n >=0; divisor >0.', ((10,3),3), ((0,2),0), ((6,1),6)),
    task('fizzbuzz(n)', 'Return strings for 1..n: Fizz for multiples of 3, Buzz for 5, FizzBuzz for both, otherwise the number. n >=0.', ((0,),[]), ((5,),['1','2','Fizz','4','Buzz']), ((15,),['1','2','Fizz','4','Buzz','Fizz','7','8','Fizz','Buzz','11','Fizz','13','14','FizzBuzz'])))
day('functions', 'Functions and decomposition',
    'Functions make a named operation reusable. Parameters are inputs; the return value is output. Break a multi-step operation into small helpers if that improves clarity.',
    'def double(value):\n    return value * 2\n\nprint(double(7))\nprint(double(double(3)))',
    task('celsius_to_fahrenheit(celsius)', 'Return celsius * 9 / 5 + 32.', ((0,),32.0), ((100,),212.0), ((-40,),-40.0)),
    task('clamp(value, low, high)', 'Return value limited to inclusive bounds. Raise ValueError when low > high.', ((5,0,10),5), ((-2,0,10),0), ((12,0,10),10), ((1,3,2),ValueError)),
    task('compound_balance(principal, rate, years)', 'Return principal after years of annual multiplication by 1+rate. principal >=0, rate >=0, years is a nonnegative integer.', ((100,0.1,2),121.0), ((50,0.2,0),50), ((0,0.5,3),0)))
day('lists', 'Lists and mutation',
    'Lists keep ordered values and can be changed. Distinguish returning a new list from mutating an input. The contracts today require fresh results.',
    'items = ["tea", "bread"]\nitems.append("fruit")\nprint(items)\nprint(items[:2])',
    task('double_all(numbers)', 'Return a new list with each number doubled. Do not mutate numbers.', (([1,2,3],),[2,4,6]), (([],),[]), (([-2,0],),[-4,0])),
    task('positives(numbers)', 'Return a new list containing only values >0 in original order.', (([-1,0,3,2],),[3,2]), (([],),[]), (([-4,-2],),[])),
    task('running_totals(numbers)', 'Return a new list of cumulative sums, preserving order.', (([2,3,-1],),[2,5,4]), (([],),[]), (([0,4,0],),[0,4,4])))
day('dictionaries', 'Dictionaries and lookups',
    'Dictionaries map unique keys to values. Use get when a missing key has a default. Iteration order follows insertion order, but equality compares mappings.',
    'stock = {"tea": 3, "rice": 8}\nprint(stock.get("bread", 0))\nfor item, count in stock.items():\n    print(item, count)',
    task('lookup(mapping, key, default)', 'Return the value for key, or default when key is absent. Stored None is a real value.', (({'a':1},'a',0),1), (({},'x',7),7), (({'a':None},'a',5),None)),
    task('frequencies(items)', 'Return a dictionary counting hashable items.', ((['a','b','a'],),{'a':2,'b':1}), (([],),{}), (([1,1,2],),{1:2,2:1})),
    task('merge_totals(left, right)', 'Return a new dictionary adding numeric values for shared keys and retaining others. Do not change either input.', (({'a':2},{'a':3,'b':1}),{'a':5,'b':1}), (({},{}),{}), (({'x':-2},{'x':2}),{'x':0})))
day('receipt', 'Project: a receipt calculator',
    'Combine functions, loops, and mappings into a small calculation pipeline. Work in integer cents so this first project needs no floating-point rounding.',
    'prices = {"tea": 250, "cake": 400}\nprint(f"Tea costs {prices[\"tea\"]} cents")',
    task('line_total(price_cents, quantity)', 'Return price times quantity. Both are nonnegative integers; reject negative inputs with ValueError.', ((250,3),750), ((0,5),0), ((2,-1),ValueError)),
    task('subtotal(lines)', 'lines is a list of (price_cents, quantity) pairs. Return their combined cost; raise ValueError for any negative price or quantity.', (([(100,2),(250,1)],),450), (([],),0), (([(5,-1)],),ValueError)),
    task('receipt(lines, discount_cents)', 'Return {subtotal, discount, total}. Reject negative line values or negative discount. Applied discount cannot exceed subtotal.', (([(100,2)],50),{'subtotal':200,'discount':50,'total':150}), (([],10),{'subtotal':0,'discount':0,'total':0}), (([(10,1)],20),{'subtotal':10,'discount':10,'total':0}), (([],-1),ValueError)))
day('slicing', 'Indexing and slicing',
    'Indices start at zero; negative indices count from the end. Slices can select ranges and strides without failing on short sequences.',
    'letters = "abcdef"\nprint(letters[1:4])\nprint(letters[::2])\nprint(letters[-1])',
    task('first_last(items)', 'Return (first, last), or None for an empty list.', (([1,2,3],),(1,3)), (([4],),(4,4)), (([],),None)),
    task('every_other(items)', 'Return a list containing indices 0, 2, 4, ... without mutating input.', (([1,2,3,4,5],),[1,3,5]), (([],),[]), (([7],),[7])),
    task('rotate(items, steps)', 'Return a new list rotated right by steps. Negative steps rotate left; normalize steps for list length; empty stays empty.', (([1,2,3],1),[3,1,2]), (([1,2,3],-1),[2,3,1]), (([],100),[]), (([1,2,3],7),[3,1,2])))
day('tuples', 'Tuples and unpacking',
    'Tuples group related values without supporting item assignment. Unpacking gives each position a name. Structured return values can describe more than one result.',
    'point = (3, 5)\nx, y = point\nprint(x, y)\nprint((x + 1, y - 1))',
    task('move(point, delta)', 'Return the 2D point plus delta coordinate by coordinate as a tuple.', (((1,2),(3,-1)),(4,1)), (((0,0),(0,0)),(0,0)), (((-1,4),(1,2)),(0,6))),
    task('bounds(numbers)', 'Return (minimum, maximum), or None if empty.', (([3,1,7],),(1,7)), (([],),None), (([-2,-2],),(-2,-2))),
    task('zip_strict(left, right)', 'Return a list of paired tuples; raise ValueError for unequal lengths.', (([1,2],['a','b']),[(1,'a'),(2,'b')]), (([],[]),[]), (([1],[]),ValueError)))
day('sets', 'Sets and uniqueness',
    'Sets store unique hashable values. Union, intersection, and difference model relationships between collections. Set iteration order is not a contract.',
    'web = {"Ada", "Bo"}\nmobile = {"Bo", "Cy"}\nprint(sorted(web | mobile))\nprint(sorted(web & mobile))',
    task('unique_count(items)', 'Return the number of distinct hashable items.', (([1,1,2],),2), (([],),0), ((['a','A'],),2)),
    task('common_items(left, right)', 'Return a set of items present in both inputs.', (([1,2],[2,3]),{2}), (([],[1]),set()), ((['x','x'],['x']),{'x'})),
    task('missing_numbers(numbers, n)', 'Return sorted integers in 1..n absent from numbers. Ignore input values outside that range; n >=0.', (([1,3],4),[2,4]), (([],0),[]), (([0,1,1,9],3),[2,3])))
day('comprehensions', 'Comprehensions',
    'A comprehension expresses mapping or filtering concisely. Keep it readable; use a loop for complicated state or multiple decisions.',
    'names = ["Ada", "Bo", "Celia"]\nprint([len(name) for name in names])\nprint({name: len(name) for name in names})',
    task('squares(n)', 'Return squares of integers 0 through n-1; n >=0.', ((4,),[0,1,4,9]), ((0,),[]), ((1,),[0])),
    task('length_map(words)', 'Return a dictionary mapping each distinct word to its length.', ((['a','cat','a'],),{'a':1,'cat':3}), (([],),{}), (([''],),{'':0})),
    task('flatten(matrix)', 'Return a list of all row items in row order; rows may be empty.', (([[1,2],[],[3]],),[1,2,3]), (([],),[]), (([[],[]],),[])))
day('parameters', 'Defaults and function parameters',
    'Defaults make optional inputs explicit. Avoid mutable default values that can retain state across calls. Keyword arguments improve readability for optional settings.',
    'def label(text, prefix="Info"):\n    return f"{prefix}: {text}"\n\nprint(label("ready"))\nprint(label("done", prefix="Status"))',
    task('repeat(text, times=2)', 'Return text repeated times; reject negative times with ValueError.', (('ha',),'haha'), (('x',0),''), (('x',-1),ValueError)),
    task('join_words(words, separator=" ")', 'Return words joined by separator, with no added outer separators.', ((['a','b'],),'a b'), (([],','),''), ((['a','b'],'-'),'a-b')),
    task('add_item(item, items=None)', 'Return a fresh list with item appended. None starts an empty list. Never mutate a supplied list or retain state between calls.', (('a',),['a']), ((3,[1,2]),[1,2,3]), ((None,[]),[None])))
day('pure_functions', 'Scope and pure functions',
    'Local variables belong to a call. Pure functions depend on inputs and return results without hidden state. Copy mutable values when the contract requires independence.',
    'original = [2, 4]\ncopy = original.copy()\ncopy.append(6)\nprint(original, copy)',
    task('increment_all(numbers, amount)', 'Return a new list adding amount to each value. Do not mutate numbers.', (([1,2],3),[4,5]), (([],5),[]), (([0],-1),[-1])),
    task('with_setting(settings, key, value)', 'Return a new dictionary with key assigned value. Do not mutate settings.', (({'a':1},'b',2),{'a':1,'b':2}), (({},'a',None),{'a':None}), (({'a':1},'a',3),{'a':3})),
    task('normalize_scores(scores)', 'Return a fresh list divided by the largest score. Scores are nonnegative; if maximum is zero, return a same-length list of zeros.', (([2,4],),[0.5,1.0]), (([],),[]), (([0,0],),[0,0])))
day('exceptions', 'Exceptions and validation',
    'Exceptions communicate invalid operations. Catch only errors you can handle and validate at a clear boundary. Returning None is different from raising an exception.',
    'try:\n    int("not-a-number")\nexcept ValueError as error:\n    print(type(error).__name__)',
    task('parse_integer(text)', 'Return int(text), accepting whitespace and signs. Return None if conversion raises ValueError. text is a string.', (('  -12 ',),-12), (('2.5',),None), (('',),None)),
    task('divide(a, b)', 'Return a / b. Explicitly raise ValueError when b is zero.', ((6,3),2.0), ((0,2),0.0), ((1,0),ValueError)),
    task('require_keys(record, required)', 'Return a new dictionary of requested keys and their values; raise KeyError if any requested key is absent.', (({'a':1,'b':2},['b']),{'b':2}), (({},[]),{}), (({'a':None},['a']),{'a':None}), (({},['x']),KeyError)))
day('nested_data', 'Nested collections',
    'Nested lists and dictionaries describe structured data. Separate navigating a record from aggregating many records. Remember that shallow copies share nested objects.',
    'profile = {"name": "Ada", "skills": ["math", "code"]}\nprint(profile["skills"][0])\nprint(len(profile["skills"]))',
    task('names(records)', 'Return each record["name"] in order. All records contain name.', (([{'name':'Ada'},{'name':'Bo'}],),['Ada','Bo']), (([],),[]), (([{'name':''}],),[''])),
    task('group_by(records, key)', 'Return a dictionary mapping each record[key] to a list of matching records in original order. All records have key; do not mutate them.', (([{'k':'a','v':1},{'k':'a','v':2}], 'k'),{'a':[{'k':'a','v':1},{'k':'a','v':2}]}), (([],'x'),{}), (([{'k':1},{'k':2}], 'k'),{1:[{'k':1}],2:[{'k':2}]})),
    task('get_nested(record, path, default=None)', 'Traverse dictionary keys in path. Return default if a key is absent or an intermediate value is not a dictionary. Empty path returns record.', (({'a':{'b':2}},['a','b']),2), (({'a':None},['a','b'],'missing'),'missing'), (({},[],0),{}), (({},['x']),None)))
day('sorting', 'Sorting and key functions',
    'sorted returns a fresh list. A key function extracts the sort criterion. Python sorting is stable: equal keys retain input order.',
    'words = ["pear", "fig", "plum"]\nprint(sorted(words, key=len))\nprint(words)',
    task('sort_numbers(numbers)', 'Return numbers in ascending order without mutating input.', (([3,1,2],),[1,2,3]), (([],),[]), (([-1,2,-1],),[-1,-1,2])),
    task('sort_words(words)', 'Return words sorted by length then by case-sensitive lexicographic order.', ((['bb','a','aa'],),['a','aa','bb']), (([],),[]), ((['b','A','a'],),['A','a','b'])),
    task('rank_players(players)', 'Return records sorted by score descending, then name ascending. Each record has name and score; do not mutate input.', (([{'name':'Bo','score':5},{'name':'Ada','score':5},{'name':'Cy','score':9}],),[{'name':'Cy','score':9},{'name':'Ada','score':5},{'name':'Bo','score':5}]), (([],),[]), (([{'name':'X','score':0}],),[{'name':'X','score':0}])))
day('leaderboard', 'Project: leaderboard',
    'Compose validation, aggregation, and sorting. Decide how duplicate names and tied scores behave, and keep the output deterministic.',
    'rounds = [{"name": "Ada", "points": 4}, {"name": "Ada", "points": 2}]\nprint([row["points"] for row in rounds])',
    task('total_points(rounds)', 'rounds contains (name, points) pairs. Return summed points by name. Negative points are allowed.', (([('a',2),('b',1),('a',3)],),{'a':5,'b':1}), (([],),{}), (([('a',-1),('a',1)],),{'a':0})),
    task('top_players(totals, limit)', 'Return up to limit (name, score) tuples ordered by score descending then name ascending. Raise ValueError for negative limit.', (({'b':4,'a':4,'c':2},2),[('a',4),('b',4)]), (({},3),[]), (({'x':2},0),[]), (({},-1),ValueError)),
    task('competition_ranks(totals)', 'Return (name, score, rank) tuples in descending score/name ascending order. Ties share rank and leave gaps: 1,1,3.', (({'b':5,'a':5,'c':3},),[('a',5,1),('b',5,1),('c',3,3)]), (({},),[]), (({'x':9},),[('x',9,1)])))
day('text_cleaning', 'Cleaning text',
    'Normalize only what the specification allows. Splitting on whitespace handles tabs and repeated spaces. Preserve meaningful punctuation unless asked to remove it.',
    'text = "  Learn\tPython   today  "\nprint(text.split())\nprint(" ".join(text.split()))',
    task('collapse_spaces(text)', 'Return whitespace-separated words joined by single spaces.', ((' a\t b\n',),'a b'), (('',),''), (('hello!',),'hello!')),
    task('slugify(text)', 'Lowercase text, split on whitespace, and join with hyphens. Keep punctuation unchanged.', ((' Hello World ',),'hello-world'), (('',),''), (('A & B',),'a-&-b')),
    task('word_counts(text)', 'Split on whitespace, lowercase words, strip only . , ! ? from both ends of each word, ignore empty results, and count.', (('Hi, hi! Bye.',),{'hi':2,'bye':1}), (('!?',),{}), (("It's PYTHON",),{"it's":1,'python':1})))
day('regex', 'Regular expressions',
    'Regular expressions describe text patterns. Use raw string literals for backslashes. fullmatch validates an entire string; findall extracts repeated matches.',
    'import re\nprint(re.findall(r"[A-Z]+", "ID 42: OK"))\nprint(bool(re.fullmatch(r"[a-z]+", "python")))',
    task('extract_integers(text)', 'Extract signed decimal integers matching -?[0-9]+ in encounter order and return ints. A plus sign is not part of the match.', (('a -12 b 3',),[-12,3]), (('none',),[]), (('x+4 y007',),[4,7])),
    task('valid_identifier(text)', 'Return whether text matches ASCII [A-Za-z_][A-Za-z0-9_]*. Keywords such as class are allowed in this exercise.', (('_x2',),True), (('2x',),False), (('',),False), (('café',),False)),
    task('redact_emails(text)', 'Replace matches of [A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,} with [redacted]. Preserve other text. This is a deliberately limited pattern.', (('Mail a@b.com now',),'Mail [redacted] now'), (('a@b.com c@d.org',),'[redacted] [redacted]'), (('no email',),'no email')))
day('parsing', 'Parsing structured text',
    'Parsing transforms text into structured values. Define whitespace, duplicate fields, and malformed input behavior before building the parser.',
    'line = "name = Ada"\nkey, value = line.split("=", 1)\nprint(key.strip(), value.strip())',
    task('parse_pair(text)', 'Split at the first = and strip both sides; return (key, value). Raise ValueError if = is missing or stripped key is empty.', ((' a = b=c ',),('a','b=c')), (('x=',),('x','')), (('oops',),ValueError), (('=x',),ValueError)),
    task('parse_config(text)', 'Parse nonblank lines as key=value with stripping. Ignore lines whose stripped form starts #. Later duplicate keys win. Raise ValueError for malformed lines or empty keys.', (('# hi\na=1\na=2\nb=x',),{'a':'2','b':'x'}), (('',),{}), (('bad',),ValueError)),
    task('parse_ranges(text)', 'Parse comma-separated positive ASCII integers or ascending ranges such as 2-4. Ignore token-edge whitespace; return sorted unique ints. Empty text returns []; reject malformed, zero, or descending tokens with ValueError.', (('1, 3-5,3',),[1,3,4,5]), (('',),[]), (('5-2',),ValueError), (('0',),ValueError), (('1,',),ValueError)))
day('dates', 'Dates and timedeltas',
    'The datetime module handles calendar rules. A date has no time zone; a timedelta expresses duration. Use ISO dates for unambiguous inputs.',
    'from datetime import date, timedelta\nstart = date(2024, 2, 28)\nprint(start + timedelta(days=2))\nprint(start.isoformat())',
    task('next_day(iso_date)', 'Parse YYYY-MM-DD using date.fromisoformat and return the next date in ISO form; propagate ValueError for invalid dates.', (('2024-02-28',),'2024-02-29'), (('2023-12-31',),'2024-01-01'), (('2023-02-29',),ValueError)),
    task('days_between(start, end)', 'Return end minus start in days for ISO dates; negative differences are allowed.', (('2024-01-01','2024-01-03'),2), (('2024-03-01','2024-02-28'),-2), (('2020-01-01','2020-01-01'),0)),
    task('business_days(start, end)', 'Count Monday-Friday dates in the inclusive ISO interval. Ignore holidays; return 0 when end precedes start.', (('2024-01-01','2024-01-07'),5), (('2024-01-06','2024-01-07'),0), (('2024-01-08','2024-01-01'),0)))
day('decimal_money', 'Decimal arithmetic',
    'Decimal constructed from strings avoids binary floating-point conversion. Specify the rounding rule when converting money to a fixed precision.',
    'from decimal import Decimal, ROUND_HALF_UP\nvalue = Decimal("1.005")\nprint(value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))',
    task('money(text)', 'Return a two-decimal string rounded with Decimal ROUND_HALF_UP. text is a valid finite decimal string.', (('1.005',),'1.01'), (('2',),'2.00'), (('-1.005',),'-1.01')),
    task('add_money(amounts)', 'Sum valid finite decimal strings exactly, then round HALF_UP once to a two-decimal string.', ((['0.1','0.2'],),'0.30'), (([],),'0.00'), ((['0.005','0.005'],),'0.01')),
    task('allocate_cents(total, people)', 'Split nonnegative integer cents evenly into people shares. First total % people shares get one extra cent. Raise ValueError for negative total or people <=0.', ((10,3),[4,3,3]), ((0,2),[0,0]), ((1,0),ValueError), ((-1,2),ValueError)))
day('files', 'Reading files safely',
    'Use pathlib and explicit UTF-8 encoding. A context manager closes resources even if processing fails. Tests create temporary files, so your code needs no external data.',
    'from pathlib import Path\nfrom uuid import uuid4\nscratch = Path(__file__).parent / ".practice_tmp"\nscratch.mkdir(exist_ok=True)\npath = scratch / f"note_{uuid4().hex}.txt"\ntry:\n    with path.open("w", encoding="utf-8") as handle:\n        handle.write("hello")\n    with path.open("r", encoding="utf-8") as handle:\n        print(handle.read())\nfinally:\n    path.unlink(missing_ok=True)',
    task('read_text(path)', 'Return the entire UTF-8 file content, preserving line breaks. path is a pathlib.Path.', ((File('hello\n'),),'hello\n'), ((File(''),),''), ((File('café'),),'café')),
    task('nonempty_lines(path)', 'Read UTF-8 text and return stripped nonempty lines in order.', ((File(' a \n\n b\t\n'),),['a','b']), ((File(''),),[]), ((File(' café '),),['café'])),
    task('file_stats(path)', 'Return {lines, words, characters}. lines uses str.splitlines(), words uses str.split(), characters uses len on the full UTF-8 text.', ((File('a b\nc\n'),),{'lines':2,'words':3,'characters':6}), ((File(''),),{'lines':0,'words':0,'characters':0}), ((File('é'),),{'lines':1,'words':1,'characters':1})))
day('csv', 'CSV records',
    'CSV fields may contain commas or newlines inside quotes. Use the csv module rather than splitting on commas. Treat parsed numeric fields explicitly.',
    'import csv\nimport io\nrows = csv.reader(io.StringIO(\'name,city\\nAda,"New York"\\n\'))\nprint(list(rows))',
    task('parse_csv(text)', 'Return all CSV rows as lists of strings using csv.reader. Empty text returns [].', (('a,b\n1,2\n',),[['a','b'],['1','2']]), (('',),[]), (('"a,b",c\n',),[['a,b','c']])),
    task('csv_records(text)', 'Use first CSV row as headers; return remaining rows as dictionaries of strings. Inputs have unique headers and equal row lengths.', (('name,age\nAda,36\n',),[{'name':'Ada','age':'36'}]), (('',),[]), (('x\n"a,b"\n',),[{'x':'a,b'}])),
    task('sum_csv_column(text, column)', 'Parse CSV with headers and sum integer values in column. Return 0 for header-only input; raise KeyError for absent column, ValueError for a noninteger value. Input always has a header.', (('x,y\n2,9\n3,8\n','x'),5), (('x\n','x'),0), (('x\n1\n','z'),KeyError), (('x\nno\n','x'),ValueError)))
day('json', 'JSON serialization',
    'JSON represents portable data with objects, arrays, strings, numbers, booleans, and null. Python tuples become arrays. Decide how strictly to validate the decoded shape.',
    'import json\nencoded = json.dumps({"ready": True, "count": 2})\nprint(encoded)\nprint(json.loads(encoded))',
    task('parse_json(text)', 'Return json.loads(text); malformed input raises ValueError (JSONDecodeError is a subclass).', (('{"a":1}',),{'a':1}), (('[true,null]',),[True,None]), (('oops',),ValueError)),
    task('canonical_json(value)', 'Return json.dumps with sort_keys=True, separators=(",", ":"), ensure_ascii=False. Inputs contain JSON-compatible values.', (({'b':2,'a':'é'},),'{"a":"é","b":2}'), (([],),'[]'), ((None,),'null')),
    task('load_users(text)', 'Decode a JSON list of objects each with a nonempty string name; return names in order. Reject other shapes and invalid names with ValueError; malformed JSON also raises ValueError.', (('[{"name":"Ada"},{"name":"Bo"}]',),['Ada','Bo']), (('[]',),[]), (('{}',),ValueError), (('[{"name":""}]',),ValueError), (('[{"name":3}]',),ValueError)))
day('paths', 'Portable paths',
    'pathlib separates path operations from string manipulation. PurePosixPath is useful for platform-independent logical paths. A suffix describes only the final extension.',
    'from pathlib import PurePosixPath\np = PurePosixPath("reports/annual.csv")\nprint(p.name, p.stem, p.suffix)\nprint(p.parent)',
    task('file_extension(path)', 'Treat path as PurePosixPath and return its final suffix lowercased, including dot.', (('a/B.TXT',),'.txt'), (('README',),''), (('archive.tar.gz',),'.gz')),
    task('replace_extension(path, suffix)', 'Return str(PurePosixPath(path).with_suffix(suffix)). suffix is empty or starts with a dot and is valid.', (('a/b.txt','.csv'),'a/b.csv'), (('file',''),'file'), (('a.tar.gz','.zip'),'a.tar.zip')),
    task('safe_relative(path)', 'For a logical POSIX path, return False if absolute or if any part is ..; otherwise True. Empty path and . are allowed.', (('images/a.png',),True), (('../secret',),False), (('/etc/passwd',),False), (('a/../b',),False), (('',),True)))
day('expense_report', 'Project: expense report',
    'Build a deterministic report from structured transactions. Keep cents as integers, validate records, and distinguish aggregation from presentation.',
    'expenses = [{"category": "travel", "cents": 250}]\nprint(expenses[0]["category"], expenses[0]["cents"])',
    task('validate_expense(record)', 'Return True if record is a dict with a nonempty string category and nonnegative integer cents (bool is invalid), otherwise False. Extra keys are allowed.', (({'category':'food','cents':0},),True), (({'category':'','cents':1},),False), (({'category':'x','cents':True},),False), (([],),False)),
    task('category_totals(records)', 'Return summed cents by category. Raise ValueError for any record failing the preceding contract.', (([{'category':'a','cents':2},{'category':'a','cents':3}],),{'a':5}), (([],),{}), (([{'category':'x','cents':-1}],),ValueError)),
    task('expense_report(records)', 'Validate as above, then return {total, categories}; categories is a list of (category, cents) sorted by total descending then category ascending.', (([{'category':'b','cents':2},{'category':'a','cents':2}],),{'total':4,'categories':[('a',2),('b',2)]}), (([],),{'total':0,'categories':[]}), (([{'category':'x','cents':-1}],),ValueError)))
day('collections', 'Counter and defaultdict',
    'collections offers common aggregation tools. Counter tracks frequencies; defaultdict creates a value when a missing key is accessed. Return ordinary dicts where required.',
    'from collections import Counter, defaultdict\nprint(Counter("banana"))\ngroups = defaultdict(list)\ngroups["fruit"].append("pear")\nprint(dict(groups))',
    task('most_common(items, limit)', 'Return up to limit (item, count) pairs, count descending and item lexicographically ascending on ties. Items are strings; limit >=0.', ((['b','a','b','a','c'],2),[('a',2),('b',2)]), (([],3),[]), ((['x'],0),[])),
    task('group_lengths(words)', 'Return a dict mapping lengths to word lists in input order, including duplicates.', ((['a','bb','c'],),{1:['a','c'],2:['bb']}), (([],),{}), ((['',''],),{0:['','']})),
    task('inventory_difference(before, after)', 'Return a dict of after count minus before count for all items whose counts changed. Inputs are lists of strings; omit zero differences.', ((['a','a','b'],['a','c']),{'a':-1,'b':-1,'c':1}), (([],[]),{}), ((['x'],['x','x']),{'x':1})))
day('deque', 'Queues and deques',
    'A deque supports efficient operations at both ends. Queue simulations should define exactly when events are processed and how empty states behave.',
    'from collections import deque\nqueue = deque(["Ada", "Bo"])\nqueue.append("Cy")\nprint(queue.popleft())\nprint(list(queue))',
    task('serve_queue(arrivals)', 'Return a fresh list of arrival names in FIFO order. Practice deque append and popleft.', ((['a','b'],),['a','b']), (([],),[]), ((['a','a'],),['a','a'])),
    task('recent_items(items, capacity)', 'Return the last capacity items in input order. capacity >=0; zero returns []. Practice deque(maxlen=...).', (([1,2,3],2),[2,3]), (([1],0),[]), (([],3),[])),
    task('round_robin(queues)', 'Return one item from each nonempty queue per round in queue order, until all are exhausted. Do not mutate input.', (([[1,2],['a'],[True,False]],),[1,'a',True,2,False]), (([[],[1,2]],),[1,2]), (([],),[])))
day('iterators', 'Iterator protocols',
    'iter obtains an iterator and next consumes it. Iterators can be exhausted and need not support len or indexing. Today inputs are generic iterables.',
    'stream = iter([10, 20])\nprint(next(stream))\nprint(next(stream))\nprint(next(stream, "finished"))',
    task('first_or(iterable, default=None)', 'Return first item or default if empty; consume no more than one item.', (([1,2],),1), (([],),None), (([],7),7)),
    task('take(iterable, n)', 'Return a list of the first up to n items; n >=0. Accept generators and avoid consuming items after the selected prefix.', (([1,2,3],2),[1,2]), (([],3),[]), (([1,2],0),[])),
    task('pairwise(iterable)', 'Return a list of adjacent pairs from a single pass over iterable.', (([1,2,3],),[(1,2),(2,3)]), (([],),[]), (([1],),[])))
day('generators', 'Generator functions',
    'yield suspends a function and produces one value at a time. Generator pipelines avoid materializing intermediate lists. These exercises must return iterators, not lists.',
    'def countdown(start):\n    while start > 0:\n        yield start\n        start -= 1\n\nprint(list(countdown(3)))',
    task('evens(limit)', 'Yield even integers from 0 through limit-1; limit >=0.', ((5,),[0,2,4]), ((0,),[]), ((2,),[0]), mode='iterator'),
    task('chunks(iterable, size)', 'Yield lists of up to size items, including a final partial chunk. Raise ValueError for size <=0 when iterated.', (([1,2,3,4,5],2),[[1,2],[3,4],[5]]), (([],3),[]), (([1],0),ValueError), mode='iterator'),
    task('unique_everseen(iterable)', 'Yield each hashable item only on its first occurrence, preserving order.', ((['b','a','b','c'],),['b','a','c']), (([],),[]), (([0,0,1],),[0,1]), mode='iterator'))
day('itertools', 'Combining iterables',
    'itertools supplies lazy building blocks for chaining, grouping, and combinations. groupby groups consecutive keys, so sorting and grouping solve different problems.',
    'from itertools import chain, combinations\nprint(list(chain([1, 2], [3])))\nprint(list(combinations("ABC", 2)))',
    task('all_pairs(items)', 'Return all index-order two-item combinations as tuples. Preserve duplicate values when they occupy different positions.', (([1,2,3],),[(1,2),(1,3),(2,3)]), (([],),[]), ((['a','a'],),[('a','a')])),
    task('run_lengths(items)', 'Return (item, count) tuples for consecutive equal runs.', ((['a','a','b','a'],),[('a',2),('b',1),('a',1)]), (([],),[]), (([1,1,1],),[(1,3)])),
    task('cartesian_product(left, right)', 'Return all (left_item, right_item) pairs in nested-loop order, left outermost.', (([1,2],['a','b']),[(1,'a'),(1,'b'),(2,'a'),(2,'b')]), (([],[1]),[]), (([1],[]),[])))
day('higher_order', 'Higher-order functions',
    'Functions are values that can be passed and returned. A higher-order function accepts a callable or returns one. Tests supply functions as inputs.',
    'def apply_twice(function, value):\n    return function(function(value))\n\nprint(apply_twice(str.upper, "ready"))',
    task('apply_all(function, items)', 'Return a list of function(item) for each item in order.', (('CALL:int',['1','2']),[1,2]), (('CALL:str',[]),[]), (('CALL:abs',[-2,3]),[2,3])),
    task('filter_by(predicate, items)', 'Return items whose predicate result is truthy, preserving order.', (('CALL:bool',[0,1,'',2]),[1,2]), (('CALL:bool',[]),[]), (('CALL:str.isupper',['A','a','B']),['A','B'])),
    task('compose_apply(functions, value)', 'Apply functions from right to left to value; empty functions returns value.', ((['CALL:str.upper','CALL:str.strip'],' hi '),'HI'), (([],3),3), ((['CALL:abs','CALL:int'],'-7'),7)))
day('recursion', 'Recursion and base cases',
    'Recursive functions solve a smaller version of the same problem. Every path needs a base case. These exercises use small inputs; trace the call stack by hand.',
    'def countdown(n):\n    if n == 0:\n        return "done"\n    return f"{n} " + countdown(n - 1)\n\nprint(countdown(3))',
    task('factorial(n)', 'Return n! recursively; 0! is 1. Raise ValueError for negative n.', ((0,),1), ((5,),120), ((-1,),ValueError)),
    task('nested_sum(value)', 'Recursively sum integers in arbitrarily nested lists. value is an integer or a list of such values.', (([1,[2,[3]],[]],),6), (([],),0), ((-2,),-2)),
    task('flatten_nested(value)', 'Return all non-list leaves from nested lists in order. A scalar input becomes a one-item list.', (([1,[2,[],[3]]],),[1,2,3]), (([],),[]), (('x',),['x'])))
day('searching', 'Linear and binary search',
    'Linear search checks each item. Binary search halves a sorted range at each step. Empty ranges and duplicate values need explicit behavior.',
    'from bisect import bisect_left\nvalues = [2, 4, 4, 8]\nprint(bisect_left(values, 4))\nprint(bisect_left(values, 5))',
    task('linear_find(items, target)', 'Return first matching index or -1 when absent.', (([3,1,3],3),0), (([],1),-1), (([1,2],2),1)),
    task('binary_find(sorted_items, target)', 'Return the first matching index or -1. Input is sorted ascending; implement binary search.', (([1,2,2,4],2),1), (([],0),-1), (([1,3],2),-1), (([1,3],3),1)),
    task('insertion_index(sorted_items, target)', 'Return leftmost insertion position preserving ascending order. Implement binary search.', (([1,2,2,4],2),1), (([],3),0), (([1,3],9),2)))
day('complexity', 'Algorithmic complexity',
    'Complexity describes how work grows with input size. Dictionaries and sets often replace repeated scans. Correctness tests do not prove a complexity bound; explain your approach.',
    'values = [4, 8, 4]\nseen = set()\nfor value in values:\n    print(value in seen)\n    seen.add(value)',
    task('has_duplicate(items)', 'Return whether hashable items contain a duplicate. Aim for expected O(n) time.', (([1,2,1],),True), (([],),False), (([1,2],),False)),
    task('two_sum(numbers, target)', 'Return (i, j) with i < j whose values sum to target, or None. Scan j ascending; pick the earliest matching i for the first valid j. Aim for O(n).', (([2,7,11],9),(0,1)), (([3,3],6),(0,1)), (([1,2],9),None), (([1,1,2],3),(0,2))),
    task('longest_unique(text)', 'Return length of the longest substring with no repeated characters. Aim for O(n) with a sliding window.', (('abcabcbb',),3), (('',),0), (('bbbbb',),1), (('abba',),2)))
day('text_index', 'Project: searchable text index',
    'Build an inverted index that maps terms to documents. Separate tokenization, indexing, and queries. Normalize consistently at every stage.',
    'documents = {"a": "Python learning", "b": "Python testing"}\nprint(sorted(documents))\nprint(documents["a"].lower().split())',
    task('tokens(text)', 'Return lowercase ASCII word matches [a-z0-9]+, preserving repetition and order. Lowercase before matching.', (('Python, PYTHON 3!',),['python','python','3']), (('',),[]), (('a_b',),['a','b'])),
    task('build_index(documents)', 'Map normalized tokens to sets of document IDs. documents maps string IDs to text; use the preceding token rules.', (({'a':'Hi hi','b':'hi bye'},),{'hi':{'a','b'},'bye':{'b'}}), (({},),{}), (({'a':'!!!'},),{})),
    task('search(index, query)', 'Normalize query with the token rules above and return sorted IDs present in ALL query terms. Empty query or any missing term returns []. Do not mutate index sets.', (({'hi':{'a','b'},'bye':{'b'}},'HI bye'),['b']), (({'a':{'x'}},''),[]), (({'a':{'x'}},'missing'),[])))
day('classes', 'Classes and instance state',
    'A class combines state and behavior. Each instance should own its mutable state. Constructors establish valid initial values; methods operate on that instance.',
    'class Label:\n    def __init__(self, text):\n        self.text = text\n\n    def render(self):\n        return f"[{self.text}]"\n\nprint(Label("ready").render())',
    task('class Counter(start=0)', 'Expose value initialized to start. increment() adds 1 and returns the new value; reset() sets value to start and returns None.', ((),ObjectChecks([('@value',(),0),('increment',(),1),('increment',(),2),('reset',(),None),('@value',(),0)])), ((5,),ObjectChecks([('increment',(),6),('reset',(),None),('@value',(),5)])), ((-1,),ObjectChecks([('increment',(),0)]))),
    task('class Rectangle(width, height)', 'Store nonnegative width and height, rejecting negatives with ValueError. area() returns width*height; perimeter() returns 2*(width+height).', ((3,4),ObjectChecks([('area',(),12),('perimeter',(),14)])), ((0,2),ObjectChecks([('area',(),0),('perimeter',(),4)])), ((-1,2),ValueError)),
    task('class BankAccount(balance=0)', 'Expose nonnegative integer balance. deposit(amount) and withdraw(amount) return new balance; reject negative amounts, negative initial balance, or overdraft with ValueError, leaving balance unchanged.', ((10,),ObjectChecks([('deposit',(5,),15),('withdraw',(8,),7),('withdraw',(8,),ValueError),('@balance',(),7)])), ((),ObjectChecks([('deposit',(-1,),ValueError),('@balance',(),0)])), ((-1,),ValueError)))
day('dataclasses', 'Dataclasses and value objects',
    'Dataclasses generate constructors, repr, and equality for declared fields. Frozen instances protect field assignment. Type annotations document expectations without enforcing them.',
    'from dataclasses import dataclass\n@dataclass(frozen=True)\nclass Tag:\n    name: str\n\nprint(Tag("python") == Tag("python"))',
    task('class Point(x, y)', 'Implement as a frozen dataclass with x and y fields. distance_from_origin() returns Euclidean distance.', ((3,4),ObjectChecks([('@x',(),3),('@y',(),4),('distance_from_origin',(),5.0)])), ((0,0),ObjectChecks([('distance_from_origin',(),0.0)])), ((-3,4),ObjectChecks([('distance_from_origin',(),5.0)]))),
    task('class Product(name, price_cents)', 'Implement as a frozen dataclass. Reject empty name or negative price_cents with ValueError. total(quantity) returns price times quantity; reject negative quantity.', (('tea',250),ObjectChecks([('@name',(),'tea'),('total',(3,),750),('total',(-1,),ValueError)])), (('',10),ValueError), (('x',-1),ValueError)),
    task('class TodoList()', 'Implement as a dataclass with independent items list default. add(text) appends and returns None. pending() returns a fresh list of items.', ((),ObjectChecks([('pending',(),[]),('add',('read',),None),('pending',(),['read'])])), ((),ObjectChecks([('add',('code',),None),('add',('test',),None),('pending',(),['code','test'])])), ((),ObjectChecks([('pending',(),[])]))))
day('polymorphism', 'Polymorphism and interfaces',
    'Different objects can implement the same method. Callers depend on that interface rather than concrete type. Composition often keeps designs simpler than deep inheritance.',
    'class Plain:\n    def render(self):\n        return "plain"\n\nclass Fancy:\n    def render(self):\n        return "**fancy**"\n\nprint([obj.render() for obj in [Plain(), Fancy()]])',
    task('class FixedDiscount(cents)', 'Reject negative cents. apply(total) returns max(0, total-cents); total is nonnegative.', ((3,),ObjectChecks([('apply',(10,),7),('apply',(2,),0)])), ((0,),ObjectChecks([('apply',(5,),5)])), ((-1,),ValueError)),
    task('class PercentDiscount(percent)', 'Reject integer percent outside 0..100. apply(total) returns total minus floor(total*percent/100); total is nonnegative integer cents.', ((25,),ObjectChecks([('apply',(10,),8),('apply',(100,),75)])), ((100,),ObjectChecks([('apply',(5,),0)])), ((101,),ValueError)),
    task('discounted_total(total, discounts)', 'Apply each callable discount to the running total from left to right; empty returns total. Callables accept and return a number. Practice an interchangeable interface.', ((10,['CALL:abs','CALL:float']),10.0), ((-3,['CALL:abs']),3), ((5,[]),5)))
day('properties', 'Properties and invariants',
    'A property gives attribute-style access to controlled behavior. Validate before mutating state so failed updates preserve a valid instance.',
    'class Constant:\n    @property\n    def value(self):\n        return 42\n\nprint(Constant().value)',
    task('class Temperature(celsius)', 'Expose read-only celsius and fahrenheit properties; fahrenheit = celsius*9/5+32. set_celsius(value) returns None and rejects values below -273.15, including at construction.', ((0,),ObjectChecks([('@fahrenheit',(),32.0),('set_celsius',(100,),None),('@fahrenheit',(),212.0)])), ((-273.15,),ObjectChecks([('@celsius',(),-273.15),('set_celsius',(-300,),ValueError),('@celsius',(),-273.15)])), ((-300,),ValueError)),
    task('class BoundedCounter(limit)', 'limit is a nonnegative integer. Expose read-only value starting at 0. increment() returns new value or raises ValueError at limit without changing it.', ((2,),ObjectChecks([('increment',(),1),('increment',(),2),('increment',(),ValueError),('@value',(),2)])), ((0,),ObjectChecks([('increment',(),ValueError)])), ((-1,),ValueError)),
    task('class Cart()', 'add(name, cents) stores or replaces a nonnegative price; reject negatives before changing state. remove(name) returns removed price, raising KeyError if absent. Read-only total sums prices.', ((),ObjectChecks([('add',('a',3),None),('add',('b',2),None),('@total',(),5),('remove',('a',),3),('@total',(),2)])), ((),ObjectChecks([('add',('x',4),None),('add',('x',-1),ValueError),('@total',(),4)])), ((),ObjectChecks([('remove',('x',),KeyError),('@total',(),0)]))))
day('object_protocols', 'Python object protocols',
    'Special methods connect your objects to len, iteration, and containment. Implement the expected protocol rather than requiring callers to know internal storage.',
    'class Words:\n    def __init__(self, text):\n        self.words = text.split()\n\n    def __len__(self):\n        return len(self.words)\n\nprint(len(Words("hello world")))',
    task('class Playlist(songs)', 'Copy songs at construction. Implement __len__, __iter__, and __contains__ with ordinary list behavior.', ((['a','b'],),ObjectChecks([('__len__',(),2),('__contains__',('a',),True),('__contains__',('x',),False),('!list',(),['a','b'])])), (([],),ObjectChecks([('__len__',(),0),('!list',(),[])])), ((['a','a'],),ObjectChecks([('!list',(),['a','a'])]))),
    task('class RangeBox(low, high)', 'Reject low > high. Implement __contains__ for inclusive numeric bounds and __len__ as high-low+1. Bounds are integers.', ((2,4),ObjectChecks([('__contains__',(3,),True),('__contains__',(5,),False),('__len__',(),3)])), ((0,0),ObjectChecks([('__len__',(),1)])), ((3,2),ValueError)),
    task('class Polynomial(coefficients)', 'Copy coefficients in ascending power order. __call__(x) evaluates the polynomial; __len__ returns coefficient count (including trailing zeros). Empty evaluates to 0.', (([1,2,3],),ObjectChecks([('__call__',(2,),17),('__len__',(),3)])), (([],),ObjectChecks([('__call__',(8,),0),('__len__',(),0)])), (([0,1],),ObjectChecks([('__call__',(-3,),-3)]))))
day('context_managers', 'Context managers',
    'A context manager brackets resource use with setup and cleanup. contextlib provides helpers. Cleanup must happen even when the body raises.',
    'from contextlib import contextmanager\n@contextmanager\ndef announced():\n    print("enter")\n    try:\n        yield\n    finally:\n        print("exit")\n\nwith announced():\n    print("body")',
    task('read_first_line(path)', 'Read a UTF-8 file using a context manager. Return its first line without trailing CR/LF, preserving spaces; empty file returns "".', ((File(' hi \nnext'),),' hi '), ((File(''),),''), ((File('one'),),'one')),
    task('capture_output(function)', 'Call a zero-argument function while capturing stdout with contextlib.redirect_stdout; return captured string. Propagate any exception.', (('CALL:print_ready',),'ready\n'), (('CALL:print_nothing',),''), (('CALL:raise_value',),ValueError)),
    task('temporary_setting(mapping, key, value, function)', 'Temporarily assign mapping[key]=value; call function(mapping) and return its result. Restore previous value or absence even on exceptions. Other keys remain untouched.', (({'x':1},'x',9,'CALL:read_x'),9), (({},'x',3,'CALL:read_x'),3), (({'x':2},'x',8,'CALL:raise_value'),ValueError)))
day('decorators', 'Decorators and wrappers',
    'A decorator receives a function and returns a replacement callable. functools.wraps preserves metadata. Wrappers must forward positional and keyword arguments.',
    'from functools import wraps\ndef announce(function):\n    @wraps(function)\n    def wrapper(*args, **kwargs):\n        print("calling", function.__name__)\n        return function(*args, **kwargs)\n    return wrapper\n\n@announce\ndef ping():\n    return "pong"\n\nprint(ping())',
    task('call_repeated(function, times, args)', 'Call function(*args) times and return the list of results; times >=0. This is the core behavior of a repetition wrapper.', (('CALL:abs',3,(-2,)),[2,2,2]), (('CALL:int',0,('1',)),[]), (('CALL:str',1,(5,)),['5'])),
    task('class Counted(function)', 'Callable wrapper with calls starting at 0. __call__(*args, **kwargs) increments calls BEFORE invoking function and returns its result; count failed calls too.', (('CALL:abs',),ObjectChecks([('__call__',(-2,),2),('__call__',(3,),3),('@calls',(),2)])), (('CALL:int',),ObjectChecks([('__call__',('bad',),ValueError),('@calls',(),1)])), (('CALL:str',),ObjectChecks([('@calls',(),0)]))),
    task('class Memoized(function)', 'Callable wrapper accepting positional hashable arguments. Cache successful return values by argument tuple; expose cache dict. Never cache exceptions.', (('CALL:abs',),ObjectChecks([('__call__',(-2,),2),('__call__',(-2,),2),('@cache',(),{(-2,):2})])), (('CALL:int',),ObjectChecks([('__call__',('bad',),ValueError),('@cache',(),{})])), (('CALL:str',),ObjectChecks([('__call__',(1,),'1'),('__call__',(2,),'2'),('@cache',(),{(1,):'1',(2,):'2'})]))))
day('typing', 'Type hints and optional values',
    'Annotations communicate shapes and enable optional static checking. They do not perform runtime validation. Distinguish a missing value from a falsy valid value.',
    'def length(text: str) -> int:\n    return len(text)\n\nprint(length("typed"))\nprint(length.__annotations__)',
    task('first_present(values)', 'Return the first value that is not None, or None if all are None. Add type hints of your choice.', (([None,0,2],),0), (([],),None), (([None,False],),False)),
    task('parse_optional_int(text)', 'Strip text. Return None for empty text, otherwise convert to int and propagate ValueError. Annotate as str -> int | None.', ((' ',),None), (('0',),0), (('bad',),ValueError)),
    task('partition_optional(values)', 'Return (present_list, missing_count), preserving all non-None values in order. Add useful annotations.', (([None,0,False,None],),([0,False],2)), (([],),([],0)), ((['x'],),(['x'],0))))
day('enums', 'Enums and explicit states',
    'Enums give states meaningful identities. State transitions should reject unsupported actions rather than silently producing impossible combinations.',
    'from enum import Enum\nclass Light(Enum):\n    RED = "red"\n    GREEN = "green"\n\nprint(Light.RED.value)\nprint(Light("green").name)',
    task('traffic_next(state)', 'Return next string in cycle red -> green -> amber -> red. Raise ValueError for unknown state.', (('red',),'green'), (('amber',),'red'), (('blue',),ValueError)),
    task('order_transition(state, action)', 'Allowed transitions: new/pay -> paid, new/cancel -> cancelled, paid/ship -> shipped, paid/cancel -> cancelled. All others raise ValueError. Return new state.', (('new','pay'),'paid'), (('paid','ship'),'shipped'), (('shipped','cancel'),ValueError)),
    task('run_order(actions)', 'Start at new, apply preceding transition rules, and return final state. Empty actions returns new; invalid action at any point raises ValueError.', ((['pay','ship'],),'shipped'), (([],),'new'), ((['cancel','pay'],),ValueError)))
day('library', 'Project: lending library',
    'Model a small domain with explicit invariants. Keep available copies separate from outstanding loans and prevent invalid operations from partially updating state.',
    'catalog = {"Python": 2, "Algorithms": 1}\nprint(sum(catalog.values()))\nprint("Python" in catalog)',
    task('class Book(title, copies)', 'Store nonempty title and nonnegative integer copies; invalid values raise ValueError. available() returns copies.', (('Python',2),ObjectChecks([('@title',(),'Python'),('available',(),2)])), (('',1),ValueError), (('X',-1),ValueError)),
    task('class LendingDesk(catalog)', 'Copy title->nonnegative copy counts. borrow(title) decrements stock and returns None, raising KeyError for unknown title or ValueError when exhausted. available(title) returns stock, raising KeyError if unknown.', (({'a':1},),ObjectChecks([('borrow',('a',),None),('available',('a',),0),('borrow',('a',),ValueError)])), (({},),ObjectChecks([('borrow',('x',),KeyError)])), (({'a':2},),ObjectChecks([('available',('a',),2)]))),
    task('class Library(catalog)', 'Copy title->nonnegative counts. borrow(member,title) returns None, decrements stock, tracks loan, and rejects duplicate member/title or no stock with ValueError; unknown title raises KeyError. return_book(member,title) reverses a loan, or raises ValueError if absent. loans(member) returns sorted titles. available(title) returns stock.', (({'a':1},),ObjectChecks([('borrow',('m','a'),None),('loans',('m',),['a']),('available',('a',),0),('return_book',('m','a'),None),('available',('a',),1)])), (({'a':2},),ObjectChecks([('borrow',('m','a'),None),('borrow',('m','a'),ValueError),('available',('a',),1)])), (({},),ObjectChecks([('loans',('x',),[]),('return_book',('x','a'),ValueError),('borrow',('x','a'),KeyError)]))))
day('stacks', 'Stacks and balanced delimiters',
    'A stack is last-in, first-out. It records unfinished work such as opening brackets or operators. Define malformed input behavior before processing tokens.',
    'stack = []\nstack.append("first")\nstack.append("second")\nprint(stack.pop())\nprint(stack)',
    task('reverse_with_stack(items)', 'Return reversed items as a fresh list; practice append/pop.', (([1,2,3],),[3,2,1]), (([],),[]), ((['x'],),['x'])),
    task('balanced(text)', 'Return whether (), [], {} are properly nested; ignore all other characters.', (('a([]){}',),True), (('([)]',),False), (('',),True), (('(',),False)),
    task('evaluate_rpn(tokens)', 'Evaluate reverse Polish tokens with integer literals and operators + - *. Each operator consumes two values, left then right. Return one integer; malformed expression raises ValueError.', ((['2','3','+','4','*'],),20), ((['5','2','-'],),3), ((['1','2'],),ValueError), ((['+'],),ValueError)))
day('linked_structures', 'Linked structures',
    'A linked structure follows references rather than contiguous indices. Here a chain is encoded as node ID -> (value, next ID). None terminates it.',
    'nodes = {"a": (10, "b"), "b": (20, None)}\nvalue, next_id = nodes["a"]\nprint(value, nodes[next_id][0])',
    task('chain_values(nodes, head)', 'Follow an acyclic valid chain and return values in order. head None returns [].', (({'a':(1,'b'),'b':(2,None)},'a'),[1,2]), (({},None),[]), (({'x':(3,None)},'x'),[3])),
    task('has_cycle(nodes, head)', 'Return whether following next references revisits a node. All referenced IDs exist; head may be None.', (({'a':(1,'a')},'a'),True), (({'a':(1,None)},'a'),False), (({},None),False)),
    task('chain_intersection(nodes, first, second)', 'For two valid acyclic chains, return the first node ID along second also reachable from first, or None. Compare IDs, not values.', (({'a':(1,'c'),'b':(2,'c'),'c':(3,None)},'a','b'),'c'), (({'a':(1,None),'b':(1,None)},'a','b'),None), (({},None,None),None)))
day('trees', 'Binary trees',
    'Represent a tree as None or (value, left, right). Recursion mirrors this structure. Distinguish tree height in nodes from height in edges.',
    'tree = (4, (2, None, None), (7, None, None))\nvalue, left, right = tree\nprint(value, left[0], right[0])',
    task('tree_size(tree)', 'Return total node count; None has size 0.', ((None,),0), (((1,None,None),),1), (((2,(1,None,None),(3,None,None)),),3)),
    task('tree_height(tree)', 'Return longest root-to-leaf node count; None has height 0.', ((None,),0), (((1,None,None),),1), (((1,(2,(3,None,None),None),None),),3)),
    task('inorder(tree)', 'Return values in left-root-right traversal order.', (((2,(1,None,None),(3,None,None)),),[1,2,3]), ((None,),[]), (((1,None,(2,None,None)),),[1,2])))
day('binary_search_trees', 'Binary search trees',
    'A strict binary search tree has all left descendants smaller and all right descendants larger. Local child comparisons alone cannot prove this invariant.',
    'from bisect import insort\nordered = [2, 5, 9]\ninsort(ordered, 4)\nprint(ordered)',
    task('bst_contains(tree, target)', 'Search a valid strict BST represented as (value,left,right) or None; return bool.', (((2,(1,None,None),(3,None,None)),3),True), ((None,1),False), (((2,None,None),1),False)),
    task('bst_min(tree)', 'Return smallest value in a valid strict BST; None returns None.', (((3,(1,None,(2,None,None)),None),),1), ((None,),None), (((0,None,None),),0)),
    task('is_bst(tree)', 'Return whether the entire tree satisfies strict BST ordering. Duplicate values are invalid; None is valid.', (((2,(1,None,None),(3,None,None)),),True), (((5,(3,None,(6,None,None)),None),),False), (((1,(1,None,None),None),),False), ((None,),True)))
day('heaps', 'Heaps and priority queues',
    'heapq maintains a minimum at index zero. A heap is not fully sorted. Include explicit tie-breakers in priority entries when determinism matters.',
    'import heapq\nqueue = [5, 2, 8]\nheapq.heapify(queue)\nprint(heapq.heappop(queue))\nprint(queue)',
    task('smallest(numbers, k)', 'Return up to k smallest numbers sorted ascending, including duplicates; k >=0.', (([5,1,3,1],3),[1,1,3]), (([],2),[]), (([1],0),[])),
    task('schedule_jobs(jobs)', 'jobs is a list of (priority,name). Return names ordered priority ascending then name ascending, preserving duplicates.', (([(2,'b'),(1,'c'),(1,'a')],),['a','c','b']), (([],),[]), (([(0,'x'),(0,'x')],),['x','x'])),
    task('merge_sorted(lists)', 'Return one sorted list merging ascending-sorted input lists without mutating them. Aim for O(n log k).', (([[1,4],[2,3],[]],),[1,2,3,4]), (([],),[]), (([[1,1],[1]],),[1,1,1])))
day('graphs', 'Graphs and reachability',
    'An adjacency mapping represents a directed graph. Referenced vertices without keys have no outgoing edges. A visited set prevents infinite traversal through cycles.',
    'graph = {"a": ["b", "c"], "b": ["c"]}\nprint(graph.get("c", []))\nprint(graph["a"])',
    task('neighbors(graph, node)', 'Return a fresh list of outgoing neighbors in stored order, or [] if absent.', (({'a':['b','c']},'a'),['b','c']), (({},'a'),[]), (({'a':[]},'a'),[])),
    task('reachable(graph, start)', 'Return the set of vertices reachable by directed edges, including start even when absent from mapping.', (({'a':['b'],'b':['a','c']},'a'),{'a','b','c'}), (({},'x'),{'x'}), (({'a':[],'b':['a']},'a'),{'a'})),
    task('has_path(graph, start, goal)', 'Return whether goal is reachable from start. A zero-edge path to itself exists.', (({'a':['b']},'a','b'),True), (({},'x','x'),True), (({'a':['b']},'b','a'),False)))
day('breadth_first', 'Breadth-first search',
    'Breadth-first search uses a queue and finds shortest paths in unweighted graphs. Mark discovered vertices once and retain predecessors to reconstruct a path.',
    'from collections import deque\nfrontier = deque([("a", 0)])\nnode, distance = frontier.popleft()\nprint(node, distance)',
    task('bfs_order(graph, start)', 'Return discovery order using a FIFO queue and neighbor order from adjacency lists; include start and visit each vertex once.', (({'a':['b','c'],'b':['c']},'a'),['a','b','c']), (({},'x'),['x']), (({'a':['a']},'a'),['a'])),
    task('distances(graph, start)', 'Return reachable vertex -> minimum directed edge count from start.', (({'a':['b','c'],'b':['d'],'c':['d']},'a'),{'a':0,'b':1,'c':1,'d':2}), (({},'x'),{'x':0}), (({'a':['b'],'b':['a']},'a'),{'a':0,'b':1})),
    task('shortest_path(graph, start, goal)', 'Return a shortest path as vertex list, or None. Break ties by FIFO discovery and stored neighbor order. start==goal returns [start].', (({'a':['b','c'],'b':['d'],'c':['d']},'a','d'),['a','b','d']), (({},'x','x'),['x']), (({},'x','y'),None)))
day('depth_first', 'Depth-first search and dependencies',
    'Depth-first search explores one branch before returning. Track active vertices to detect directed cycles. A topological ordering respects every dependency edge.',
    'stack = ["a"]\nstack.extend(reversed(["b", "c"]))\nprint(stack.pop())\nprint(stack.pop())',
    task('dfs_order(graph, start)', 'Return recursive preorder DFS, following neighbors in stored order and visiting each vertex once.', (({'a':['b','c'],'b':['d']},'a'),['a','b','d','c']), (({},'x'),['x']), (({'a':['a']},'a'),['a'])),
    task('directed_cycle(graph)', 'Return whether any component contains a directed cycle. Include vertices mentioned only as neighbors.', (({'a':['b'],'b':['a']},),True), (({'a':['b']},),False), (({},),False)),
    task('topological_order(graph)', 'Return a topological ordering of all keys and neighbors. Among currently zero-indegree vertices always choose the lexicographically smallest string. Raise ValueError for cycles.', (({'a':['c'],'b':['c']},),['a','b','c']), (({},),[]), (({'a':['b'],'b':['a']},),ValueError)))
day('dynamic_programming', 'Dynamic programming',
    'Dynamic programming reuses overlapping subproblems. Choose a state, recurrence, and base cases before coding. Avoid measuring correctness by timing thresholds.',
    'ways = [1, 1]\nfor index in range(2, 6):\n    ways.append(ways[index - 1] + ways[index - 2])\nprint(ways)',
    task('fibonacci(n)', 'Return F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2); n >=0. Use iterative O(n) work.', ((0,),0), ((10,),55), ((30,),832040)),
    task('min_coins(coins, amount)', 'Return minimum coins needed for amount, or None if impossible. Unlimited positive integer coin denominations; amount >=0.', (([1,3,4],6),2), (([2],3),None), (([],0),0)),
    task('edit_distance(left, right)', 'Return Levenshtein distance with insert/delete/replace each costing 1.', (('kitten','sitting'),3), (('','abc'),3), (('same','same'),0)))
day('route_planner', 'Project: weighted route planner',
    'Weighted paths need accumulated costs rather than plain edge counts. Nonnegative weights permit Dijkstra; missing vertices have no outgoing edges.',
    'roads = {"a": [("b", 4), ("c", 2)]}\nprint(min(roads["a"], key=lambda edge: edge[1]))',
    task('path_cost(graph, path)', 'graph maps nodes to (neighbor,weight) lists with unique neighbors and nonnegative weights. Return sum along path; paths of length <=1 cost 0. Missing edge raises ValueError.', (({'a':[('b',4)]},['a','b']),4), (({},[]),0), (({},['a','b']),ValueError)),
    task('dijkstra_distances(graph, start)', 'Return minimum costs to all reachable nodes, including start at 0. Weights are nonnegative integers; use a heap.', (({'a':[('b',5),('c',1)],'c':[('b',1)]},'a'),{'a':0,'c':1,'b':2}), (({},'x'),{'x':0}), (({'a':[('b',0)],'b':[('a',0)]},'a'),{'a':0,'b':0})),
    task('cheapest_route(graph, start, goal)', 'Return {cost, path} or None if unreachable. For equal costs choose lexicographically smallest full path. Node names are strings; weights are strictly positive, except zero-edge start==goal.', (({'a':[('c',1),('b',1)],'b':[('d',1)],'c':[('d',1)]},'a','d'),{'cost':2,'path':['a','b','d']}), (({},'x','x'),{'cost':0,'path':['x']}), (({},'x','y'),None)))
day('boundary_tests', 'Choosing boundary tests',
    'Good tests separate partitions and inspect boundaries: empty, one, many, just below, at, and just above a threshold. Add at least one learner-authored test per exercise today.',
    'import unittest\nclass SampleTest(unittest.TestCase):\n    def test_empty(self):\n        self.assertEqual(len(""), 0)\n\nprint(SampleTest("test_empty").countTestCases())',
    task('password_length_ok(text)', 'Return whether length is between 8 and 64 inclusive. Only length matters.', (('1234567',),False), (('12345678',),True), (('x'*64,),True), (('x'*65,),False)),
    task('ticket_price(age)', 'Reject negative age. Return 0 for under 5, 8 for 5..17, 12 for 18..64, and 6 for >=65.', ((4,),0), ((5,),8), ((18,),12), ((65,),6), ((-1,),ValueError)),
    task('chunk_count(length, size)', 'Return number of chunks needed for nonnegative length and positive size. Reject invalid bounds with ValueError.', ((0,3),0), ((6,3),2), ((7,3),3), ((1,0),ValueError)))
day('invariants', 'Invariants and property-style tests',
    'Example tests check selected outcomes. Invariants describe relationships across many inputs. Use deterministic loops to explore properties without adding a dependency.',
    'for number in range(-5, 6):\n    assert abs(number) >= 0\n    assert abs(-number) == abs(number)\nprint("properties checked")',
    task('reverse_text(text)', 'Return the reversed text. Add a test proving reversing twice restores input.', (('abc',),'cba'), (('',),''), (('été',),'été')),
    task('deduplicate(items)', 'Return first occurrence of each hashable item in order. Add tests for idempotence and preserved membership.', (([2,1,2,3],),[2,1,3]), (([],),[]), (([0,0],),[0])),
    task('encode_runs(text)', 'Return consecutive (character,count) tuples. Add a test reconstructing text from the result.', (('aaabb',),[('a',3),('b',2)]), (('',),[]), (('aba',),[('a',1),('b',1),('a',1)])))
day('dependency_injection', 'Dependency injection',
    'Pass changing dependencies such as clocks and external functions explicitly. Tests can then control behavior without network access or wall-clock waits.',
    'def timestamped(message, clock):\n    return (clock(), message)\n\nprint(timestamped("ready", lambda: 100))',
    task('stamp(message, clock)', 'Return {time: clock(), message: message}; call zero-argument clock once.', (('hi','CALL:clock_100'),{'time':100,'message':'hi'}), (('','CALL:clock_0'),{'time':0,'message':''}), (('x','CALL:raise_value'),ValueError)),
    task('convert_prices(prices, converter)', 'Return converter(price) for each price in order. Propagate exceptions.', (([-1,2],'CALL:abs'),[1,2]), (([],'CALL:abs'),[]), (([1],'CALL:raise_value'),ValueError)),
    task('fetch_or_default(key, fetcher, default)', 'Call fetcher(key); return default only when it raises KeyError. Preserve falsy successful values; other errors propagate.', (('x','CALL:lookup_zero',9),0), (('missing','CALL:lookup_zero',9),9), (('x','CALL:raise_value',9),ValueError)))
day('test_doubles', 'Fakes, spies, and mocks',
    'A fake implements simplified behavior; a spy records calls. Assert interactions only when they are part of the contract. unittest.mock can control side effects.',
    'from unittest.mock import Mock\nservice = Mock(return_value="ok")\nprint(service("request"))\nservice.assert_called_once_with("request")',
    task('notify_all(names, notifier)', 'Call notifier(name) once for each name in order and return number called. Stop and propagate any exception.', ((['a','b'],'CALL:noop'),2), (([],'CALL:noop'),0), ((['a'],'CALL:raise_value'),ValueError)),
    task('class Spy(function)', 'Callable wrapper: record positional argument tuples in calls before forwarding to function, even if it raises. Expose calls list.', (('CALL:abs',),ObjectChecks([('__call__',(-2,),2),('@calls',(),[(-2,)])])), (('CALL:int',),ObjectChecks([('__call__',('bad',),ValueError),('@calls',(),[('bad',)])])), (('CALL:str',),ObjectChecks([('@calls',(),[])]))),
    task('fallback_call(primary, secondary, value)', 'Call primary(value); call secondary(value) only if primary raises LookupError. Other errors propagate.', (('CALL:abs','CALL:str',-2),2), (('CALL:always_missing','CALL:str',3),'3'), (('CALL:raise_value','CALL:str',3),ValueError)))
day('logging', 'Structured log processing',
    'Logging records events for diagnosis. Separate parsing from filtering and aggregation. Avoid testing timestamps or output that depends on the machine.',
    'import logging\nlogger = logging.getLogger("lesson")\nhandler = logging.StreamHandler()\nlogger.addHandler(handler)\nlogger.setLevel(logging.INFO)\nlogger.info("processed %s records", 3)',
    task('parse_log(line)', 'Parse LEVEL|message at first |. Allowed levels DEBUG INFO WARNING ERROR; return {level,message}. Reject malformed or unknown level with ValueError. Preserve message.', (('INFO|ready',),{'level':'INFO','message':'ready'}), (('ERROR|a|b',),{'level':'ERROR','message':'a|b'}), (('oops',),ValueError)),
    task('filter_logs(records, minimum)', 'Return records at or above minimum using DEBUG<INFO<WARNING<ERROR. Inputs have valid levels; invalid minimum raises ValueError.', (([{'level':'INFO'},{'level':'ERROR'}],'WARNING'),[{'level':'ERROR'}]), (([],'DEBUG'),[]), (([],'BAD'),ValueError)),
    task('error_summary(lines)', 'Parse lines with the preceding rules, ignore malformed lines, and return counts of ERROR messages only.', ((['ERROR|oops','INFO|ok','ERROR|oops','bad'],),{'oops':2}), (([],),{}), ((['WARNING|x'],),{})))
day('command_line', 'Command-line arguments',
    'argparse converts argument lists into structured options. Accept an explicit argv list so tests avoid process-global arguments. Use SystemExit for argparse validation failures.',
    'import argparse\nparser = argparse.ArgumentParser()\nparser.add_argument("--name", default="friend")\nprint(parser.parse_args(["--name", "Ada"]).name)',
    task('parse_name(argv)', 'Use argparse with optional --name defaulting to world. Return parsed name. Unknown options raise SystemExit.', (([],),'world'), ((['--name','Ada'],),'Ada'), ((['--unknown'],),SystemExit)),
    task('parse_count(argv)', 'Use argparse with optional --count integer defaulting to 1. Return count; invalid integer or missing option value raises SystemExit.', (([],),1), ((['--count','3'],),3), ((['--count','x'],),SystemExit)),
    task('parse_cli(argv)', 'Use argparse: positional action in {add,list}; optional --limit integer default 10; --verbose boolean flag. Return dict with action, limit, verbose. Invalid choice raises SystemExit.', ((['list'],),{'action':'list','limit':10,'verbose':False}), ((['add','--limit','2','--verbose'],),{'action':'add','limit':2,'verbose':True}), ((['delete'],),SystemExit)))
day('configuration', 'Modules and configuration boundaries',
    'Modules group related functions. Keep parsing and validation separate from use. Make precedence rules explicit so configuration changes are predictable.',
    'from math import ceil\nimport math\nprint(ceil(2.3))\nprint(math.isfinite(3.0))',
    task('merge_config(defaults, file_config, overrides)', 'Return a new dict; later layers override earlier ones even with None. Do not mutate inputs.', (({'x':1},{'x':2},{'y':3}),{'x':2,'y':3}), (({},{},{}),{}), (({'x':1},{},{'x':None}),{'x':None})),
    task('parse_bool(text)', 'Strip and lowercase. true/1/yes return True; false/0/no return False; everything else raises ValueError.', ((' YES ',),True), (('0',),False), (('maybe',),ValueError)),
    task('validate_config(config)', 'Return a new dict containing host and port only. host is a nonempty string; port is an int excluding bool in 1..65535. Missing or invalid values raise ValueError.', (({'host':'localhost','port':8080,'x':1},),{'host':'localhost','port':8080}), (({'host':'','port':1},),ValueError), (({'host':'x','port':True},),ValueError), (({},),ValueError)))
day('sqlite', 'SQLite and parameterized queries',
    'sqlite3 works locally without a server. Use placeholders for data values, never SQL string interpolation. Tests supply an in-memory connection and own its lifetime.',
    'import sqlite3\nwith sqlite3.connect(":memory:") as connection:\n    connection.execute("CREATE TABLE notes (text TEXT)")\n    connection.execute("INSERT INTO notes VALUES (?)", ("hello",))\n    print(connection.execute("SELECT text FROM notes").fetchall())',
    task('user_names(connection)', 'Table users(id INTEGER, name TEXT) exists. Return names ordered by id ascending. Do not close the supplied connection.', ((Database("CREATE TABLE users(id INTEGER,name TEXT); INSERT INTO users VALUES (2,'Bo'),(1,'Ada');"),),['Ada','Bo']), ((Database('CREATE TABLE users(id INTEGER,name TEXT);'),),[]), ((Database("CREATE TABLE users(id INTEGER,name TEXT); INSERT INTO users VALUES (1,'é');"),),['é'])),
    task('find_user(connection, name)', 'Query users(id INTEGER,name TEXT) using a parameter. Return smallest matching id or None.', ((Database("CREATE TABLE users(id INTEGER,name TEXT); INSERT INTO users VALUES (2,'Ada'),(1,'Ada');"),'Ada'),1), ((Database('CREATE TABLE users(id INTEGER,name TEXT);'),"' OR 1=1 --"),None), ((Database("CREATE TABLE users(id INTEGER,name TEXT); INSERT INTO users VALUES (1,'Bo');"),'Ada'),None)),
    task('score_totals(connection)', 'Table scores(name TEXT,points INTEGER) exists. Return (name,total) tuples grouped by name ordered total descending then name ascending.', ((Database("CREATE TABLE scores(name TEXT,points INTEGER); INSERT INTO scores VALUES ('a',2),('a',3),('b',5);"),),[('a',5),('b',5)]), ((Database('CREATE TABLE scores(name TEXT,points INTEGER);'),),[]), ((Database("CREATE TABLE scores(name TEXT,points INTEGER); INSERT INTO scores VALUES ('x',-1);"),),[('x',-1)])))
JOIN_SCHEMA = 'CREATE TABLE users(id INTEGER,name TEXT); CREATE TABLE tasks(id INTEGER,user_id INTEGER,done INTEGER);'
day('sql_relations', 'Relational joins and aggregates',
    'A join connects rows using keys. LEFT JOIN retains rows without matches. COUNT(column) ignores nulls, while COUNT(*) counts result rows.',
    'import sqlite3\nconnection = sqlite3.connect(":memory:")\ntry:\n    print(connection.execute("SELECT COUNT(*) FROM sqlite_master").fetchone()[0])\nfinally:\n    connection.close()',
    task('task_owners(connection)', 'Tables users(id,name), tasks(id,user_id,done). Return (task_id,user_name) for matching users only, ordered task_id.', ((Database(JOIN_SCHEMA+"INSERT INTO users VALUES (1,'Ada'); INSERT INTO tasks VALUES (2,1,0),(3,9,0);"),),[(2,'Ada')]), ((Database(JOIN_SCHEMA),),[]), ((Database(JOIN_SCHEMA+'INSERT INTO tasks VALUES (1,9,0);'),),[])),
    task('user_task_counts(connection)', 'Return (user_id,count) for ALL users including those with zero tasks, ordered user_id. Same schema as above.', ((Database(JOIN_SCHEMA+"INSERT INTO users VALUES (1,'A'),(2,'B'); INSERT INTO tasks VALUES (1,1,0),(2,1,1);"),),[(1,2),(2,0)]), ((Database(JOIN_SCHEMA),),[]), ((Database(JOIN_SCHEMA+"INSERT INTO users VALUES (3,'C');"),),[(3,0)])),
    task('completion_rates(connection)', 'Return (user_id, rate) for all users ordered user_id. rate is completed tasks / all tasks, or 0.0 for none. done is 0 or 1.', ((Database(JOIN_SCHEMA+"INSERT INTO users VALUES (1,'A'),(2,'B'); INSERT INTO tasks VALUES (1,1,0),(2,1,1);"),),[(1,0.5),(2,0.0)]), ((Database(JOIN_SCHEMA),),[]), ((Database(JOIN_SCHEMA+"INSERT INTO users VALUES (1,'A'); INSERT INTO tasks VALUES (1,1,1);"),),[(1,1.0)])))
day('task_tracker', 'Project: task tracker',
    'Combine IDs, validation, state, and serialization. Ensure each failed operation leaves existing state intact. Public results should not expose mutable internals.',
    'import json\ntask = {"id": 1, "title": "read", "done": False}\nprint(json.dumps(task, sort_keys=True))',
    task('class TaskTracker()', 'add(title) returns sequential ID starting at 1; nonempty string title required or ValueError. list_tasks() returns fresh records {id,title,done}, insertion order, initially done=False.', ((),ObjectChecks([('add',('read',),1),('list_tasks',(),[{'id':1,'title':'read','done':False}])])), ((),ObjectChecks([('add',('',),ValueError),('add',('x',),1)])), ((),ObjectChecks([('list_tasks',(),[])]))),
    task('complete_tasks(tasks, ids)', 'Return fresh records with done=True for supplied IDs; retain other fields. Unknown requested ID raises KeyError; do not mutate input.', (([{'id':1,'title':'x','done':False}], [1]),[{'id':1,'title':'x','done':True}]), (([],[]),[]), (([],[1]),KeyError)),
    task('task_report(tasks)', 'Return {total,completed,pending}; pending is sorted titles of tasks with done=False. Each record has title and boolean done.', (([{'title':'b','done':False},{'title':'a','done':True}],),{'total':2,'completed':1,'pending':['b']}), (([],),{'total':0,'completed':0,'pending':[]}), (([{'title':'z','done':False},{'title':'a','done':False}],),{'total':2,'completed':0,'pending':['a','z']})))
day('urls', 'URLs and query strings',
    'urllib.parse separates URL components and handles percent encoding. Network concepts can be practiced with strings offline. Query keys may have multiple values.',
    'from urllib.parse import urlsplit, urlencode\nprint(urlsplit("https://example.test/path?q=python").path)\nprint(urlencode({"q": "hello world"}))',
    task('url_host(url)', 'Return urlsplit(url).hostname, or None if absent.', (('https://EXAMPLE.test:443/a',),'example.test'), (('/relative',),None), (('http://localhost/',),'localhost')),
    task('query_values(url)', 'Return parse_qs of the URL query with keep_blank_values=True.', (('https://x.test/?a=1&a=2&b=',),{'a':['1','2'],'b':['']}), (('/path',),{}), (('/?q=hello+world',),{'q':['hello world']})),
    task('build_url(base, params)', 'Append urlencode(params, doseq=True) to base, which has no query or fragment. Empty params returns base. Preserve insertion order.', (('https://x.test/a',{'q':'a b','tag':['x','y']}),'https://x.test/a?q=a+b&tag=x&tag=y'), (('/a',{}),'/a'), (('/a',{'x':'&'}),'/a?x=%26')))
day('api_contracts', 'Validating API payloads',
    'An external payload needs validation before use. Keep error handling deterministic and avoid coercing surprising types. These exercises process local values only.',
    'payload = {"items": [{"id": 1}], "next": None}\nprint(isinstance(payload["items"], list))\nprint(payload["next"] is None)',
    task('valid_status(code)', 'Return whether code is an integer excluding bool in HTTP success range 200..299.', ((200,),True), ((299,),True), ((300,),False), ((True,),False)),
    task('validate_item(item)', 'Return a fresh {id,name} dict if item is a dict with positive integer id excluding bool and nonempty string name. Otherwise raise ValueError; ignore extra keys.', (({'id':1,'name':'a','x':2},),{'id':1,'name':'a'}), (({'id':True,'name':'a'},),ValueError), (({'id':1,'name':''},),ValueError)),
    task('decode_response(status, text)', 'Reject non-success status with ValueError. Decode JSON object containing items list, validate each item as above, and return normalized records. Malformed JSON or shape raises ValueError.', ((200,'{"items":[{"id":1,"name":"a"}]}'),[{'id':1,'name':'a'}]), ((204,'{"items":[]}'),[]), ((404,'{}'),ValueError), ((200,'{"items":{}}'),ValueError)))
day('pagination', 'Pagination and cursors',
    'Pagination bounds each response. Define offset semantics and cursor termination so loops cannot repeat indefinitely. Test empty and partial final pages.',
    'items = list(range(7))\nprint(items[0:3])\nprint(items[3:6])\nprint(items[6:9])',
    task('page(items, offset, limit)', 'Return a fresh slice; offset >=0 and limit >0 required or ValueError.', (([1,2,3],1,2),[2,3]), (([],0,3),[]), (([1],0,0),ValueError)),
    task('paginate(items, size)', 'Return {items,next_offset} pages from offset 0. next_offset is next start or None for final page. Empty input returns []; size <=0 raises ValueError.', (([1,2,3],2),[{'items':[1,2],'next_offset':2},{'items':[3],'next_offset':None}]), (([],1),[]), (([],0),ValueError)),
    task('collect_pages(pages, start)', 'pages maps cursor strings to {items,next} records. Follow next until None and concatenate items. Revisited cursor raises ValueError; missing cursor raises KeyError.', (({'a':{'items':[1],'next':'b'},'b':{'items':[2],'next':None}},'a'),[1,2]), (({'a':{'items':[],'next':'a'}},'a'),ValueError), (({},'x'),KeyError)))
day('retries', 'Retry policy without sleeping',
    'Retries need an explicit attempt limit and a narrow set of retryable failures. Inject sleep or compute delay schedules instead of waiting in tests.',
    'delays = [0.1 * 2 ** attempt for attempt in range(4)]\nprint(delays)',
    task('backoff(base, attempts)', 'Return base*2**i for i in range(attempts). Reject negative base or attempts with ValueError.', ((1,4),[1,2,4,8]), ((0.5,0),[]), ((-1,2),ValueError)),
    task('retryable(status)', 'Return True only for 408, 429, and 500..599 integer status codes.', ((429,),True), ((503,),True), ((404,),False)),
    task('first_success(outcomes, max_attempts)', 'Inspect up to max_attempts status codes. Return 1-based attempt of first 200..299, otherwise None. Stop immediately on a nonretryable failure using previous rules; max_attempts >0 or ValueError.', (([500,200],3),2), (([404,200],3),None), (([500,200],1),None), (([],0),ValueError)))
day('caching', 'Caches and expiration',
    'A cache stores reusable results. Expiry compares a supplied logical time rather than the system clock. Decide whether the exact expiry boundary counts as expired.',
    'entry = {"value": "ready", "expires": 10}\nnow = 10\nprint(now < entry["expires"])',
    task('fresh(entry, now)', 'entry has expires numeric. Return whether now < expires; equality is expired.', (({'expires':10},9),True), (({'expires':10},10),False), (({'expires':0},1),False)),
    task('cache_get(cache, key, now)', 'cache maps keys to {value,expires}. Return value if present and fresh, otherwise None. Do not remove entries.', (({'x':{'value':0,'expires':10}},'x',9),0), (({},'x',0),None), (({'x':{'value':3,'expires':10}},'x',10),None)),
    task('class LRUCache(capacity)', 'capacity >0 or ValueError. get(key) returns value or None and marks hits most recent. put(key,value) returns None, updates recency, and evicts least recent if over capacity. keys() returns least-to-most-recent keys.', ((2,),ObjectChecks([('put',('a',1),None),('put',('b',2),None),('get',('a',),1),('put',('c',3),None),('keys',(),['a','c']),('get',('b',),None)])), ((1,),ObjectChecks([('put',('a',1),None),('put',('a',2),None),('get',('a',),2)])), ((0,),ValueError)))
day('hashes', 'Hashes and content identity',
    'Cryptographic hashes produce stable content fingerprints. Python hash() is unsuitable for persistent identifiers. Hashing is not encryption or a password storage recipe.',
    'import hashlib\nprint(hashlib.sha256(b"example").hexdigest())\nprint(hashlib.sha256(b"example").digest_size)',
    task('sha256_text(text)', 'Return SHA-256 hex digest of UTF-8 text.', (('',),'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'), (('abc',),'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'), (('hello',),'2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')),
    task('same_content(left, right)', 'Return whether two byte strings have identical content. Compare SHA-256 digests for this exercise.', ((b'a',b'a'),True), ((b'a',b'b'),False), ((b'',b''),True)),
    task('duplicate_files(files)', 'files maps filenames to byte contents. Return groups of identical content with at least two filenames; sort names inside groups and groups lexicographically.', (({'b':b'x','a':b'x','c':b'y'},),[['a','b']]), (({},),[]), (({'c':b'','a':b'','d':b'z','b':b'z'},),[['a','c'],['b','d']])))
day('randomness', 'Deterministic random simulations',
    'A local random.Random instance isolates pseudo-random state. Seeding makes a simulation reproducible. Tests should avoid global state and statistical flakiness.',
    'import random\nrng = random.Random(7)\nprint([rng.randint(1, 6) for _ in range(3)])',
    task('roll_dice(seed, count)', 'Use local random.Random(seed); return count randint(1,6) draws. count >=0.', ((7,3),[3,2,4]), ((1,0),[]), ((1,3),[2,5,1])),
    task('shuffled(items, seed)', 'Copy items and shuffle once with local random.Random(seed); return the copy without changing input.', (([1,2,3,4],0),[3,1,2,4]), (([],7),[]), ((['x'],1),['x'])),
    task('dice_histogram(seed, count)', 'Draw count dice using the same rules above and return counts for ALL faces 1..6, including zeros.', ((7,3),{1:0,2:1,3:1,4:1,5:0,6:0}), ((0,0),{1:0,2:0,3:0,4:0,5:0,6:0}), ((1,3),{1:1,2:1,3:0,4:0,5:1,6:0})))
day('futures', 'Concurrency with futures',
    'ThreadPoolExecutor is useful for independent I/O work. Submission order and completion order differ. Use context managers and let worker exceptions reach the caller.',
    'from concurrent.futures import ThreadPoolExecutor\nwith ThreadPoolExecutor(max_workers=2) as pool:\n    print(list(pool.map(abs, [-2, -4, 3])))',
    task('parallel_map(function, items)', 'Use ThreadPoolExecutor to apply function to items. Return results in input order; propagate worker exceptions.', (('CALL:abs',[-2,3]),[2,3]), (('CALL:str',[]),[]), (('CALL:int',['bad']),ValueError)),
    task('parallel_lengths(texts)', 'Use threads to compute each text length and return (text,length) pairs in input order.', ((['abc','x'],),[('abc',3),('x',1)]), (([],),[]), ((['','é'],),[('',0),('é',1)])),
    task('parallel_batches(function, batches)', 'Use one thread task per batch, applying function to each item. Return nested result lists in batch order, including empty batches. Propagate errors.', (('CALL:abs',[[-1,2],[],[-3]]),[[1,2],[],[3]]), (('CALL:str',[]),[]), (('CALL:int',[['bad']]),ValueError)))
day('asyncio', 'Async functions and gather',
    'async def produces a coroutine. await cooperatively suspends it. asyncio.gather preserves argument order in its results. Do not start event loops inside these functions.',
    'import asyncio\nasync def echo(value):\n    await asyncio.sleep(0)\n    return value\n\nasync def main():\n    print(await asyncio.gather(echo("a"), echo("b")))\n\nasyncio.run(main())',
    task('async async_double(value)', 'Coroutine returning value*2 after await asyncio.sleep(0).', ((3,),6), ((0,),0), ((-2,),-4), mode='async'),
    task('async gather_values(values)', 'Use gather to run a coroutine for each value and return the original values in order. Each coroutine awaits sleep(0).', (([3,1,2],),[3,1,2]), (([],),[]), (([None,False],),[None,False]), mode='async'),
    task('async async_apply(function, values)', 'Create one coroutine per value; each awaits sleep(0), then calls synchronous function(value). Gather results in order and propagate errors.', (('CALL:abs',[-2,3]),[2,3]), (('CALL:str',[]),[]), (('CALL:int',['bad']),ValueError), mode='async'))
day('offline_client', 'Project: offline API client',
    'Build a client pipeline from local response fixtures: pagination, validation, and normalization. No network is needed to verify API behavior.',
    'response = {"status": 200, "body": {"items": [1, 2], "next": None}}\nprint(response["status"], response["body"]["items"])',
    task('unwrap_response(response)', 'Require status integer excluding bool in 200..299 and body dict with items list and next string or None. Return body; invalid shape raises ValueError.', (({'status':200,'body':{'items':[1],'next':None}},),{'items':[1],'next':None}), (({'status':500,'body':{}},),ValueError), (({'status':200,'body':{'items':[],'next':2}},),ValueError)),
    task('fetch_all(responses, start)', 'responses maps cursors to valid response records under preceding contract. Follow body.next, concatenate body.items. Invalid response or repeated cursor raises ValueError; missing cursor raises KeyError.', (({'a':{'status':200,'body':{'items':[1],'next':'b'}},'b':{'status':200,'body':{'items':[2],'next':None}}},'a'),[1,2]), (({},'a'),KeyError), (({'a':{'status':200,'body':{'items':[],'next':'a'}}},'a'),ValueError)),
    task('sync_items(responses, start)', 'Fetch all pages under preceding rules; validate items with positive int id excluding bool and nonempty string name. Later duplicates by id replace earlier; return normalized {id,name} records sorted by id. Invalid items raise ValueError.', (({'a':{'status':200,'body':{'items':[{'id':2,'name':'old'},{'id':1,'name':'a'},{'id':2,'name':'new'}],'next':None}}},'a'),[{'id':1,'name':'a'},{'id':2,'name':'new'}]), (({'a':{'status':200,'body':{'items':[],'next':None}}},'a'),[]), (({'a':{'status':200,'body':{'items':[{'id':0,'name':'x'}],'next':None}}},'a'),ValueError)))
day('unicode', 'Unicode and normalization',
    'Text and bytes are different. Unicode can encode visually equivalent text in different sequences. Normalize when matching; casefold handles more cases than lower.',
    'import unicodedata\nprint("Straße".casefold())\nprint(unicodedata.normalize("NFC", "e\\u0301"))',
    task('utf8_length(text)', 'Return number of bytes in UTF-8 encoding, not number of characters.', (('abc',),3), (('é',),2), (('',),0)),
    task('normalized_equal(left, right)', 'Return equality after NFC normalization and casefolding each string.', (('é','e\u0301'),True), (('Straße','STRASSE'),True), (('a','b'),False)),
    task('unique_normalized(words)', 'Normalize each word using NFC then casefold; return unique normalized strings in first occurrence order.', ((['É','e\u0301','Straße','STRASSE'],),['é','strasse']), (([],),[]), ((['A','a','B'],),['a','b'])))
day('binary', 'Binary data and bit operations',
    'Bytes store integers 0..255. Bit masks isolate flags. Specify byte order when converting integers to byte sequences.',
    'value = 0b1010\nprint(value & 0b0010)\nprint((258).to_bytes(2, "big"))\nprint(int.from_bytes(b"\\x01\\x02", "big"))',
    task('has_flag(value, flag)', 'Return whether all bits in nonnegative flag are present in nonnegative value. Zero flag is always present.', ((10,2),True), ((10,3),False), ((0,0),True)),
    task('pack_u16(value)', 'Return exactly two big-endian bytes for integer 0..65535; otherwise raise ValueError.', ((258,),b'\x01\x02'), ((65535,),b'\xff\xff'), ((-1,),ValueError), ((65536,),ValueError)),
    task('xor_bytes(data, key)', 'Return bytes with each byte XORed with integer key in 0..255. Invalid key raises ValueError. Applying twice restores input.', ((b'ABC',1),b'@CB'), ((b'',0),b''), ((b'x',256),ValueError)))
day('matrices', 'Matrices and shape validation',
    'A rectangular matrix has equal row lengths. Validate shapes before combining data. Today empty matrix [] is allowed, but nonempty matrices have at least one column.',
    'matrix = [[1, 2], [3, 4]]\nprint([row[0] for row in matrix])\nprint([sum(row) for row in matrix])',
    task('matrix_shape(matrix)', 'Return (rows,columns). [] gives (0,0). Ragged rows or nonempty matrices with zero columns raise ValueError.', (([[1,2],[3,4]],),(2,2)), (([],),(0,0)), (([[1],[2,3]],),ValueError), (([[]],),ValueError)),
    task('transpose(matrix)', 'Return a new transposed matrix, validating with preceding rules. [] gives [].', (([[1,2,3],[4,5,6]],),[[1,4],[2,5],[3,6]]), (([],),[]), (([[1],[2,3]],),ValueError)),
    task('matrix_multiply(left, right)', 'Return matrix product after shape validation. Inner dimensions must match or ValueError. Both empty returns []; exactly one empty raises ValueError.', (([[1,2]],[[3],[4]]),[[11]]), (([],[]),[]), (([[1,2]],[[1,2]]),ValueError), (([[1]],[]),ValueError)))
day('statistics', 'Descriptive statistics',
    'Mean, median, and variance describe different aspects of data. Specify whether variance is population or sample. Empty data needs an explicit policy.',
    'import statistics\nvalues = [2, 3, 9]\nprint(statistics.mean(values))\nprint(statistics.median(values))\nprint(statistics.pvariance(values))',
    task('mean(numbers)', 'Return arithmetic mean; empty raises ValueError.', (([1,2,3],),2.0), (([0],),0.0), (([],),ValueError)),
    task('median(numbers)', 'Return middle sorted value, or mean of two middle values. Empty raises ValueError; do not mutate input.', (([3,1,2],),2), (([4,1,2,3],),2.5), (([],),ValueError)),
    task('population_variance(numbers)', 'Return mean squared deviation from mean, dividing by n. Empty raises ValueError.', (([1,2,3],),2/3), (([4],),0.0), (([],),ValueError)))
day('windows', 'Sliding windows',
    'A fixed-size window updates as one item enters and another leaves. Reuse partial results rather than recomputing every slice. Handle windows larger than the input.',
    'from collections import deque\nwindow = deque(maxlen=3)\nfor item in [1, 2, 3, 4]:\n    window.append(item)\n    print(list(window))',
    task('window_sums(numbers, size)', 'Return sums of every full consecutive size window. size >0 or ValueError; no full windows returns []. Aim for O(n).', (([1,2,3,4],2),[3,5,7]), (([1],2),[]), (([],0),ValueError)),
    task('moving_average(numbers, size)', 'Return averages of full consecutive windows. Same size validation as above.', (([2,4,6],2),[3.0,5.0]), (([],1),[]), (([1],0),ValueError)),
    task('window_maxima(numbers, size)', 'Return maximum of each full consecutive window; size >0 or ValueError. Aim for O(n) with a monotonic deque.', (([1,3,-1,-3,5,3,6,7],3),[3,3,5,5,6,7]), (([2,2],1),[2,2]), (([],0),ValueError)))
day('intervals', 'Intervals and sweep lines',
    'Represent intervals as half-open [start,end). Touching intervals do not overlap, but merging may deliberately combine them. State that policy in the contract.',
    'interval = (2, 5)\nprint(interval[0] <= 4 < interval[1])\nprint(interval[0] <= 5 < interval[1])',
    task('overlap(left, right)', 'Return whether valid nonempty half-open intervals overlap with positive length.', (((1,3),(2,4)),True), (((1,2),(2,3)),False), (((0,1),(3,4)),False)),
    task('merge_intervals(intervals)', 'Return sorted merged (start,end) tuples, combining overlapping OR touching intervals. Each interval has start<end. Do not mutate input.', (([(3,5),(1,3),(8,9)],),[(1,5),(8,9)]), (([],),[]), (([(1,4),(2,3)],),[(1,4)])),
    task('max_concurrent(intervals)', 'Return maximum number of simultaneously active half-open intervals. Process endings before starts at equal times; all start<end.', (([(1,3),(2,4),(3,5)],),2), (([],),0), (([(1,2),(2,3)],),1)))
day('backtracking', 'Backtracking search',
    'Backtracking builds candidates and abandons invalid prefixes. Restore state after exploring a branch. Ordering rules make otherwise equivalent outputs testable.',
    'from itertools import product\nfor candidate in product([0, 1], repeat=2):\n    print(candidate)',
    task('subsets(items)', 'Return subsets by ascending bitmask, with bit i selecting items[i]; each subset is a list in original order. Input items are distinct.', ((['a','b'],),[[],['a'],['b'],['a','b']]), (([],),[[]]), (([1],),[[],[1]])),
    task('balanced_parentheses(n)', 'Return all balanced strings with n pairs sorted lexicographically. n >=0; n=0 returns [""]. Use backtracking.', ((2,),['(())','()()']), ((0,),['']), ((3,),['((()))','(()())','(())()','()(())','()()()'])),
    task('n_queens_count(n)', 'Count placements of n nonattacking queens on n*n board; n >=0, empty board has one placement. Use backtracking.', ((0,),1), ((4,),2), ((5,),10)))
day('expression_parser', 'A tiny expression language',
    'A parser should accept only its defined grammar. Avoid eval for user-supplied expressions. Today the grammar uses nonnegative integers, +, *, parentheses, and whitespace.',
    'import re\nprint(re.findall(r"[0-9]+|[+*()]", "12 + (3 * 4)"))',
    task('tokenize(expression)', 'Return integer tokens and single-character + * ( ) tokens; ignore whitespace. Reject every other character with ValueError. Empty returns [].', (('12 + (3*4)',),[12,'+','(',3,'*',4,')']), (('',),[]), (('1-2',),ValueError)),
    task('evaluate_flat(expression)', 'Evaluate nonempty integer (+ integer)* with whitespace allowed. No *, parentheses, signs, or adjacent integers. Invalid syntax raises ValueError. Do not use eval.', (('1 + 2 + 30',),33), (('0',),0), (('1+',),ValueError), (('1 2',),ValueError)),
    task('evaluate(expression)', 'Evaluate the full grammar: * precedes +, parentheses override precedence. Reject empty/malformed expressions with ValueError. Do not use eval.', (('2+3*4',),14), (('(2+3)*4',),20), (('2**3',),ValueError), (('',),ValueError)))
day('events', 'Event sourcing',
    'Events record facts in order; reducers derive current state. Replaying the same event stream should produce the same state. Reject invalid events explicitly.',
    'events = [{"kind": "add", "amount": 3}, {"kind": "add", "amount": 2}]\nprint([event["amount"] for event in events])',
    task('balance_events(events)', 'Events are (kind,amount), kind deposit or withdraw, amount nonnegative. Starting at 0, return balance. Unknown kind, negative amount, or overdraft raises ValueError.', (([('deposit',5),('withdraw',2)],),3), (([],),0), (([('withdraw',1)],),ValueError)),
    task('replay_counter(events)', 'Start at 0. Events are (kind,value): set assigns value, add adds value. Return history including initial 0; unknown kind raises ValueError.', (([('add',2),('set',7),('add',-1)],),[0,2,7,6]), (([],),[0]), (([('oops',1)],),ValueError)),
    task('deduplicate_events(events)', 'Records contain id (hashable) and arbitrary other fields. Return first record for each id in original order; do not mutate records.', (([{'id':1,'v':'a'},{'id':1,'v':'b'},{'id':2,'v':'c'}],),[{'id':1,'v':'a'},{'id':2,'v':'c'}]), (([],),[]), (([{'id':0}],),[{'id':0}])))
day('inventory', 'Project: inventory events',
    'Derive inventory from events while preventing negative stock. Use integer quantities and explicit ordering. Add your own tests for failed events and repeated IDs.',
    'event = {"sku": "TEA", "delta": 3}\nprint(event["sku"], event["delta"])',
    task('apply_stock(stock, sku, delta)', 'Return a new stock dict applying integer delta to sku (absent starts 0). Negative resulting stock raises ValueError; retain zero entries.', (({'a':2},'a',-1),{'a':1}), (({},'x',0),{'x':0}), (({},'x',-1),ValueError)),
    task('replay_stock(events)', 'Events have sku and integer delta. Starting empty apply each event with the previous rules; return final stock or raise ValueError for negative intermediate stock.', (([{'sku':'a','delta':3},{'sku':'a','delta':-2}],),{'a':1}), (([],),{}), (([{'sku':'a','delta':-1},{'sku':'a','delta':2}],),ValueError)),
    task('inventory_report(events, thresholds)', 'Replay stock as above. Return {stock,low_stock}; low_stock is sorted SKUs in thresholds whose final stock (default 0) is strictly below threshold. Negative intermediate stock raises ValueError.', (([{'sku':'a','delta':2}],{'a':3,'b':1}),{'stock':{'a':2},'low_stock':['a','b']}), (([],{}),{'stock':{},'low_stock':[]}), (([{'sku':'x','delta':-1}],{}),ValueError)))
day('schema_migrations', 'Versioned data and migrations',
    'Persisted data outlives code versions. Migration converts old shapes into a documented current shape without mutating the source. Reject unknown versions.',
    'legacy = {"name": "Ada Lovelace"}\nupdated = {"display_name": legacy["name"], "version": 2}\nprint(updated)',
    task('migrate_user(record)', 'v1 record {version:1,name:nonempty string} becomes {version:2,display_name:name}. v2 requires nonempty display_name and is normalized to those two keys. Invalid or unknown version raises ValueError; bool version invalid.', (({'version':1,'name':'Ada'},),{'version':2,'display_name':'Ada'}), (({'version':2,'display_name':'Bo','extra':1},),{'version':2,'display_name':'Bo'}), (({'version':3},),ValueError), (({'version':True,'name':'A'},),ValueError)),
    task('migrate_users(records)', 'Migrate each record under previous rules, preserving order; any invalid record raises ValueError. Return fresh records.', (([{'version':1,'name':'A'}],),[{'version':2,'display_name':'A'}]), (([],),[]), (([{'version':1,'name':''}],),ValueError)),
    task('migration_report(records)', 'Try each migration independently. Return {users,errors}; users contains successful normalized records in order, errors contains zero-based indices of invalid records.', (([{'version':1,'name':'A'},{'version':9},{'version':2,'display_name':'B'}],),{'users':[{'version':2,'display_name':'A'},{'version':2,'display_name':'B'}],'errors':[1]}), (([],),{'users':[],'errors':[]}), (([{}],),{'users':[],'errors':[0]})))
day('streaming_pipeline', 'Streaming data pipelines',
    'Streaming separates source, transformation, and sink. Process records as they arrive and bound memory where possible. Return iterators for the first two stages today.',
    'def nonblank(lines):\n    for line in lines:\n        if line.strip():\n            yield line.strip()\n\nprint(list(nonblank(iter([" a ", "", " b "]))))',
    task('parse_numbers(lines)', 'Yield int(stripped_line) for nonblank lines; malformed integers raise ValueError during iteration.', (([' 1 ','','-2'],),[1,-2]), (([],),[]), ((['bad'],),ValueError), mode='iterator'),
    task('positive_batches(numbers, size)', 'Filter values >0 and yield lists of size, including final partial batch. size <=0 raises ValueError during iteration.', (([-1,1,2,0,3],2),[[1,2],[3]]), (([],2),[]), (([],0),ValueError), mode='iterator'),
    task('stream_summary(lines)', 'Ignore blank lines, parse other lines as integers, and return {count,sum,min,max}. No numbers gives count/sum 0 and min/max None; malformed integer raises ValueError. Use one pass.', ((['1','-2','3'],),{'count':3,'sum':2,'min':-2,'max':3}), (([' '],),{'count':0,'sum':0,'min':None,'max':None}), ((['bad'],),ValueError)))
day('sorting_algorithms', 'Implementing sorting algorithms',
    'Implement algorithms to understand their tradeoffs, even though production Python offers sorted. Output tests establish correctness; a written explanation establishes the complexity claim.',
    'left, right = [1, 4], [2, 3]\nprint(left[0] <= right[0])\nprint(len(left) + len(right))',
    task('insertion_sort(items)', 'Implement insertion sort, returning a fresh ascending list. Do not use sorted or list.sort.', (([3,1,2],),[1,2,3]), (([],),[]), (([2,2,-1],),[-1,2,2])),
    task('merge_sort(items)', 'Implement stable merge sort, returning a fresh ascending list. Do not use sorted or list.sort.', (([4,1,3,2],),[1,2,3,4]), (([],),[]), (([3,3,1],),[1,3,3])),
    task('count_inversions(items)', 'Return number of i<j pairs with items[i]>items[j]. Aim for O(n log n) using a merge process; do not mutate input.', (([3,1,2],),2), (([],),0), (([2,2,1],),2), (([4,3,2,1],),6)))
day('transactions', 'Atomic updates',
    'Atomicity means all intended updates succeed together or none take effect. Validate a complete operation before exposing state. These pure functions return committed copies.',
    'balances = {"a": 5, "b": 2}\nproposed = balances.copy()\nproposed["a"] -= 1\nproposed["b"] += 1\nprint(balances, proposed)',
    task('transfer(balances, source, target, amount)', 'Return fresh balances after transfer. Missing account raises KeyError; negative amount or insufficient source raises ValueError. Same source/target is a no-op after validation. Do not mutate input.', (({'a':5,'b':1},'a','b',3),{'a':2,'b':4}), (({'a':5},'a','a',2),{'a':5}), (({'a':1,'b':0},'a','b',2),ValueError)),
    task('batch_transfers(balances, transfers)', 'transfers is (source,target,amount) list. Apply previous rules sequentially to a copy; any error propagates without changing input. Return final balances.', (({'a':5,'b':0},[('a','b',3),('b','a',1)]),{'a':3,'b':2}), (({},[]),{}), (({'a':5,'b':0},[('a','b',3),('a','b',3)]),ValueError)),
    task('reserve_order(stock, order)', 'Return fresh stock subtracting order sku->quantity. Validate all quantities as nonnegative int excluding bool; bad quantity/insufficient stock raises ValueError, unknown SKU raises KeyError. Input unchanged on failure.', (({'a':3,'b':2},{'a':2,'b':1}),{'a':1,'b':1}), (({},{}),{}), (({'a':1},{'a':2}),ValueError), (({}, {'x':1}),KeyError)))
day('thread_safety', 'Shared state and locks',
    'A lock protects a multi-step invariant across threads. Avoid relying on interpreter details for correctness. Tests use bounded work and no timing-based assertions.',
    'from threading import Lock\nlock = Lock()\nwith lock:\n    value = 1\nprint(value)',
    task('class SafeCounter(start=0)', 'Thread-safe increment(amount=1) adds amount and returns new value. Expose value property protected by the same lock. Each instance owns its lock and value.', ((0,),ObjectChecks([('increment',(),1),('increment',(3,),4),('@value',(),4)])), ((5,),ObjectChecks([('increment',(-2,),3)])), ((),ObjectChecks([('@value',(),0)]))),
    task('count_in_threads(workers, increments)', 'Use SafeCounter and ThreadPoolExecutor. Each worker performs increments increments of 1. Return final value; nonnegative workers/increments required or ValueError; zero workers returns 0.', ((4,1000),4000), ((0,10),0), ((-1,2),ValueError)),
    task('class LockedInventory(stock)', 'Copy nonnegative stock. buy(sku,quantity) atomically subtracts and returns remaining stock; nonpositive quantity or insufficient stock raises ValueError; unknown SKU raises KeyError. snapshot() returns an independent dict. Protect operations with a lock.', (({'a':3},),ObjectChecks([('buy',('a',2),1),('buy',('a',2),ValueError),('snapshot',(),{'a':1})])), (({},),ObjectChecks([('buy',('x',1),KeyError)])), (({'a':1},),ObjectChecks([('buy',('a',0),ValueError),('snapshot',(),{'a':1})]))))
day('codecs', 'Encoding and decoding protocols',
    'An encoding needs a reversible format and validation rules. Base64 represents bytes as ASCII. Length prefixes allow payloads containing delimiter-like data.',
    'import base64\nencoded = base64.b64encode(b"hello")\nprint(encoded)\nprint(base64.b64decode(encoded, validate=True))',
    task('to_base64(data)', 'Return standard base64 encoding of bytes as an ASCII string.', ((b'hello',),'aGVsbG8='), ((b'',),''), ((b'\x00\xff',),'AP8=')),
    task('from_base64(text)', 'Decode ASCII base64 with validate=True, returning bytes. Convert invalid encoding errors into ValueError.', (('aGVsbG8=',),b'hello'), (('',),b''), (('@@@',),ValueError)),
    task('decode_frames(data)', 'Parse concatenated frames: two-byte big-endian unsigned byte length followed by that many payload bytes. Return list of byte payloads. Truncated prefix or payload raises ValueError.', ((b'\x00\x02hi\x00\x00',),[b'hi',b'']), ((b'',),[]), ((b'\x00\x03hi',),ValueError), ((b'\x00',),ValueError)))
day('rate_limits', 'Rate limiting with logical time',
    'Rate limits operate on time windows. Inject timestamps so tests are instant and deterministic. State exactly which side of a window boundary is included.',
    'times = [1, 3, 5]\nnow, window = 5, 3\nprint([t for t in times if now - window < t <= now])',
    task('requests_in_window(times, now, window)', 'Count timestamps satisfying now-window < t <= now. window >0 or ValueError; times need not be sorted.', (([1,3,5,6],5,3),2), (([],10,1),0), (([],0,0),ValueError)),
    task('fixed_window_decisions(times, limit, window)', 'times are nondecreasing nonnegative integers. Bucket by t//window, allow first limit in each bucket. Return booleans. limit >=0, window >0 or ValueError.', (([0,1,2,5,6],2,5),[True,True,False,True,True]), (([0],0,1),[False]), (([],1,0),ValueError)),
    task('sliding_window_decisions(times, limit, window)', 'For sorted nonnegative timestamps, allow request only if fewer than limit previously ACCEPTED timestamps lie in (t-window,t]. Rejected requests consume no capacity. Return booleans; limit >=0, window >0 or ValueError.', (([0,1,2,5,6],2,5),[True,True,False,True,True]), (([0,0,0],1,5),[True,False,False]), (([],1,0),ValueError)))
day('build_dependencies', 'Dependency planning',
    'Build systems map each task to prerequisites. A plan must include transitive dependencies and detect cycles. Avoid confusing prerequisite edges with execution-order edges.',
    'dependencies = {"package": ["test"], "test": ["compile"], "compile": []}\nprint(dependencies["package"])',
    task('dependency_closure(dependencies, target)', 'Return set of all transitive prerequisites, excluding target. Referenced missing keys have no prerequisites. Raise ValueError for a cycle reachable from target.', (({'a':['b'],'b':['c']},'a'),{'b','c'}), (({},'x'),set()), (({'a':['a']},'a'),ValueError)),
    task('build_plan(dependencies, target)', 'Return prerequisites plus target in valid execution order. Among available nodes choose lexicographically smallest string. Only include target closure; reachable cycle raises ValueError.', (({'app':['test','compile'],'test':['compile'],'compile':[]},'app'),['compile','test','app']), (({},'x'),['x']), (({'a':['b'],'b':['a']},'a'),ValueError)),
    task('affected_targets(dependencies, changed)', 'Return sorted keys OR referenced nodes that are changed or transitively depend on a changed node. Include changed nodes even if absent. Handle cycles without looping.', (({'app':['lib'],'test':['lib'],'lib':['base']},['base']),['app','base','lib','test']), (({},['x']),['x']), (({'a':['b'],'b':['a']},['a']),['a','b'])))
day('analytics_capstone', 'Capstone: transaction analytics',
    'Build an end-to-end normalization and reporting pipeline. Keep records immutable, document rejection policy, and add tests that combine duplicate IDs, invalid records, and ties.',
    'row = {"id": "t1", "category": "food", "cents": 125}\nprint(tuple(row[key] for key in ("id", "category", "cents")))',
    task('normalize_transaction(record)', 'Require dict with nonempty string id/category, integer cents excluding bool (negative refunds allowed). Return only those three keys; invalid record raises ValueError.', (({'id':'a','category':'food','cents':-2,'x':1},),{'id':'a','category':'food','cents':-2}), (({'id':'','category':'x','cents':0},),ValueError), (({'id':'a','category':'x','cents':True},),ValueError)),
    task('clean_transactions(records)', 'Validate each record independently, skip invalid records, keep first valid record per id, return normalized records in encounter order.', (([{'id':'a','category':'x','cents':1},{},{'id':'a','category':'y','cents':2}],),[{'id':'a','category':'x','cents':1}]), (([],),[]), (([{'id':'a','category':'','cents':1},{'id':'a','category':'x','cents':2}],),[{'id':'a','category':'x','cents':2}])),
    task('analytics_report(records)', 'Clean as above. Return {count,total,by_category}; by_category is list of (category,net_cents) sorted net descending then name ascending. Retain zero totals.', (([{'id':'a','category':'x','cents':3},{'id':'b','category':'x','cents':-3},{'id':'c','category':'y','cents':2}],),{'count':3,'total':2,'by_category':[('y',2),('x',0)]}), (([],),{'count':0,'total':0,'by_category':[]}), (([{}],),{'count':0,'total':0,'by_category':[]})))
day('workflow_capstone', 'Capstone: workflow engine',
    'Combine dependencies, deterministic planning, and failure propagation. Finish with a design review explaining state transitions, complexity, and what your tests cannot prove.',
    'states = {"extract": "success", "transform": "pending"}\nprint(all(states.get(name) == "success" for name in ["extract"]))',
    task('ready_tasks(dependencies, completed)', 'dependencies maps task names to prerequisite name lists; all prerequisites are keys. Return sorted uncompleted tasks whose prerequisites are ALL completed. Do not mutate inputs.', (({'a':[],'b':['a'],'c':[]},['a']),['b','c']), (({},[]),[]), (({'a':['b'],'b':['a']},[]),[])),
    task('workflow_layers(dependencies)', 'Return execution layers: each contains ALL currently ready tasks sorted, then mark whole layer complete. All prerequisites must be keys or KeyError. Cycles raise ValueError.', (({'a':[],'b':['a'],'c':[]},),[['a','c'],['b']]), (({},),[]), (({'a':['a']},),ValueError), (({'a':['missing']},),KeyError)),
    task('run_workflow(dependencies, outcomes)', 'Validate full graph as above before running. outcomes maps every task to boolean success (missing raises KeyError). Process valid layers. State success/failed by outcome when all prerequisites succeeded; otherwise blocked. Return task->state dict. Empty graph returns {}.', (({'a':[],'b':['a'],'c':[]},{'a':False,'b':True,'c':True}),{'a':'failed','b':'blocked','c':'success'}), (({},{}),{}), (({'a':[]},{}),KeyError), (({'a':['a']},{'a':True}),ValueError)))

PHASES = [
    'Foundations', 'Working with collections', 'Text, files, and data formats',
    'Iteration and problem solving', 'Objects and domain models',
    'Data structures and algorithms', 'Testing and local applications',
    'Offline APIs and concurrency', 'Advanced data processing', 'Integration and capstones',
]

def literal(value):
    if isinstance(value, type) and issubclass(value, BaseException):
        return value.__name__
    if isinstance(value, File):
        return f'File({value.content!r})'
    if isinstance(value, Database):
        return f'Database({value.script!r})'
    if isinstance(value, ObjectChecks):
        return f'ObjectChecks({literal(value.steps)})'
    if isinstance(value, tuple):
        return '(' + ', '.join(map(literal, value)) + (',' if len(value) == 1 else '') + ')'
    if isinstance(value, list):
        return '[' + ', '.join(map(literal, value)) + ']'
    if isinstance(value, dict):
        return '{' + ', '.join(f'{literal(k)}: {literal(v)}' for k, v in value.items()) + '}'
    return repr(value)

def build():
    assert len(DAYS) == 100, f'Expected 100 days, got {len(DAYS)}'
    index = ['# Curriculum', '', 'Each day has three levels: foundation, application, and stretch.',
             'Finish one day before moving on; revisit earlier work when a later test exposes a gap.', '']
    for number, lesson in enumerate(DAYS, 1):
        if (number - 1) % 10 == 0:
            index += [f'## Days {number:03d}–{number+9:03d}: {PHASES[(number-1)//10]}', '', '| Day | Topic |', '| --- | --- |']
        folder_name = f'day_{number:03d}_{lesson["slug"]}'
        folder = ROOT / 'days' / folder_name
        folder.mkdir(parents=True, exist_ok=True)
        index.append(f'| {number:03d} | [{lesson["title"]}](days/{folder_name}/README.md) |')
        if number % 10 == 0:
            index.append('')
        readme = [f'# Day {number:03d}: {lesson["title"]}', '',
                  f'**Phase:** {PHASES[(number-1)//10]}', '',
                  '**Prerequisites:** ' + ('None; begin here.' if number == 1 else f'Complete days 001–{number-1:03d} first.'), '',
                  '## Learn', '', lesson['explanation'], '',
                  'Read and predict the example output before running it. Change one input, predict again, and explain the result.', '',
                  '```powershell', f'python practice.py {number} --examples', '```', '',
                  'The worked examples teach the topic. The exercise file contains only contracts and unfinished stubs.', '',
                  '## Exercises', '']
        source = [f'"""Day {number:03d}: {lesson["title"]}. Implement these contracts after attempting them."""', '']
        tests = [f'"""Behavioral checks for day {number:03d}; expected failures until you implement the stubs."""',
                 'from tests._support import CurriculumCase, File, Database, ObjectChecks',
                 f'from days.{folder_name} import exercises as work', '', '', 'class ExerciseTests(CurriculumCase):']
        for level, exercise in enumerate(lesson['tasks'], 1):
            signature = exercise['signature']
            kind = 'class' if signature.startswith('class ') else 'function'
            clean = signature.removeprefix('class ').removeprefix('async ')
            name = clean.split('(')[0]
            readme += [f'### {level}. {["Foundation", "Application", "Stretch"][level-1]}: `{clean}`', '',
                       exercise['contract'], '', '```powershell', f'python practice.py {number} --exercise {level}', '```', '']
            if kind == 'class':
                parameters = clean.split('(', 1)[1][:-1]
                source += [f'class {name}:', f'    {exercise["contract"]!r}', '',
                           f'    def __init__(self{", " if parameters else ""}{parameters}):',
                           f'        raise NotImplementedError("Attempt day {number:03d}, exercise {level}: {name}")', '', '']
            else:
                source += [f'{"async " if exercise["mode"] == "async" else ""}def {clean}:',
                           f'    {exercise["contract"]!r}',
                           f'    raise NotImplementedError("Attempt day {number:03d}, exercise {level}: {name}")', '', '']
            for case_number, (args, expected) in enumerate(exercise['cases'], 1):
                tests += [f'    def test_{level:02d}_{name}_case_{case_number:02d}(self):',
                          f'        self.check(work.{name}, {literal(args)}, {literal(expected)},',
                          f'                   mode={exercise["mode"]!r}, dataclass_required={number == 42!r},',
                          f'                   frozen={number == 42 and level < 3!r})', '']
        readme += ['## Reflect', '',
                   '- What does each function or object promise, and which boundary was easiest to miss?',
                   '- Add at least one meaningful test of your own. Which mistake would it catch?',
                   '- Explain your approach without reading your code; include complexity once algorithms appear.',
                   '- Record attempts and remaining questions in your journal. Request a hint or review after attempting.', '']
        (folder / 'README.md').write_text('\n'.join(readme), encoding='utf-8')
        (folder / 'exercises.py').write_text('\n'.join(source), encoding='utf-8')
        example = f'"""Worked learning example for day {number:03d}; independent of the exercises."""\n\n'
        example += 'def main():\n' + textwrap.indent(lesson['example'], '    ') + '\n\n\nif __name__ == "__main__":\n    main()\n'
        (folder / 'examples.py').write_text(example, encoding='utf-8')
        (folder / 'test_exercises.py').write_text('\n'.join(tests), encoding='utf-8')
        (folder / '__init__.py').write_text('', encoding='utf-8')
    (ROOT / 'CURRICULUM.md').write_text('\n'.join(index), encoding='utf-8')
    (ROOT / 'days' / '__init__.py').write_text('"""One independent package per learning day."""\n', encoding='utf-8')
    print(f'Built {len(DAYS)} days and {sum(len(d["tasks"]) for d in DAYS)} exercises.')

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--overwrite', action='store_true', help='Explicitly replace existing lessons, attempts, and tests')
    options = parser.parse_args()
    if (ROOT / 'days').exists() and not options.overwrite:
        parser.error('days/ already exists. Use a clean checkout, or deliberately supply --overwrite after backing up attempts.')
    build()
