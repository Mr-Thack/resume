## <<entry.company>>, <<entry.position>>

((* if entry.date_string *))- <<entry.date_string>>
((* endif *))
((* if entry.location *))- <<entry.location>>
((* endif *))
((* if entry.link *))- <<entry.link>>
((* endif *))
((* for item in entry.highlights *))
- <<item>>
((* endfor *))
