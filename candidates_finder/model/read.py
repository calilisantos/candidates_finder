from candidates_finder.configs import request as request_confs
import requests


class Read:
    def get_followers_request(self) -> dict:
        followers_response = requests.get(request_confs.FOLLOWERS_URL, headers=request_confs.HEADERS)
        followers_response.raise_for_status()

        return followers_response.json()

    def get_followers_info_list(self, followers_list) -> list:
        return list(map(lambda follower: follower[request_confs.PROFILE_KEY], followers_list))

    def get_followers_info_request(self, follower_url) -> dict:
        try:
            followers_info_response = requests.get(follower_url, headers=request_confs.HEADERS)
            followers_info_response.raise_for_status()

            return {column: followers_info_response.json()[column] for column in request_confs.COLUMNS_LIST}
        except Exception as e:
            print(f"Error: {e}")
            return {column: None for column in request_confs.COLUMNS_LIST}
