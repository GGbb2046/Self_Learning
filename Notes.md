
https://www.youtube.com/watch?v=sa-TUpSx1JA

const string msgFormat = "table[{0}], tr[{1}], td[{2}], a: {3}, b: {4}";

const string table_pattern = "<table.*?>(.*?)</table>";

const string tr_pattern = "<tr>(.*?)</tr>";

const string td_pattern = "<td.*?>(.*?)</td>";

const string a_pattern = "<a href=\"(.*?)\"></a>";

const string b_pattern = "<b>(.*?)</b>";


Code	Meaning
\d	a digit
\D	a non-digit
\s	whitespace (tab, space, newline, etc.)
\S	non-whitespace
\w	alphanumeric
\W	non-alphanumeric


^ matches the beginning of a string.
$ matches the end of a string.
\b matches a word boundary.
\d matches any numeric digit.
\D matches any non-numeric character.
(x|y|z) matches exactly one of x, y or z.
(x) in general is a remembered group. We can get the value of what matched by using the groups() method of the object returned by re.search.
x? matches an optional x character (in other words, it matches an x zero or one times).
x* matches x zero or more times.
x+ matches x one or more times.
x{m,n} matches an x character at least m times, but not more than n times.
?: matches an expression but do not capture it. Non capturing group.
?= matches a suffix but exclude it from capture. Positive look ahead.
a(?=b) will match the "a" in "ab", but not the "a" in "ac"
In other words, a(?=b) matches the "a" which is followed by the string 'b', without consuming what follows the a.
?! matches if suffix is absent. Negative look ahead.
a(?!b) will match the "a" in "ac", but not the "a" in "ab"
?<= positive look behind
?<! negative look behind

https://levelup.gitconnected.com/7-different-ways-to-merge-dictionaries-in-python-30148bf27add # dicionaries