# Search Challenge for EDITED

## Dependencies
No third-party libraries. You should have Python > 3.x, which comes pre-installed in MacOS and Ubuntu.
Use `python3 --version` to check if Python works on your machine and the version is correct.

## Run the project
Run `python3 search.py "<query>"`,
where `<query>` indicates your search query, e.g.

```
python3 search.py "toyota car" 
```

Note: the double quotes are necessary to indicate it's a string query.

## Rationale
Simple search algorithm that came to my mind - word count.

The inspiration came from Google of course, first thing that came to mind were the words in bold in the search results page.

## Considerations
I was hesitating whether I should add more weight to brand or some other feature such as size or colour, as I think if it's a human searching this query, brand should take more weight than other things, i.e. `blue shirt long sleeve unknown brand` shouldn't be as relevant as `blue shirt prada`? But then I thought this would not be a neutral way to provide relevant results.

On the other hand, matching typos and prefixes would require a more sophisticated approach that would go beyond the 2 hours, and potentially make the code more brittle. So I decided to keep it simple, I believe it's better to release an MVP that works well than ship a ton of features in a short window, risking quality. Instead I decided to add some tests for some of the cases mentioned in the challenge, which you can run this way:

`python3 tests.py`

### Performance
I don't think there is any considerable impact if this is scaled up to thousands or millions of entries. I'd say in the case of adding typo parsing and dealing with prefixes and human error in general could lead to a more considerable impact.
