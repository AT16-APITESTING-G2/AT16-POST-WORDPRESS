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

    def delete_post(self):
        return

    def update_post(self):
        return


