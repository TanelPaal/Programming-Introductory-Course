"""API exercise."""
from typing import Any
import requests
import requests.exceptions
from requests import Response, RequestException


def get_request(url: str) -> int:
    """
    Send an HTTP GET request to the specified URL.

    Return the resulting response object status code.

    :param url: The URL to which the GET request will be sent.
    :return: Server's response to the request.
    """
    response = requests.get(url)
    return response.status_code


def get_request_error_handling(url: str) -> int | requests.RequestException:
    """
    Send an HTTP GET request to the specified URL with error handling.

    Handle any exceptions that may occur during the request.

    :param url: The URL to which the GET request will be sent.
    :return: Server's response object or the exception object if an error occurs.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.status_code
    except requests.exceptions.RequestException as error:
        return error


def post_request(url: str, data: dict) -> Response | RequestException:
    """
    Send an HTTP POST request with JSON data to the specified URL.

    Handle any exceptions that may occur during the request.

    :param url: The URL to which the POST request will be sent.
    :param data: Dictionary to be sent along with the POST request.
    :return: Server's response json object or the exception object if an error occurs.
    """
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as error:
        return error


def delete_request(url: str) -> int | requests.RequestException:
    """
    Send an HTTP DELETE request to the specified URL.

    Handle any exceptions that may occur during the request.

    :param url: The URL to which the DELETE request will be sent.
    :return: Server's response status code or the exception object if an error occurs.
    """
    try:
        response = requests.delete(url)
        response.raise_for_status()
        return response.status_code
    except requests.exceptions.RequestException as error:
        return error


def stream_request(url: str) -> str:
    """
    Send an HTTP GET request to the specified URL and stream the response.

    More information:
    https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests

    Return a string containing the streamed content.

    :param url: The URL to send the GET request to.
    :return: A string containing the streamed content.
    """
    content = ""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        for chunk in response.iter_lines():
            if chunk:
                decoded_chunk = chunk.decode("utf-8")
                content += decoded_chunk + '\n'
        return content
    except requests.exceptions.RequestException as error:
        return str(error)


def get_authenticated_request(url: str, auth_token: str) -> Any | requests.RequestException:
    """
    Send an authenticated HTTP GET request using the provided token.

    Note: Do not push your auth token into GIT.

    :param url: The URL to which the GET request will be sent.
    :param auth_token: The authentication token for the request.
    :return: Server's response json object or the exception object if an error occurs.

    """
    headers = {"Authorization": f"Bearer {auth_token}"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        return error


def advanced_user_filter(url, min_followers: int, min_posts: int, min_following: int) -> list:
    """
    Fetch user data from a URL and filter based on specified criteria.

    Return specific fields for users meeting the follower, post, and following thresholds.
    Each user in the returned list has to include their username, full_name, followers, following, and posts.

    :param url: URL for user data.
    :param min_followers: Minimum followers required.
    :param min_posts: Minimum posts required.
    :param min_following: Minimum following required.
    :return: List of user data dictionaries.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        users = response.json()

        filtered_users = []
        # Iterates over users and filters based on criteria.
        for user in users:
            if user.get('followers', 0) >= min_followers and user.get('posts', 0) >= min_posts and user.get('following', 0) >= min_following:
                filtered_users.append({
                    'username': user.get('username'),
                    'full_name': user.get('full_name'),
                    'followers': user.get('followers'),
                    'following': user.get('following'),
                    'posts': user.get('posts')
                })

        return filtered_users

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []


def fetch_aggregate_data(url: str) -> dict:
    """
    Process a list of JSON objects to aggregate specific data points.

    Aggregate such as the total and average number of followers,
    posts, and following for all users.

    https://cs.taltech.ee/services/ex14/json-data

    The dictionary should have the following information:
    - 'average_followers'
    - 'average_following'
    - 'average_posts'
    - 'total_followers'
    - 'total_following'
    - 'total_posts'

    :param url: URL from which to fetch user data.
    :return: Aggregated data including total and average values.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        users = response.json()

        total_followers = total_following = total_posts = 0
        # Accumulates total followers, following, and posts.
        for user in users:
            total_followers += user.get('followers', 0)
            total_following += user.get('following', 0)
            total_posts += user.get('posts', 0)

        num_users = len(users)
        avg_followers = total_followers / num_users if num_users else 0
        avg_following = total_following / num_users if num_users else 0
        avg_posts = total_posts / num_users if num_users else 0

        # Returns a dictionary with aggregate data.
        return {
            'average_followers': avg_followers,
            'average_following': avg_following,
            'average_posts': avg_posts,
            'total_followers': total_followers,
            'total_following': total_following,
            'total_posts': total_posts
        }

    except requests.RequestException as error:
        print(f"Error fetching data: {error}")
        return {}


if __name__ == '__main__':
    print(get_request("https://www.google.com"))  # 200
    print(get_authenticated_request("https://jsonplaceholder.typicode.com/todos/1", "1234"))
    print(advanced_user_filter(
        "https://cs.taltech.ee/services/ex14/json-data",
        750000, 900, 2500))
    print(fetch_aggregate_data(
        "https://cs.taltech.ee/services/ex14/json-data"))
