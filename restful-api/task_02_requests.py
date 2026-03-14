import requests
import csv

def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints the status code.
    If successful, it prints the titles of all the posts.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print the status code
    print(f"Status Code: {response.status_code}")

    # If the request was successful, parse and print titles
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder.
    If successful, structures the data and saves it to a CSV file.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # Structure the data into a list of dictionaries with specific keys
        structured_posts = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]

        # Write the data into a CSV file called posts.csv
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write the headers
            writer.writeheader()

            # Write the rows of structured data
            writer.writerows(structured_posts)
