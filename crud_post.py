import requests


class CrudPost:

    def create_post(self, url, token,title, content, page, status):
        payload = {'title': title,
                   'content': content,
                   'page': page,
                   'status': status}

        headers = {
            'Authorization': token
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response

    def retrieve_post(self, url, token, id_post):
        new_url = url + id_post
        payload = {}
        files = {}
        headers = {
            'Authorization': token
        }

        response = requests.request("GET", new_url, headers=headers, data=payload, files=files)
        return response

    def delete_post(self):
        return

    def update_post(self):
        return


