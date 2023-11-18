import sys
import json


def calculate_score(text, query):
    return sum(
        text.lower()
        .replace("-", " ")
        .replace('"', "")
        .count(word.lower().replace("-", " "))
        for word in query.split(" ")
    )


def relevance_scoring_search(query, data):
    search_results = []
    if query is None or len(query) == 0:
        raise ValueError("Please provide a query")

    for item in data:
        name_score = calculate_score(item["name"], query)
        brand_score = calculate_score(item["brand"], query)
        total_score = name_score + brand_score
        if total_score > 0:
            search_results.append((item, total_score))

    search_results.sort(key=lambda x: x[1], reverse=True)
    return search_results


def main():
    with open("./search_dataset.json", "r") as f:
        data = json.load(f)
        sys.argv.pop(0)
        query_keywords = sys.argv
        if len(query_keywords) > 2:
            raise ValueError("Please provide a single string of keywords separted by spaces")

        search_results = relevance_scoring_search(query_keywords[0], data)

        for result, score in search_results[:10]:
            print(
                f"Name: {result['name']}, Brand: {result['brand']}, Relevancy Score: {score}"
            )


if __name__ == "__main__":
    main()
    pass
